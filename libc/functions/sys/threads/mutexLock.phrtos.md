# mutexLock

## Synopsis

```c
#include <sys/threads.h>

int mutexLock(handle_t h);
```

## Status

Implemented

## Conformance

Phoenix-RTOS specific

## Description

The `mutexLock()` function shall lock the mutex referenced by `h`. If the mutex was already locked, the calling thread
shall block until the mutex becomes available.

## Return value

If successful, the `mutexLock()` function shall return zero; otherwise,
an error number shall be returned to indicate the error.

## Errors

The `mutexLock()` function shall fail if:

* `-EINVAL` - The provided handle _`h`_ does not point to a valid mutex object.
* `-EDEADLK` - _`PH_LOCK_ERRORCHECK`_ attribute was set and the mutex was already locked by the same thread.
* `-EAGAIN` - _`PH_LOCK_RECURSIVE`_ attribute was set and the mutex was already locked by the same thread.
* `-EINTR` - The lock's owner thread was destroyed.

## Tests

Tested in [test-sys](https://github.com/phoenix-rtos/phoenix-rtos-tests/tree/master/sys)

## Known bugs

None
