# interrupt_queueCreate

## Synopsis

```c
#include <sys/interrupt.h>

int interrupt_queueCreate(handle_t *queue, int clock);
```

## Status

Implemented

## Conformance

Phoenix-RTOS specific

## Description

The `interrupt_queueCreate()` function shall create an interrupt queue referenced by _`queue`_. An interrupt queue is
a conditional variable created with the `PH_COND_UNLOCKED` attribute (see
[`condCreateWithAttr()`](../threads/condCreateWithAttr.phrtos.md)), i.e. it has no mutex associated with it.

The handle returned in _`queue`_ is meant to be passed as the _`queue`_ argument of the `interrupt()` syscall (see
[Handling interrupts](../../../../devices/interrupts.md)). The kernel broadcasts on the queue when the registered
interrupt handler returns a value greater than or equal to zero, which wakes up the thread blocked in
[`interrupt_queueWait()`](interrupt_queueWait.phrtos.md).

The _`clock`_ argument selects the clock used to interpret the _`timeout`_ argument of
[`interrupt_queueWait()`](interrupt_queueWait.phrtos.md). The following values are supported:

* `PH_CLOCK_RELATIVE` - _`timeout`_ is relative to the current time,
* `PH_CLOCK_REALTIME` - _`timeout`_ is an absolute time based on the real-time clock,
* `PH_CLOCK_MONOTONIC` - _`timeout`_ is an absolute time based on the monotonic clock.

A queue created by this function may be waited on by **only one thread at a time**. If more than one thread has to be
woken up by the same interrupt, or the interrupt state has to be inspected under a lock, use
[`interrupt_queueCreateLocked()`](interrupt_queueCreateLocked.phrtos.md) together with
[`interrupt_queueWaitLocked()`](interrupt_queueWaitLocked.phrtos.md) instead.

The queue shall be released with `resourceDestroy()`.

## Return value

Upon successful completion, a value of zero shall be returned; otherwise, an error number shall be returned to
indicate the error.

## Errors

The `interrupt_queueCreate()` function shall fail if:

* `-ENOMEM` - Insufficient memory exists to initialize the queue,
* `-EINVAL` - The value of _`clock`_ is invalid,
* `-EFAULT` - The address specified by _`queue`_ is invalid.

## Tests

Tested through [test-sys](https://github.com/phoenix-rtos/phoenix-rtos-tests/tree/master/sys)

## Known bugs

None
