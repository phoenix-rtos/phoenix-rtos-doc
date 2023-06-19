# Platform management

## `syscalls_platformCtl` (`syscalls_platformctl`)

````C
GETFROMSTACK(ustack, void *, ptr, 0);
````

Executes platform controls call with argument given by `ptr`.

## `syscall_platformWdogReload` (`syscalls_wdgreload`)

Reloads watchdog device when it is available.

## `syscalls_platformSyspageProg` (`syscalls_syspageprog`)

````C
GETFROMSTACK(ustack, syspageprog_t *, prog, 0);
GETFROMSTACK(ustack, int, i, 1);
````

## `syscalls_platformKeepIdle` (`syscalls_keepidle`)

````C
GETFROMSTACK(ustack, int, t, 0);
````

## See also

1. [System calls](README.md)
2. [Table of Contents](../../README.md)
