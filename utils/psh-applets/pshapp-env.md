# Environment variables

Environment variables are variables that apply to both the current shell and to
any subshells that it creates.  If you change the value of an environment
variable, the change is passed forward to subsequent shells, but not backward
to the parent shell.


## export

The `export` is a builtin command which sets and exports variables to the
process environment.

#### Syntax
```
export [NAME[=value] ...]
```

The `export` command is probably most commonly used to set or modify the `PATH`
environment variable. Specifies the directories to search for the command.
Therefore, it will serve as a basic usage example:

```bash
(psh)% export PATH=/usr/sbin:/usr/bin:/sbin:/bin
```

Multiple variables can be given to the export command. In example below, the
variables A, B, C, D are exported.  If a variable name is directly followed by
`=word`, the value of the variable is set to `word` (like B and D in the
following example):
```bash
(psh)$ export A B=1 C D=2
```

If no arguments are specified, the `export` command lists the names and values
of exported variables:

```bash
(psh)% export
export PATH=/bin:/sbin:/usr/bin:/usr/sbin
export HOME=/root
export TEMP=/tmp
```

`export` returns an exit status of `0` unless an invalid option is encountered,
`1` if one of the names is not a valid shell variable name.

## unset

The `unset` is builtin command that removes variables from the shell's exported
environment. It is implemented as a shell builtin, because it directly
manipulates the internals of the shell.

#### Syntax
```
unset [VARIABLE]...
```

The variables given by the list of names are unassigned from environment like
in example below.

```
(psh)% unset A B C D
```

Returned exit value is `0`, even if variable was not set or exported.
