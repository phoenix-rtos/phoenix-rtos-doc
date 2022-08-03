# cd

The `cd` command provided as a `psh` applet can be used to change the current working directory.

---

If used with `-h` as the argument it prints the basic usage, which is:

```
Usage: cd [directory]
```

The `directory` argument of the `cd` command is an absolute or relative pathname which becomes the new working directory.
To change the working directory with the `cd` command, the target `directory` may be specified as in the following example:

```bash
cd /usr/bin
```

If `directory` part is omitted it will be read from the `HOME` environment variable. If the `HOME` variable is empty or
not set, the current working directory will be changed to `/` (as a fallback).

It is possible to switch back to the previous working directory by using `-` (a dash) as the `directory` argument to the
`cd` command:

```bash
(psh)% cd /usr/bin
(psh)% cd ../../etc
(psh)% cd -
/usr/bin
(psh)% cd -
/etc
(psh)% cd -
/usr/bin
(psh)% cd -
/etc
```


## See also

1. [Phoenix-RTOS shell](psh.md)
2. [Phoenix-RTOS Utilities](README.md)
3. [Table of Contents](../README.md)
