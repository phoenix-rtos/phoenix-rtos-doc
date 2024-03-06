# History

`history` prints the history of entered commands.

---

If `history` is run with `-h` parameter the help message appears as follows:

```bash
usage: help [options] or no args to print command history
  -c:  clears command history
  -h:  shows this help message
```

History is stored chronologically and not redundant so that consecutive entries of exactly the same command are not
duplicated.

It is also possible to scroll through commands history using arrow keys when entering a command.

## See also

1. [Phoenix-RTOS shell](../psh.md)
2. [Phoenix-RTOS Utilities](../README.md)
3. [Table of Contents](../../README.md)
