###Synopsis

`#include <sys/select.h>`

`int pselect(int nfds, fd_set *restrict readfds, fd_set *restrict writefds, fd_set *restrict errorfds, const struct timespec *restrict timeout, const sigset_t *restrict sigmask);`

`int select(int nfds, fd_set *restrict readfds, fd_set *restrict writefds, fd_set *restrict errorfds, struct timeval *restrict timeout);`

`void FD_CLR(int fd, fd_set *fdset);`

`int FD_ISSET(int fd, fd_set *fdset);`

`void FD_SET(int fd, fd_set *fdset); `

`void FD_ZERO(fd_set *fdset);` 

###Description

The functions execute synchronous I/O multiplexing.

Arguments:

<u>nfds</u> - the range of descriptors to be tested. The first <u>nfds</u> descriptors are checked in each set; that is, the descriptors from zero through <u>nfds</u>-1 in the descriptor sets are examined.
<u>readfds</u> - If the <u>readfds</u> argument is not a null pointer, it points to an object of type `fd_set` that on input specifies the file descriptors to be checked for being ready to read, and on output indicates which file descriptors are ready to read.

<u>writefds</u> - If the <u>writefds</u> argument is not a null pointer, it points to an object of type `fd_set` that on input specifies the file descriptors to be checked for being ready to write, and on output indicates which file descriptors are ready to write.

<u>errorfds</u> - If the <u>errorfds</u> argument is not a null pointer, it points to an object of type `fd_set` that on input specifies the file descriptors to be checked for error conditions pending, and on output indicates which file descriptors have error conditions pending.

<u>timeout</u> - For the `select()` function, the timeout period is given in seconds and microseconds in an argument of type `struct timeval`, whereas for the `pselect()` function the <u>timeout</u> period is given in seconds and nanoseconds in an argument of type `struct timespec`.

<u>sigmask</u> - If <u>sigmask</u> is not a null pointer, then the `pselect()` function replaces the signal mask of the caller by the set of signals pointed to by <u>sigmask</u> before examining the descriptors, and restores the signal mask of the calling thread before returning.

<u>fd</u> - the file descriptor

<u>fdset</u> - the set of file descriptors.

The `pselect()` function examines the file descriptor sets whose addresses are passed in the <u>readfds</u>, <u>writefds</u>, and <u>errorfds</u> parameters to see whether some of their descriptors are ready for reading, are ready for writing, or have an exceptional condition pending, respectively. If a thread gets canceled during a pselect() call, the signal mask in effect when executing the registered cleanup functions is either the original signal mask or the signal mask installed as part of the pselect() call.

The `select()` function is be equivalent to the `pselect()` function, except as follows:

 * For the `select()` function, the timeout period is given in seconds and microseconds in an argument of type `struct timeval`, whereas for the `pselect()` function the timeout period is given in seconds and nanoseconds in an argument of type `struct timespec`.

 * The `select()` function has no <u>sigmask</u> argument; it behave as pselect() does when sigmask is a null pointer.

 * Upon successful completion, the `select()` function may modify the object pointed to by the <u>timeout</u> argument.

The `pselect()` and `select()` functions support regular files, terminal and pseudo-terminal devices, STREAMS-based files, FIFOs, pipes, and sockets. The behavior of `pselect()` and `select()` on file descriptors that refer to other types of file is unspecified.

File descriptor masks of type `fd_set` can be initialized and tested with `FD_CLR()`, `FD_ISSET()`, `FD_SET()`, and `FD_ZERO()`. It is unspecified whether each of these is a macro or a function. If a macro definition is suppressed in order to access an actual function, or a program defines an external identifier with any of these names, the behavior is undefined.

`FD_CLR(<u>fd</u>, <u>fdsetp</u>)` removes the file descriptor <u>fd</u> from the set pointed to by <u>fdsetp</u>. If <u>fd</u> is not a member of this set, there is no effect on the set, nor will an error be returned.

`FD_ISSET(<u>fd</u>, <u>fdsetp</u>)` evaluates to `1` if the file descriptor <u>fd</u> is a member of the set pointed to by <u>fdset</u>, and evaluates to zero otherwise.

`FD_SET(<u>fd</u>, <u>fdsetp</u>)` adds the file descriptor <u>fd</u> to the set pointed to by <u>fdsetp</u>. If the file descriptor fd is already in this set, there shall be no effect on the set, nor will an error be returned.

`FD_ZERO(<u>fdsetp</u>)` initializes the descriptor set pointed to by <u>fdsetp</u> to the null set. No error is returned if the set is not empty at the time `FD_ZERO()` is invoked.

The behavior of these macros is undefined if the <u>fd</u> argument is less than `0` or greater than or equal to `FD_SETSIZE`, or if <u>fd</u> is not a valid file descriptor, or if any of the arguments are expressions with side-effects.

###Return value

Upon successful completion, the `pselect()` and `select()` functions return the total number of bits set in the bit masks. Otherwise, `-1` is returned, and `errno` is set to indicate the error.

`FD_CLR()`, `FD_SET()`, and `FD_ZERO()` do not return a value. 

`FD_ISSET()` return `1` if the bit for the file descriptor <u>fd</u> is set in the file descriptor set pointed to by <u>fdset</u>, and `0` otherwise.

###Errors

[`EBADF`] One or more of the file descriptor sets specified a file descriptor that is not a valid open file descriptor.

[`EINTR`] The function was interrupted while blocked waiting for any of the selected descriptors to become ready and before the timeout interval expired.

[`EINVAL`] An invalid timeout interval was specified. or
           The <u>nfds</u> argument is less than `0` or greater than `FD_SETSIZE`. or
           One of the specified file descriptors refers to a STREAM or multiplexer that is linked (directly or indirectly) downstream from a multiplexer.     

###Implementation tasks

 * Implement `pselect()` function
 * Implement error detection as described above.
 * Implement `FD_CLR()`, `FD_ISSET()`, `FD_SET()`, and `FD_ZERO()`
