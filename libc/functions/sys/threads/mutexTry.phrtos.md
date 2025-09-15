# mutexTry

## Synopsis

```c
#include <sys/threads.h>

int mutexTry(handle_t h);
```

## Status

Implemented

## Conformance

Phoenix-RTOS specific

## Description

The `mutexTry()` function shall lock the mutex referenced by `h`. If the mutex was already locked, the function shall
return `-EBUSY` instead.

## Return value

If successful, the `mutexTry()` function shall return zero; otherwise,
an error number shall be returned to indicate the error.

## Errors

The `mutexTry()` function shall fail if:

* `-EINVAL` - The provided handle _`h`_ does not point to a valid mutex object.
* `-EBUSY` - The mutex is already locked.

## Tests

Tested in [test-sys](https://github.com/phoenix-rtos/phoenix-rtos-tests/tree/master/sys)

## Known bugs

None
