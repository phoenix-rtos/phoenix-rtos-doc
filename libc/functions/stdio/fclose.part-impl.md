# fclose

## Synopsis

```c
#include <stdio.h>

int fclose(FILE *stream);
```

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `fclose()` function shall cause the stream pointed to by _stream_ to be flushed and the associated file to be
closed. Any unwritten buffered data for the stream shall be written to the file. Any unread buffered data shall be
discarded.

Whether the call succeeds, the _stream_ shall be disassociated from the file and any buffer set by the `setbuf()`
or `setvbuf()` function shall be disassociated from the stream. If the associated buffer was automatically allocated,
it shall be deallocated.

If the file is not already at `EOF`, and the file is one capable of seeking, the file offset of the underlying open file
description shall be set to the file position of the _stream_ if the _stream_ is the active handle to the underlying
file description.

The `fclose()` function shall mark for update the last data modification and last file status change timestamps of the
underlying file, if the _stream_ was writable, and if buffered data remains that has not yet been written to the file.
The `fclose()` function shall perform the equivalent of a `close()` on the file descriptor that is associated with the
stream pointed to by _stream_.

After the call to `fclose()`, any use of stream results in undefined behavior.

## Return value

Upon successful completion, `fclose()` shall return `0`; otherwise, it shall return `EOF` and set
`errno` to indicate the error.

## Errors

The `fclose()` function shall fail if:

* `EAGAIN` - The `O_NONBLOCK` flag is set for the file descriptor underlying _stream_ and the thread would be delayed
in the write operation.

* `EBADF` - The file descriptor underlying _stream_ is not valid.

* `EFBIG` - An attempt was made to write a file that exceeds the maximum file size.

* `EFBIG` - An attempt was made to write a file that exceeds the file size limit of the process.

* `EFBIG` - The file is a regular file and an attempt was made to write at or beyond the offset maximum associated with
the corresponding _stream_.

* `EINTR` - The `fclose()` function was interrupted by a signal.

* `EIO` - The process is a member of a background process group attempting to write to its controlling terminal,
`TOSTOP` is set, the calling thread is not blocking `SIGTTOU`, the process is not ignoring `SIGTTOU`, and the process
group of the process is orphaned. This error may also be returned under implementation-defined conditions.

* `ENOMEM` - The underlying _stream_ was created by `open_memstream()` or `open_wmemstream()` and insufficient memory
is available.

* `ENOSPC` - There was no free space remaining on the device containing the file or in the buffer used by the
`fmemopen()` function.

* `EPIPE` - An attempt is made to write to a pipe or FIFO that is not open for reading by any process. A `SIGPIPE`
signal shall also be sent to the thread.

The `fclose()` function may fail if:

* `ENXIO` - A request was made of a nonexistent device, or the request was outside the capabilities of the device.

## Tests

Untested

## Known bugs

None
