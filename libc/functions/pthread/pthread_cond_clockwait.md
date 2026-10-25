# pthread_cond_clockwait

## Synopsis

```c
#include <pthread.h>

int pthread_cond_clockwait(pthread_cond_t *restrict cond,
                           pthread_mutex_t *restrict mutex, clockid_t clock_id,
                           const struct timespec *restrict abstime);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2024

## Description

The `pthread_cond_clockwait()` function shall block on a condition variable. The application shall ensure that this
function is called with _mutex_ locked by the calling thread; otherwise, an error (for `PTHREAD_MUTEX_ERRORCHECK` and
robust mutexes) or undefined behavior (for other mutexes) results.

The function atomically releases _mutex_ and causes the calling thread to block on the condition variable _cond_;
atomically here means "atomically with respect to access by another thread to the mutex and then the condition
variable". That is, if another thread is able to acquire the mutex after the about-to-block thread has released it,
then a subsequent call to `pthread_cond_broadcast()` or `pthread_cond_signal()` in that thread shall behave as if it
were issued after the about-to-block thread has blocked.

Upon successful return, the mutex shall have been locked and shall be owned by the calling thread.

If _mutex_ is a robust mutex where an owner terminated while holding the lock and the state is recoverable, the mutex
shall be acquired even though the function returns `EOWNERDEAD`.

When using condition variables there is always a Boolean predicate involving shared variables associated with each
condition wait that is true if the thread should proceed. Spurious wakeups from the `pthread_cond_clockwait()` function
may occur. Since the return from `pthread_cond_clockwait()` does not imply anything about the value of this predicate,
the predicate should be re-evaluated upon such return.

When a thread waits on a condition variable, having specified a particular mutex to the `pthread_cond_clockwait()`
operation, a dynamic binding is formed between that mutex and condition variable that remains in effect as long as at
least one thread is blocked on the condition variable. During this time, the effect of an attempt by any thread to wait
on that condition variable using a different mutex is undefined. Once all waiting threads have been unblocked (as by the
`pthread_cond_broadcast()` operation), the next wait operation on that condition variable shall form a new dynamic
binding with the mutex specified by that wait operation. The unblocked thread shall always re-acquire the mutex
specified in the condition wait operation call from which it is returning.

A condition wait (whether timed or not) is a cancellation point. A thread that has been unblocked because it has been
canceled while blocked in a call to `pthread_cond_clockwait()` shall not consume any condition signal that may be
directed concurrently at the condition variable if there are other threads blocked on the condition variable.

The `pthread_cond_clockwait()` function shall be equivalent to `pthread_cond_wait()`, except that an error is returned
if the absolute time specified by _abstime_ as measured against the clock indicated by _clock_id_ passes (that is, the
current time measured by that clock equals or exceeds _abstime_) before the condition _cond_ is signaled or broadcasted,
or if the absolute time specified by _abstime_ has already been passed at the time of the call. Implementations shall
support passing `CLOCK_REALTIME` and `CLOCK_MONOTONIC` to `pthread_cond_clockwait()` as the _clock_id_ argument
(`CLOCK_MONOTONIC_RAW` is also accepted, as an alias of `CLOCK_MONOTONIC`). When such timeouts occur,
`pthread_cond_clockwait()` shall nonetheless release and re-acquire the mutex referenced by _mutex_, and may consume a
condition signal directed concurrently at the condition variable.

If a signal is delivered to a thread waiting for a condition variable, upon return from the signal handler the thread
resumes waiting for the condition variable as if it was not interrupted, or it shall return zero due to spurious
wakeup.

The behavior is undefined if the value specified by the _cond_ or _mutex_ argument to this function does not refer to an
initialized condition variable or an initialized mutex object, respectively.

## Return value

Except for `ETIMEDOUT`, `ENOTRECOVERABLE`, and `EOWNERDEAD`, all the error checks shall act as if they were performed
immediately at the beginning of processing for the function and shall cause an error return, in effect, prior to
modifying the state of the mutex specified by _mutex_ or the condition variable specified by _cond_.

Upon successful completion, a value of zero shall be returned; otherwise, an error number shall be returned to indicate
the error.

## Errors

The `pthread_cond_clockwait()` function shall fail if:

* `EAGAIN` - The mutex is a robust mutex and the system resources available for robust mutexes owned would be exceeded.

* `ENOTRECOVERABLE` - The state protected by the mutex is not recoverable.

* `EOWNERDEAD` - The mutex is a robust mutex and the process containing the previous owning thread terminated while
holding the mutex lock. The mutex lock shall be acquired by the calling thread, and it is up to the new owner to make
the state consistent.

* `EPERM` - The mutex type is `PTHREAD_MUTEX_ERRORCHECK` or the mutex is a robust mutex, and the current thread does not
own the mutex.

* `ETIMEDOUT` - The time specified by _abstime_ has passed.

* `EINVAL` - The _abstime_ argument specified a nanosecond value less than zero or greater than or equal to 1000
million, or the _clock_id_ argument is invalid or not supported.

The `pthread_cond_clockwait()` function may fail if:

* `EOWNERDEAD` - The mutex is a robust mutex and the previous owning thread terminated while holding the mutex lock. The
mutex lock shall be acquired by the calling thread, and it is up to the new owner to make the state consistent.

This function shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
