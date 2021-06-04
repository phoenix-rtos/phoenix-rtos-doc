# `/` (runfile)

`/` command allows to execute a file. This command is provided by `runfile` applet.

---

Prefixing filename with `/` executes the file. Usage:
```
/filename
```
will execute a file called filename, but in contrast to [`exec`](exec.md) the current shell will not be substituted by the file process.

The value of executed file will not be returned from `/`