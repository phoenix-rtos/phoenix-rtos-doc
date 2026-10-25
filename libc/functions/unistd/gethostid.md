# gethostid

## Synopsis

```c
#include <unistd.h>

long gethostid(void);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `gethostid()` function shall retrieve a 32-bit identifier for the current host.

In Phoenix-RTOS the identifier is read from the `/etc/hostid` file, where it is stored by `sethostid()`. If the file
doesn't exist (for example there is no root file system), `gethostid()` returns `0`.

## Return value

Upon successful completion, `gethostid()` shall return an identifier for the current host.

## Errors

No errors are defined.

## POSIX deviations

No POSIX deviations discovered.
