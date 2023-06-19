# Synopsis

`#include <unistd.h>`

`char *ttyname(int fildes);`

`int ttyname_r(int fildes, char *name, size_t namesize);`

## Status

Declared, not implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `ttyname()` function shall return a pointer to a string containing a null-terminated path name of the terminal
associated with file descriptor _fildes_. The application shall not modify the string returned. The returned pointer
might be invalidated, or the string content might be overwritten by a subsequent call to `ttyname()`. The returned
pointer and the string content might also be invalidated if the calling thread is terminated.

The `ttyname()` function need not be thread-safe.

The `ttyname_r()` function shall store the null-terminated path name of the terminal associated with the file descriptor
_fildes_ in the character array referenced by _name_. The array is _namesize_ characters long and should have space
for the _name_ and the terminating null character. The maximum length of the terminal name shall be `TTY_NAME_MAX`.

## Return value

Upon successful completion, `ttyname()` shall return a pointer to a string. Otherwise, a null pointer shall be returned
and errno set to indicate the error.

If successful, the `ttyname_r()` function shall return zero. Otherwise, an error number shall be returned to indicate
the error.

## Errors

The `ttyname()` function may fail if:

* `EBADF` - The _fildes_ argument is not a valid file descriptor.

* `ENOTTY` - The file associated with the _fildes_ argument is not a terminal.

The `ttyname_r()` function may fail if:

* `EBADF` - The _fildes_ argument is not a valid file descriptor.

* `ENOTTY` - The file associated with the _fildes_ argument is not a terminal.

* `ERANGE` - The value of _namesize_ is smaller than the length of the string to be returned including the terminating
null character.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
