# getpriority

## Synopsis

```c
#include <sys/resource.h>

int getpriority(int which, id_t who);

int setpriority(int which, id_t who, int value);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `getpriority()` function shall obtain the nice value of a process, process group, or user. The `setpriority()`
function shall set the nice value of a process, process group, or user to _value_+{`NZERO`}.

Target processes are specified by the values of the _which_ and _who_ arguments. The _which_ argument may be one of the
following values: `PRIO_PROCESS`, `PRIO_PGRP`, or `PRIO_USER`, indicating that the _who_ argument is to be interpreted
as a process ID, a process group ID, or an effective user ID, respectively. A `0` value for the _who_ argument specifies
the current process, process group, or user. Phoenix-RTOS has no user accounts, so for `PRIO_USER` only a _who_ value of
`0` is accepted; any other value is rejected with `EINVAL`.

The nice value set with `setpriority()` shall be applied to the process. If the process is multithreaded, the nice
value shall affect all system scope threads in the process.

If more than one process is specified, `getpriority()` shall return value {`NZERO`} less than the lowest nice value
pertaining to any of the specified processes, and `setpriority()` shall set the nice values of all the specified
processes to _value_+{`NZERO`}.

The default nice value is {`NZERO`}; lower nice values shall cause more favorable scheduling. Only a process with
appropriate privileges can lower its nice value.

Any processes or threads using `SCHED_FIFO` or `SCHED_RR` shall be unaffected by a call to `setpriority()`. This is not
considered an error. In Phoenix-RTOS `setpriority()` changes nothing and `getpriority()` always returns `0`, the default
nice value less {`NZERO`}. Both functions only validate _which_ and check that the process or process group specified by
_who_ exists. To change the priority of a thread, use `sched_setparam()` or `pthread_setschedprio()`, see [Scheduling
priorities](../../../posix.md#scheduling-priorities).

Since `getpriority()` can return the value `-1` upon successful completion, it is necessary to set `errno` to `0` prior
to a call to `getpriority()`. If `getpriority()` returns the value `-1`, then `errno` can be checked to see if an error
occurred or if the value is a legitimate nice value.

## Return value

Upon successful completion, `getpriority()` shall return an integer in the range -{`NZERO`} to {`NZERO`}-1. Otherwise,
`-1` shall be returned and `errno` set to indicate the error.

Upon successful completion, `setpriority()` shall return `0`; otherwise, `-1` shall be returned and `errno` set to
indicate the error.

## Errors

The `getpriority()` and `setpriority()` functions shall fail if:

* `ESRCH` - No process could be located using the _which_ and _who_ argument values specified.

* `EINVAL` - The value of the _which_ argument was not recognized, or the value of the _who_ argument is not a valid
  process ID, process group ID, or user ID.

In addition, `setpriority()` may fail if:

* `EPERM` - A process was located, but neither the real nor effective user ID of the executing process match the
  effective user ID of the process whose nice value is being changed.

* `EACCES` - A request was made to change the nice value to a lower numeric value and the current process does not
  have appropriate privileges.

## POSIX deviations

No POSIX deviations discovered.
