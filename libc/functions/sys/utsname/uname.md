# uname

## Synopsis

```c
#include <sys/utsname.h>

int uname(struct utsname *name);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `uname()` function shall store information identifying the current system in the structure pointed to by _name_.

The `uname()` function uses the `utsname` structure defined in `<sys/utsname.h>`.

The `uname()` function shall return a string naming the current system in the character array `sysname`. Similarly,
`nodename` shall contain the name of this node within an implementation-defined communications network. The arrays
`release` and `version` shall further identify the operating system. The array `machine` shall contain a name that
identifies the hardware that the system is running on.

The format of each member is implementation-defined. In Phoenix-RTOS:

* `sysname` is `Phoenix-RTOS`,

* `nodename` is the host name set with `sethostname()` (the same name `gethostname()` returns); it is an empty string
until a host name is set,

* `release` is the release number of the kernel and `version` identifies its build (both are taken from the version
control description of the kernel sources),

* `machine` is the target architecture family the kernel was built for (for example `ia32`).

## Return value

Upon successful completion, a non-negative value shall be returned. Otherwise, `-1` shall be returned and `errno` set to
indicate the error.

## Errors

No errors are defined.

## POSIX deviations

No POSIX deviations discovered.
