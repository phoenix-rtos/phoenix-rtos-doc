###Synopsis

`#include <unistd.h>`

`pid_t fork(void);`


###Description

The `fork()` function creates a new process. The new process (child process) is an exact copy of the calling process (parent process) except some exceptions.
 
Arguments:
None.

The differences between child and parent process are as follows:
   
 * The child process has a unique process ID.
 * The child process ID also does not match any active process group ID.
 * The child process has a different parent process ID, which is the process ID of the calling process.
 * The child process has its own copy of the parent's file descriptors. Each of the child's file descriptors refers to the same open file description with the corresponding file descriptor of the parent.
 * The child process has its own copy of the parent's open directory streams. Each open directory stream in the child process shares directory stream positioning with the corresponding directory stream of the parent.
 * The child process has its own copy of the parent's message catalogue descriptors.
 * The child process values of `tms_utime`, `tms_stime`, `tms_cutime`, and `tms_cstime` is set to `0`.
 * The time left until an alarm clock signal is reset to zero, and the alarm, if any, is cancelled.
 * All `semadj` values are cleared. 
 * File locks set by the parent process are not inherited by the child process.
 * The set of signals pending for the child process is initialized to the empty set.
 * Interval timers are reset in the child process. 
 * Any semaphores that are open in the parent process are also opened in the child process.
 * The child process does not inherit any address space memory locks established by the parent process via calls to `mlockall()` or `mlock()`. 
 * Memory mappings created in the parent are retained in the child process. `MAP_PRIVATE` mappings inherited from the parent are also `MAP_PRIVATE` mappings in the child, and any modifications to the data in these mappings made by the parent prior to calling `fork()` are visible to the child. Any modifications to the data in `MAP_PRIVATE` mappings made by the parent after `fork()` returns is visible only to the parent. Modifications to the data in `MAP_PRIVATE` mappings made by the child are visible only to the child.
 * For the `SCHED_FIFO` and `SCHED_RR` scheduling policies, the child process inherits the policy and priority settings of the parent process during a `fork()` function. 
 * Per-process timers created by the parent are not inherited by the child process.
 * The child process has its own copy of the message queue descriptors of the parent. Each of the message descriptors of the child refers to the same open message queue description as the corresponding message descriptor of the parent. 
 * No asynchronous input or asynchronous output operations are inherited by the child process. Any use of asynchronous control blocks created by the parent produces undefined behaviour.
 * A process is created with a single thread. If a multi-threaded process calls `fork()`, the new process contains a replica of the calling thread and its entire address space, possibly including the states of mutexes and other resources. Consequently, to avoid errors, the child process may only execute async-signal-safe operations until such time as one of the `exec` functions is called.
 * If the `Trace` option and the `Trace Inherit` option are both supported:
     If the calling process was being traced in a trace stream that had its inheritance policy set to `POSIX_TRACE_INHERITED`, the child process is traced into that trace stream, and the child process inherits the parent's mapping of trace event names to trace event type identifiers. If the trace stream in which the calling process was being traced had its inheritance policy set to `POSIX_TRACE_CLOSE_FOR_CHILD`, the child process is not traced into that trace stream. The inheritance policy is set by a call to the `posix_trace_attr_setinherited()` function. 
 * If the `Trace` option is supported, but the `Trace Inherit` option is not supported the child process is not traced into any of the trace streams of its parent process. 
 * If the `Trace` option is supported, the child process of a trace controller process does not control the trace streams controlled by its parent process. 
 * The initial value of the CPU-time clock of the child process is set to zero. 
 * The initial value of the CPU-time clock of the single thread of the child process is set to zero. 

After `fork()`, both the parent and the child processes are capable of executing independently before either one terminates.

###Return value

Upon successful completion, `fork()` returns `0` to the child process and returns the process ID of the child process to the parent process. Both processes continue to execute from the `fork()` function. 
Otherwise, `-1` is returned to the parent process, no child process is created, and `errno` is set to indicate the error.

###Errors

[`EAGAIN`] The system lacked the necessary resources to create another process, or the system-imposed limit on the total number of processes under execution system-wide or by a single user {`CHILD_MAX`} would be exceeded.
[`ENOMEM`] Insufficient storage space is available. 

###Implementation tasks

* Implement error handling.