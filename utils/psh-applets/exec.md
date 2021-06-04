# exec

`exec` applet provides a way to execute a command/executable file. The shell from which the `exec` command is run is replaced with that file. 

---

If used without any parameters specified it prints help message as follows:

```
usage: %s command [args]...
```

where `[args]` are areguments passed to file/command being executed.

As an example a new `psh` can be run using `exec` command:
```
exec /bin/psh
```
### exec return values
`exec` command, by default, returns the value returned by executed file. The `exec` specific errors are:
 - `ENOMEM` if there is not enough memory to execute command
 - `EINVAL` if the executable file has no valid form
