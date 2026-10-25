# clock_getcpuclockid

## Synopsis

```c
#include <time.h>

int clock_getcpuclockid(pid_t pid, clockid_t *clock_id);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `clock_getcpuclockid()` function shall return the clock ID of the CPU-time clock of the process specified by _pid_.
If the process described by _pid_ exists and the calling process has permission, the clock ID of this clock shall be
returned in _clock_id_.

If _pid_ is zero, the `clock_getcpuclockid()` function shall return the clock ID of the CPU-time clock of the process
making the call, in _clock_id_.

The conditions under which one process has permission to obtain the CPU-time clock ID of other processes are
implementation-defined. Every process has permission to obtain the CPU-time clock ID of any other process.

## Return value

Upon successful completion, `clock_getcpuclockid()` shall return zero; otherwise, an error number shall be returned to
indicate the error.

## Errors

The `clock_getcpuclockid()` function shall fail if:

* `EPERM` - The requesting process does not have permission to access the CPU-time clock for the process.

The `clock_getcpuclockid()` function may fail if:

* `ESRCH` - No process can be found corresponding to the process specified by _pid_.

## POSIX deviations

No POSIX deviations discovered.
