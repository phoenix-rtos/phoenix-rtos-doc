# getPriority

## Synopsis

```c
#include <sys/threads.h>

int getPriority(void);
```

## Status

Implemented

## Conformance

Phoenix-RTOS specific

## Description

The `getPriority()` function shall return the base priority of the calling thread.

The returned value may be negative, as the priority range supported by the kernel is signed, with lower values denoting
higher criticality. It is therefore not possible to distinguish an error from a valid priority by inspecting the return
value. `PH_PRIO_DEFAULT` is returned if the underlying `sys_priority` system call fails, which is not expected to
happen for a call made from a running thread.

The value returned is the base priority requested for the thread, not the effective priority the scheduler currently
uses, which may be higher if the thread holds a mutex using priority inheritance or the priority ceiling protocol.

`getPriority()` replaces the deprecated [`priority()`](priority.phrtos.md) function called with an argument of `-1`.

## Return value

The `getPriority()` function shall return the base priority of the calling thread.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None
