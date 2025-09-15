# mutexUnlock

## Synopsis

```c
#include <sys/threads.h>

int mutexUnlock(handle_t h);
```

## Status

Implemented

## Conformance

Phoenix-RTOS specific

## Description

The `mutexUnlock()` function shall unlock the mutex referenced by `h`.

## Return value

If successful, the `mutexUnlock()` function shall return zero; otherwise,
an error number shall be returned to indicate the error.

## Errors

The `mutexUnlock()` function shall fail if:

* `-EINVAL` - The provided handle _`h`_ does not point to a valid mutex object.
* `-EPERM` - The lock's owner thread was destroyed.

## Tests

Tested in [test-sys](https://github.com/phoenix-rtos/phoenix-rtos-tests/tree/master/sys)

## Known bugs

None
