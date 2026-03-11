# sem_open

## Synopsis

```c
#include <fcntl.h>
#include <semaphore.h>

sem_t *sem_open(const char *name, int oflag, ... /* mode_t mode, unsigned int value*/);
```

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2024

## Description

`sem_open()` opens an existing named semaphore or creates a new one.
The semaphore is identified by `name` value, which can optionally have a leading slash,
but no further characters can be slashes.
`name` value shall be smaller than `NAME_MAX - 18`.

Value of `oflag` parameters controls operation of the call, it can contain following bitflags.

* Setting `O_CREAT` bit will cause the call to try to create a semaphore identified by `name`.
   If such semaphore does already exist, it will open the existing one instead.
* `O_EXCL` can be set in combination with `O_CREAT`. Such combination will cause the call
   to try to create a new semaphore. If such semaphore already exists, the call will fail.

When `O_CREAT` is set in value of `oflag` parameter, two more parameters have to be passed.
Value of `value` parameter specifies the initial value of the semaphore.

Handling `mode` parameter is not implemented, every created semaphore will have 0666 mode.

## Return value

On success, `sem_open()` returns the address of a newly opened semaphore.
On error, `sem_open()` returns `SEM_FAILED` with `errno` set to indicate the error.

## Errors

* `ENOMEM` - Insufficient memory.

* `EINVAL` - Invalid `name` parameter was passed.

* `ENOENT` - If `O_CREAT` flag was not set and there is no semaphore identified by `name` in the system.

* `ENODEV` - The semaphore subsystem has not yet been initialized.

* `ENAMETOOLONG` - Length of `name` parameter exceeds the maximum allowed length.

## Tests

Tested in [test-posix](https://github.com/phoenix-rtos/phoenix-rtos-tests/tree/master/posix)

## Known bugs

None
