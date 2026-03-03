# Picking ports to install using ports.yaml

To include a specific port in a Phoenix-RTOS build, the appropriate `ports.yaml`
file for the given target must be modified.

A `ports.yaml` is a YAML file that defines which
ports are included in a build and how they are configured. It may also use
[Jinja2](https://jinja.palletsprojects.com/en/stable/) templating, allowing
build-time configuration based on environment variables.

## Static example of `ports.yaml`

The following `ports.yaml` requests a simple (unconditional) installation of
`busybox` and a complex installation of a `lua` port:

```yaml
tests: true                     # Optional. Default: false
ports:
  - name: busybox               # Required. String. Must match port.def.sh 'name' of port
  - name: lua                   
    tests: true                 # Optional. Boolean. Default: false. AND-ed with global 'tests'
    use: ["safe"]               # Optional. List of strings. Default: []
```

The global `tests` field controls the test building for all ports that
specify per-port `tests` field by **AND-ing** the fields. Thus, in the above
case, despite the global `tests: true` the `busybox` will be built without
tests, as it doesn't specify the per-port `tests` field, and it defaults to
`false`. However, the `lua` port will be built with tests since both global and
per-port fields are `true`.

The `lua` port is additionally specified to be built with a `safe` flag. This
flag must be present in the `lua` port.def.sh `iuse` field (see:
{ref}`port_def_variant_flags`).

## Environment-dependent `ports.yaml`

The previous example can be rewritten so that it is controlled by the
environment variables using Jinja2 snippets. In the following `ports.yaml`,
building tests is enabled for all testable ports only if
`LONG_TEST=y`, and the `lua` port is installed only if `INSTALL_LUA=y`:

```yaml
tests: '{{ env.LONG_TEST }}'
ports:
  - name: busybox
  - name: lua                   
    tests: true
    use: ["safe"]
    if: '{{ env.INSTALL_LUA }}' # Optional. Boolean. Default: true
```

The `if` field is an additional, optional attribute that controls whether a port
is built. If the expression evaluates to `false`, the port is skipped.

Here is another `ports.yaml` example that uses Jinja2 `if` block for
`azure_sdk` port and a conditional inclusion of variant flag `longtest` flag for
`micropython`:

```jinja
tests: '{{ env.LONG_TEST }}'
ports:
  - name: azure_sdk
    {% if env.LONG_TEST %}
    use: [longtest]
    tests: true
    {% endif %}
  - name: micropython
    use: {{ ["longtest"] if env.LONG_TEST }}
    tests: True
```

This example exploits the fact that the `ports.yaml` is first treated as a Jinja2
template, while the previous example passed Jinja2 snippets as strings.
