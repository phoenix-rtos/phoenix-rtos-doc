# Processes creation

Processes are created in Phoenix-RTOS using forking technique. When new process should be created the current process forks into two instances - parent and child.

## Creating new process using fork()

The well-known method of creating new process in general purpose operting systems (e.g. UN*X) is forking technique. The explanation of this method is quite simple. In certain point of time process calls `fork()` system call which creates new process (child process) based on address space and operating system resources used by process calling `fork()` (named parent process). From this point of time processess are separated and their operate and own address spaces what means that all modification of memory are visible only in processes modifying this memory.

This technique can be effectively implemented on processors equipped with MMU providing mechansms for memory virtualization (e.g. paging) which enables programs to use the same linear address to access different segments of physical memory.

## Creating new process using vfork()


## See also

1. [Kernel - Processes and threads](README.MD)
2. [Kernel - Processes and threads - Synchronization primitives](sync.md)
3. [Kernel - Processes and threads - Message passing](msg.md)
4. [Kernel - Processes and threads - Namespace](namespace.md)
5. [Table of Contents](../../README.md)