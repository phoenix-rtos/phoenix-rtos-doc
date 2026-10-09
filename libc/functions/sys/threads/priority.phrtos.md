# priority

## Synopsis

```c
#include <sys/threads.h>

int priority(int val) __attribute__((deprecated));
```

## Status

Implemented, deprecated

## Conformance

Phoenix-RTOS specific

## Description

The `priority()` function is **deprecated**. Use [`setPriority()`](setPriority.phrtos.md) to set the base priority of
the calling thread and [`getPriority()`](getPriority.phrtos.md) to retrieve it. Using `priority()` produces a compiler
deprecation warning.

`priority()` sets the base priority of the calling thread to _`val`_ and is equivalent to `sys_priority(val, NULL)`.

The function has been deprecated because its original interface is not compatible with the current, signed priority
range:

* it returned the priority as a non-negative return value, which conflicts with negative priorities being legal
values,
* it used the magic value `-1` to retrieve the current priority, which is now a valid priority. The replacement for
that use is `getPriority()`, or `sys_priority()` called with `PH_GET_PRIO`.

Note that `priority(-1)` no longer retrieves the priority - it sets the priority of the calling thread to -1.

## Return value

If successful, the `priority()` function shall return zero; otherwise, an error number shall be returned to indicate
the error.

## Errors

The `priority()` function shall fail if:

* `-EINVAL` - _`val`_ is not a valid priority value.

## Tests

Untested

## Known bugs

None
