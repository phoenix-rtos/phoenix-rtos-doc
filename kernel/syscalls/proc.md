## Process management

### `syscalls_procFork` (`syscalls_sys_fork`)

Forks current process into two processes.

<br>

### `syscalls_procVirtualFork` (`syscalls_vforksvc`)

Forks current process into two processes, but they initialy share the address space until `exec()` or `exit()` calls are called. Parent process execution is suspended until `exec()` or `exit()` call as well.

<br>

### `syscalls_procExec` (`syscalls_exec`)

````C
GETFROMSTACK(ustack, char *, path, 0);
GETFROMSTACK(ustack, char **, argv, 1);
GETFROMSTACK(ustack, char **, envp, 2);
````

<br>

### `syscalls_procSpawnSyspage`

````C
GETFROMSTACK(ustack, char *, map, 0);
GETFROMSTACK(ustack, char *, name, 1);
GETFROMSTACK(ustack, char **, argv, 2);
````

<br>

### `syscalls_procSpawn` (`syscalls_sys_spawn`)

````C
GETFROMSTACK(ustack, char *, path, 0);
GETFROMSTACK(ustack, char **, argv, 1);
GETFROMSTACK(ustack, char **, envp, 2);
````

<br>

### `syscalls_procExit` (`syscalls_sys_exit`)

````C
GETFROMSTACK(ustack, int, code, 0);
````

<br>

### `syscalls_procWait` (`syscalls_sys_waitpid`)

````C
GETFROMSTACK(ustack, int, pid, 0);
GETFROMSTACK(ustack, int *, stat, 1);
GETFROMSTACK(ustack, int, options, 2);
````

<br>

### `syscalls_procGetID` (`syscalls_getpid`)

Returns current process identifier

<br>

### `syscalls_procGetParentID` (`syscalls_getppid`)

Returns parent process identifier

<br>

### `syscalls_procSetGroupID` (`syscalls_sys_setpgid`)

````C
GETFROMSTACK(ustack, pid_t, pid, 0);
GETFROMSTACK(ustack, pid_t, pgid, 1);
````

<br>

### DEPRECATED `syscalls_sys_setpgrp` => `syscalls_procSetGroupID`

<br>

### `syscalls_procGetGroupID` (`syscalls_sys_getpgid`)

<br>

### DEPRECATED `syscalls_sys_getpgrp` => `syscalls_procGetGroupID`

<br>

### `syscalls_procSetSession` (`syscalls_sys_setsid`)

<br>

## See also

1. [System calls](README.md)
2. [Table of Contents](../../README.md)
