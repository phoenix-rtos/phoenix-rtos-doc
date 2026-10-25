# sched_setparam

## Synopsis

```c
#include <sched.h>

int sched_setparam(pid_t pid, const struct sched_param *param);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `sched_setparam()` function shall set the scheduling parameters of the process specified by _pid_ to the values
specified by the `sched_param` structure pointed to by _param_. The value of the `sched_priority` member in the
`sched_param` structure shall be any integer within the inclusive priority range for the current scheduling policy of
the process specified by _pid_. Higher numerical values for the priority represent higher priorities. The priority range
of `SCHED_RR`, the only policy supported by Phoenix-RTOS, is returned by `sched_get_priority_min()` and
`sched_get_priority_max()`, see [Scheduling priorities](../../posix.md#scheduling-priorities). If the value of _pid_ is
negative, the behavior of the `sched_setparam()` function is unspecified; Phoenix-RTOS returns `-1` and sets `errno` to
`EINVAL`.

If a process specified by _pid_ exists, and if the calling process has permission, the scheduling parameters shall be
set for the process whose process ID is equal to _pid_.

If _pid_ is zero, the scheduling parameters shall be set for the calling process.

The conditions under which one process has permission to change the scheduling parameters of another process are
implementation-defined. Phoenix-RTOS does not restrict changing the scheduling parameters of other processes.

This function is not atomic with respect to other threads in the process. Threads may continue to execute while this
function call is in the process of changing the scheduling policy for the underlying kernel-scheduled entities used by
the process contention scope threads.

## Return value

If successful, the `sched_setparam()` function shall return zero.

If the call to `sched_setparam()` is unsuccessful, the priority shall remain unchanged, and the function shall return a
value of `-1` and set `errno` to indicate the error.

## Errors

The `sched_setparam()` function shall fail if:

* `EINVAL` - One or more of the requested scheduling parameters is outside the range defined for the scheduling policy
  of the specified _pid_.

* `EPERM` - The requesting process does not have permission to set the scheduling parameters for the specified
  process, or does not have appropriate privileges to invoke `sched_setparam()`.

* `ESRCH` - No process can be found corresponding to that specified by _pid_.

## POSIX deviations

No POSIX deviations discovered.
