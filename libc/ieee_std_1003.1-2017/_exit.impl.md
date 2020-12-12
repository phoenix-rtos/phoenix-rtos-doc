### Synopsis
`#include <stdlib.h>`

`void _exit(int status);`

### Description


The `_exit()` function terminates the calling process. 

The value of status may be `0`, `EXIT_SUCCESS`, `EXIT_FAILURE`, or any other value, though only the least significant 8 bits (that is, `status & 0xff`) are available from `wait()` and `waitpid()`; the full value is available from `waitid()` and in the `siginfo_t` passed to a signal handler for `SIGCHLD`.

The `_exit()` function does not call functions registered with `atexit()` nor any registered signal handlers. Open streams are not flushed. Whether open streams are closed (without flushing) is implementation-defined. Finally, the calling process is terminated with the consequences described below.

### Consequences of Process Termination:

* All of the file descriptors, directory streams, conversion descriptors, and message catalog descriptors open in the calling process are closed.

* If the parent process of the calling process has set its `SA_NOCLDWAIT` flag or has set the action for the `SIGCHLD` signal to `SIG_IGN`:

  * The process' status information, if any, is discarded.

  * The lifetime of the calling process ends immediately. If `SA_NOCLDWAIT` is set, it is implementation-defined whether a `SIGCHLD` signal is sent to the parent process.

  * If a thread in the parent process of the calling process is blocked in `wait()`, `waitpid()`, or `waitid()`, and the parent process has no remaining child processes in the set of waited-for children, the `wait()`, `waitid()`, or `waitpid()` function fails and sets errno to `[ECHILD]`.

* Otherwise:

  * Status information is generated.
    - The calling process is transformed into a zombie process. Its status information is made available to the parent process until the process' lifetime ends.
    - The process' lifetime shall end once its parent obtains the process' status information via a currently-blocked or future call to `wait()`, `waitid()` (without WNOWAIT), or `waitpid()`.
    - If one or more threads in the parent process of the calling process is blocked in a call to `wait()`, `waitid()`, or `waitpid()` awaiting termination of the process, one (or, if any are calling waitid() with `WNOWAIT`, possibly more) of these threads obtains the process' status information as specified in Status Information and becomes unblocked.
    - A `SIGCHLD` is sent to the parent process.
* Termination of a process does not directly terminate its children. The sending of a `SIGHUP` signal as described below indirectly terminates children in some circumstances.
* The parent process ID of all of the existing child processes and zombie processes of the calling process are set to the process ID of an implementation-defined system process. That is, these processes are inherited by a special system process.
* Each attached shared-memory segment is detached and the value of `shm_nattch` (see `shmget`()) in the data structure associated with its shared memory ID shall be decremented by 1.  
* For each semaphore for which the calling process has set a semadj value (see semop()), that value is added to the semval of the specified semaphore.  
* If the process is a controlling process, the `SIGHUP` signal is sent to each process in the foreground process group of the controlling terminal belonging to the calling process.
* If the process is a controlling process, the controlling terminal associated with the session is disassociated from the session, allowing it to be acquired by a new controlling process.
* If the exit of the process causes a process group to become orphaned, and if any member of the newly-orphaned process group is stopped, then a `SIGHUP` signal followed by a `SIGCONT` signal is sent to each process in the newly-orphaned process group.
  * All open named semaphores in the calling process are closed as if by appropriate calls to `sem_close()`.
  * Any memory locks established by the process via calls to `mlockall`() or mlock() shall be removed. If locked pages in the address space of the calling process are also mapped into the address spaces of other processes and are locked by those processes, the locks established by the other processes shall be unaffected by the call by this process to _Exit().
  * Memory mappings that were created in the process shall be unmapped before the process is destroyed.
  * Any blocks of typed memory that were mapped in the calling process shall be unmapped, as if `munmap()` was implicitly called to unmap them.  
  * All open message queue descriptors in the calling process shall be closed as if by appropriate calls to `mq_close()`. 
  * Any outstanding cancelable asynchronous I/O operations may be cancelled. Those asynchronous I/O operations that are not cancelled  shall complete as if the `_Exit`() operation had not yet occurred, but any associated signal notifications shall be suppressed. The `_Exit()` operation may block awaiting such I/O completion. Whether any I/O is cancelled, and which I/O may be cancelled upon _Exit(), is implementation-defined.
  * Threads terminated by a call to `_Exit()` shall not invoke their cancellation cleanup handlers or per-thread data destructors.
  * If the calling process is a trace controller process, any trace streams that were created by the calling process shall be shut down as described by the `posix_trace_shutdown()` function, and mapping of trace event names to trace event type identifiers of any process built for these trace streams may be deallocated. 


### Return value

`_exit()` can never return.

### Errors
No errors are defined.