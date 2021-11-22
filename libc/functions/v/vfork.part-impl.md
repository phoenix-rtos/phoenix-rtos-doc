<!-- Documentation template to fill -->
<!-- #MUST_BE: make good synopsis -->
# Synopsis 

`#include <unistd.h>`</br>

`pid_t vfork(void);`</br>

## Status

Partially implemented

## Conformance

IEEE Std 1003.1, 2004

## Description 
 
`vfork()` creates a new process; share virtual memory

The `vfork()` function shall be equivalent to `fork()`, except that the behavior is undefined if the process created by `vfork()` either modifies any data other than a variable of type `pid_t` used to store the return value from `vfork()`, or returns from the function in which `vfork()` was called, or calls any other function before successfully calling `_exit()` or one of the exec family of functions.

## Return value

Upon successful completion, `vfork()` shall return `0` to the child process and return the process ID of the child process to the parent process. Otherwise, `-1` shall be returned to the parent, no child process shall be created, and `errno` shall be set to indicate the error.

## Errors

The `vfork()` function shall fail if:
* `EAGAIN` - The system-wide limit on the total number of processes under execution would be exceeded, or the system-imposed limit on the total number of processes under execution by a single user would be exceeded.
* `ENOMEM` - There is insufficient swap space for the new process.

<!-- #MUST_BE: function by default shall be untested, when tested there should be a link to test location and test command for ia32 test runner  -->
## Tests

Untested 

<!-- #MUST_BE: check for pending issues in  -->
## Known bugs 

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)