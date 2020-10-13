# System calls

## `syscall_debug`
Displays string given by `s` on kernel console

## `syscalls_mmap`
Maps part of object given by `oid`, `offs` and `size` at `vaddr` with protection attributes given by `prot` using mapping mode defined by `flags`.

## `syscalls_munmap` 
## `syscalls_sys_fork` 
## `syscalls_vforksvc`
## `syscalls_exec` 
## `syscalls_sys_exit`
## `syscalls_sys_waitpid` 
## `syscalls_threadJoin`
## `syscalls_getpid` 
## `syscalls_getppid` 
## `syscalls_gettid`
	syscalls_beginthreadex) 
	syscalls_endthread) 
	syscalls_usleep) 
	syscalls_mutexCreate) 
	syscalls_phMutexLock) 
	syscalls_mutexTry) 
	syscalls_mutexUnlock) 
	syscalls_condCreate) 
	syscalls_phCondWait) 
	syscalls_condSignal) 
	syscalls_condBroadcast) 
	syscalls_resourceDestroy) 
	syscalls_interrupt) 
	syscalls_portCreate) 
	syscalls_portDestroy) 
	syscalls_portRegister) 
	syscalls_msgSend) 
	syscalls_msgRecv) 
	syscalls_msgRespond) 
	## syscalls_lookup) 
	## syscalls_gettime) 
	## syscalls_settime) 
	## syscalls_keepidle) 
	## syscalls_mmdump) 
	## syscalls_platformctl) 
	## syscalls_wdgreload) 
	## syscalls_fileAdd) 
	## syscalls_fileSet) 
	## syscalls_fileGet) 
	## syscalls_fileRemove) 
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
	## syscalls_priority) 
	
	## syscalls_sys_read) 
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
	## syscalls_sys_spawn) 
	## syscalls_release) 
	## syscalls_sbi_putchar) 
	## syscalls_sbi_getchar)