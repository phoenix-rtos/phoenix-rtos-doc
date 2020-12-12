###Synopsis

`#include <fenv.h>`

`int feclearexcept(int excepts);`

###Description

The `feclearexcept()` function attempts to clear the supported floating-point exceptions represented by <u>excepts</u>.

Arguments:

<u>excepts</u> - the exceptions to be cleared.

###Return value

If the argument is zero or if all the specified exceptions were successfully cleared, `feclearexcept()` returns zero. Otherwise, it returns `-1`.

###Errors

No errors are defined.

###Implementation tasks

 * Implement `feclearexcept()` function.