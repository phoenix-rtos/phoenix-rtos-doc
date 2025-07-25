# seteuid

## Synopsis

```c
#include <unistd.h>

int seteuid(uid_t uid);
```

## Status

Declared, not implemented

## Conformance

IEEE Std 1003.1-2017

## Description

If _uid_ is equal to the real user ID or the saved set-user-ID, or if the process has appropriate privileges,
`seteuid()` shall set the effective user ID of the calling process to _uid_; the real user ID and saved set-user-ID
shall remain unchanged.

The `seteuid()` function shall not affect the supplementary group list in any way.

## Return value

Upon successful completion, 0 shall be returned; otherwise, -1 shall be returned and `errno` set to indicate the error.

## Errors

The `seteuid()` function shall fail if:

* `EINVAL` - The value of the _uid_ argument is invalid and is not supported by the implementation.

* `EPERM` - The process does not have appropriate privileges and _uid_ does not match the real user ID or the saved
set-user-ID.

## Tests

Untested

## Known bugs

None
