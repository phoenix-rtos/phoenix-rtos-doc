# mutexCreate

## Synopsis

`#include <sys/threads.h>`

`int mutexCreate(handle_t *h);`

## Status

Implemented

## Conformance

Phoenix-RTOS specific

## Description

The `mutexCreate()` function shall initialize the mutex referenced by `h` using default attributes. Upon
successful initialization, the state of the mutex shall become initialized.

Attempting to initialize an already initialized mutex results in undefined behavior.

## Return value

If successful, the `mutexCreate()` function shall return zero; otherwise,
an error number shall be returned to indicate the error.

## Errors

The `mutexCreate()` function shall fail if:

* `-ENOMEM` - Insufficient memory exists to initialize the mutex.
* `-EFAULT` - The address specified by `h` is invalid.

These functions shall not return an error code of `EINTR`.

## Tests

Tested in [test-sys](https://github.com/phoenix-rtos/phoenix-rtos-tests/tree/master/sys)

## Known bugs

None

## See Also

1. [Standard library functions](../../index.md)
2. [Table of Contents](../../../../index.md)
