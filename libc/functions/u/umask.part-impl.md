<!-- Documentation template to fill -->
<!-- #MUST_BE: make good synopsis -->
# unmask

## Synopsis

`#include <sys/stat.h>`

`mode_t umask(mode_t cmask);`

<!-- #MUST_BE: check status according to implementation -->
## Status

Partially implemented

<!-- #MUST_BE: if function shall be posix compliant print the standard signature  -->
## Conformance

IEEE Std 1003.1-2017

<!-- #MUST_BE: update description from opengroup AND READ IT and check if it matches  -->
## Description

The `umask()` function shall set the file mode creation mask of the process to _cmask_ and return the previous value of
 the mask. Only the file permission bits of _cmask_ (see `<sys/stat.h>`) are used; the meaning of the other bits is
 implementation-defined.

The file mode creation mask of the process is used to turn off permission bits in the mode argument supplied during
calls to the following functions:

* `open()`, `openat()`, `creat()`, `mkdir()`, `mkdirat()`, `mkfifo()`, and `mkfifoat()`
* `mknod()`, `mknodat()`
* `mq_open()`
* `sem_open()`

Bit positions that are set in _cmask_ are cleared in the mode of the created file.

<!-- #MUST_BE: check return values by the function  -->
## Return value

The file permission bits in the value returned by `umask()` shall be the previous value of the file mode creation mask.
The state of any other bits in that value is unspecified, except that a subsequent call to `umask()` with the returned
value as _cmask_ shall leave the state of the mask the same as its state before the first call, including any
unspecified use of those bits.

<!-- #MUST_BE: check what errors can cause the function to fail  -->
## Errors

No errors are defined.

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
