# pthread_equal

## Synopsis

```c
#include <pthread.h>

int pthread_equal(pthread_t t1, pthread_t t2);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_equal()` function shall compare the thread IDs _t1_ and _t2_.

## Return value

The `pthread_equal()` function shall return a non-zero value if _t1_ and _t2_ are equal; otherwise, zero shall be
returned.

If either _t1_ or _t2_ are not valid thread IDs, the behavior is undefined.

## Errors

No errors are defined.

The `pthread_equal()` function shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
