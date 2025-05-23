# setuid

## Synopsis

```c
#include <unistd.h>

int setuid(uid_t uid);
```

## Status

Declared, not implemented

## Conformance

IEEE Std 1003.1-2017

## Description

If the process has appropriate privileges, `setuid()` shall set the real user ID, effective user ID, and the saved
set-user-ID of the calling process to _uid_.

If the process does not have appropriate privileges, but _uid_ is equal to the real user ID or the saved set-user-ID,
`setuid()` shall set the effective user ID to _uid_; the real user ID and saved set-user-ID shall remain unchanged.

The `setuid()` function shall not affect the supplementary group list in any way.

## Return value

Upon successful completion, 0 shall be returned. Otherwise, -1 shall be returned and `errno` set to indicate the error.

## Errors

The `setuid()` function shall fail, return -1, and set `errno` to the corresponding value if one or more of the
following are true:

* `EINVAL` - The value of the _uid_ argument is invalid and not supported by the implementation.

* `EPERM` - The process does not have appropriate privileges and _uid_ does not match the real user ID or the saved
set-user-ID.

## Tests

Untested

## Known bugs

None
