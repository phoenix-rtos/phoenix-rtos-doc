###Synopsis
`#include <setjmp.h>`

`int _setjmp(jmp_buf env);`
`void _longjmp(jmp_buf env, int val);`

###Description

The `_setjmp()` saves the current environment, while `_longjmp` executes non-local goto using the saved environment.

Arguments:
<u>jmp_buf env</u> - saved environment (by last call to `_setjmp()`)
<u>val</u> - value to which the `_setjmp` expression evaluates.

The `_setjmp()` function saves the current environment in its <u>env</u> argument. It is equivalent to `setjmp()` with the additional restriction that `_setjmp()` does not manipulate the signal mask. 
The `_longjmp()` function is equivalent to `longjmp()` with the additional restriction that `_longjmp()` does not manipulate the signal mask.

If `_longjmp()` is called even though <u>env</u> was never initialized by a call to `_setjmp()`, or when the last such call was in a function that has since returned, the results are undefined.

###Return value
After `_longjmp()` is completed, program execution continues as if the corresponding invocation of `_setjmp()` had just returned the value specified by <u>val</u>. The `_longjmp()` function does not cause `_setjmp()` to return `0`; if <u>val</u> is `0`, `_setjmp()` returns `1`.

###Errors
No errors are defined.

###Comments
The `_longjmp()` and `_setjmp()` functions may be removed in a future version.
