###Synopsis

`#include <unistd.h>`

`extern char **environ;`
`int execl(const char *path, const char *arg0, ... /*, (char *)0 */);`
`int execle(const char *path, const char *arg0, ... /*,*/`
`       (char *)0, char *const envp[]*/);`
`int execlp(const char *file, const char *arg0, ... /*, (char *)0 */);`
`int execv(const char *path, char *const argv[]);`
`int execve(const char *path, char *const argv[], char *const envp[]);`
`int execvp(const char *file, char *const argv[]);`
`int fexecve(int fd, char *const argv[], char *const envp[]);`

###Description

Each function in the `exec` family of functions replaces the current process image with a new process image. The new image is constructed from a regular, executable file called the new process image file. There is no return from a successful `exec`, because the calling process image is overlaid by the new process image.

Arguments:
    
<u>path</u> - a pathname that identifies the new process image file,
<u>arg0</u> - a filename string that is associated with the process being started by the exec function,
<u>argv</u> - an array of character pointers to null-terminated strings. The application ensures that the last member of this array is a null pointer. These strings constitute the argument list available to the new process image. The value in `argv[0]` points to a filename string that is associated with the process being started by one of the `exec` functions.
<u>envp</u> - an array of character pointers to null-terminated strings. These strings constitute the environment for the new process image. The <u>envp</u> array is terminated by a null pointer.
<u>file</u> - used to construct a pathname that identifies the new process image file. If the <u>file</u> argument contains a <slash> character, the <u>file</u> argument is used as the pathname for this file. 
<u>fd</u> - a file descriptor identifying the new process image file,


When a C-language program is executed as a result of a call to one of the exec family of functions, it is entered as a C-language function call as follows:

`int main (int argc, char *argv[]);`

where `argc` is the argument count and `argv` is an array of character pointers to the arguments themselves. In addition, the following variable, which must be declared by the user if it is to be used directly:

`extern char **environ;`

is initialized as a pointer to an array of character pointers to the environment strings. The `argv` and environ arrays are each terminated by a null pointer. The null pointer terminating the `argv` array is not counted in `argc`.

Applications can change the entire environment in a single operation by assigning the `environ` variable to point to an array of character pointers to the new environment strings. After assigning a new value to `environ`, applications should not rely on the new environment strings remaining part of the environment, as a call to `getenv()`, `putenv()`, `setenv()`, `unsetenv()`, or any function that is dependent on an environment variable may, on noticing that environ has changed, copy the environment strings to a new array and assign `environ` to point to it.

Any application that directly modifies the pointers to which the environ variable points has undefined behavior.

Conforming multi-threaded applications do not use the `environ` variable to access or modify any environment variable while any other thread is concurrently modifying any environment variable. A call to any function dependent on any environment variable shall be considered a use of the `environ` variable to access that environment variable.

The arguments specified by a program with one of the `exec` functions are passed on to the new process image in the corresponding `main()` arguments.

There are two distinct ways in which the contents of the process image file may cause the execution to fail, distinguished by the setting of `errno` to either [`ENOEXEC`] or [`EINVAL`]. In the cases where the other members of the exec family of functions would fail and set `errno` to [`ENOEXEC`], the `execlp()` and `execvp()` functions execute a command interpreter and the environment of the executed command is as if the process invoked the `sh` utility using `execl()` as follows:

`execl(<shell path>, arg0, file, arg1, ..., (char *)0);`

where <`shell path`> is an unspecified pathname for the `sh` utility, <u>file</u> is the process image file, and for `execvp()`, where <u>arg0</u>, <u>arg1</u>, and so on correspond to the values passed to `execvp()` in <u>argv[0]</u>, <u>argv[1]</u>, and so on.

The arguments represented by <u>arg0</u>,... are pointers to null-terminated character strings. These strings constitute the argument list available to the new process image. The list is terminated by a null pointer. The argument `arg0` points to a filename string that is associated with the process being started by one of the `exec` functions.

For those forms not containing an <u>envp</u> pointer (`execl()`, `execv()`, `execlp()`, and `execvp()`), the environment for the new process image is taken from the external variable `environ` in the calling process.

The number of bytes available for the new process' combined argument and environment lists is {`ARG_MAX`}. 

File descriptors open in the calling process image remain open in the new process image, except for those whose close-on- exec flag `FD_CLOEXEC` is set. For those file descriptors that remain open, all attributes of the open file description remain unchanged. For any file descriptor that is closed for this reason, file locks are removed as a result of the close as described in `close()`. Locks that are not removed by closing of file descriptors remain unchanged.

If file descriptor `0`, `1`, or `2` would otherwise be closed after a successful call to one of the `exec` family of functions, implementations may open an unspecified file for the file descriptor in the new process image. 

Directory streams open in the calling process image are closed in the new process image.

The state of the floating-point environment in the initial thread of the new process image is set to the default.

The state of conversion descriptors and message catalog descriptors in the new process image is undefined.

For the new process image, the:

`setlocale(LC_ALL, "C")`

is executed at start-up.

Signals set to the default action (`SIG_DFL`) in the calling process image are set to the default action in the new process image. Except for `SIGCHLD`, signals set to be ignored (`SIG_IGN`) by the calling process image are set to be ignored by the new process image. Signals set to be caught by the calling process image are set to the default action in the new process image.

If the `SIGCHLD` signal is set to be ignored by the calling process image, it is unspecified whether the `SIGCHLD` signal is set to be ignored or to the default action in the new process image.

After a successful call to any of the `exec` functions, alternate signal stacks are not preserved and the `SA_ONSTACK` flag is cleared for all signals.

After a successful call to any of the `exec` functions, any functions previously registered by the `atexit()` or `pthread_atfork()` functions are no longer registered.

If the `ST_NOSUID` bit is set for the file system containing the new process image file, then the effective user ID, effective group ID, saved set-user-ID, and saved set-group-ID are unchanged in the new process image. Otherwise, if the set-user-ID mode bit of the new process image file is set, the effective user ID of the new process image is set to the user ID of the new process image file. Similarly, if the set-group-ID mode bit of the new process image file is set, the effective group ID of the new process image is set to the group ID of the new process image file. The real user ID, real group ID, and supplementary group IDs of the new process image remain the same as those of the calling process image. The effective user ID and effective group ID of the new process image are saved (as the saved set-user-ID and the saved set-group-ID) for use by `setuid()`.

Any shared memory segments attached to the calling process image are not attached to the new process image.
Any named semaphores open in the calling process are closed as if by appropriate calls to `sem_close()`.

Any blocks of typed memory that were mapped in the calling process are unmapped, as if `munmap()` was implicitly called to unmap them. 

Memory locks established by the calling process via calls to `mlockall()` or `mlock()` are removed. If locked pages in the address space of the calling process are also mapped into the address spaces of other processes and are locked by those processes, the locks established by the other processes are not affected by the call by this process to the `exec` function. If the `exec` function fails, the effect on memory locks is unspecified.

Memory mappings created in the process are unmapped before the address space is rebuilt for the new process image.

When the calling process image does not use the `SCHED_FIFO`, `SCHED_RR`, or `SCHED_SPORADIC` scheduling policies, the scheduling policy and parameters of the new process image and the initial thread in that new process image are implementation-defined.

When the calling process image uses the `SCHED_FIFO`, `SCHED_RR`, or `SCHED_SPORADIC` scheduling policies, the process policy and scheduling parameter settings are not changed by a call to an `exec` function. The initial thread in the new process image inherits the process scheduling policy and parameters. It has the default system contention scope, but inherits its allocation domain from the calling process image.

Per-process timers created by the calling process are deleted before replacing the current process image with the new process image.

All open message queue descriptors in the calling process are closed.

Any outstanding asynchronous I/O operations may be canceled. Those asynchronous I/O operations that are not canceled complete as if the `exec` function had not yet occurred, but any associated signal notifications are suppressed and the `exec` function itself blocks awaiting such I/O completion. In no event, however, the new process image created by the `exec` function be affected by the presence of outstanding asynchronous I/O operations at the time the `exec` function is called.

The new process image inherits the CPU-time clock of the calling process image. This inheritance means that the process CPU-time clock of the process being exec-ed are not reinitialized or altered as a result of the `exec` function other than to reflect the time spent by the process executing the `exec` function itself. 

The initial value of the CPU-time clock of the initial thread of the new process image is set to zero.

If the calling process is being traced, the new process image continues to be traced into the same trace stream as the original process image, but the new process image does not inherit the mapping of trace event names to trace event type identifiers that was defined by calls to the `posix_trace_eventid_open()` or the `posix_trace_trid_eventid_open()` functions in the calling process image.

If the calling process is a trace controller process, any trace streams that were created by the calling process are shut down as described in the `posix_trace_shutdown()` function.

The initial thread in the new process image has its cancellation type set to `PTHREAD_CANCEL_DEFERRED` and its cancellation state set to `PTHREAD_CANCEL_ENABLED`.

The initial thread in the new process image has all thread-specific data values set to `NULL` and all thread-specific data keys are removed by the call to `exec` without running destructors.

The initial thread in the new process image is joinable, as if created with the detachstate attribute set to `PTHREAD_CREATE_JOINABLE`.

The new process inherits the following attributes from the calling process image:

 * Nice value
 * semadj values 
 * Process ID
 * Parent process ID
 * Process group ID
 * Session membership
 * Real user ID
 * Real group ID
 * Supplementary group IDs
 * Time left until an alarm clock signal 
 * Current working directory
 * Root directory
 * File mode creation mask
 * File size limit 
 * Process signal mask
 * Pending signal
 * tms_utime, tms_stime, tms_cutime, and tms_cstime 
 * Resource limits
 * Controlling terminal
 * Interval timers 

The initial thread of the new process inherits the following attributes from the calling thread:

 * Signal mask
 * Pending signals

All other process attributes are inherited in the new process image from the old process image. All other thread attributes are inherited in the initial thread in the new process image from the calling thread in the old process image. 

A call to any `exec` function from a process with more than one thread results in all threads being terminated and the new executable image loaded and executed. No destructor functions or cleanup handlers are called.

Upon successful completion, the `exec` functions mark for update the last data access timestamp of the file. If an `exec` function failed but was able to locate the process image file, whether the last data access timestamp is marked for update is unspecified. Should the exec function succeed, the process image file shall be considered to have been opened with open(). The corresponding close() shall be considered to occur at a time after this open, but before process termination or successful completion of a subsequent call to one of the `exec` functions, `posix_spawn()`, or `posix_spawnp()`. The `argv[]` and `envp[]` arrays of pointers and the strings to which those arrays point are not modified by a call to one of the `exec` functions, except as a consequence of replacing the process image.

The saved resource limits in the new process image are set to be a copy of the process' corresponding hard and soft limits. 
    
The `fexecve()` function is equivalent to the `execve()` function except that the file to be executed is determined by the file descriptor <u>fd</u> instead of a pathname. The file offset of <u>fd</u> is ignored.

###Return value

On success the functions do not return. If one of the `exec` functions returns to the calling process image, an error has occurred. The return value is then `-1`, and `errno` is set to indicate the error.

###Errors

The `exec` functions fail if:

[`E2BIG`] The number of bytes used by the new process image's argument list and environment list is greater than the system-imposed limit of {`ARG_MAX`} bytes.
[`EACCES`] The new process image file is not a regular file and the implementation does not support execution of files of its type.
[`EINVAL`] The new process image file has appropriate privileges and has a recognized executable binary format, but the system does not support execution of a file with this format.

The `exec` functions, except for `fexecve()`, fail if:

[`EACCES`] Search permission is denied for a directory listed in the new process image file's path prefix, or the new process image file denies execution permission.
[`ELOOP`] A loop exists in symbolic links encountered during resolution of the path or file argument.
[`ENAMETOOLONG`] The length of a component of a pathname is longer than {`NAME_MAX`}.
[`ENOENT`] A component of path or file does not name an existing file or path or file is an empty string.
[`ENOTDIR`] A component of the new process image file's path prefix names an existing file that is neither a directory nor a symbolic link to a directory, or the new process image file's pathname contains at least one non- <slash> character and ends with one or more trailing <slash> characters and the last pathname component names an existing file that is neither a directory nor a symbolic link to a directory.

The `exec` functions, except for `execlp()` and `execvp()`, fail if:

[`ENOEXEC`] The new process image file has the appropriate access permission but has an unrecognized format.

The `fexecve()` function fails if:

[`EBADF`] The <u>fd</u> argument is not a valid file descriptor open for executing.

The `exec` functions may fail if:

[`ENOMEM`] The new process image requires more memory than is allowed by the hardware or system-imposed memory management constraints.

The `exec` functions, except for `fexecve()`, may fail if:

[`ELOOP`] More than {`SYMLOOP_MAX`} symbolic links were encountered during resolution of the <u>path</u> or <u>file</u> argument.
[`ENAMETOOLONG`] The length of the <u>path</u> argument or the length of the pathname constructed from the <u>file</u> argument exceeds {`PATH_MAX`}, or pathname resolution of a symbolic link produced an intermediate result with a length that exceeds {`PATH_MAX`}.
[`ETXTBSY`] The new process image file is a pure procedure (shared text) file that is currently open for writing by some process.

###Implementation tasks

* Finish the implementation of the `execlp()` function.
* Implement the `fexecve()` function.
* Complete error detection for all these functions
