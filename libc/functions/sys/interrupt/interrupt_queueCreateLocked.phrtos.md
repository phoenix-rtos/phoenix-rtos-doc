# interrupt_queueCreateLocked

## Synopsis

```c
#include <sys/interrupt.h>

int interrupt_queueCreateLocked(handle_t *queue, int clock);
```

## Status

Implemented

## Conformance

Phoenix-RTOS specific

## Description

The `interrupt_queueCreateLocked()` function shall create an interrupt queue referenced by _`queue`_. In contrast to
[`interrupt_queueCreate()`](interrupt_queueCreate.phrtos.md), the queue is a regular conditional variable created with
the `PH_COND_NORMAL` attribute (see [`condCreateWithAttr()`](../threads/condCreateWithAttr.phrtos.md)) and therefore
has to be waited on with a mutex held, using
[`interrupt_queueWaitLocked()`](interrupt_queueWaitLocked.phrtos.md).

This variant must be used whenever more than one thread may wait on the same interrupt, or when the predicate checked
after the wake-up is shared with other threads and needs to be protected by a mutex.

The handle returned in _`queue`_ is meant to be passed as the _`queue`_ argument of the `interrupt()` syscall (see
[Handling interrupts](../../../../devices/interrupts.md)).

The _`clock`_ argument selects the clock used to interpret the _`timeout`_ argument of
[`interrupt_queueWaitLocked()`](interrupt_queueWaitLocked.phrtos.md). The following values are supported:

* `PH_CLOCK_RELATIVE` - _`timeout`_ is relative to the current time,
* `PH_CLOCK_REALTIME` - _`timeout`_ is an absolute time based on the real-time clock,
* `PH_CLOCK_MONOTONIC` - _`timeout`_ is an absolute time based on the monotonic clock.

The queue shall be released with `resourceDestroy()`.

## Return value

Upon successful completion, a value of zero shall be returned; otherwise, an error number shall be returned to
indicate the error.

## Errors

The `interrupt_queueCreateLocked()` function shall fail if:

* `-ENOMEM` - Insufficient memory exists to initialize the queue,
* `-EINVAL` - The value of _`clock`_ is invalid,
* `-EFAULT` - The address specified by _`queue`_ is invalid.

## Tests

Tested through [test-sys](https://github.com/phoenix-rtos/phoenix-rtos-tests/tree/master/sys)

## Known bugs

None
