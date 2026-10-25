# sched_setscheduler

## Synopsis

```c
#include <sched.h>

int sched_setscheduler(pid_t pid, int policy,
                       const struct sched_param *param);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `sched_setscheduler()` function shall set the scheduling policy and scheduling parameters of the process specified
by _pid_ to _policy_ and the parameters specified in the `sched_param` structure pointed to by _param_, respectively.
The value of the `sched_priority` member in the `sched_param` structure shall be any integer within the inclusive
priority range for the scheduling policy specified by _policy_. If the value of _pid_ is negative, the behavior of the
`sched_setscheduler()` function is unspecified; Phoenix-RTOS returns `-1` and sets `errno` to `EINVAL`.

The priority is a POSIX priority, see [Scheduling priorities](../../posix.md#scheduling-priorities).

If a process specified by _pid_ exists, and if the calling process has permission, the scheduling policy and scheduling
parameters shall be set for the process whose process ID is equal to _pid_.

If _pid_ is zero, the scheduling policy and scheduling parameters shall be set for the calling process.

The conditions under which one process has appropriate privileges to change the scheduling parameters of another
process are implementation-defined. Phoenix-RTOS does not restrict changing the scheduling parameters of other
processes.

The `sched_setscheduler()` function shall be considered successful if it succeeds in setting the scheduling policy and
scheduling parameters of the process specified by _pid_ to the values specified by _policy_ and the structure pointed to
by _param_, respectively.

This function is not atomic with respect to other threads in the process. Threads may continue to execute while this
function call is in the process of changing the scheduling policy and associated scheduling parameters for the
underlying kernel-scheduled entities used by the process contention scope threads.

## Return value

Upon successful completion, the function shall return the former scheduling policy of the specified process. If the
`sched_setscheduler()` function fails to complete successfully, the policy and scheduling parameters shall remain
unchanged, and the function shall return a value of `-1` and set `errno` to indicate the error.

## Errors

The `sched_setscheduler()` function shall fail if:

* `EINVAL` - The value of the _policy_ parameter is invalid, or one or more of the parameters contained in _param_ is
  outside the valid range for the specified scheduling policy.

* `EPERM` - The requesting process does not have permission to set either or both of the scheduling parameters or the
  scheduling policy of the specified process.

* `ESRCH` - No process can be found corresponding to that specified by _pid_.

## POSIX deviations

No POSIX deviations discovered.
