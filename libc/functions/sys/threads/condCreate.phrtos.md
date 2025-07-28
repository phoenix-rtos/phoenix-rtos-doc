# condCreate

## Synopsis

```c
#include <sys/threads.h>

int condCreate(handle_t *h);
```

## Status

Implemented

## Conformance

Phoenix-RTOS specific

## Description

The `condCreate()` function shall initialize the condition variable referenced by _h_ using default attributes. Upon
successful initialization, the state of the condition variable shall become initialized.

Attempting to initialize an already initialized condition variable results in undefined behavior.

## Return value

If successful, the `condCreate()` function shall return zero; otherwise,
an error number shall be returned to indicate the error.

## Errors

The `condCreate()` function shall fail if:

* `-ENOMEM` - Insufficient memory exists to initialize the condition variable.
* `-EFAULT` - The address specified by `h` is invalid.

These functions shall not return an error code of `EINTR`.

## Tests

Tested in [test-sys](https://github.com/phoenix-rtos/phoenix-rtos-tests/tree/master/sys)

## Known bugs

None
