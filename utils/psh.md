# Phoenix Shell (psh)

Phoenix Shell is a compact program that enables you to control the Phoenix-RTOS from the command line.
## Login

`psh` can be run in login mode by launching it from name `pshlogin`. User credentials are read from `/etc/passwd` file.

Additional user credentials can be passed using the `PSH_DEFUSRPWDHASH` environment variable defined at compile time. `PSH_DEFUSRPWDHASH` should store only one hash of a password. Then one can also log in using:
- username: defuser
- password: (corresponding with given hash)

------------


## Sysexec command white list

The built-in whitelist functionality provides the ability to predefine an available set of `sysexec` commands. These commands can be defined in two ways: 
- `/etc/whitelist` file
- `PSH_SYSEXECWL` environment variable at compile time

If storing commands in `/etc/whitelist` file each complete `sysexec` command should be stored in separate line with line length not exceeding 79 characters:

    sysexec argA1 argA2 argA3
    sysexec argB1 argB2
    sysexec argC1 argC2 argC3

If the commands are stored in the `PSH_SYSEXECWL` environment variable, each command should end with a semicolon (`;`), as in the example below:

```bash
export PSH_SYSEXECWL="sysexec argD1 argD2 argD3;sysexec argE1 argE2 argE3;sysexec argF1 argF2"
```
if neither `/etc/whitelist` and `PSH_SYSEXECWL` is defined then sysexec will not have any restrictions.
