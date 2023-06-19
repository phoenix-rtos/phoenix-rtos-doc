# `/` (runfile)

`/` command allows to execute a file. This command is provided by `runfile` applet.

---

Prefixing filename with `/` executes the file. Usage:

```bash
/filename
```

Will execute a file called filename, but in contrast to [`exec`](exec.md) the current shell will not be substituted by
the file process.

The value of an executed file will not be returned from `/`

## See also

1. [Phoenix-RTOS shell](psh.md)
2. [Phoenix-RTOS Utilities](README.md)
3. [Table of Contents](../README.md)
