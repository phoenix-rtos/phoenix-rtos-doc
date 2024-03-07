# top

`top` is a real time processes and threads monitor which lists basic information about currently active processes.

---

`top` may be seen as [`ps`](ps.md) command which updates itself with a given rate. Execution of `top` applet may be
controlled with command-line arguments and further with interactive commands when being

When `top` is run with `-h` argument the help message is displayed as follows:

```bash
Command-line arguments
  -h:  prints help
  -H:  starts with threads mode
  -d:  sets refresh rate (integer greater than 0)
  -n:  sets number of iterations (by default its infinity)

Interactive commands:
   <ENTER> or <SPACE>:  refresh
   H:  toggle threads mode
   q:  quit
   P:  sort by CPU
   M:  sort by MEM
   T:  sort by TIME
   N:  sort by PID
   R:  reverse sorting
```

If sole:

```bash
top
```

Is run it presents the user with a live monitor of processes sorted by *%CPU* usage. The monitor is structured in
columns with headers. Each row represents a process.

Column headers are:

- PID - process ID,
- PPID - parent process ID,
- PR - priority,
- STATE - state of process,
- %CPU - CPU usage of process,
- WAIT - wait for processor time,
- TIME - age of process,
- VMEM - memory used,
- CMD - command that started that process,

## See also

1. [Phoenix-RTOS shell](psh.md)
2. [Phoenix-RTOS Utilities](README.md)
3. [Table of Contents](../README.md)
