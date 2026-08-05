# interrupt_queueWaitLocked

## Synopsis

```c
#include <sys/interrupt.h>

int interrupt_queueWaitLocked(handle_t queue, handle_t lock, time_t timeout);
```

## Status

Implemented

## Conformance

Phoenix-RTOS specific

## Description

The `interrupt_queueWaitLocked()` function shall block the calling thread on the interrupt queue _`queue`_, previously
created with [`interrupt_queueCreateLocked()`](interrupt_queueCreateLocked.phrtos.md), until the queue is signaled by
the kernel after the interrupt handler returns a value greater than or equal to zero, or until _`timeout`_ expires.

The application shall ensure that the mutex _`lock`_ is locked by the calling thread. The mutex is atomically released
while the thread is blocked and re-acquired before the function returns. This is the variant that must be used when
more than one thread waits for the same interrupt, or when the predicate checked after the wake-up is shared with
other threads.

The function is equivalent to calling [`condWait()`](../threads/condWait.phrtos.md) on the queue handle.

The _`timeout`_ argument is interpreted according to the clock selected when the queue was created. A _`timeout`_ of
zero waits indefinitely. Spurious wake-ups may occur, so the condition the thread is waiting for should be
re-evaluated after return.

## Return value

Upon successful completion, a value of zero shall be returned; otherwise, an error number shall be returned to
indicate the error.

## Errors

The `interrupt_queueWaitLocked()` function shall fail if:

* `-EINVAL` - The value _`queue`_ does not refer to a valid interrupt queue, or _`lock`_ does not refer to an
  initialized mutex,
* `-ETIME` - The queue was not signaled before the specified timeout expired.

## Tests

Tested through [test-sys](https://github.com/phoenix-rtos/phoenix-rtos-tests/tree/master/sys)

## Known bugs

None
