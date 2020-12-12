###Synopsis
`#include <setjmp.h>`

`int _setjmp(jmp_buf env);`

###Description

The `_setjmp()` function saves the current environment. It is equivalent to `setjmp()` with the additional restriction that `_setjmp()` does not manipulate the signal mask. 
The `_longjmp()` and `_setjmp()` functions may be removed in a future version.

Arguments:
<u> env </u> - the calling environment to be saved for later use by `_longjmp()`.

###Return value
If the return is from a direct invocation, `_setjmp()` returns `0`. If the return is from a call to `longjmp()`,`_setjmp()` returns a non-zero value.

###Errors

No errors are defined.

###Comments
The `_longjmp()` and `_setjmp()` functions may be removed in a future version.