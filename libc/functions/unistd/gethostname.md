# gethostname

## Synopsis

```c
#include <unistd.h>

int gethostname(char *name, size_t namelen);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `gethostname()` function shall return the standard host name for the current machine. The _namelen_ argument
shall specify the size of the array pointed to by the _name_ argument. The returned name shall be null-terminated,
except that if _namelen_ is an insufficient length to hold the host name, then the returned name shall be truncated, and
it is unspecified whether the returned name is null-terminated. In Phoenix-RTOS a truncated name is not
null-terminated.

Host names are limited to `HOST_NAME_MAX` bytes.

The host name is set with `sethostname()`. Until it is set, the host name is an empty string.

## Return value

Upon successful completion, `0` shall be returned; otherwise, `-1` shall be returned.

## Errors

No errors are defined.

## POSIX deviations

No POSIX deviations discovered.
