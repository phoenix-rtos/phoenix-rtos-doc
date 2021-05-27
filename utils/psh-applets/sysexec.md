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

#### Command template
If command should accept variable or multiple arguments (e.g. program parameters) the command template may be specified using `*` wildcard . Checking will be performed only on arguments prior to `*`.

Command template `sysexec arg1 arg2 *` has following impact:
```bash
sysexec arg1 arg2	#executed
sysexec arg1 arg2 arg3 .. argN	#executed
sysexec arg3 arg4	#NOT executed
sysexec arg2 arg1	#NOT executed
```
Important note: `*` works only as standalone argument. It does not perform any lexical matching (e.g. `arg*`)
