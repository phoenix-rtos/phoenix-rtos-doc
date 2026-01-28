# sem_open

## Synopsis

```c
#include <semaphore.h>

sem_t *sem_open(const char *name, int oflag, ... /* mode_t mode, unsigned int value */);
```

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `sem_open()` function shall establish a connection between a named semaphore and the
calling process, returning a semaphore that may be used in subsequent calls to
`sem_wait()`, `sem_timedwait()`, `sem_trywait()`, `sem_post()`, `sem_getvalue()` and
`sem_close()`.

_name_ shall consist of a single path component, optionally preceded by one `/`; the two
forms refer to the same semaphore. Its length shall not exceed `NAME_MAX`.

If `O_CREAT` is set in _oflag_, two further arguments are expected: a `mode_t` _mode_ and an
`unsigned int` _value_, which shall not exceed `SEM_VALUE_MAX`. If `O_CREAT` and `O_EXCL`
are both set, `sem_open()` shall fail when the semaphore already exists. If `O_CREAT` is set
without `O_EXCL`, an existing semaphore is opened and _mode_ and _value_ are ignored.

Named semaphores live in `posixsrv`, which publishes each of them as a device node under
`/dev/posix/sem/`. The returned semaphore holds a file descriptor on that node, opened with
`O_CLOEXEC`, so it is closed across a successful `exec()` and released by the server when
the process exits.

_mode_ is accepted but not applied: the node is published with fixed permissions, because
`create_dev()` takes no mode argument. The number of semaphores that may exist at one time
is bounded by `SEM_NSEMS_MAX`, the value reported by `sysconf(_SC_SEM_NSEMS_MAX)`.

## Return value

Upon successful completion, `sem_open()` shall return the address of the semaphore.
Otherwise it shall return `SEM_FAILED` and set `errno` to indicate the error.

## Errors

This function shall fail if:

* `EACCES` - the named semaphore exists but the permissions specified by _oflag_ are denied,

* `EEXIST` - `O_CREAT` and `O_EXCL` are both set and the named semaphore already exists,

* `EINVAL` - _name_ is not a valid semaphore name, or _value_ exceeds `SEM_VALUE_MAX`,

* `ENAMETOOLONG` - the length of _name_ exceeds `NAME_MAX`,

* `ENOENT` - `O_CREAT` is not set and the named semaphore does not exist,

* `ENOMEM` - insufficient memory is available,

* `ENOSPC` - there is insufficient space for the new semaphore, or `SEM_NSEMS_MAX`
  semaphores already exist.

## Tests

Tested in [test-libc-semaphore](https://github.com/phoenix-rtos/phoenix-rtos-tests/tree/master/libc/semaphore)

## Known bugs

The _mode_ argument is ignored; the semaphore node is always created with the fixed
permissions that `create_dev()` applies.
