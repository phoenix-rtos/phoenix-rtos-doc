# pthread_cleanup_pop

## Synopsis

```c
#include <pthread.h>

void pthread_cleanup_pop(int execute);

void pthread_cleanup_push(void (*routine)(void*), void *arg);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_cleanup_pop()` function shall remove the routine at the top of the calling thread's cancellation cleanup
stack and optionally invoke it (if _execute_ is non-zero).

The `pthread_cleanup_push()` function shall push the specified cancellation cleanup handler _routine_ onto the calling
thread's cancellation cleanup stack. The cancellation cleanup handler shall be popped from the cancellation cleanup
stack and invoked with the argument _arg_ when:

* The thread exits (that is, calls `pthread_exit()`).

* The thread acts upon a cancellation request.

* The thread calls `pthread_cleanup_pop()` with a non-zero _execute_ argument.

It is unspecified whether `pthread_cleanup_push()` and `pthread_cleanup_pop()` are macros or functions. In Phoenix-RTOS
they are functions. If a macro definition is suppressed in order to access an actual function, or a program defines an
external identifier with any of these names, the behavior is undefined. The application shall ensure that they appear
as statements, and in pairs within the same lexical scope (that is, the `pthread_cleanup_push()` macro may be thought
to expand to a token list whose first token is `'{'` with `pthread_cleanup_pop()` expanding to a token list whose last
token is the corresponding `'}'`).

The effect of calling `longjmp()` or `siglongjmp()` is undefined if there have been any calls to
`pthread_cleanup_push()` or `pthread_cleanup_pop()` made without the matching call since the jump buffer was filled.
The effect of calling `longjmp()` or `siglongjmp()` from inside a cancellation cleanup handler is also undefined unless
the jump buffer was also filled in the cancellation cleanup handler.

The effect of the use of `return`, `break`, `continue`, and `goto` to prematurely leave a code block described by a
pair of `pthread_cleanup_push()` and `pthread_cleanup_pop()` functions calls is undefined.

## Return value

The `pthread_cleanup_push()` and `pthread_cleanup_pop()` functions shall not return a value.

## Errors

No errors are defined.

These functions shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
