# sysconf

## Synopsis

```c
#include <unistd.h>

long sysconf(int name);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `sysconf()` function provides a method for the application to determine the current value of a configurable system
limit or option (variable). The implementation shall support all the variables listed in IEEE Std 1003.1-2017 and
may support others.

The _name_ argument represents the system variable to be queried. The variables are the limits from `<limits.h>` (for
example `ARG_MAX`, `HOST_NAME_MAX`, `IOV_MAX`, `OPEN_MAX`, `PAGESIZE`) and the options from `<unistd.h>` (for example
`_POSIX_FSYNC`, `_POSIX_SPIN_LOCKS`), queried with the corresponding symbolic constants defined in `<unistd.h>`
(`_SC_ARG_MAX`, `_SC_HOST_NAME_MAX`, `_SC_IOV_MAX`, `_SC_OPEN_MAX`, `_SC_PAGESIZE`, `_SC_FSYNC`, `_SC_SPIN_LOCKS` and so
on).

In Phoenix-RTOS:

* `sysconf(_SC_OPEN_MAX)` returns `-1` without changing `errno`, as the limit is indeterminate - the file descriptor
table of a process grows dynamically when descriptors are allocated. `_SC_STREAM_MAX`, which follows the limit of open
files, is reported in the same way.

* Limits of resources which are allocated dynamically and bounded only by the available memory (for example
`_SC_THREAD_KEYS_MAX`, `_SC_THREAD_THREADS_MAX`, `_SC_CHILD_MAX`), as well as `_SC_NPROCESSORS_CONF` and
`_SC_NPROCESSORS_ONLN`, are reported as `-1` without changing `errno`.

* An option which is not supported is reported as `-1` without changing `errno`. The supported options are
`_POSIX_CLOCK_SELECTION`, `_POSIX_FSYNC`, `_POSIX_READER_WRITER_LOCKS`, `_POSIX_REGEXP`, `_POSIX_SPIN_LOCKS` and, on
targets with an MMU, `_POSIX_MEMORY_PROTECTION`.

## Return value

If _name_ is an invalid value, `sysconf()` shall return `-1` and set `errno` to indicate the error. If the variable
corresponding to _name_ is described in `<limits.h>` as a maximum or minimum value and the variable has no limit,
`sysconf()` shall return `-1` without changing the value of `errno`. Note that indefinite limits do not imply infinite
limits; see `<limits.h>`.

Otherwise, `sysconf()` shall return the current variable value on the system. The value returned shall not be more
restrictive than the corresponding value described to the application when it was compiled with the implementation's
`<limits.h>` or `<unistd.h>`. The value shall not change during the lifetime of the calling process, except that
`sysconf(_SC_OPEN_MAX)` may return different values before and after a call to `setrlimit()` which changes the
`RLIMIT_NOFILE` soft limit.

If the variable corresponding to _name_ is dependent on an unsupported option, the results are unspecified.

## Errors

The `sysconf()` function shall fail if:

* `EINVAL` - The value of the _name_ argument is invalid.

## POSIX deviations

Phoenix-RTOS is a lightweight system and supports only selected options of IEEE Std 1003.1-2017. The options which are
mandatory in the standard but not supported, for example `_POSIX_THREADS`, `_POSIX_SEMAPHORES`, `_POSIX_TIMERS`,
`_POSIX_JOB_CONTROL` and `_POSIX_SAVED_IDS`, as well as `_POSIX_VERSION`, are not defined and `sysconf()` returns `-1`
without changing `errno` for them. The `_SC_*` constants of the obsolescent options (`_SC_TRACE` and the other
`_SC_TRACE_*` constants, `_SC_XOPEN_STREAMS`, `_SC_2_FORT_DEV`, `_SC_2_PBS` and the other `_SC_2_PBS_*` constants, and
the `_SC_V6_*` constants) are not defined either.
