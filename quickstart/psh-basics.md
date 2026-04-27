# Shell basics

After booting Phoenix-RTOS the default shell `psh` (Phoenix Shell) presents a command prompt:

```
(psh)%
```

## Getting help

Type `help` to list available commands. The set of commands depends on the target configuration -
microcontroller targets have a smaller set than full-featured ones.

```
(psh)% help
```

For detailed documentation on each command, see [Phoenix-RTOS Shell (psh)](../utils/psh/index.md).

## Inspecting processes

Use `ps` to display running processes and threads:

```
(psh)% ps
```

The columns show process ID, parent PID, priority, state, CPU usage, wait time, cumulative time, virtual
memory usage, thread count, and command name.

Use `top` for a continuously updating view:

```
(psh)% top
```

Press `q` or `ctrl+c` to exit `top`.

## Running programs

Applications installed in the root filesystem can be run by their path:

```
(psh)% /usr/bin/hello
```

Programs loaded from syspage (embedded in the boot image) can be launched with `sysexec`:

```
(psh)% sysexec myapp
```

## See also

- [Phoenix-RTOS Shell (psh)](../utils/psh/index.md) - full command reference
- [Building](../building/index.md) - how to build the system image
