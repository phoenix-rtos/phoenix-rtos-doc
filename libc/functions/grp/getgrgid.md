# getgrgid

## Synopsis

```c
#include <grp.h>

struct group *getgrgid(gid_t gid);

int getgrgid_r(gid_t gid, struct group *grp, char *buffer,
               size_t bufsize, struct group **result);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `getgrgid()` function shall search the group database for an entry with a matching _gid_. The group database is the
`/etc/group` file.

The `getgrgid()` function need not be thread-safe.

Applications wishing to check for error situations should set `errno` to `0` before calling `getgrgid()`. If
`getgrgid()` returns a `null` pointer and `errno` is set to non-zero, an error occurred.

The `getgrgid_r()` function shall update the `group` structure pointed to by _grp_ and store a pointer to that
structure at the location pointed to by _result_. The structure shall contain an entry from the group database with a
matching _gid_. Storage referenced by the `group` structure is allocated from the memory provided with the _buffer_
parameter, which is _bufsize_ bytes in size. A call to `sysconf(_SC_GETGR_R_SIZE_MAX)` returns either `-1` without
changing `errno` or an initial value suggested for the size of this buffer (`2048`). A `null` pointer shall be
returned at the location pointed to by _result_ on error or if the requested entry is not found.

## Return value

The `getgrgid()` function shall return a pointer to a `struct group` with the structure defined in `<grp.h>` with a
matching entry if one is found. The `getgrgid()` function shall return a `null` pointer if either the requested entry
was not found, or an error occurred. If the requested entry was not found, `errno` shall not be changed. On error,
`errno` shall be set to indicate the error.

The application shall not modify the structure to which the return value points, nor any storage areas pointed to by
pointers within the structure. The returned pointer, and pointers within the structure, might be invalidated or the
structure or the storage areas might be overwritten by a subsequent call to `getgrent()`, `getgrgid()`, or
`getgrnam()`. The returned pointer, and pointers within the structure, might also be invalidated if the calling thread
is terminated.

If successful, the `getgrgid_r()` function shall return zero; otherwise, an error number shall be returned to indicate
the error.

## Errors

The `getgrgid()` and `getgrgid_r()` functions may fail if:

* `EIO` - An I/O error has occurred.

* `EINTR` - A signal was caught during `getgrgid()`.

* `EMFILE` - All file descriptors available to the process are currently open.

* `ENFILE` - The maximum allowable number of files is currently open in the system.

The `getgrgid_r()` function may fail if:

* `ERANGE` - Insufficient storage was supplied via _buffer_ and _bufsize_ to contain the data to be referenced by the
resulting `group` structure.

## POSIX deviations

No POSIX deviations discovered.
