# interrupt_queueWait

## Synopsis

```c
#include <sys/interrupt.h>

int interrupt_queueWait(handle_t queue, time_t timeout);
```

## Status

Implemented

## Conformance

Phoenix-RTOS specific

## Description

The `interrupt_queueWait()` function shall block the calling thread on the interrupt queue _`queue`_, previously
created with [`interrupt_queueCreate()`](interrupt_queueCreate.phrtos.md), until the queue is signaled by the kernel
after the interrupt handler returns a value greater than or equal to zero, or until _`timeout`_ expires.

No mutex is taken or required. Only one thread may wait on a given queue at a time - if multiple threads have to be
woken up by the same interrupt, use [`interrupt_queueCreateLocked()`](interrupt_queueCreateLocked.phrtos.md) and
[`interrupt_queueWaitLocked()`](interrupt_queueWaitLocked.phrtos.md) instead.

The queue is sticky: if it was signaled while no thread was waiting on it, the first subsequent
`interrupt_queueWait()` shall return immediately. Spurious wake-ups may occur, so the condition the thread is waiting
for should be re-evaluated after return.

The _`timeout`_ argument is interpreted according to the clock selected when the queue was created. A _`timeout`_ of
zero waits indefinitely. Waits interrupted by a signal are restarted internally, so `-EINTR` is never returned to the
caller.

## Return value

Upon successful completion, a value of zero shall be returned; otherwise, an error number shall be returned to
indicate the error.

## Errors

The `interrupt_queueWait()` function shall fail if:

* `-EINVAL` - The value _`queue`_ does not refer to a valid interrupt queue,
* `-ETIME` - The queue was not signaled before the specified timeout expired,
* `-EBUSY` - Another thread is already waiting on the queue.

## Tests

Tested through [test-sys](https://github.com/phoenix-rtos/phoenix-rtos-tests/tree/master/sys)

## Known bugs

None
