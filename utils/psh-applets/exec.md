# exec

`exec` applet provides a way to execute a command/executable file. The shell from which it is run is replaced with that
file.

---

If used without any parameters specified it prints help message as follows:

```bash
usage: %s command [args]...
```

Where `[args]` are arguments passed to the file/command being executed.

As an example a new `psh` can be run using the `exec` command:

```bash
exec /bin/psh
```

## Exec return values

`exec` command, by default, returns the value returned by executed file. The `exec` specific errors are:

- `ENOMEM` if there is not enough memory to execute a command
- `EINVAL` if the executable file has no valid form

## See also

1. [Phoenix-RTOS shell](psh.md)
2. [Phoenix-RTOS Utilities](README.md)
3. [Table of Contents](../README.md)
