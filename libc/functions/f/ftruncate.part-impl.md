# Synopsis

`#include <unistd.h>`

`int ftruncate(int fildes, off_t length);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The purpose is to truncate a file to a specified length. If _fildes_ is not a valid file descriptor open for writing,
the `ftruncate()` function shall fail.

If _fildes_ refers to a regular file, the `ftruncate()` function shall cause the size of the file to be truncated to
 _length_.

If the size of the file previously exceeded _length_, the extra data shall no longer be available to reads on the file.

If the file previously was smaller than this size, `ftruncate()` shall increase the size of the file. If the file size
is increased, the extended area shall appear as if it were zero-filled. The value of the seek pointer shall not be
modified by a call to `ftruncate()`.

Upon successful completion, if _fildes_ refers to a regular file, `ftruncate()` shall mark for update the last data
modification and last file status change timestamps of the file and the `S_ISUID` and `S_ISGID` bits of the file mode
may be cleared.

If the `ftruncate()` function is unsuccessful, the file is unaffected.

If the request would cause the file size to exceed the soft file size limit for the process, the request shall fail and
the implementation shall generate the `SIGXFSZ` signal for the thread.

If _fildes_ refers to a directory, `ftruncate()` shall fail.

If _fildes_ refers to any other file type, except a shared memory object, the result is unspecified.

If _fildes_ refers to a shared memory object, `ftruncate()` shall set the size of the shared memory object to _length_.

If the effect of `ftruncate()` is to decrease the size of a memory mapped file or a shared memory object and whole pages
beyond the new end were previously mapped, then the whole pages beyond the new end shall be discarded.

References to discarded pages shall result in the generation of a `SIGBUS` signal.

If the effect of `ftruncate()` is to increase the size of a memory object, it is unspecified whether the
contents of any mapped pages between the old end-of-file and the new are flushed to the underlying object.

## Return value

Upon successful completion, `ftruncate()` shall return `0`, otherwise, `-1` shall be returned and `errno`
set to indicate the error.

## Errors

The `ftruncate()` function shall fail if:

* `EINTR` - A signal was caught during execution.
* `EINVAL` - The _length_ argument was less than `0`.
* `EFBIG` or `EINVAL` - The _length_ argument was greater than the maximum file size.
* `EFBIG` - The file is a regular file and _length_ is greater than the offset maximum established in the open file
 description associated with _fildes_.
* `EIO` - An I/O error occurred while reading from or writing to a file system.
* `EBADF` or `EINVAL` - The _fildes_ argument is not a file descriptor open for writing.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
