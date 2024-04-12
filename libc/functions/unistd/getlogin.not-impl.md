# getlogin

## Synopsis

`#include <unistd.h>`

`char *getlogin(void);`

`int getlogin_r(char *name, size_t namesize);`

## Status

Declared, not implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `getlogin()` function shall return a pointer to a string containing the username associated by the login activity
with the controlling terminal of the current process. If `getlogin()` returns a non-null pointer, then that pointer
points to the name that the user logged in under, even if there are several login names with the same user ID.

The `getlogin()` function need not be thread-safe.

The `getlogin_r()` function shall put the name associated by the login activity with the controlling terminal of the
current process in the character array pointed to by _name_. The array is _namesize_ characters long and should have
space for the_name_ and the terminating null character. The maximum size of the login name is `LOGIN_NAME_MAX`.

If `getlogin_r()` is successful, _name_ points to the name the user used at login, even if there are several login names
with the same user ID.

The `getlogin()` and `getlogin_r()` functions may make use of file descriptors 0, 1, and 2 to find the controlling
terminal of the current process, examining each in turn until the terminal is found. If in this case none of these
three file descriptors is open to the controlling terminal, these functions may fail. The method used to find the
terminal associated with a file descriptor may depend on the file descriptor being open to the actual terminal device,
not /dev/tty.

## Return value

Upon successful completion, `getlogin()` shall return a pointer to the login name or a null pointer if the user's login
name cannot be found. Otherwise, it shall return a null pointer and set `errno` to indicate the error.

The application shall not modify the string returned. The returned pointer might be invalidated, or the string content
might be overwritten by a subsequent call to `getlogin()`. The returned pointer and the string content might also be
invalidated if the calling thread is terminated.

If successful, the `getlogin_r()` function shall return zero; otherwise, an error number shall be returned to indicate
the error.

## Errors

These functions may fail if:

* `EMFILE` - All file descriptors available to the process are currently open.

* `ENFILE` - The maximum allowable number of files is currently open in the system.

* `ENOTTY` - None of the file descriptors 0, 1, or 2 is open to the controlling terminal of the current process.

* `ENXIO` - The calling process has no controlling terminal.

The `getlogin_r()` function may fail if:

* `ERANGE` - The value of _namesize_ is smaller than the length of the string to be returned including the terminating
 null character.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../functions.md)
2. [Table of Contents](../../../README.md)
