# endpwent

## Synopsis

```c
#include <pwd.h>

void endpwent(void);

struct passwd *getpwent(void);

void setpwent(void);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

These functions shall retrieve information about users.

The `getpwent()` function shall return a pointer to a structure containing the broken-out fields of an entry in the
user database. Each entry in the user database contains a `passwd` structure. If the user database is not already open,
`getpwent()` shall open it and return a pointer to a `passwd` structure containing the first entry in the database.
Thereafter, it shall return a pointer to a `passwd` structure containing the next entry in the user database.
Successive calls can be used to search the entire user database. The user database is the `/etc/passwd` file.

If an end-of-file or an error is encountered on reading, `getpwent()` shall return a `null` pointer.

The `setpwent()` function shall rewind the user database so that the next `getpwent()` call returns the first entry,
allowing repeated searches.

The `endpwent()` function shall close the user database.

The `setpwent()` and `endpwent()` functions shall not change the setting of `errno` if successful.

On error, the `setpwent()` and `endpwent()` functions shall set `errno` to indicate the error.

Since no value is returned by the `setpwent()` and `endpwent()` functions, an application wishing to check for error
situations should set `errno` to `0`, then call the function, then check `errno`.

These functions need not be thread-safe.

## Return value

On successful completion, `getpwent()` shall return a pointer to a `passwd` structure. On end-of-file, `getpwent()`
shall return a `null` pointer and shall not change the setting of `errno`. On error, `getpwent()` shall return a `null`
pointer and `errno` shall be set to indicate the error.

The application shall not modify the structure to which the return value points, nor any storage areas pointed to by
pointers within the structure. The returned pointer, and pointers within the structure, might be invalidated or the
structure or the storage areas might be overwritten by a subsequent call to `getpwuid()`, `getpwnam()`, or
`getpwent()`. The returned pointer, and pointers within the structure, might also be invalidated if the calling thread
is terminated.

## Errors

These functions may fail if:

* `EINTR` - A signal was caught during the operation.

* `EIO` - An I/O error has occurred.

In addition, `getpwent()` and `setpwent()` may fail if:

* `EMFILE` - All file descriptors available to the process are currently open.

* `ENFILE` - The maximum allowable number of files is currently open in the system.

## POSIX deviations

No POSIX deviations discovered.
