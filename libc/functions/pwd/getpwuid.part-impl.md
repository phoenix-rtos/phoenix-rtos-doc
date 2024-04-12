# getpwuid

## Synopsis

`#include <pwd.h>`

`struct passwd *getpwuid(uid_t uid);`

`int getpwuid_r(uid_t uid, struct passwd *pwd, char *buffer, size_t bufsize, struct passwd **result);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `getpwuid()` function shall search the user database for an entry with a matching _uid_.

The `getpwuid()` function need not be thread-safe.

Applications wishing to check for error situations should set `errno` to `0` before calling `getpwuid()`.
If `getpwuid()` returns a `null` pointer and `errno` is set to non-zero, an error occurred.

The ``getpwuid_r()`` function shall update the passwd structure pointed to by _pwd_ and store a pointer to that
structure at the location pointed to by _result_. The structure shall contain an entry from the user database with
a matching _uid_. Storage referenced by the structure is allocated from the memory provided with the buffer parameter,
which is _bufsize_ bytes in size. A call to `sysconf(_SC_GETPW_R_SIZE_MAX)` returns either `-1` without changing `errno`
or an initial value suggested for the size of this buffer. A `null` pointer shall be returned to the location pointed to
by _result_ on error or if the requested entry is not found.

## Return value

The `getpwuid()` function shall return a pointer to a struct passwd with the structure as defined in `<pwd.h>` with a
matching entry if found. A `null` pointer shall be returned if the requested entry is not found, or an error occurs.
If the requested entry was not found, `errno` shall not be changed. On error, `errno` shall be set to indicate the
error.

The application shall not modify the structure to which the return value points, nor any storage areas pointed to by
pointers within the structure. The returned pointer, and pointers within the structure, might be invalidated or the
structure or the storage areas might be overwritten by a subsequent call to `getpwent()`, `getpwnam()`, or `getpwuid()`.
The returned pointer, and pointers within the structure, might also be invalidated if the calling thread is terminated.

If successful, the `getpwuid_r()` function shall return zero, otherwise, an error number shall be returned to indicate
the error.

## Errors

These functions may fail if:

* `EIO` - An I/O error has occurred.

* `EINTR` - A signal was caught during `getpwuid()`.

* `EMFILE` - All file descriptors available to the process are currently open.

* `ENFILE` - The maximum allowable number of files is currently open in the system.

The `getpwuid_r()` function may fail if:

* `ERANGE` - Insufficient storage was supplied via buffer and _bufsize_ to contain the data to be referenced by the
resulting passwd structure.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../functions.md)
2. [Table of Contents](../../../README.md)
