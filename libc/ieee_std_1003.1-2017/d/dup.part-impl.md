###Synopsis

`#include <unistd.h>`

`int dup(int fildes);`
`int dup2(int fildes, int fildes2);`

###Description

The functions duplicate an open file descriptor.

Arguments:
    
<u>fildes</u> - the file descriptor to be duplicated.
<u>fildes2</u> - the file descriptor received as a result of duplication.


The `dup()` function duplicates an existing object descriptor and returns its value to the calling process.  The argument <u>fildes</u> is a small non-negative integer index in the per-process descriptor table. The new descriptor returned by the call is the lowest numbered descriptor currently not in use by the process.

In `dup2()` function, the value of the new descriptor <u>fildes2</u> is specified as a second argument.  If <u>fildes</u> and <u>fildes2</u> are equal, then `dup2() `just returns <u>fildes2</u>; no other changes are made to the existing descriptor.  Otherwise, if descriptor <u>fildes2</u> is already in use, it is first deallocated as if a `close(2)` call had been done.

###Return value

The resulting file descriptor is returned on success,  otherwise `-1` is returned and `errno` set to indicate the error.

###Errors

For the `dup()` function:

[`EBADF`] - The <u>fildes</u> argument is not a valid open file descriptor.
[`EMFILE`] - All file descriptors available to the process are currently open.

For the `dup2()` function:

[`EBADF`] - The <u>fildes</u> argument is not a valid open file descriptor or the argument <u>fildes2</u> is negative or greater than or equal to {`OPEN_MAX`}.
[`EINTR`] - The `dup2()` function was interrupted by a signal.
[`EIO`] -  An I/O error occurred while attempting to close <u>fildes2</u>.

###Implementation tasks

* Implement error detection for errors described above.