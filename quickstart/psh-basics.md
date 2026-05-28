# Shell basics

After Phoenix-RTOS boots, the default `psh` (Phoenix Shell) prompt appears on the console.

```
(psh)%
```

The command set depends on the target image. Microcontroller targets usually include fewer applets than QEMU or PC
targets.

## List available commands

Use `help` to print registered applets and short descriptions.

```
(psh)% help
Available commands:
  cat       - concatenate files and print on the standard output
  cd        - change current directory
  echo      - display a line of text
  help      - prints this help message
  ls        - list directory contents
  ps        - prints processes and threads
  sysexec   - run program from syspage
  top       - top utility
(psh)%
```

For detailed documentation on each command, see [Phoenix-RTOS Shell (psh)](../utils/psh/index.md).

## Inspect processes

Use `ps` to display a snapshot of processes. The source prints columns for process ID, parent process ID, priority,
state, CPU usage, wait time, cumulative CPU time, virtual memory use, thread count, and command name.

```
(psh)% ps
     PID     PPID PR STATE  %CPU    WAIT        TIME   VMEM THR CMD
       1        0  4 sleep   0.0      0s    00:00:00    32K   1 dummyfs
       2        0  4 sleep   0.0      0s    00:00:00    28K   1 tty
       3        0  4 ready   0.1      0s    00:00:00    36K   1 psh
(psh)%
```

Use `top -n 1` for one refreshed screen and an immediate return to the prompt.

```
(psh)% top -n 1
Tasks:    3 total, running: 1, sleeping: 2

     PID     PPID PR STATE  %CPU    WAIT       TIME     VMEM CMD
       3        0  4 ready   0.1      0s       0:00.01    36K psh
       1        0  4 sleep   0.0      0s       0:00.00    32K dummyfs
       2        0  4 sleep   0.0      0s       0:00.00    28K tty
(psh)%
```

Use `top -h` to print its keyboard shortcuts without starting the interactive monitor.

```
(psh)% top -h
Command line arguments:
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
(psh)%
```

## Run programs from the filesystem

Applications installed in the root filesystem can be run by path. The `_user/hello` example prints one line and exits.

```
(psh)% /usr/bin/hello
Hello World!!
(psh)%
```

## Run programs from syspage

On non-MMU targets, PLO can place programs in syspage with the `app` command. Use `sysexec` to start such a program.

When the `hello` example is registered in syspage, the command output matches the program output.

```
(psh)% sysexec hello
Hello World!!
(psh)%
```

`sysexec -h` prints the command syntax.

```
(psh)% sysexec -h
Usage: sysexec [OPTIONS] progname [args]...
Options:
  -m datamap   select data memory map
  -M codemap   select code memory map
  -d           daemonize
  -s           do not close stdin on daemonization
(psh)%
```

## See also

- [Phoenix-RTOS Shell (psh)](../utils/psh/index.md) - full command reference
- [Building](../building/index.md) - how to build the system image