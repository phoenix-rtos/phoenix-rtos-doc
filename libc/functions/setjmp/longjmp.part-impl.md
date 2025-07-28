# longjmp

## Synopsis

```c
#include <setjmp.h>

void longjmp(jmp_buf env, int val);
```

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `longjmp()` function shall restore the environment saved by the most recent invocation of `setjmp()` in the same
process, with the corresponding `jmp_buf` argument. If the most recent invocation of `setjmp()` with the corresponding
`jmp_buf` occurred in another thread, or if there is no such invocation, or if the function containing the invocation of
`setjmp()` has terminated execution in the interim, or if the invocation of `setjmp()` was within the scope of an
identifier with variably modified type and execution has left that scope in the interim, the behavior is undefined.
It is unspecified whether `longjmp()` restores the signal mask, leaves the signal mask unchanged, or restores it to
its value at the time `setjmp()` was called. All accessible objects have values, and all other components of the
abstract machine have state (for example, floating-point status flags and open files), as of the time `longjmp()`
was called, except that the values of objects of automatic storage duration are unspecified if they meet all the
following conditions:

* They are local to the function containing the corresponding `setjmp()` invocation.

* They do not have volatile-qualified type.

* They are changed between the `setjmp()` invocation and `longjmp()` call.

Although `longjmp()` is an async-signal-safe function, if it is invoked from a signal handler which interrupted a
non-async-signal-safe function or equivalent (such as the processing equivalent to `exit()` performed after a return
from the initial call to `main()`), the behavior of any subsequent call to a non-async-signal-safe function or
equivalent is undefined.

The effect of a call to `longjmp()` where initialization of the `jmp_buf` structure was not performed in the calling
thread is undefined.

## Return value

After `longjmp()` is completed, program execution continues as if the corresponding invocation of `setjmp()` had just
returned the value specified by _val_. The `longjmp()` function shall not cause `setjmp()` to return `0`; if _val_ is
`0`, `setjmp()` shall return `1`.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None
