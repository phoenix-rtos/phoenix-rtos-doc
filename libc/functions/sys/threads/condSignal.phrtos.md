# condSignal

## Synopsis

```c
#include <sys/threads.h>

int condBroadcast(handle_t h);

int condSignal(handle_t h);
```

## Status

Implemented

## Conformance

Phoenix-RTOS specific

## Description

These functions shall unblock threads blocked on a condition variable.

The `condBroadcast()` function shall unblock all threads currently blocked on the specified conditional variable _h_.

The `condSignal()` function shall unblock at least one of the threads that are blocked on the specified condition
variable _h_ (if any threads are blocked on _h_).

If more than one thread is blocked on a condition variable, the scheduling policy shall determine the order in which
threads are unblocked. When each thread unblocked as a result of a `condBroadcast()` or `condSignal()` returns from its
call to `condWait()`, the thread shall own the mutex with which it is called `condWait()`. The thread(s) that are
unblocked shall contend for the mutex according to the scheduling policy (if applicable),
and as if each had called `mutexLock()`.

The `condBroadcast()` or `condSignal()` functions may be called by a thread whether it
currently owns the mutex that threads calling `condWait()` have associated with the condition variable
during their waits; however, if predictable scheduling behavior is required, then that mutex shall be locked by the
thread calling `condBroadcast()` or `condSignal()`.

When there is no thread waiting on condition invoking `condBroadcast()` and `condSignal()` internal condition state
is changed. First condWait invoked on condition exits immediately without waiting. This property is known as being
"sticky". Condition signaling performed on user space interrupt handler is performed without lock acquired. Sticky
condition implementation ensures that signals sent without lock can be reliably detected.

The behavior is undefined if the value specified by the cond argument to `condBroadcast()` or
`condSignal()` does not refer to an initialized condition variable.

## Return value

If successful, the `condBroadcast()` and `condSignal()` functions shall return zero; otherwise, an
error number shall be returned to indicate the error.

## Errors

The `condBroadcast()` and `condSignal()` function may fail if:

* `-EINVAL` - The value _h_ does not refer to an initialized condition variable.

* `-EINVAL` - Parent process for _h_ variable ceased to exist during function call

These functions shall not return an error code of `-EINTR`.

## Tests

Tested in [test-sys](https://github.com/phoenix-rtos/phoenix-rtos-tests/tree/master/sys)

## Known bugs

None
