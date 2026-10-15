# getc_unlocked

## Synopsis

```c
#include <stdio.h>

int getc_unlocked(FILE *stream);

int getchar_unlocked(void);

int putc_unlocked(int c, FILE *stream);

int putchar_unlocked(int c);
```

## Description

`stdio` functions with explicit client locking.

Arguments:

_stream_ - the stream to be read or written,
_c_ - a character to be put down.

Versions of the functions with names without "_unlocked" which are functionally equivalent to the original versions,
with the exception that they are not implemented in a fully thread-safe manner. They are thread-safe when used within
a scope protected by `flockfile()` (or `ftrylockfile()`) and `funlockfile()`. These functions can safely be used in a
multithreaded program if and only if they are called while the invoking thread owns the (`FILE *`) object, as is the
case after a successful call to the `flockfile()` or `ftrylockfile()` functions.

If `getc_unlocked()` or `putc_unlocked()` are implemented as macros they may evaluate stream more than once, so the
_stream_ argument should never be an expression with side effects.

## Return value

Upon successful completion, the functions return the byte read or written to or from the stream pointed to by _stream_.

## Errors

* [`EAGAIN`] The `O_NONBLOCK` flag is set for the file descriptor underlying stream and the thread would be delayed in
the operation.
* [`EBADF`] The file descriptor underlying stream is not a valid file descriptor open for reading or writing.
* [`EFBIG`] An attempt was made to write to a file that exceeds the maximum file size.
* [`EINTR`] The read or write operation was terminated due to the receipt of a signal, and no data was transferred.
* [`EIO`] A physical I/O error has occurred, or the process is in a background process group attempting to read or
write from or to its controlling terminal.
* [`ENOSPC`] There was no free space remaining on the device containing the file.
* [`EOVERFLOW`] The file is a regular file and an attempt was made to read at or beyond the offset maximum associated
with the corresponding stream.
* [`ENOMEM`] Insufficient storage space is available.
* [`ENXIO`] A request was made of a nonexistent device, or the request was outside the capabilities of the device.
* [`EPIPE`] An attempt is made to write to a pipe or `FIFO` that is not open for reading by any process. A `SIGPIPE`
signal is also sent to the thread.

## Implementation tasks

* Implement error handling for the `getc_unlocked()` function.
* Implement error handling for the `getchar_unlocked()` function.
* Implement error handling for the `putc_unlocked()` function.
* Implement error handling for the `putchar_unlocked()` function.
