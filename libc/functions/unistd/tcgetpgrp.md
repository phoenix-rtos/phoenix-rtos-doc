# tcgetpgrp

## Synopsis

```c
#include <unistd.h>

pid_t tcgetpgrp(int fildes);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

`tcgetpgrp()` - get the foreground process group ID

The `tcgetpgrp()` function shall return the value of the process group ID of the foreground process group associated
with the terminal.

If there is no foreground process group, `tcgetpgrp()` shall return a value greater than `1` that does not match the
process group ID of any existing process group.

The `tcgetpgrp()` function is allowed from a process that is a member of a background process group; however, the
information may be subsequently changed by a process that is a member of a foreground process group.

## Return value

The functions can never return. Upon successful completion, `tcgetpgrp()` shall return the value of the process
group ID of the foreground process associated with the terminal. Otherwise, `-1` shall be returned and `errno`
set to indicate the error.

## Errors

The `tcgetpgrp()` function shall fail if:

* `EBADF` - The _fildes_ argument is not a valid file descriptor.

* `EINVAL` - The file associated with _fildes_ is not a terminal, and the server handling it reports unsupported
requests with `EINVAL` (see POSIX deviations).

* `ENOTTY` - The calling process does not have a controlling terminal, or the file is not the controlling terminal.

## POSIX deviations

If the file associated with _fildes_ is not a terminal, the error reported by `tcgetpgrp()` depends on the server
handling the file. The function is implemented on top of `ioctl()`, and the kernel forwards every request to the server
without checking the type of the file. Servers that do not handle terminal requests report them either with `ENOTTY`
(for example files in `jffs2`) or with `EINVAL` (for example pipes and files in `dummyfs`).
