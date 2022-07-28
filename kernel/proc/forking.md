# Kernel - Processes and threads - Processes creation

Processes are created in Phoenix-RTOS using forking technique. When new process is created the current process forks into two instances - parent and child. There are two functions used for process creation in Phoenix-RTOS - each of them should be used depending on the platform and MMU presence. The differences between these functions and circumstnces of their usage are discussed in this chapter.

## Creating new process using `fork()`

The well-known method of creating new process in general purpose operting systems (e.g. UN*X) is a forking. The explanation of this method is quite simple. In the certain point of time process calls `fork()` system call which creates new process (child process) based on linear address space and operating system resources used by process calling `fork()` (parent process). From this point of time processess are separated and their operate on their own address spaces what means that all modification of process memory are visible only within them. For example lets consider process A forking into processes A and B. After forking, process A modifies variable located at address `addr` and stores there value 1 and process B modifies the same variable at address `addr` and stores there 2. The modification are specific for the forked processes and operating system assures that process A sees the variable located at `addr` as 1 and process B sees it as 2.

This technique can be only implemented only on processors equipped with MMU providing mechansms for memory virtualization (e.g. paging) which enables programs to use the same linear address to access different segments of physical memory. On processors lacked of MMU the `fork()` method is unavailable and it is replaced by `vfork()`.

## Creating new process using `vfork()`

Historically vfork() is designed to be used in the specific case where the child will exec() another program, and the parent can block until this happens. A traditional fork() requires duplicating all the memory of the parent process in the child what leads to a significant overhead. The goal of the vfork() function was to reduce this overhead by preventing unecessary memory copying when new process is created. Usually after proces creation using fork() function a new program is executed. In such case traditional fork before exec() leads to unecessary overhead (memory is copied to the child process then is freed and replaced by new memory objects as the result of exec()).

In UN*X operatng system history "The Mach VM system" added Copy On Write (COW), which made the fork() much cheaper, and in BSD 4.4, vfork() was made synonymous to fork().

vfork() function has another important repercussions for non-MMU architectures. Because of it semantics it allows to launch a new process it the same way like using fork() what enables application portability.

Some consider the semantics of vfork() to be an architectural blemish and POSIX.1-2008 removed vfork() from the standard and replaced by posix_spawn(). The POSIX rationale for the posix_spawn() function notes that that function, which provides functionality equivalent to fork()+exec(), is designed to be implementable on systems that lack an MMU.

## Process termination

## Binary object (program) execution

## Thread management

## See also

1. [Kernel - Processes and threads](README.MD)
2. [Kernel - Processes and threads - Synchronization primitives](sync.md)
3. [Kernel - Processes and threads - Message passing](msg.md)
4. [Kernel - Processes and threads - Namespace](namespace.md)
5. [Table of Contents](../../README.md)
