# tcflow

## Synopsis

```c
#include <termios.h>

int tcflow(int fildes, int action);
```

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `tcflow()` function shall suspend or restart transmission or reception of data on the object referred to by
_fildes_, depending on the value of _action_. The _fildes_ argument is an open file descriptor associated with a
terminal.

* If _action_ is `TCOOFF`, output shall be suspended.

* If _action_ is `TCOON`, suspended output shall be restarted.

* If _action_ is `TCIOFF`, the system shall transmit a `STOP` character, which is intended to cause the terminal device
to stop transmitting data to the system.

* If _action_ is `TCION`, the system shall transmit a `START` character, which is intended to cause the terminal device
to start transmitting data to the system.

If _fildes_ is associated with a pseudo-terminal, the `STOP` and `START` characters need not be transmitted.

The default on the opening of a terminal file is that neither its input nor its output are suspended.

Attempts to use `tcflow()` from a process which is a member of a background process group on a _fildes_ associated
with its controlling terminal, shall cause the process group to be sent a `SIGTTOU` signal. If the calling thread is
blocking `SIGTTOU` signals or the process is ignoring `SIGTTOU` signals, the process shall be allowed to perform the
operation, and no signal is sent.

## Return value

Upon successful completion, `0` shall be returned. Otherwise, `-1` shall be returned and `errno` set to indicate the
error.

## Errors

The `tcflow()` function shall fail if:

* `EBADF` - The _fildes_ argument is not a valid file descriptor.

* `EINVAL` - The _action_ argument is not a supported value.

* `EIO` - The process group of the writing process is orphaned, the calling thread is not blocking `SIGTTOU`, and the
process is not ignoring `SIGTTOU`.

* `ENOTTY` - The file associated with _fildes_ is not a terminal.

## POSIX deviations

No POSIX deviations discovered.
