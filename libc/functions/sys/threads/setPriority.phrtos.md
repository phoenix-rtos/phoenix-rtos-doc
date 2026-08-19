# setPriority

## Synopsis

```c
#include <sys/threads.h>

int setPriority(int val);
```

## Status

Implemented

## Conformance

Phoenix-RTOS specific

## Description

The `setPriority()` function shall set the base priority of the calling thread to _`val`_.

The priority range supported by the kernel is signed, with lower values denoting higher criticality. It shall be
queried at runtime with `schedInfo()` for the `SCHED_RR` policy (or with the POSIX `sched_get_priority_min()` and
`sched_get_priority_max()` functions) rather than hardcoded, because it depends on the kernel `NPRIOS` configuration.
The default thread priority is `PH_PRIO_DEFAULT`.

Setting the priority affects the base priority of the thread only. If the thread currently holds a mutex that raised
its effective priority (through priority inheritance or the priority ceiling protocol), the effective priority shall
not be reduced below the inherited one until the mutex is unlocked.

Lowering the priority of the calling thread may cause an immediate reschedule.

`setPriority()` replaces the deprecated [`priority()`](priority.phrtos.md) function.

## Return value

If successful, the `setPriority()` function shall return zero; otherwise, an error number shall be returned to
indicate the error.

## Errors

The `setPriority()` function shall fail if:

* `-EINVAL` - _`val`_ is not a valid priority value.

## Tests

Untested

## Known bugs

None
