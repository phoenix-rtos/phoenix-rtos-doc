# pthread_getcpuclockid

## Synopsis

```c
#include <pthread.h>
#include <time.h>

int pthread_getcpuclockid(pthread_t thread_id, clockid_t *clock_id);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_getcpuclockid()` function shall return in _clock_id_ the clock ID of the CPU-time clock of the thread
specified by _thread_id_, if the thread specified by _thread_id_ exists.

The returned clock ID can be used with `clock_gettime()` to read the CPU time consumed by the thread.

## Return value

Upon successful completion, `pthread_getcpuclockid()` shall return zero; otherwise, an error number shall be returned
to indicate the error.

## Errors

No errors are defined.

## POSIX deviations

No POSIX deviations discovered.
