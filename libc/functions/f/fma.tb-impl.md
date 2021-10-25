###Synopsis

`#include <math.h>`

`double fma(double x, double y, double z);`
`float fmaf(float x, float y, float z);`
`long double fmal(long double x, long double y, long double z);`

###Description

These functions compute (<u>x</u> * <u>y</u>) + <u>z</u>, rounded as one ternary operation: they compute the value (as if) to infinite precision and round once to the result format, according to the rounding mode characterized by the value of `FLT_ROUNDS`.

Arguments:
<u>x</u> - the first argument of the function.
<u>y</u> - the second argument of the function.
<u>z</u> - the third argument of the function.

An application wishing to check for error situations should set `errno` to zero and call `feclearexcept(FE_ALL_EXCEPT)` before calling these functions. On return, if `errno` is non-zero or `fetestexcept(FE_INVALID | FE_DIVBYZERO | FE_OVERFLOW | FE_UNDERFLOW)` is non-zero, an error has occurred.

###Return value

Upon successful completion, these functions return (<u>x</u> * <u>y</u>) + <u>z</u>, rounded as one ternary operation.

If <u>x</u> or <u>y</u> are `NaN`, a `NaN` is returned.

If <u>x</u> multiplied by <u>y</u> is an exact infinity and <u>z</u> is also an infinity but with the opposite sign, a domain error occurs, and either a `NaN` (if supported), or an implementation-defined value is returned.

If one of <u>x</u> and <u>y</u> is infinite, the other is zero, and <u>z</u> is not a `NaN`, a domain error occurs, and either a `NaN` (if supported), or an implementation-defined value is returned.

If one of <u>x</u> and <u>y</u> is infinite, the other is zero, and <u>z</u> is a `NaN`, a `NaN` is returned and a domain error may occur.

If <u>x</u> * <u>y</u> is not `0` * Inf nor Inf * `0` and <u>z</u> is a `NaN`, a `NaN` is returned.

###Errors

[`ERANGE`]  The result overflows or underflows. 
           If the integer expression (`math_errhandling & MATH_ERRNO`) is non-zero, then `errno` is set to [`ERANGE`]. If the integer expression (`math_errhandling & MATH_ERREXCEPT`) is non-zero, then the overflow or underflow floating-point exception is raised.

[`EDOM`]  

 * The value of <u>x</u> * <u>y</u> + <u>z</u> is invalid, or the value <u>x</u> *  <u>y</u> is invalid and <u>z</u> is not a `NaN`.
If the integer expression (`math_errhandling & MATH_ERRNO`) is non-zero, then `errno` is set to [`EDOM`]. If the integer expression (`math_errhandling & MATH_ERREXCEPT`) is non-zero, then the invalid floating-point exception is raised. 

 * The value <u>x</u>* <u>y</u> is invalid and <u>z</u> is a `NaN`.
    

###Implementation tasks

 * Implement the `fma()` function.
 * Implement the `fmaf()` function.
 * Implement the `fmal()` function.
