# pthread_cond_timedwait

## Synopsis

```c
#include <pthread.h>

int pthread_cond_timedwait(pthread_cond_t *restrict cond,
                           pthread_mutex_t *restrict mutex,
                           const struct timespec *restrict abstime);

int pthread_cond_wait(pthread_cond_t *restrict cond,
                      pthread_mutex_t *restrict mutex);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_cond_timedwait()` and `pthread_cond_wait()` functions shall block on a condition variable. The application
shall ensure that these functions are called with _mutex_ locked by the calling thread; otherwise, an error (for
`PTHREAD_MUTEX_ERRORCHECK` and robust mutexes) or undefined behavior (for other mutexes) results.

These functions atomically release _mutex_ and cause the calling thread to block on the condition variable _cond_;
atomically here means "atomically with respect to access by another thread to the mutex and then the condition
variable". That is, if another thread is able to acquire the mutex after the about-to-block thread has released it,
then a subsequent call to `pthread_cond_broadcast()` or `pthread_cond_signal()` in that thread shall behave as if it
were issued after the about-to-block thread has blocked.

Upon successful return, the mutex shall have been locked and shall be owned by the calling thread. If _mutex_ is a
robust mutex where an owner terminated while holding the lock and the state is recoverable, the mutex shall be acquired
even though the function returns an error code.

When using condition variables there is always a Boolean predicate involving shared variables associated with each
condition wait that is true if the thread should proceed. Spurious wakeups from the `pthread_cond_timedwait()` or
`pthread_cond_wait()` functions may occur. Since the return from `pthread_cond_timedwait()` or `pthread_cond_wait()`
does not imply anything about the value of this predicate, the predicate should be re-evaluated upon such return.

When a thread waits on a condition variable, having specified a particular mutex to either the
`pthread_cond_timedwait()` or the `pthread_cond_wait()` operation, a dynamic binding is formed between that mutex and
condition variable that remains in effect as long as at least one thread is blocked on the condition variable. During
this time, the effect of an attempt by any thread to wait on that condition variable using a different mutex is
undefined. Once all waiting threads have been unblocked (as by the `pthread_cond_broadcast()` operation), the next wait
operation on that condition variable shall form a new dynamic binding with the mutex specified by that wait operation.

A condition wait (whether timed or not) is a cancellation point.

The `pthread_cond_timedwait()` function shall be equivalent to `pthread_cond_wait()`, except that an error is returned
if the absolute time specified by _abstime_ passes (that is, system time equals or exceeds _abstime_) before the
condition _cond_ is signaled or broadcasted, or if the absolute time specified by _abstime_ has already been passed at
the time of the call. When such timeouts occur, `pthread_cond_timedwait()` shall nonetheless release and re-acquire the
mutex referenced by _mutex_, and may consume a condition signal directed concurrently at the condition variable.

The condition variable shall have a clock attribute which specifies the clock that shall be used to measure the time
specified by the _abstime_ argument. The default clock is `CLOCK_REALTIME`; it can be changed to `CLOCK_MONOTONIC` with
`pthread_condattr_setclock()`.

If a signal is delivered to a thread waiting for a condition variable, upon return from the signal handler the thread
resumes waiting for the condition variable as if it was not interrupted, or it shall return zero due to spurious
wakeup.

The behavior is undefined if the value specified by the _cond_ or _mutex_ argument to these functions does not refer to
an initialized condition variable or an initialized mutex object, respectively.

## Return value

Except for `ETIMEDOUT`, `ENOTRECOVERABLE`, and `EOWNERDEAD`, all these error checks shall act as if they were performed
immediately at the beginning of processing for the function and shall cause an error return, in effect, prior to
modifying the state of the mutex specified by _mutex_ or the condition variable specified by _cond_.

Upon successful completion, a value of zero shall be returned; otherwise, an error number shall be returned to indicate
the error.

## Errors

These functions shall fail if:

* `ENOTRECOVERABLE` - The state protected by the mutex is not recoverable.

* `EOWNERDEAD` - The mutex is a robust mutex and the process containing the previous owning thread terminated while
holding the mutex lock. The mutex lock shall be acquired by the calling thread, and it is up to the new owner to make
the state consistent.

* `EPERM` - The mutex type is `PTHREAD_MUTEX_ERRORCHECK` or the mutex is a robust mutex, and the current thread does not
own the mutex.

The `pthread_cond_timedwait()` function shall fail if:

* `ETIMEDOUT` - The time specified by _abstime_ to `pthread_cond_timedwait()` has passed.

* `EINVAL` - The _abstime_ argument specified a nanosecond value less than zero or greater than or equal to 1000
million.

These functions may fail if:

* `EOWNERDEAD` - The mutex is a robust mutex and the previous owning thread terminated while holding the mutex lock. The
mutex lock shall be acquired by the calling thread, and it is up to the new owner to make the state consistent.

These functions shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
