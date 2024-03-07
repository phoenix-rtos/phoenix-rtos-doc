<!-- Documentation template to fill -->
# tcgetpgrp

## Synopsis

`#include <unistd.h>`

`pid_t tcgetpgrp(int fildes);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

`tcgetpgrp()` - get the foreground process group ID

The `tcgetpgrp()` function shall return the value of the process group ID of the foreground process group associated
with the terminal.

If there is no foreground process group, `tcgetpgrp()` shall return a value greater than `1` that does not match the
process group ID of any existing process group.

The `tcgetpgrp()` function is allowed from a process that is a member of a background process group; however, the
information may be subsequently changed by a process that is a member of a foreground process group.

## Return value

The functions can never return. Upon successful completion, `tcgetpgrp()` shall return the value of the process
group ID of the foreground process associated with the terminal. Otherwise, `-1` shall be returned and `errno`
set to indicate the error.

## Errors

The `tcgetpgrp()` function shall fail if:

* `EBADF` - The _fildes_ argument is not a valid file descriptor.

* `ENOTTY` - The calling process does not have a controlling terminal, or the file is not the controlling terminal.

<!-- #MUST_BE: function by default shall be untested, when tested there should be a link to test location and test 
command for ia32 test runner  -->
## Tests

Untested

<!-- #MUST_BE: check for pending issues in  -->
## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
