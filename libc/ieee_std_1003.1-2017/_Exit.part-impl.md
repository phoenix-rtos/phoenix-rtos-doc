###Synopsis
`#include <stdlib.h>`
`void _Exit(int status);`

`#include <unistd.h>`
`void _exit(int status);`

###Description

The `_Exit()` and `_exit()` functions terminate the calling process. 

The value of status may be `0`, `EXIT_SUCCESS`, `EXIT_FAILURE`, or any other value, though only the least significant 8 bits (that is, `status & 0xff`) are available from `wait()` and `waitpid()`; the full value is available from `waitid()` and in the `siginfo_t` passed to a signal handler for `SIGCHLD`.

The functions do not call functions registered with `atexit()` nor any registered signal handlers. Open streams are not flushed, but opened file descriptors are closed. Finally, the calling process is terminated with the consequences described below.

###Consequences of Process Termination:

* All of the file descriptors, directory streams, conversion descriptors, and message catalog descriptors open in the calling process are closed.
* If the parent process of the calling process has set the action for the `SIGCHLD` signal to `SIG_IGN`:
    - The process' status information, if any, is discarded.
    - The lifetime of the calling process ends immediately and a `SIGCHLD` signal is sent to the parent process.
    - If a thread in the parent process of the calling process is blocked in `wait()`, `waitpid()`, or `waitid()`, and the parent process has no remaining child processes in the set of waited-for children, the `wait()`, `waitid()`, or `waitpid()` function fails and sets errno to `[ECHILD]`.
* Otherwise:
    - Status information is generated.
    - The calling process is transformed into a zombie process. Its status information is made available to the parent process until the process' lifetime ends.
    - The process' lifetime ends once its parent obtains the process' status information via a currently-blocked or future call to `wait()`, `waitid()` (without WNOWAIT), or `waitpid()`.
    - If one or more threads in the parent process of the calling process is blocked in a call to `wait()`, `waitid()`, or `waitpid()` awaiting termination of the process, one (or, if any are calling waitid() with `WNOWAIT`, possibly more) of these threads obtains the process' status information as specified in Status Information and becomes unblocked.
    - A `SIGCHLD` is sent to the parent process.
* Termination of a process does not directly terminate its children. The sending of a `SIGHUP` signal as described below indirectly terminates children in some circumstances.
* If the process is a controlling process, the SIGHUP signal is sent to each process in the foreground process group of the controlling terminal belonging to the calling process. 
* If the process is a controlling process, the controlling terminal associated with the session is disassociated from the session, allowing it to be acquired by a new controlling process.
* The parent process ID of all of the existing child processes and zombie processes of the calling process are set to the process ID of an `init` system process. That is, these processes are inherited by a `init` process.
* Memory mappings that were created in the process are unmapped before the process is destroyed.
* Threads terminated by a call to `_Exit()` do not invoke their cancellation cleanup handlers or per-thread data destructors.
* If the calling process is a trace controller process, any trace streams that were created by the calling process are shut down as described by the `posix_trace_shutdown()` function, and mapping of trace event names to trace event type identifiers of any process built for these trace streams may be deallocated. 

###Return value

The functions can never return.

###Errors

No errors are defined.

###Implementation tasks

* after the process' death all its streams are closed in the sense as all its file descriptors are closed are closed;
* implement init() process which executes wait() properly after the orphan process death,
* implement shared memory and api shm,
* implement signal handling to: " If the exit of the process causes a process group to become orphaned, and if any member of the newly-orphaned process group is stopped, then a SIGHUP signal followed by a SIGCONT signal is sent to each process in the newly-orphaned process group."
* implement typed memory handling to make possible: "Any blocks of typed memory that were mapped in the calling process are unmapped, as if munmap() was implicitly called to unmap them."  
* implement posix_trace_ with all its functions,
* implement the process' SA_NOCLDWAIT flag and its handling,
* implement the asynchronous I/O operations,
* implement semaphors handling,
* implement memory  locks,
* implement message queues,
* implement the full   controlling terminal of the session handling especially add process' death handling in the controlling terminal handling,

###Tests

======

###EXAMPLES
None.











APPLICATION USAGE
Normally applications should use exit() rather than _Exit() or _exit().

RATIONALE
Process Termination
Early proposals drew a distinction between normal and abnormal process termination. Abnormal termination was caused only by certain signals and resulted in implementation-defined "actions", as discussed below. Subsequent proposals distinguished three types of termination: normal termination (as in the current specification), simple abnormal termination, and abnormal termination with actions. Again the distinction between the two types of abnormal termination was that they were caused by different signals and that implementation-defined actions would result in the latter case. Given that these actions were completely implementation-defined, the early proposals were only saying when the actions could occur and how their occurrence could be detected, but not what they were. This was of little or no use to conforming applications, and thus the distinction is not made in this volume of POSIX.1-2017.

The implementation-defined actions usually include, in most historical implementations, the creation of a file named core in the current working directory of the process. This file contains an image of the memory of the process, together with descriptive information about the process, perhaps sufficient to reconstruct the state of the process at the receipt of the signal.

There is a potential security problem in creating a core file if the process was set-user-ID and the current user is not the owner of the program, if the process was set-group-ID and none of the user's groups match the group of the program, or if the user does not have permission to write in the current directory. In this situation, an implementation either should not create a core file or should make it unreadable by the user.

Despite the silence of this volume of POSIX.1-2017 on this feature, applications are advised not to create files named core because of potential conflicts in many implementations. Some implementations use a name other than core for the file; for example, by appending the process ID to the filename.

Terminating a Process
It is important that the consequences of process termination as described occur regardless of whether the process called _exit() (perhaps indirectly through exit()) or instead was terminated due to a signal or for some other reason. Note that in the specific case of exit() this means that the status argument to exit() is treated in the same way as the status argument to _exit().

A language other than C may have other termination primitives than the C-language exit() function, and programs written in such a language should use its native termination primitives, but those should have as part of their function the behavior of _exit() as described. Implementations in languages other than C are outside the scope of this version of this volume of POSIX.1-2017, however.

As required by the ISO C standard, using return from main() has the same behavior (other than with respect to language scope issues) as calling exit() with the returned value. Reaching the end of the main() function has the same behavior as calling exit(0).

A value of zero (or EXIT_SUCCESS, which is required to be zero) for the argument status conventionally indicates successful termination. This corresponds to the specification for exit() in the ISO C standard. The convention is followed by utilities such as make and various shells, which interpret a zero status from a child process as success. For this reason, applications should not call exit(0) or _exit(0) when they terminate unsuccessfully; for example, in signal-catching functions.

Historically, the implementation-defined process that inherits children whose parents have terminated without waiting on them is called init and has a process ID of 1.

The sending of a SIGHUP to the foreground process group when a controlling process terminates corresponds to somewhat different historical implementations. In System V, the kernel sends a SIGHUP on termination of (essentially) a controlling process. In 4.2 BSD, the kernel does not send SIGHUP in a case like this, but the termination of a controlling process is usually noticed by a system daemon, which arranges to send a SIGHUP to the foreground process group with the vhangup() function. However, in 4.2 BSD, due to the behavior of the shells that support job control, the controlling process is usually a shell with no other processes in its process group. Thus, a change to make _exit() behave this way in such systems should not cause problems with existing applications.

The termination of a process may cause a process group to become orphaned in either of two ways. The connection of a process group to its parent(s) outside of the group depends on both the parents and their children. Thus, a process group may be orphaned by the termination of the last connecting parent process outside of the group or by the termination of the last direct descendant of the parent process(es). In either case, if the termination of a process causes a process group to become orphaned, processes within the group are disconnected from their job control shell, which no longer has any information on the existence of the process group. Stopped processes within the group would languish forever. In order to avoid this problem, newly orphaned process groups that contain stopped processes are sent a SIGHUP signal and a SIGCONT signal to indicate that they have been disconnected from their session. The SIGHUP signal causes the process group members to terminate unless they are catching or ignoring SIGHUP. Under most circumstances, all of the members of the process group are stopped if any of them are stopped.

The action of sending a SIGHUP and a SIGCONT signal to members of a newly orphaned process group is similar to the action of 4.2 BSD, which sends SIGHUP and SIGCONT to each stopped child of an exiting process. If such children exit in response to the SIGHUP, any additional descendants receive similar treatment at that time. In this volume of POSIX.1-2017, the signals are sent to the entire process group at the same time. Also, in this volume of POSIX.1-2017, but not in 4.2 BSD, stopped processes may be orphaned, but may be members of a process group that is not orphaned; therefore, the action taken at _exit() must consider processes other than child processes.

It is possible for a process group to be orphaned by a call to setpgid() or setsid(), as well as by process termination. This volume of POSIX.1-2017 does not require sending SIGHUP and SIGCONT in those cases, because, unlike process termination, those cases are not caused accidentally by applications that are unaware of job control. An implementation can choose to send SIGHUP and SIGCONT in those cases as an extension; such an extension must be documented as required in <signal.h>.

The ISO/IEC 9899:1999 standard adds the _Exit() function that results in immediate program termination without triggering signals or atexit()-registered functions. In POSIX.1-2017, this is equivalent to the _exit() function.

FUTURE DIRECTIONS
None.

SEE ALSO
atexit, exit, mlock, mlockall, mq_close, munmap, posix_trace_create, sem_close , semop, setpgid, setsid, shmget, wait, waitid

XBD <stdlib.h>, <unistd.h>

CHANGE HISTORY
First released in Issue 1. Derived from Issue 1 of the SVID.

Issue 5
The DESCRIPTION is updated for alignment with the POSIX Realtime Extension and the POSIX Threads Extension.

Interactions with the SA_NOCLDWAIT flag and SIGCHLD signal are further clarified.

The values of status from exit() are better described.

Issue 6
Extensions beyond the ISO C standard are marked.

The DESCRIPTION is updated for alignment with IEEE Std 1003.1j-2000 by adding semantics for typed memory.

The following changes are made for alignment with the ISO/IEC 9899:1999 standard:

The _Exit() function is included.

The DESCRIPTION is updated.

The description of tracing semantics is added for alignment with IEEE Std 1003.1q-2000.

References to the wait3() function are removed.

IEEE Std 1003.1-2001/Cor 1-2002, item XSH/TC1/D6/16 is applied, correcting grammar in the DESCRIPTION.

Issue 7
Austin Group Interpretation 1003.1-2001 #031 is applied, separating these functions from the exit() function.

Austin Group Interpretation 1003.1-2001 #085 is applied, clarifying the text regarding flushing of streams and closing of temporary files.

Functionality relating to the Asynchronous Input and Output, Memory Mapped Files, and Semaphores options is moved to the Base.

POSIX.1-2008, Technical Corrigendum 2, XSH/TC2-2008/0033 [594] and XSH/TC2-2008/0034 [594,690] are applied.

End of informative text.