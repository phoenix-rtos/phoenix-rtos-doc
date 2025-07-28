# tcsetpgrp

## Synopsis

```c
#include <unistd.h>

int tcsetpgrp(int fildes, pid_t pgid_id);
```

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

`tcsetpgrp()` - set the foreground process group ID

If the process has a controlling terminal, `tcsetpgrp()` shall set the foreground process group ID associated with the
terminal to _pgid_id_. The application shall ensure that the file associated with _fildes_ is the controlling terminal
of the calling process and the controlling terminal is currently associated with the session of the calling process. The
application shall ensure that the value of _pgid_id_ matches a process group ID of a process in the same session as the
calling process.

Attempts to use `tcsetpgrp()` from a process which is a member of a background process group on a _fildes_ associated
with its controlling terminal shall cause the process group to be sent a `SIGTTOU` signal. If the calling thread is
blocking `SIGTTOU` signals or the process is ignoring `SIGTTOU` signals, the process shall be allowed to perform the
operation, and no signal is sent.

## Return value

Upon successful completion, `0` shall be returned. Otherwise, `-1` shall be returned and `errno` set to indicate the
error.

## Errors

The `tcsetpgrp()` function shall fail if:

* `EBADF` - The _fildes_ argument is not a valid file descriptor.

* `EINVAL` - This implementation does not support the value in the _pgid_id_ argument.

* `EIO` - The process group of the writing process is orphaned, the calling thread is not blocking `SIGTTOU`, and the
process is not ignoring SIGTTOU.

* `ENOTTY` - The calling process does not have a controlling terminal, or the file is not the controlling terminal, or
the controlling terminal is no longer associated with the session of the calling process.

* `EPERM` - The value of _pgid_id_ is a value supported by the implementation, but does not match the process group ID
of a process in the same session as the calling process.

## Tests

Untested

## Known bugs

None
