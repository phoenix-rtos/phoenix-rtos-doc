# umask

## Synopsis

```c
#include <sys/stat.h>

mode_t umask(mode_t cmask);
```

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `umask()` function shall set the file mode creation mask of the process to _cmask_ and return the previous value of
 the mask. Only the file permission bits of _cmask_ (see `<sys/stat.h>`) are used; the meaning of the other bits is
 implementation-defined.

The file mode creation mask of the process is used to turn off permission bits in the mode argument supplied during
calls to the following functions:

* `open()`, `openat()`, `creat()`, `mkdir()`, `mkdirat()`, `mkfifo()`, and `mkfifoat()`
* `mknod()`, `mknodat()`
* `mq_open()`
* `sem_open()`

Bit positions that are set in _cmask_ are cleared in the mode of the created file.

## Return value

The file permission bits in the value returned by `umask()` shall be the previous value of the file mode creation mask.
The state of any other bits in that value is unspecified, except that a subsequent call to `umask()` with the returned
value as _cmask_ shall leave the state of the mask the same as its state before the first call, including any
unspecified use of those bits.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None
