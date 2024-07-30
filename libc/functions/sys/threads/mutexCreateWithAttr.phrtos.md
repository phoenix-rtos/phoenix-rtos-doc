# mutexCreateWithAttr

## Synopsis

`#include <sys/threads.h>`

`int mutexCreateWithAttr(handle_t *h, struct lockAttr *attr);`

## Status

Implemented

## Conformance

Phoenix-RTOS specific

## Description

The `mutexCreateWithAttr()` function shall initialize the mutex referenced by `h` using attributes specified by `attr`
(non-`NULL`). Upon successful initialization, the state of the mutex shall become initialized.

Attempting to initialize an already initialized mutex results in undefined behavior.

Attributes structure `lockAttr` is defined as follows:

```c
struct lockAttr {
	int type;
};
```

The `type` field specifies the type of the mutex. The following values are supported:

* `PH_LOCK_NORMAL` - The mutex is a normal mutex.
* `PH_LOCK_RECURSIVE` - The mutex is a recursive mutex. A recursive mutex allows the same thread to lock the mutex
multiple times.
* `PH_LOCK_ERRORCHECK` - The mutex is an error-checking mutex. An error-checking mutex checks for deadlock conditions
and return an error if such condition is detected.

## Return value

If successful, the `mutexCreateWithAttr()` function shall return zero; otherwise, an error number shall be returned to
indicate the error.

## Errors

The `mutexCreateWithAttr()` function shall fail if:

* `-ENOMEM` - Insufficient memory exists to initialize the mutex.
* `-EINVAL` - The attributes specified in `attr` are invalid.
* `-EFAULT` - The address specified by `h` or `attr` is invalid.

These functions shall not return an error code of `EINTR`.

## Tests

Tested in [test-sys](https://github.com/phoenix-rtos/phoenix-rtos-tests/tree/master/sys)

## Known bugs

None

## See Also

1. [Standard library functions](../../index.md)
2. [Table of Contents](../../../../index.md)
