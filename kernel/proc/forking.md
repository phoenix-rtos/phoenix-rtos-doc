# Kernel - Processes and threads - Processes creation

Processes are created in Phoenix-RTOS using forking technique. When new process is created the current process forks into two instances - parent and child.

## Creating new process using `fork()`

The well-known method of creating new process in general purpose operting systems (e.g. UN*X) is a forking. The explanation of this method is quite simple. In the certain point of time process calls `fork()` system call which creates new process (child process) based on linear address space and operating system resources used by process calling `fork()` (parent process). From this point of time processess are separated and their operate on their own address spaces what means that all modification of process memory are visible only within them. For example lets consider process A forking into processes A and B. After forking, process A modifies variable located at address `addr` and stores there value 1 and process B modifies the same variable at address `addr` and stores there 2. The modification are specific for the forked processes and operating system assures that process A sees the variable located at `addr` as 1 and process B sees it as 2.

This technique can be only implemented on processors equipped with MMU providing mechansms for memory virtualization (e.g. paging) which enables programs to use the same linear address to access different segments of physical memory. On processors lacked of MMU the `fork()` method is unavailable and it is replaced by `vfork()`.

## Creating new process using `vfork()`


## See also

1. [Kernel - Processes and threads](README.MD)
2. [Kernel - Processes and threads - Synchronization primitives](sync.md)
3. [Kernel - Processes and threads - Message passing](msg.md)
4. [Kernel - Processes and threads - Namespace](namespace.md)
5. [Table of Contents](../../README.md)