# fflush

## Synopsis

```c
#include <stdio.h>

int fflush(FILE *stream);
```

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

If _stream_ points to an output stream or an update stream in which the most recent operation was not input, `fflush()`
shall cause any unwritten data for that stream to be written to the file, and the last data modification and last
file status change timestamps of the underlying file shall be marked for update.

For a stream open for reading with an underlying file description, if the file is not already at `EOF`, and the file is
one capable of seeking, the file offset of the underlying open file description shall be set to the file position of
the stream, and any characters pushed back onto the stream by `ungetc()` or `ungetwc()` that have not subsequently been
read from the stream shall be discarded (without further changing the file offset).

If _stream_ is a `null` pointer, `fflush()` shall perform this flushing action on all streams for which the behavior is
defined above.

## Return value

Upon successful completion, `fflush()` shall return `0`. Otherwise, it shall set the error indicator for the stream,
return `EOF`, and set `errno` to indicate the error.

## Errors

The `fflush()` function shall fail if:

* `EAGAIN` - The `O_NONBLOCK` flag is set for the file descriptor underlying _stream_ and the thread would be delayed in
the write operation.

* `EBADF` - The file descriptor underlying _stream_ is not valid.

* `EFBIG` - An attempt was made to write a file that exceeds the maximum file size.

* `EFBIG` - An attempt was made to write a file that exceeds the file size limit of the process.

* `EFBIG` - The file is a regular file and an attempt was made to write at or beyond the offset maximum associated with
the corresponding
_stream_.

* `EINTR` - The `fflush()` function was interrupted by a signal.

* `EIO` - The process is a member of a background process group attempting to write to its controlling terminal,
`TOSTOP` is set, the calling thread is not blocking `SIGTTOU`, the process is not ignoring `SIGTTOU`, and the process
group of the process is orphaned. This error may also be returned under implementation-defined conditions.

* `ENOMEM` - The underlying _stream_ was created by `open_memstream()` or `open_wmemstream()` and insufficient memory is
available.

* `ENOSPC` - There was no free space remaining on the device containing the file or in the buffer used by the
`fmemopen()` function.

* `EPIPE` - An attempt is made to write to a pipe or FIFO that is not open for reading by any process. A `SIGPIPE`
signal shall also be sent to the thread.

The `fflush()` function may fail if:

* `ENXIO` - A request was made of a nonexistent device, or the request was outside the capabilities of the device.

## Tests

Untested

## Known bugs

None
