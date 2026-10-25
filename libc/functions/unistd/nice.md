# nice

## Synopsis

```c
#include <unistd.h>

int nice(int incr);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `nice()` function shall add the value of _incr_ to the nice value of the calling process. A nice value of a process
is a non-negative number for which a more positive value shall result in less favorable scheduling.

A maximum nice value of 2*{`NZERO`}-1 and a minimum nice value of 0 shall be imposed by the system. Requests for values
above or below these limits shall result in the nice value being set to the corresponding limit. Only a process with
appropriate privileges can lower the nice value.

Calling the `nice()` function has no effect on the priority of processes or threads with policy `SCHED_FIFO` or
`SCHED_RR`. Phoenix-RTOS supports only the `SCHED_RR` policy, so `nice()` changes nothing: the nice value of every
process stays at the default value {`NZERO`}, and `nice()` always returns `0` and never fails. To change the priority of
a thread, use `sched_setparam()` or `pthread_setschedprio()`, see
[Scheduling priorities](../../posix.md#scheduling-priorities).

The nice value set with `nice()` shall be applied to the process. If the process is multithreaded, the nice value
shall affect all system scope threads in the process.

As `-1` is a permissible return value in a successful situation, an application wishing to check for error situations
should set `errno` to `0`, then call `nice()`, and if it returns `-1`, check to see whether `errno` is non-zero.

## Return value

Upon successful completion, `nice()` shall return the new nice value -{`NZERO`}. Otherwise, `-1` shall be returned, the
nice value of the process shall not be changed, and `errno` shall be set to indicate the error.

## Errors

The `nice()` function shall fail if:

* `EPERM` - The _incr_ argument is negative, and the calling process does not have appropriate privileges.

## POSIX deviations

No POSIX deviations discovered.
