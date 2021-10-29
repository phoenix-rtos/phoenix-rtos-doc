<!-- Documentation template to fill -->
<!-- #MUST_BE: make good synopsis -->
# Synopsis 

`#include <termios.h>`</br>
`int tcgetattr(int fildes, struct termios *termios_p);`

<!-- #MUST_BE: check status according to implementation -->
## Status

Partially implemented

<!-- #MUST_BE: if function shall be posix compliant print the standard signature  -->
## Conformance

IEEE Std 1003.1-2017 

## Description 
 
`tcgetattr()` - get the parameters associated with the terminal

The `tcgetattr()` function shall get the parameters associated with the terminal referred to by _fildes_ and store them in the termios structure referenced by _termios_p_. The _fildes_ argument is an open file descriptor associated with a terminal.

The _termios_p_ argument is a pointer to a termios structure.

The `tcgetattr()` operation is allowed from any process.

If the terminal device supports different input and output baud rates, the baud rates stored in the termios structure returned by `tcgetattr()` shall reflect the actual baud rates, even if they are equal. If differing baud rates are not supported, the rate returned as the output baud rate shall be the actual baud rate. If the terminal device does not support split baud rates, the input baud rate stored in the termios structure shall be the output rate (as one of the symbolic values).

## Return value

Upon successful completion, `0` shall be returned. Otherwise, `-1` shall be returned and `errno` set to indicate the error.

## Errors

The `tcgetattr()` function shall fail if:

* `EBADF` - The _fildes_ argument is not a valid file descriptor.

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