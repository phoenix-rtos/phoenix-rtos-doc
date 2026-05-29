# Dependency resolution

The port manager uses a backtracking dependency resolver built on top of the
[resolvelib](https://github.com/sarugaku/resolvelib) library. The resolver computes a
conflict-free set of port versions that satisfies all requirements before any build step
runs.

## Concepts

### Candidates

A candidate represents a single version of a port that the resolver can select. Three
candidate types exist:

`Candidate`
: Base class. Holds a name, version, list of requirements, list of conflicts, definition
  path, exposed use flags, active use flags, `required_use` expressions, and description.

`InstallableCandidate`
: A candidate backed by a `port.def.sh` that can be prepared and built. Determines its
  own `install_path` based on whether the port declares conflicts: conflicting ports
  install into `PREFIX_BUILD_VERSIONED/NAME-VERSION`, while non-conflicting ports install
  directly into `PREFIX_BUILD`.

`OsCandidate`
: A virtual candidate that represents the host environment or Phoenix-RTOS itself. The
  port manager creates an `OsCandidate` named `phoenix` with the version taken from the
  `PHOENIX_VER` environment variable, and another named `host` with version `0`. These
  candidates satisfy `supports` requirements declared by ports (e.g. `phoenix>=3.3`).

### Requirements

A requirement constrains which candidate versions can satisfy a dependency. Requirement
types map to the fields in `port.def.sh`:

| Requirement type | `port.def.sh` field | Behavior |
|------------------|---------------------|----------|
| `BaseRequirement` | `depends`, `supports` | Must be satisfied. Resolution fails if no matching candidate exists. |
| `ConditionalRequirement` | `depends` with `flag ? ( dep... )` | Active only when the parent candidate has the condition flag enabled. |
| `ConflictRequirement` | `conflicts` | Excludes candidates whose version falls within the declared conflict range. |

Each `BaseRequirement` or `ConditionalRequirement` can also carry propagated USE flags,
for example `bar>=1.1[ssl,crypto]`.

### Version specifiers

Port versions and requirement constraints follow
[Python Version Specifiers](https://packaging.python.org/en/latest/specifications/version-specifiers/).
The `PhxVersionGrammar` parser accepts space-separated requirement expressions:

- Unconditional dependency: `NAME OPERATOR VERSION`
- Conditional dependency: `FLAG ? ( DEPENDENCY ... )`
- USE propagation on a dependency: `NAME OPERATOR VERSION[flag1,flag2]`

Example:

```text
baz>=1.0 ssl ? ( bar>=1.1.1[crypto] )
```

Supported operators: `>=`, `<=`, `==`, `>`, `<`, `!=`.

When an expression omits operator and version for a dependency name, the parser defaults to
`>=0.0`, which matches any version.

### REQUIRED_USE constraints

Each candidate can declare `required_use` expressions in `port.def.sh`. These constraints
are parsed by `required_use.py` and validated whenever USE flags are set or propagated, and
again before install.

Supported forms:

```text
^^ ( a b c )
?? ( a b c )
|| ( a b c )
ssl? ( crypto )
!minimal? ( extras )
ssl? ( !gnutls )
```

Validation failures abort the build with an explicit error, including the source of
propagated flags when available.

## Resolution algorithm

The resolver processes each user-requested port independently. For every port listed in
`ports.yaml`, the port manager creates a `BaseRequirement` pinned to the exact version
(`==`) of the selected candidate and passes it to `PhxResolver.resolve()`.

`PhxResolver` wraps `resolvelib.Resolver` with a custom provider (`PhxProvider`) and
reporter (`MyReporter`):

1. `PhxProvider.find_matches()` returns all candidate versions for an identifier that
   satisfy the current requirements and do not conflict, sorted newest-first.
2. `PhxProvider.get_dependencies()` yields dependencies from `candidate.iter_dependencies()`.
  Conditional dependencies are included only when the condition flag is active.
3. `MyReporter.rejecting_candidate()` emits debug traces for unsatisfied requirements.

If resolution fails after exhausting retries, `PhxResolver` raises a
`ResolutionImpossible` or `ResolutionTooDeep` exception with diagnostic information about
which requirements could not be satisfied.

After initial resolution, `PortManager.resolve_propagated_deps()` runs a combined
propagation and re-resolution loop:

1. `propagate_use_flags()` propagates dependency USE flags to resolved candidates.
2. For each mapping, the loop checks whether any candidate's active
   `ConditionalRequirement` now names a target that is absent from the mapping.
   An absent target means a flag was activated after the initial resolution and the
   resolver did not know the dependency existed.
3. If any mapping has a missing target, `resolve_for_namever()` re-resolves that
   mapping from its root requirement, including all now-active conditional deps.
4. `propagate_use_flags()` runs again for any newly resolved candidates.
5. Steps 2 through 4 repeat until no mapping has a missing target and no new
   flags are added.

This loop guarantees that a chain such as `baz` propagating `ssl` to `foo`,
which in turn activates `ssl ? ( bar>=1.0 )`, results in `bar` being present in
`baz`'s mapping before installation starts.

### Independent resolution per user port

Each port requested in `ports.yaml` is resolved separately. This design allows two
user-requested ports to depend on conflicting alternatives of the same library. For
example, `foo` can depend on `bar` while `baz` depends on `barng` (a conflicting
alternative to `bar`), because each port gets its own resolution mapping.

During installation, shared dependencies that appear in multiple mappings are installed
only once (the `installed` flag on each candidate prevents duplicate work).

When multiple parents propagate flags to the same dependency, flags are additive.
The candidate records origins for each flag (`use_flags_origins`) to support diagnostics.

## Resolution errors

Common resolution failures and their causes:

| Error | Cause |
|-------|-------|
| `ResolutionImpossible` | A required dependency has no available candidate, or conflicting constraints make it impossible to pick a version. |
| `ResolutionTooDeep` | The resolver exceeded its backtracking limit, usually because mutual conflicts create a cycle. |
| `unrecognized port: NAME` | A port name in `ports.yaml` does not match any discovered `port.def.sh`. |
| `REQUIRED_USE violated on NAME-VERSION` | Active USE flags (including propagated flags) violate a `required_use` expression. |
