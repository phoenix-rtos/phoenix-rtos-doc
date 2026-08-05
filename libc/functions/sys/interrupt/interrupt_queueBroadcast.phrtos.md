# interrupt_queueBroadcast

## Synopsis

```c
#include <sys/interrupt.h>

int interrupt_queueBroadcast(handle_t queue);
```

## Status

Implemented

## Conformance

Phoenix-RTOS specific

## Description

The `interrupt_queueBroadcast()` function shall unblock all threads waiting on the interrupt queue _`queue`_.

Waking up more than one thread is possible only if the queue was created with
[`interrupt_queueCreateLocked()`](interrupt_queueCreateLocked.phrtos.md), since a queue created with
[`interrupt_queueCreate()`](interrupt_queueCreate.phrtos.md) may have at most one waiter. For such a queue the call
behaves like [`interrupt_queueSignal()`](interrupt_queueSignal.phrtos.md).

The function is intended to be called from the thread context only - it must not be used inside an interrupt handler.
The kernel signals the queue on its own after the handler returns a value greater than or equal to zero.

The queue is sticky: if it is broadcast while no thread is waiting on it, the next call to
[`interrupt_queueWait()`](interrupt_queueWait.phrtos.md) or
[`interrupt_queueWaitLocked()`](interrupt_queueWaitLocked.phrtos.md) shall return immediately.

No mutex is required to call this function, regardless of how the queue was created.

## Return value

Upon successful completion, a value of zero shall be returned; otherwise, an error number shall be returned to
indicate the error.

## Errors

The `interrupt_queueBroadcast()` function shall fail if:

* `-EINVAL` - The value _`queue`_ does not refer to a valid interrupt queue.

## Tests

Tested through [test-sys](https://github.com/phoenix-rtos/phoenix-rtos-tests/tree/master/sys)

## Known bugs

None
