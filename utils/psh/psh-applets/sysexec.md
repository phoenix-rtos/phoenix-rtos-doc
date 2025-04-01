# sysexec

`sysexec` is a `psh` utility to run programs on systems without MMU.

---

Usage:

```console
sysexec [-m mapname] progname [args]...
```

The `-m` parameter is optional and allows to specify a non-default memory map where the program data will be placed.
The default memory map is the one assigned with the `app` command in the plo script.

As an example, if in the script plo it is set:

```console
app flash1 -x progname xip1 ocram2
```

then `ocram2` is the default map for an app, so

```console
sysexec progname arg1 arg2
```

to use a different map with read & write attributes set, provide an optional map with `-m` argument:

```console
sysexec -m dtcm progname arg1 arg2
```

## Sysexec command white list

The built-in whitelist functionality provides the ability to predefine an available set of `sysexec` commands.
These commands can be defined in two ways:

- `/etc/whitelist` file
- `PSH_SYSEXECWL` environment variable at compile time

If storing commands in the `/etc/whitelist` file each complete `sysexec` command should be stored in a separate line
with a line length not exceeding 79 characters:

```console
    sysexec argA1 argA2 argA3
    sysexec argB1 argB2
    sysexec argC1 argC2 argC3
```

If the commands are stored in the `PSH_SYSEXECWL` environment variable, each command should end with a semicolon
(`;`), as in the example below:

```console
export PSH_SYSEXECWL="sysexec argD1 argD2 argD3;sysexec argE1 argE2 argE3;sysexec argF1 argF2"
```

If neither `/etc/whitelist` and `PSH_SYSEXECWL` is defined then sysexec will not have any restrictions.

### Command template

If the command should accept variable or multiple arguments (e.g. program parameters) the command template may be
specified using `*` wildcard. Checking will be performed only on arguments prior to `*`.

Command template `sysexec arg1 arg2 *` has the following impact:

```console
sysexec arg1 arg2   #executed
sysexec arg1 arg2 arg3 .. argN  #executed
sysexec arg3 arg4   #NOT executed
sysexec arg2 arg1   #NOT executed
```

Important note: `*` works only as a standalone argument. It does not perform any lexical matching (e.g. `arg*`)

## See also

1. [Feniks-RTOS shell](../index.md)
2. [Feniks-RTOS Utilities](../../index.md)
3. [Table of Contents](../../../index.md)
