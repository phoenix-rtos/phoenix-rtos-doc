# System calls

## Debug

### `syscall_debug`

````C
GETFROMSTACK(ustack, char *, s, 0);
````

Displays string given by `s` on kernel console

<br>

## Memory management

Functions allow to manage process address spaces.

### `syscalls_memMap` (`syscalls_mmap`)

````C
GETFROMSTACK(ustack, void *, vaddr, 0);
GETFROMSTACK(ustack, size_t, size, 1);
GETFROMSTACK(ustack, int, prot, 2);
GETFROMSTACK(ustack, int, flags, 3);
GETFROMSTACK(ustack, oid_t *, oid, 4);
GETFROMSTACK(ustack, offs_t, offs, 5);
````

Maps part of object given by `oid`, `offs` and `size` at `vaddr` with protection attributes given by `prot` using mapping mode defined by `flags`.

<br>

### `syscalls_memUnmap` (`syscalls_munmap`)

````C
GETFROMSTACK(ustack, void *, vaddr, 0);
GETFROMSTACK(ustack, size_t, size, 1);
````

Unmaps part of address space defined by `vaddr` and `size`.

<br>

### `syscalls_memDump` (`syscalls_mmdump`)

Returns memory map entries associated with calling process.

<br>

### `syscalls_memGetInfo` (`syscalls_meminfo`)

````C
GETFROMSTACK(ustack, meminfo_t *, info, 0);
````

<br>

### `syscalls_memGetPhysAddr` (`syscalls_va2pa`)

````C
GETFROMSTACK(ustack, void *, va, 0);
````

<br>

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

## Thread management

### `syscalls_threadCreate` (`syscalls_beginthread`)

````C
GETFROMSTACK(ustack, void *, start, 0);
GETFROMSTACK(ustack, unsigned int, priority, 1);
GETFROMSTACK(ustack, void *, stack, 2);
GETFROMSTACK(ustack, unsigned int, stacksz, 3);
GETFROMSTACK(ustack, void *, arg, 4);
GETFROMSTACK(ustack, unsigned int *, id, 5);
````

Starts thread from entry point given by `start` at priority defined by `priority`. Thread stack is defined by `stack` and `stacksz` arguments. Executed thread id is returned in `id` variable.

<br>

### `syscalls_threadDestroy` (`syscalls_endthread`)

Terminates executing thread.

<br>

### `syscalls_threadWait` (`syscalls_threadJoin`)

````C
GETFROMSTACK(ustack, time_t, timeout, 0);
````

### `syscalls_threadSleep` (`syscalls_usleep`)

````C
GETFROMSTACK(ustack, unsigned int, us, 0);
````

Suspends thread execution for number of microseconds defined by `us`.

### `syscalls_threadGetInfo` (`syscalls_threadinfo`)

````C
GETFROMSTACK(ustack, int, n, 0);
GETFROMSTACK(ustack, threadinfo_t *, info, 1);
````

Returns thread information `info` for thread given by `n`.

### `syscalls_threadGetID` (`syscalls_gettid`)

Returns identifier of calling thread.

### `syscalls_threadSetPriority` (`syscalls_priority`)

````C
GETFROMSTACK(ustack, int, priority, 0);
````

## Thread synchronization

### `syscalls_mutexCreate`

````C
GETFROMSTACK(ustack, unsigned int *, h, 0);
````

Creates mutex and returns resource handle `h`.

### `syscalls_phMutexLock`

````C
GETFROMSTACK(ustack, unsigned int, h, 0);
````

Locks mutex given by handle `h`.

### `syscalls_mutexTry`

````C
GETFROMSTACK(ustack, unsigned int, h, 0);
````

Tries to lock mutex given by handle `h`.

### `syscalls_mutexUnlock`

````C
GETFROMSTACK(ustack, unsigned int, h, 0);
````

Unlocks mutex given by `h`.

### `syscalls_condCreate`

````C
GETFROMSTACK(ustack, unsigned int *, h, 0);
````

Creates conditional variable and returns its handle in variable `h`.

### `syscalls_phCondWait`

````C
GETFROMSTACK(ustack, unsigned int, h, 0);
GETFROMSTACK(ustack, unsigned int, m, 1);
GETFROMSTACK(ustack, time_t, timeout, 2);
````

Waits on conditional given by 'h' for number of microseconds giveb by `timeout`. Before suspending a calling thread execution mutex identified by `m` handle is unlocked to enable other thread modifying variables used to check condtionals after conditional signalisation. When conditional variable is signaled mutex `m` is locked.

### `syscalls_condSignal`

````C
GETFROMSTACK(ustack, unsigned int, h, 0);
````

Signals conditional given by `h`.

### `syscalls_condBroadcast`

````C
GETFROMSTACK(ustack, unsigned int, h, 0);
````

Signals conditional to all waiting threads.

## Inter-process communication

### `syscalls_portCreate`

````C
GETFROMSTACK(ustack, u32 *, port, 0);
````

Creates new communication queue and returns its identifier in `port` variable.

### `syscalls_portDestroy`

````C
GETFROMSTACK(ustack, u32, port, 0);
````

Destroys communication queue identified by `port` variable.

### `syscalls_portRegister`

````C
GETFROMSTACK(ustack, unsigned int, port, 0);
GETFROMSTACK(ustack, char *, name, 1);
GETFROMSTACK(ustack, oid_t *, oid, 2);
````

Registers `port` in the namespace at `name` and returns object identifier `oid` identifying this association.

### `syscalls_msgSend`

````C
GETFROMSTACK(ustack, u32, port, 0);
GETFROMSTACK(ustack, msg_t *, msg, 1);
````

Sends message `msg` to queue identified by `port`. Execution of calling thread is suspended until receiving thread responds to this message.

### `syscalls_msgRecv`

````C
GETFROMSTACK(ustack, u32, port, 0);
GETFROMSTACK(ustack, msg_t *, msg, 1);
GETFROMSTACK(ustack, unsigned long int *, rid, 2);
````

Receives message `msg` from queue identified by `port`. The reception context is stored in variable `rid`.

### `syscalls_msgRespond`

````C
GETFROMSTACK(ustack, u32, port, 0);
GETFROMSTACK(ustack, msg_t *, msg, 1);
GETFROMSTACK(ustack, unsigned long int, rid, 2);
````

Responds to message `msg` using reception context `rid`.

### `syscalls_lookup`

````C
GETFROMSTACK(ustack, char *, name, 0);
GETFROMSTACK(ustack, oid_t *, file, 1);
GETFROMSTACK(ustack, oid_t *, dev, 2);
````

Lookups for object identifier (`port` and resource `id`) associated with `name`. Object identifier representing file is returned in `file` variable. If file is associated with other object the other object id is returned in `dev`.

### `syscalls_signalHandle` 
### `syscalls_signalPost`
### `syscalls_signalMask`
### `syscalls_signalSuspend`
### `syscalls_sys_tkill`


## File operations

### `DEPRECATED` (`syscalls_fileAdd`) => `syscalls_fileOpen`

````C
GETFROMSTACK(ustack, unsigned int *, h, 0);
GETFROMSTACK(ustack, oid_t *, oid, 1);
GETFROMSTACK(ustack, unsigned int, mode, 2);
````

Adds file given by `oid` to process resources. Added process resource is identified by handle returned in `h` variable. The access mode is set to `mode`.

### `syscalls_fileOpen` (`syscalls_sys_open`)

````C
GETFROMSTACK(ustack, const char *, filename, 0);
GETFROMSTACK(ustack, int, oflag, 1);
````

### `DEPRECATED` `syscalls_fileSet` => `syscalls_fileRead`, `syscalls_fileWrite`

````C
GETFROMSTACK(ustack, unsigned int, h, 0);
GETFROMSTACK(ustack, char, flags, 1);
GETFROMSTACK(ustack, oid_t *, oid, 2);
GETFROMSTACK(ustack, offs_t, offs, 3);
GETFROMSTACK(ustack, unsigned, mode, 4);
````

Updates file parameters for file given by resource handle `h`.

### `DEPRECATED` `syscalls_fileGet` => `syscalls_fileRead`, `syscalls_fileWrite`

````C
GETFROMSTACK(ustack, unsigned int, h, 0);
GETFROMSTACK(ustack, int, flags, 1);
GETFROMSTACK(ustack, oid_t *, oid, 2);
GETFROMSTACK(ustack, offs_t *, offs, 3);
GETFROMSTACK(ustack, unsigned *, mode, 4);
````

Retrieves file parameters for file given by resource handle `h`.

### DEPRECATED `syscalls_fileRemove` => `syscalls_fileClose`

````C
GETFROMSTACK(ustack, unsigned int, h, 0);
````

Removes file given by `h` from resources of calling process.

### DEPRECATED `syscalls_resourceDestroy` => `syscalls_fileClose`, `syscalls_mutexDestroy`, `syscalls_condDestroy`

````C
GETFROMSTACK(ustack, unsigned int, h, 0);
````

Destroys resource given by `h`.

### `syscalls_fileRead` (`syscalls_sys_read`)

````C
GETFROMSTACK(ustack, int, fildes, 0);
GETFROMSTACK(ustack, void *, buf, 1);
GETFROMSTACK(ustack, size_t, nbyte, 2);
````

### `syscalls_fileWrite` (`syscalls_sys_write`)

````C
GETFROMSTACK(ustack, int, fildes, 0);
GETFROMSTACK(ustack, void *, buf, 1);
GETFROMSTACK(ustack, size_t, nbyte, 2);
````

### `syscalls_fileClose` (`syscalls_sys_close`) 



### `syscalls_sys_link` 
	## syscalls_sys_unlink) 
	## syscalls_sys_fcntl) 
	## syscalls_sys_ftruncate) 
	## syscalls_sys_lseek) 
	## syscalls_sys_dup) 
	## syscalls_sys_dup2) 
	## syscalls_sys_pipe) 
	## syscalls_sys_mkfifo) 
	## syscalls_sys_chmod) 
	## syscalls_sys_fstat) 

	## syscalls_sys_ioctl) 
	## syscalls_sys_utimes)

### `syscalls_filePoll` (`syscalls_sys_poll`)

````C
GETFROMSTACK(ustack, struct pollfd *, fds, 0);
GETFROMSTACK(ustack, nfds_t, nfds, 1);
GETFROMSTACK(ustack, int, timeout_ms, 2);
````

## Communication sockets

### `syscalls_sys_accept` 
### `syscalls_sys_accept4` 
### `syscalls_sys_bind` 
### `syscalls_sys_connect`
### `syscalls_sys_getpeername`
### `syscalls_sys_getsockname` 
### `syscalls_sys_getsockopt` 
### `syscalls_sys_listen` 
### `syscalls_sys_recvfrom` 
### `syscalls_sys_sendto` 
### `syscalls_sys_socket` 
### `syscalls_sys_shutdown`
### `syscalls_sys_setsockopt` 

## Time management

### `syscalls_gettime`

````C
GETFROMSTACK(ustack, time_t *, praw, 0);
GETFROMSTACK(ustack, time_t *, poffs, 1);
````

Returns current time in `praw` and `poffs` variables.

### `syscalls_settime`

````C
GETFROMSTACK(ustack, time_t, offs, 0);
````

Setup system time to value given by `offs`.

## Interrupts management

### `syscalls_interrupt`

````C
GETFROMSTACK(ustack, unsigned int, n, 0);
GETFROMSTACK(ustack, void *, f, 1);
GETFROMSTACK(ustack, void *, data, 2);
GETFROMSTACK(ustack, unsigned int, cond, 3);
GETFROMSTACK(ustack, unsigned int *, handle, 4);
````

Installs interrupt handler `f` for interrupt given by `n`.

## Performance monitoring

### `syscalls_perf_start`
### `syscalls_perf_read`
### `syscalls_perf_finish`

### `syscalls_keepidle`

````C
GETFROMSTACK(ustack, int, t, 0);
````



### `syscalls_platformCtl` (`syscalls_platformctl`)

````C
GETFROMSTACK(ustack, void *, ptr, 0);
````

Executes platform controll call with argument given by `ptr`.

### `syscall_platformWdogReload` (`syscalls_wdgreload`)

Reloads watchdog device when it is available.

### `syscalls_platformSyspageProg` (`syscalls_syspageprog`)

## RISC-V specific 

### `syscalls_sbi_putchar` 
### `syscalls_sbi_getchar`

### REMOVE `syscalls_release` 
