# Platform management

## `syscalls_platformCtl` (`syscalls_platformctl`)

````C
GETFROMSTACK(ustack, void *, ptr, 0);
````

Executes platform controll call with argument given by `ptr`.

## `syscall_platformWdogReload` (`syscalls_wdgreload`)

Reloads watchdog device when it is available.

## `syscalls_platformSyspageProg` (`syscalls_syspageprog`)
