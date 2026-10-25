# sched_rr_get_interval

## Synopsis

```c
#include <sched.h>

int sched_rr_get_interval(pid_t pid, struct timespec *interval);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `sched_rr_get_interval()` function shall update the `timespec` structure referenced by the _interval_ argument to
contain the current execution time limit (that is, time quantum) for the process specified by _pid_. If _pid_ is zero,
the current execution time limit for the calling process shall be returned.

In Phoenix-RTOS the time quantum is the period of the kernel system tick (`SYSTICK_INTERVAL`), which is the same for all
threads and depends on the target platform, e.g. 10 ms on ia32 and 1 ms on ARM targets. A negative _pid_ or a
`NULL` _interval_ is rejected with `EINVAL`.

## Return value

If successful, the `sched_rr_get_interval()` function shall return zero. Otherwise, it shall return a value of `-1` and
set `errno` to indicate the error.

## Errors

The `sched_rr_get_interval()` function shall fail if:

* `ESRCH` - No process can be found corresponding to that specified by _pid_.

## POSIX deviations

No POSIX deviations discovered.
