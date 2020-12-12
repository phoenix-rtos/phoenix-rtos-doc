###Synopsis

`#include <fenv.h>`

`int fegetexceptflag(fexcept_t *flagp, int excepts);`
`int fesetexceptflag(const fexcept_t *flagp, int excepts);`

###Description

`fegetexceptflag()`, `fesetexceptflag()` - get and set current floating-point flags.

Arguments:

<u>flagp</u> - the object saving the floating-point status flags.
<u>excepts</u> -  the floating-point status flags. 

The `fegetexceptflag()` function stores the states of the floating-point status flags indicated by the argument <u>excepts</u> in the object pointed to by the argument <u>flagp</u>.

The `fesetexceptflag()` function sets the floating-point status flags indicated by the argument <u>excepts</u> to the states stored in the object pointed to by <u>flagp</u>. The value pointed to by <u>flagp</u> has been set by a previous call to `fegetexceptflag()` whose second argument represented at least those floating-point exceptions represented by the argument <u>excepts</u>. This function does not raise floating-point exceptions, but only sets the state of the flags.

###Return value

If the representation was successfully stored, `fegetexceptflag()` returns zero. Otherwise, it returns `-1`. 
If the <u>excepts</u> argument is zero or if all the specified exceptions were successfully set, `fesetexceptflag()` returns zero. Otherwise, it returns `-1`.

###Errors

No errors are defined.

###Implementation tasks

 * Implement `fenv.h`.
 * Implement `fegetexceptflag`.
 * Implement `fesetexceptflag`.