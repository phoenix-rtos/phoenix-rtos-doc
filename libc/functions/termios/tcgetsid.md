# tcgetsid

## Synopsis

```c
#include <termios.h>

pid_t tcgetsid(int fildes);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

`tcgetsid()` - get the process group ID for the session leader for the controlling terminal

The `tcgetsid()` function shall obtain the process group ID of the session for which the terminal specified by _fildes_
is the controlling terminal.

## Return value

Upon successful completion, `tcgetsid()` shall return the process group ID of the session associated with the terminal.
Otherwise, a value of `-1` shall be returned and `errno` set to indicate the error.

## Errors

The `tcgetsid()` function shall fail if:

* `EBADF` - The _fildes_ argument is not a valid file descriptor.

* `ENOTTY` - The calling process does not have a controlling terminal, or the file is not the controlling terminal.

* `EINVAL` - The file associated with _fildes_ is not a terminal, and the server handling it reports unsupported
requests with `EINVAL` (see POSIX deviations).

## POSIX deviations

If the file associated with _fildes_ is not a terminal, the error reported by `tcgetsid()` depends on the server
handling the file. The function is implemented on top of `ioctl()`, and the kernel forwards every request to the server
without checking the type of the file. Servers that do not handle terminal requests report them either with `ENOTTY`
(for example files in `jffs2`) or with `EINVAL` (for example pipes and files in `dummyfs`).
