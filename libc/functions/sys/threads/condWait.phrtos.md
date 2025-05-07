# condWait

## Synopsis

`#include <sys/threads.h>`

`int condWait(handle_t h, handle_t m, time_t timeout);`

## Status

Implemented

## Conformance

Phoenix-RTOS specific

## Description

The `condWait()` function shall block on a condition variable specified by _h_ until it is signaled or _timeout_
microseconds passes. The application shall ensure that these functions are called with mutex _m_ locked by the calling
thread; otherwise, an error or undefined behavior results.

These functions atomically release mutex and cause the calling thread to block on the condition variable _h_;
atomically here means "atomically with respect to access by another thread to the mutex _m_ and then the condition
variable". That is, if another thread is able to acquire the mutex after the about-to-block thread has released it,
then a subsequent call to `condSignal()` or `condBroadcast()` in that thread shall behave as if it were issued after
the about-to-block thread has blocked.

Upon successful return, the mutex _m_ shall have been locked and shall be owned by the calling thread.

When using condition variables there is always a Boolean predicate involving shared variables associated with each
condition wait that is true if the thread should proceed. Spurious wake-ups from the `condWait()` functions may occur.
Since the return from `condWait()` does not imply anything about the value of this predicate, the predicate should be
re-evaluated upon such return.

If condition was signaled when no thread was waiting on it first `condWait()` on it will return immediately.

When a thread waits on a condition variable, having specified a particular mutex to the `condWait()` operation, a
dynamic binding is formed between that mutex and condition variable that remains in effect as long as at least one
thread is blocked on the condition variable. During this time, the effect of an attempt by any thread to wait on that
condition variable using a different mutex is undefined. Once all waiting threads have been unblocked
(as by the `condBroadcast()` operation), the next wait operation on that condition variable shall form a new dynamic
binding with the mutex specified by that wait operation. Even though the dynamic binding between condition variable and
mutex may be removed or replaced between the time a thread is unblocked from a wait on the condition variable and the
time that it returns to the caller or begins cancellation cleanup, the unblocked thread shall always re-acquire the
mutex specified in the condition wait operation call from which it is returning.

A thread that has been unblocked because it has been canceled while blocked in a call to `condWait()` shall not consume
any condition signal that may be directed concurrently at the condition variable if there are other threads blocked on
the condition variable.

If a signal is delivered to a thread waiting for a condition variable, upon return from the signal handler the thread
resumes waiting for the condition variable as if it was not interrupted, or it shall return zero due to spurious
wake-up.

The behavior is undefined if the value specified by the _h_ or mutex _m_ argument to these functions does not refer
to an initialized condition variable or an initialized mutex object, respectively.

If _timeout_ is nonzero `-ETIME` is returned if condition is not signaled after waiting for _timeout_ microseconds. Zero
_timeout_ waits indefinitely until condition is signaled. Note that due to internal implementation timeout is restarted
when signal is received (retry on `EINTR`).

## Return value

Upon successful completion, a value of zero shall be returned; otherwise, an error number shall be returned to indicate
the error.

## Errors

This function shall fall if:

* `-EINVAL` - The value _h_ does not refer to an initialized condition variable,

* `-EINVAL` - Parent process for _h_ variable or mutex _m_ ceased to exist during function call

* `-ETIME` - Condition was not signaled before specified timeout

## Tests

Tested in [test-sys](https://github.com/phoenix-rtos/phoenix-rtos-tests/tree/master/sys)

## Known bugs

None
