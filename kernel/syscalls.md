# System calls

## `syscall_debug`

````C
GETFROMSTACK(ustack, char *, s, 0);
````

Displays string given by `s` on kernel console

## `syscalls_mmap`

````C
GETFROMSTACK(ustack, void *, vaddr, 0);
GETFROMSTACK(ustack, size_t, size, 1);
GETFROMSTACK(ustack, int, prot, 2);
GETFROMSTACK(ustack, int, flags, 3);
GETFROMSTACK(ustack, oid_t *, oid, 4);
GETFROMSTACK(ustack, offs_t, offs, 5);
````

Maps part of object given by `oid`, `offs` and `size` at `vaddr` with protection attributes given by `prot` using mapping mode defined by `flags`.

## `syscalls_munmap`

````C
GETFROMSTACK(ustack, void *, vaddr, 0);
GETFROMSTACK(ustack, size_t, size, 1);
````

Unmaps part of address space defined by `vaddr` and `size`.

## `syscalls_sys_fork`

Forks current process into two processes.

## `syscalls_vforksvc`

Forks current process into two processes, but they initialy share the address space until `exec()` or `exit()` calls are called. Parent process execution is suspended until `exec()` or `exit()` call as well.

## `syscalls_exec`

````C
GETFROMSTACK(ustack, char *, path, 0);
GETFROMSTACK(ustack, char **, argv, 1);
GETFROMSTACK(ustack, char **, envp, 2);
````

## `syscalls_sys_exit`

````C
GETFROMSTACK(ustack, int, code, 0);
````

## `syscalls_sys_waitpid`

````C
GETFROMSTACK(ustack, int, pid, 0);
GETFROMSTACK(ustack, int *, stat, 1);
GETFROMSTACK(ustack, int, options, 2);
````

## `syscalls_threadJoin`

````C
GETFROMSTACK(ustack, time_t, timeout, 0);
````

## `syscalls_getpid`

Returns current process identifier

## `syscalls_getppid`

Returns parent process identifier

## `syscalls_gettid`

Returns identifier of current thread.

## `syscalls_beginthreadex`

````C
GETFROMSTACK(ustack, void *, start, 0);
GETFROMSTACK(ustack, unsigned int, priority, 1);
GETFROMSTACK(ustack, void *, stack, 2);
GETFROMSTACK(ustack, unsigned int, stacksz, 3);
GETFROMSTACK(ustack, void *, arg, 4);
GETFROMSTACK(ustack, unsigned int *, id, 5);
````

Starts thread from entry point given by `start` at priority defined by `priority`. Thread stack is defined by `stack` and 'stacksz' arguments. Executed thread id is returned in `id` variable.

## `syscalls_endthread`

Terminates executing thread.

## `syscalls_usleep`

````C
GETFROMSTACK(ustack, unsigned int, us, 0);
````

Suspends thread execution for number of microseconds defined by `us`.

## `syscalls_mutexCreate`

````C
GETFROMSTACK(ustack, unsigned int *, h, 0);
````

Creates mutex and returns resource handle `h`.

## `syscalls_phMutexLock`

````C
GETFROMSTACK(ustack, unsigned int, h, 0);
````

Locks mutex given by handle `h`.

## `syscalls_mutexTry`

````C
GETFROMSTACK(ustack, unsigned int, h, 0);
````

Tries to lock mutex given by handle `h`.

## `syscalls_mutexUnlock`

````C
GETFROMSTACK(ustack, unsigned int, h, 0);
````

Unlocks mutex given by `h`.

## `syscalls_condCreate`

````C
GETFROMSTACK(ustack, unsigned int *, h, 0);
````

Creates conditional variable and returns its handle in variable `h`.

## `syscalls_phCondWait`

````C
GETFROMSTACK(ustack, unsigned int, h, 0);
GETFROMSTACK(ustack, unsigned int, m, 1);
GETFROMSTACK(ustack, time_t, timeout, 2);
````

Waits on conditional given by 'h' for number of microseconds giveb by `timeout`. Before suspending a calling thread execution mutex identified by `m` handle is unlocked to enable other thread modifying variables used to check condtionals after conditional signalisation. When conditional variable is signaled mutex `m` is locked.

## `syscalls_condSignal`

````C
GETFROMSTACK(ustack, unsigned int, h, 0);
````

Signals conditional given by `h`.

## `syscalls_condBroadcast`

````C
GETFROMSTACK(ustack, unsigned int, h, 0);
````

Signals conditional to all waiting threads.

## `syscalls_resourceDestroy`

````C
GETFROMSTACK(ustack, unsigned int, h, 0);
````

Destroys resource given by `h`.

## `syscalls_interrupt`

````C
GETFROMSTACK(ustack, unsigned int, n, 0);
GETFROMSTACK(ustack, void *, f, 1);
GETFROMSTACK(ustack, void *, data, 2);
GETFROMSTACK(ustack, unsigned int, cond, 3);
GETFROMSTACK(ustack, unsigned int *, handle, 4);
````

Installs interrupt handler `f` for interrupt given by `n`.

## `syscalls_portCreate`

````C
GETFROMSTACK(ustack, u32 *, port, 0);
````

Creates new communication queue and returns its identifier in `port` variable.

## `syscalls_portDestroy`

````C
GETFROMSTACK(ustack, u32, port, 0);
````

Destroys communication queue identified by `port` variable.

## `syscalls_portRegister`

````C
GETFROMSTACK(ustack, unsigned int, port, 0);
GETFROMSTACK(ustack, char *, name, 1);
GETFROMSTACK(ustack, oid_t *, oid, 2);
````

Registers `port` in the namespace at `name` and returns object identifier `oid` identifying this association.

## `syscalls_msgSend`

````C
GETFROMSTACK(ustack, u32, port, 0);
GETFROMSTACK(ustack, msg_t *, msg, 1);
````

Sends message `msg` to queue identified by `port`. Execution of calling thread is suspended until receiving thread responds to this message.

## `syscalls_msgRecv`

````C
GETFROMSTACK(ustack, u32, port, 0);
GETFROMSTACK(ustack, msg_t *, msg, 1);
GETFROMSTACK(ustack, unsigned long int *, rid, 2);
````

Receives message `msg` from queue identified by `port`. The reception context is stored in variable `rid`.

## `syscalls_msgRespond`

````C
GETFROMSTACK(ustack, u32, port, 0);
GETFROMSTACK(ustack, msg_t *, msg, 1);
GETFROMSTACK(ustack, unsigned long int, rid, 2);
````

Responds to message `msg` using reception context `rid`.

## `syscalls_lookup`

````C
GETFROMSTACK(ustack, char *, name, 0);
GETFROMSTACK(ustack, oid_t *, file, 1);
GETFROMSTACK(ustack, oid_t *, dev, 2);
````

Lookups for object identifier (`port` and resource `id`) associated with `name`. Object identifier representing file is returned in `file` variable. If file is associated with other object the other object id is returned in `dev`.

## `syscalls_gettime`

````C
GETFROMSTACK(ustack, time_t *, praw, 0);
GETFROMSTACK(ustack, time_t *, poffs, 1);
````

Returns current time in `praw` and `poffs` variables.

## `syscalls_settime`

````C
GETFROMSTACK(ustack, time_t, offs, 0);
````

Setup system time to value given by `offs`.

## `syscalls_keepidle`

````C
GETFROMSTACK(ustack, int, t, 0);
````

## `syscalls_mmdump`

Returns memory map entries associated with calling process.

## `syscalls_platformctl`

````C
GETFROMSTACK(ustack, void *, ptr, 0);
````

Executes platform controll call with argument given by `ptr`.

## `syscalls_wdgreload`

Reloads watchdog device when it is available.

## `syscalls_fileAdd`

````C
GETFROMSTACK(ustack, unsigned int *, h, 0);
GETFROMSTACK(ustack, oid_t *, oid, 1);
GETFROMSTACK(ustack, unsigned int, mode, 2);
````

Adds file given by `oid` to process resources. Added process resource is identified by handle returned in `h` variable. The access mode is set to `mode`.

## `syscalls_fileSet`

````C
GETFROMSTACK(ustack, unsigned int, h, 0);
GETFROMSTACK(ustack, char, flags, 1);
GETFROMSTACK(ustack, oid_t *, oid, 2);
GETFROMSTACK(ustack, offs_t, offs, 3);
GETFROMSTACK(ustack, unsigned, mode, 4);
````

Updates file parameters for file given by resource handle `h`.

## `syscalls_fileGet`

````C
GETFROMSTACK(ustack, unsigned int, h, 0);
GETFROMSTACK(ustack, int, flags, 1);
GETFROMSTACK(ustack, oid_t *, oid, 2);
GETFROMSTACK(ustack, offs_t *, offs, 3);
GETFROMSTACK(ustack, unsigned *, mode, 4);
````

Retrieves file parameters for file given by resource handle `h`.

## syscalls_fileRemove

````C
GETFROMSTACK(ustack, unsigned int, h, 0);
````

Removes file given by `h` from resources of calling process.



	## syscalls_threadsinfo) 
	## syscalls_meminfo) 
	## syscalls_perf_start) 
	## syscalls_perf_read) 
	## syscalls_perf_finish) 
	## syscalls_syspageprog) 
	## syscalls_va2pa) 
	## syscalls_signalHandle) 
	## syscalls_signalPost) 
	## syscalls_signalMask) 
	## syscalls_signalSuspend)

## `syscalls_priority`
````C
GETFROMSTACK(ustack, int, priority, 0);
````
	
## `syscalls_sys_read`
````C
````

	## syscalls_sys_write) 
	## syscalls_sys_open) 
	## syscalls_sys_close) 
	## syscalls_sys_link) 
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
	
	## syscalls_sys_accept) 
	## syscalls_sys_accept4) 
	## syscalls_sys_bind) 
	## syscalls_sys_connect) 
	## syscalls_sys_getpeername) 
	## syscalls_sys_getsockname) 
	## syscalls_sys_getsockopt) 
	## syscalls_sys_listen) 
	## syscalls_sys_recvfrom) 
	## syscalls_sys_sendto) 
	## syscalls_sys_socket) 
	## syscalls_sys_shutdown) 
	## syscalls_sys_setsockopt) 
	
	## syscalls_sys_ioctl) 
	## syscalls_sys_utimes) 
	## syscalls_sys_poll) 
	
	## syscalls_sys_tkill) 
	
	## syscalls_sys_setpgid) 
	## syscalls_sys_getpgid) 
	## syscalls_sys_setpgrp) 
	## syscalls_sys_getpgrp) 
	## syscalls_sys_setsid) 
## syscalls_sys_spawn

````C
GETFROMSTACK(ustack, char *, path, 0);
GETFROMSTACK(ustack, char **, argv, 1);
GETFROMSTACK(ustack, char **, envp, 2);
````

	## syscalls_release) 
	## syscalls_sbi_putchar) 
	## syscalls_sbi_getchar)