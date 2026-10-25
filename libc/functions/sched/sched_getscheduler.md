# sched_getscheduler

## Synopsis

```c
#include <sched.h>

int sched_getscheduler(pid_t pid);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `sched_getscheduler()` function shall return the scheduling policy of the process specified by _pid_. If the value
of _pid_ is negative, the behavior of the `sched_getscheduler()` function is unspecified; Phoenix-RTOS returns `-1` and
sets `errno` to `EINVAL`.

The values that can be returned by `sched_getscheduler()` are defined in the `<sched.h>` header. Phoenix-RTOS supports
only the `SCHED_RR` policy, so `SCHED_RR` is returned for every process.

If a process specified by _pid_ exists, and if the calling process has permission, the scheduling policy shall be
returned for the process whose process ID is equal to _pid_. Phoenix-RTOS does not restrict access to the scheduling
policy of other processes.

If _pid_ is zero, the scheduling policy shall be returned for the calling process.

## Return value

Upon successful completion, the `sched_getscheduler()` function shall return the scheduling policy of the specified
process. If unsuccessful, the function shall return `-1` and set `errno` to indicate the error.

## Errors

The `sched_getscheduler()` function shall fail if:

* `EPERM` - The requesting process does not have permission to determine the scheduling policy of the specified
  process.

* `ESRCH` - No process can be found corresponding to that specified by _pid_.

## POSIX deviations

No POSIX deviations discovered.
