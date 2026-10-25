# pthread_self

## Synopsis

```c
#include <pthread.h>

pthread_t pthread_self(void);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_self()` function shall return the thread ID of the calling thread.

## Return value

The `pthread_self()` function shall always be successful, and no return value is reserved to indicate an error.

## Errors

No errors are defined.

## POSIX deviations

No POSIX deviations discovered.
