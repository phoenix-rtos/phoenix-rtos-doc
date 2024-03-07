<!-- Documentation template to fill -->
<!-- #MUST_BE: make good synopsis -->
# umount

## Synopsis

`#include <sys/mount.h>`

`int umount(const char *path);`

<!-- #MUST_BE: check status according to implementation -->
## Status

Declared, not implemented

<!-- #MUST_BE: if function shall be posix compliant print the standard signature  -->
## Conformance

Phoenix-RTOS specific

<!-- #MUST_BE: update description from opengroup AND READ IT and check if it matches  -->
## Description

`umount()` remove the attachment of the filesystem mounted on target under _path_.

<!-- #MUST_BE: check return values by the function  -->
## Return value

On success, zero is returned. On error, `-1` is returned, and `errno` is set to indicate the error.

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
