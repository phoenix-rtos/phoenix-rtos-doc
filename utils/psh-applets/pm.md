# Pm

`pm` monitors all processes that has been started before `pm`.

---

If used with `-r` parameter it restarts the machine when any of monitored processes dies.

```bash
Usage: pm [options]
  -p:       disable monitoring of `pm` parent process
  -r:       restarts the machine when any of monitored processes dies
  -t secs:  sets monitor check interval
  -h:       shows this help message
```

## See also

1. [Phoenix-RTOS shell](psh.md)
2. [Phoenix-RTOS Utilities](README.md)
3. [Table of Contents](../README.md)
