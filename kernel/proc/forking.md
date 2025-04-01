# Management

Processes are created in Feniks-RTOS using forking technique. When new process is created the current process
forks into two processes - parent (process which initializes fork) and child. There are two forking functions
used for process creation in Feniks-RTOS - each of them should be used depending on the platform and MMU presence.
The differences between these functions and circumstances of their usage are discussed in this chapter.

## Creating new process using `fork()`

The well-known method of creating new process in general purpose operating systems (e.g. UN*X) is a forking.
The explanation of this method is quite simple. In the certain point of time a thread within a process calls `fork()`
system call which creates a new process (child process) based on linear address space and operating system resources
used by process calling `fork()` (parent process) and launches the thread within a child process. From this point of
time processes are separated, and they operate on their own address spaces. It means that all modifications of process
memory are visible only within them. For example, let's consider process A forking into processes A and B.
After forking, one of the threads of process A modifies variable located at address `addr` and stores their value 1
and thread of process B modifies the same variable at address `addr` and stores there 2. The modification is specific
for the forked processes, and operating system assures that process A sees the variable located at `addr`
as 1 and process B sees it as 2.

This technique can be only implemented when processors are equipped with MMU providing mechanisms for memory
virtualization (e.g. paging) which enables programs to use the same linear address to access different segments of
physical memory. On processors lacked of MMU the `fork()` method is unavailable, and it is replaced by `vfork()`.

## Creating new process using `vfork()`

Historically `vfork()` is designed to be used in the specific case where the child will `exec()` another program, and
the parent can block until this happens. A traditional `fork()` requires duplicating all the memory of the parent
process in the child which leads to significant overhead. The goal of the `vfork()` function was to reduce this
overhead by preventing unnecessary memory copying when new process is created. Usually, after process creation using
`fork()` function a new program is executed. In such case, traditional fork before `exec()` leads to unnecessary
overhead (memory is copied to the child process and then is freed and replaced by new memory objects as the result of
`exec()`).

In UN*X operating system history "The Mach VM system" added Copy On Write (COW), which made the `fork()` much cheaper,
and in BSD 4.4, `vfork()` was made synonymous to `fork()`.

`vfork()` function has another important repercussion for non-MMU architectures. Because of semantics, it allows
launching a new process in the same way as using `fork()` which enables application portability.

Some consider the semantics of `vfork()` to be an architectural blemish and POSIX.1-2008 removed `vfork()` from the
standard and replaced it with `posix_spawn()`. The POSIX rationale for the `posix_spawn()` function notes that that
function, which provides functionality equivalent to `fork()`+`exec()`, is designed to be implementable on
systems that lack an MMU.

## Process termination

Process can be terminated abnormally - as the consequence of receiving signal or normally after executing `exit()`
function. When process exits all of its threads are terminated, all memory objects are unmapped and all resource handles
are freed/closed. The parent process receives `SIGCHLD` signal notifying it about the child termination. `SIGCHLD`
signal plays another important role in process termination sequence. It allows to safe remove the remaining child
process resources which are not able to be removed during the process runtime (e.g. last thread kernel stack).

## Program execution

To execute a new program the binary object representing it should be mapped into the process linear address space and
control have to be passed to the program entry point. This is the responsibility of `exec()` family functions.

On non-MMU architectures, there is one important step performed after a binary object is mapped and before control is
passed to the program entry point. This step is the program relocation which recalculates some program structures
(e.g. `GOT`) used for accessing variables during the runtime. The relocation depends on the current memory location of
program.

## Thread management

While process represents a memory space and operating system resources devoted for particular executed program the
thread represents the program instruction stream executed concurrently to other threads in the process context
(using defined linear address space and associated operating system resources). To manage threads `beginthread()`,
`endthread()` functions should be used.

`beginthread()` function starts a new thread using function address and stack allocated by a calling thread. The kernel
stacks for all of desired thread execution modes are allocated. `endthread()` function terminates calling thread and
releases allocated kernel stacks.

## See also

1. [Kernel - Processes and threads](index.md)
2. [Kernel - Processes and threads - Scheduler](scheduler.md)
3. [Kernel - Processes and threads - Synchronization primitives](sync.md)
4. [Kernel - Processes and threads - Message passing](msg.md)
5. [Kernel - Processes and threads - Namespace](namespace.md)
6. [Table of Contents](../../index.md)
