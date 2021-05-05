###Synopsis

`#include <unistd.h>`

`int fsync(int fildes);`

###Description

The `fsync()` function requests that all data for the open file descriptor named by <u>fildes</u> is to be transferred to the storage device associated with the file described by <u>fildes</u>. The nature of the transfer is implementation-defined. The `fsync()` function does not return until the system has completed that action or until an error is detected.

If `_POSIX_SYNCHRONIZED_IO` is defined, the `fsync()` function forces all currently queued I/O operations associated with the file indicated by file descriptor <u>fildes</u> to the synchronized I/O completion state. All I/O operations are completed as defined for synchronized I/O file integrity completion.

Arguments:

<u>fildes</u> - the file descriptor of the file of interest.

The `fsync()` function should be used by programs which require modifications to a file to be completed before continuing; for example, a program which contains a simple transaction facility might use it to ensure that all modifications to a file or files caused by a transaction are recorded.

The `fsync()` function is intended to force a physical write of data from the buffer cache, and to assure that after a system crash or other failure that all data up to the time of the `fsync()` call is recorded on the disk. Since the concepts of "buffer cache", "system crash", "physical write", and "non-volatile storage" are not defined here, the wording has to be more abstract.

###Return value

Upon successful completion, `0` is returned. Otherwise, `-1` is returned and `errno` set to indicate the error.
If the `fsync()` function fails, outstanding I/O operations are not guaranteed to have been completed.

###Errors

[`EBADF`] The <u>fildes</u> argument is not a valid descriptor.
[`EINTR`] The `fsync()` function was interrupted by a signal.
[`EINVAL`] The <u>fildes</u> argument does not refer to a file on which this operation is possible.
[`EIO`] An I/O error occurred while reading from or writing to the file system.
  
    
###Implementation tasks:
    
 * Implement `fsync()` function.
