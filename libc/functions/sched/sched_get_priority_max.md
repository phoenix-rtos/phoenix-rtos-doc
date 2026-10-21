# sched_get_priority_max

## Synopsis

```c
#include <sched.h>

int sched_get_priority_max(int policy);

int sched_get_priority_min(int policy);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `sched_get_priority_max()` and `sched_get_priority_min()` functions shall return the appropriate maximum or minimum,
respectively, for the scheduling policy specified by _policy_.

The value of _policy_ shall be `SCHED_RR`, the only scheduling policy supported by Phoenix-RTOS. The returned values are
POSIX priorities, as described in [Scheduling priorities](../../posix.md#scheduling-priorities).

## Return value

If successful, the `sched_get_priority_max()` and `sched_get_priority_min()` functions shall return the appropriate
maximum or minimum values, respectively. If unsuccessful, they shall return a value of `-1` and set `errno` to indicate
the error.

## Errors

The `sched_get_priority_max()` and `sched_get_priority_min()` functions shall fail if:

* `EINVAL` - The value of the _policy_ parameter does not represent a defined scheduling policy.

* `ENOTSUP` - The value of the _policy_ parameter is `SCHED_FIFO` or `SCHED_OTHER`.

## POSIX deviations

IEEE Std 1003.1-2017 requires the functions to return the priority range of every scheduling policy defined in
`<sched.h>`. Phoenix-RTOS supports only the `SCHED_RR` policy, so for `SCHED_FIFO` and `SCHED_OTHER` the functions
return `-1` and set `errno` to `ENOTSUP`, an error that the standard does not define for them. The Phoenix-RTOS kernel
schedules all threads with a single priority-based round-robin policy, which keeps the scheduler small and its behaviour
predictable on resource-constrained real-time targets.
