# tcflush

## Synsopsis

```c
#include <termios.h>

int tcflush(int fildes, int queue_selector);
```

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

`tcflush()` - flush non-transmitted output data, non-read input data, or both

Upon successful completion, `tcflush()` shall discard data written to the object referred to by _fildes_ (an open file
descriptor associated with a terminal) but not transmitted, or data received but not read, depending on the value of
_queue_selector_:

* If _queue_selector_ is `TCIFLUSH`, it shall flush data received but not read.

* If _queue_selector_ is `TCOFLUSH`, it shall flush data written but not transmitted.

* If _queue_selector_ is `TCIOFLUSH`, it shall flush both data received but not read and data written but not
transmitted.

Attempts to use `tcflush()` from a process which is a member of a background process group on a _fildes_ associated
with its controlling terminal shall cause the process group to be sent a `SIGTTOU` signal. If the calling thread is
blocking `SIGTTOU` signals or the process is ignoring `SIGTTOU` signals, the process shall be allowed to perform the
operation, and no signal is sent.

## Return value

Upon successful completion, `0` shall be returned. Otherwise, `-1` shall be returned and `errno` set to indicate the
error.

## Errors

The `tcflush()` function shall fail if:

* `EBADF` - The _fildes_ argument is not a valid file descriptor.

* `EINVAL` - The _queue_selector_ argument is not a supported value.

* `EIO` - The process group of the writing process is orphaned, the calling thread is not blocking SIGTTOU, and the
process is not ignoring SIGTTOU.

* `ENOTTY` - The file associated with _fildes_ is not a terminal.

## Tests

Untested

## Known bugs

None
