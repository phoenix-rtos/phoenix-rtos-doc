# fdopen

## Synopsis

`#include <stdio.h>`

`FILE *fdopen(int fildes, const char *mode);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `fdopen()` function shall associate a stream with a file descriptor.

The _mode_ argument is a character string having one of the following values:

* `r` or `rb` - Open a file for reading.
* `w` or `wb` - Open a file for writing.
* `a` or `ab` - Open a file for writing at end-of-file.
* `r+` or `rb+` or `r+b` - Open a file for update (reading and writing).
* `w+` or `wb+` or `w+b` - Open a file for update (reading and writing).
* `a+` or `ab+` or `a+b` - Open a file for update (reading and writing) at end-of-file.

The meaning of these flags is exactly as specified in `fopen()`, except that modes beginning with w shall not cause
truncation of the file.

Additional values for the _mode_ argument may be supported by an implementation.

The application shall ensure that the mode of the stream as expressed by the _mode_ argument is allowed by the file
access mode of the open file description to which _fildes_ refers. The file position indicator associated with the new
stream is set to the position indicated by the file offset associated with the file descriptor.

The error and end-of-file indicators for the stream shall be cleared. The `fdopen()` function may cause the last data
access timestamp of the underlying file to be marked for update.

If _fildes_ refers to a shared memory object, the result of the `fdopen()` function is unspecified.

If _fildes_ refers to a typed memory object, the result of the `fdopen()` function is unspecified.
The `fdopen()` function shall preserve the offset maximum previously set for the open file description corresponding to
_fildes_.

## Return value

Upon successful completion, `fdopen()` shall return a pointer to a stream, otherwise, a `null` pointer shall be returned
and `errno` set to indicate the error.

## Errors

The `fdopen()` function shall fail if:

* `EMFILE` - `STREAM_MAX` streams are currently open in the calling process.

The `fdopen()` function may fail if:

* `EBADF` - The _fildes_ argument is not a valid file descriptor.

* `EINVAL` - The _mode_ argument is not a valid mode.

* `EMFILE` - `FOPEN_MAX` streams are currently open in the calling process.

* `ENOMEM` - Insufficient space to allocate a buffer.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
