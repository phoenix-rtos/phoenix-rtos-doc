# tcdrain

## Synopsis

`#include <termios.h>`

`int tcdrain(int fildes);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `tcdrain()` function shall block until all output written to the object referred to by _fildes_ is transmitted. The
_fildes_ argument is an open file descriptor associated with a terminal.

Any attempts to use `tcdrain()` from a process which is a member of a background process group on a _fildes_ associated
with its controlling terminal, shall cause the process group to be sent a `SIGTTOU` signal. If the calling thread is
blocking `SIGTTOU` signals or the process is ignoring `SIGTTOU` signals, the process shall be allowed to perform the
operation, and no signal is sent.

## Return value

Upon successful completion, `0` shall be returned. Otherwise, `-1` shall be returned and `errno` set to indicate the
error.

## Errors

The `tcdrain()` function shall fail if:

* `EBADF` - The _fildes_ argument is not a valid file descriptor.

* `EINTR` - A signal interrupted `tcdrain()`.

* `EIO` - The process group of the writing process is orphaned, the calling thread is not blocking `SIGTTOU`, and the
process is not ignoring `SIGTTOU`.

* `ENOTTY` - The file associated with _fildes_ is not a terminal.

## Tests

Untested

## Known bugs

None
