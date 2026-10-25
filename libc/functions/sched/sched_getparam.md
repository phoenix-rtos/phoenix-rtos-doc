# sched_getparam

## Synopsis

```c
#include <sched.h>

int sched_getparam(pid_t pid, struct sched_param *param);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `sched_getparam()` function shall return the scheduling parameters of a process specified by _pid_ in the
`sched_param` structure pointed to by _param_.

If a process specified by _pid_ exists, and if the calling process has permission, the scheduling parameters for the
process whose process ID is equal to _pid_ shall be returned. Phoenix-RTOS does not restrict access to the scheduling
parameters of other processes.

If _pid_ is zero, the scheduling parameters for the calling process shall be returned. The behavior of the
`sched_getparam()` function is unspecified if the value of _pid_ is negative; Phoenix-RTOS returns `-1` and sets
`errno` to `EINVAL`.

The `sched_priority` member is set to a POSIX priority, see [Scheduling
priorities](../../posix.md#scheduling-priorities).

## Return value

Upon successful completion, the `sched_getparam()` function shall return zero. If the call to `sched_getparam()` is
unsuccessful, the function shall return a value of `-1` and set `errno` to indicate the error.

## Errors

The `sched_getparam()` function shall fail if:

* `EPERM` - The requesting process does not have permission to obtain the scheduling parameters of the specified
  process.

* `ESRCH` - No process can be found corresponding to that specified by _pid_.

## POSIX deviations

No POSIX deviations discovered.
