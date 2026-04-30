# Process management

Process management syscalls create processes, replace program images, wait for children, and manage process groups.
The kernel handlers read arguments from the user stack with `GETFROMSTACK()` and delegate most POSIX semantics to the
process or POSIX compatibility layers.

## Process creation and execution

| Handler | Arguments | Purpose |
| --- | --- | --- |
| `syscalls_sys_fork()` | None | Calls `proc_fork()` to create a child process. |
| `syscalls_vforksvc()` | None | Calls `proc_vfork()` and suspends the parent until child `exec()` or exit. |
| `syscalls_sys_spawn()` | `path`, `argv`, `envp` | Starts an executable from a file with `proc_fileSpawn()`. |
| `syscalls_exec()` | `path`, `argv`, `envp` | Replaces the current program image with `proc_execve()`. |
| `syscalls_spawnSyspage()` | `imap`, `dmap`, `name`, `argv` | Starts a program from `syspage`. |
| `syscalls_release()` | None | Releases process state by calling `proc_release()`. |

The `spawnSyspage` handler reads four user-stack arguments:

```c
GETFROMSTACK(ustack, char *, imap, 0U);
GETFROMSTACK(ustack, char *, dmap, 1U);
GETFROMSTACK(ustack, char *, name, 2U);
GETFROMSTACK(ustack, char **, argv, 3U);
```

## Process termination and waiting

| Handler | Arguments | Purpose |
| --- | --- | --- |
| `syscalls_sys_exit()` | `code` | Stores the exit status and terminates the current process. |
| `syscalls_sys_waitpid()` | `pid`, `status`, `options` | Waits for a child state change through `posix_waitpid()`. |

When `status` is not `NULL`, `syscalls_sys_waitpid()` verifies that the pointer belongs to the calling process map.

## Process identifiers

| Handler | Purpose |
| --- | --- |
| `syscalls_getpid()` | Returns the current process ID. |
| `syscalls_getppid()` | Returns the parent process ID. |
| `syscalls_sys_uname()` | Fills a user-provided `struct utsname` through `posix_uname()`. |

## Process groups and sessions

| Handler | Arguments | Purpose |
| --- | --- | --- |
| `syscalls_sys_setpgid()` | `pid`, `pgid` | Sets a process group ID through `posix_setpgid()`. |
| `syscalls_sys_getpgid()` | `pid` | Returns a process group ID through `posix_getpgid()`. |
| `syscalls_sys_setpgrp()` | None | Calls `posix_setpgid(0, 0)` for the calling process. |
| `syscalls_sys_getpgrp()` | None | Calls `posix_getpgid(0)` for the calling process. |
| `syscalls_sys_setsid()` | None | Creates a new session through `posix_setsid()`. |
