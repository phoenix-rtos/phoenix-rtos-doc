<!-- Documentation template to fill -->
# Synopsis 

`#include <termios.h>`</br>
`int tcsendbreak(int fildes, int duration);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017 

## Description 

`tcsendbreak()` - send a break for a specific duration

If the terminal is using asynchronous serial data transmission, `tcsendbreak()` shall cause transmission of a continuous stream of zero-valued bits for a specific duration. If _duration_ is `0`, it shall cause transmission of zero-valued bits for at least `0.25` seconds, and not more than `0.5` seconds. If _duration_ is not `0`, it shall send zero-valued bits for an implementation-defined period of time.

The _fildes_ argument is an open file descriptor associated with a terminal.

If the terminal is not using asynchronous serial data transmission, it is implementation-defined whether `tcsendbreak()` sends data to generate a break condition or returns without taking any action.

Attempts to use `tcsendbreak()` from a process which is a member of a background process group on a _fildes_ associated with its controlling terminal shall cause the process group to be sent a `SIGTTOU` signal. If the calling thread is blocking `SIGTTOU` signals or the process is ignoring `SIGTTOU` signals, the process shall be allowed to perform the operation, and no signal is sent.

## Return value

Upon successful completion, `0` shall be returned. Otherwise, `-1` shall be returned and `errno` set to indicate the error.

## Errors

The `tcsendbreak()` function shall fail if:

* `EBADF` - The _fildes_ argument is not a valid file descriptor.

* `EIO` - The process group of the writing process is orphaned, the calling thread is not blocking `SIGTTOU`, and the process is not ignoring `SIGTTOU`.

* `ENOTTY` - The file associated with _fildes_ is not a terminal.

<!-- #MUST_BE: function by default shall be untested, when tested there should be a link to test location and test command for ia32 test runner  -->
## Tests

Untested 

<!-- #MUST_BE: check for pending issues in  -->
## Known bugs 

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)