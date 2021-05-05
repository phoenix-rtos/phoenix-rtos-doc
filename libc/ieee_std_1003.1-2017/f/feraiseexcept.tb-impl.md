###Synopsis

`#include <fenv.h>`

`int feraiseexcept(int excepts);`

###Description

The `feraiseexcept` function raises floating-point exception.

Arguments:

<u>excepts</u> - the supported floating-point exceptions.

The `feraiseexcept()` function raises the supported floating-point exceptions. 

`feraiseexcept()` invokes any traps that have been enabled for the given exceptions. The argument is a bitwise OR of the values of the following macros, defined in fenv.h to represent the floating-point exception flags:

* `FE_DIVBYZERO` - this exception occurs when a nonzero, noninfinite number is divided by zero.
* `FE_INEXACT` - this exception indicates that true result of an operation cannot be represented with  the  available  precision,  and  has  been  rounded  in  the  current  rounding direction.
* `FE_INVALID` - this exception flag is set when the program attempts an operation which has nodefined result, such as dividing zero by zero or subtracting infinity from infinity.Some systems may also set FE_INVALID whenever an overflow or underflow exception is raised.
* `FE_OVERFLOW` - the result of an operation exceeds the range of representable values.
* `FE_UNDERFLOW` - the  result  of  an  operation  is  nonzero,  but  too  small  in  magnitude  to  be represented.
* `FE_ALL_EXCEPT` - the bitwise OR of all of the macros that are supported.

###Return value

The `feraiseexcept()` function returns zero if successful, otherwise it returns -1.

###Errors

No errors are defined.

###Implementation tasks

 * Implement `fenv.h`.
 * Implement `feraiseexcept()`.