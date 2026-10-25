# fsetpos

## Synopsis

```c
#include <stdio.h>

int fsetpos(FILE *stream, const fpos_t *pos);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `fsetpos()` function shall set the file position and state indicators for the stream pointed to by _stream_
according to the value of the object pointed to by _pos_, which the application shall ensure is a value obtained from
an earlier call to `fgetpos()` on the same stream. If a read or write error occurs, the error indicator for the stream
shall be set and `fsetpos()` fails.

A successful call to the `fsetpos()` function shall clear the end-of-file indicator for the stream and undo any effects
of `ungetc()` on the same stream. After an `fsetpos()` call, the next operation on an update stream may be either input
or output.

The behavior of `fsetpos()` on devices which are incapable of seeking is implementation-defined. The value of the file
offset associated with such a device is undefined.

The `fsetpos()` function is equivalent to `fseeko()` called with the offset stored in _pos_ and _whence_ set to
`SEEK_SET`.

The `fsetpos()` function shall not change the setting of `errno` if successful.

## Return value

The `fsetpos()` function shall return `0` if it succeeds; otherwise, it shall return a non-zero value and set `errno`
to indicate the error.

## Errors

The `fsetpos()` function shall fail if, either the stream is unbuffered or the stream's buffer needed to be flushed,
and the call to `fsetpos()` causes an underlying `lseek()` or `write()` to be invoked, and:

* `EAGAIN` - The `O_NONBLOCK` flag is set for the file descriptor and the thread would be delayed in the write
operation.

* `EBADF` - The file descriptor underlying the stream file is not open for writing or the stream's buffer needed to be
flushed, and the file is not open.

* `EFBIG` - An attempt was made to write a file that exceeds the maximum file size.

* `EFBIG` - An attempt was made to write a file that exceeds the file size limit of the process.

* `EFBIG` - The file is a regular file and an attempt was made to write at or beyond the offset maximum associated with
the corresponding stream.

* `EINTR` - The write operation was terminated due to the receipt of a signal, and no data was transferred.

* `EIO` - A physical I/O error has occurred, or the process is a member of a background process group attempting to
perform a `write()` to its controlling terminal, `TOSTOP` is set, the calling thread is not blocking `SIGTTOU`, the
process is not ignoring `SIGTTOU`, and the process group of the process is orphaned. This error may also be returned
under implementation-defined conditions.

* `ENOSPC` - There was no free space remaining on the device containing the file.

* `EPIPE` - An attempt was made to write to a pipe or FIFO that is not open for reading by any process; a `SIGPIPE`
signal shall also be sent to the thread.

* `ESPIPE` - The file descriptor underlying _stream_ is associated with a pipe, FIFO, or socket.

The `fsetpos()` function may fail if:

* `ENXIO` - A request was made of a nonexistent device, or the request was outside the capabilities of the device.

## POSIX deviations

No POSIX deviations discovered.
