# fmod

## Synopsis

```c
#include <math.h>

double fmod(double x, double y);

float fmodf(float x, float y);

long double fmodl(long double x, long double y);
```

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

These functions shall return the floating-point remainder of the division of _x_ by _y_.

An application wishing to check for error situations should set `errno` to zero and call `feclearexcept(FE_ALL_EXCEPT)`
before calling these functions. On return, if `errno` is non-zero or
`fetestexcept(FE_INVALID | FE_DIVBYZERO | FE_OVERFLOW | FE_UNDERFLOW)` is non-zero, an error has occurred.

## Return value

These functions shall return the value `(x-i*y)`, for some integer `i` such that, if _y_ is non-zero, the result has the
same sign as _x_ and magnitude less than the magnitude of _y_.

* If the correct value would cause underflow and is not representable, a range error may occur, and `fmod()`, `modf()`,
 and `fmodl()` shall return `0.0`, or (if the `IEC 60559` Floating-Point option is not supported) an
 implementation-defined value no greater in magnitude than `DBL_MIN`, `FLT_MIN`, and `LDBL_MIN`, respectively.

* If _x_ or _y_ is `NaN`, a `NaN` shall be returned, and none of the conditions below shall be considered.
* If _y_ is zero, a domain error shall occur, and a `NaN` shall be returned.
* If _x_ is infinite, a domain error shall occur, and a `NaN` shall be returned.
* If _x_ is `±0` and _y_ is not zero, `±0` shall be returned.
* If _x_ is not infinite and _y_ is `±Inf`, _x_ shall be returned.
* If the correct value would cause underflow, and is representable, a range error may occur, and the correct value shall
 be returned.

## Errors

These functions shall fail if:

* `Domain Error` - The _x_ argument is infinite or _y_ is zero.

* If the integer expression `(math_errhandling & MATH_ERRNO)` is non-zero, then `errno` shall be set to `EDOM`.
* If the integer expression `(math_errhandling & MATH_ERREXCEPT)` is non-zero, then the invalid floating-point
 exception shall be raised.

These functions may fail if:

* `Range Error` - The result underflows.
* If the integer expression `(math_errhandling & MATH_ERRNO)` is non-zero, then `errno` shall be set to `ERANGE`.
* If the integer expression `(math_errhandling & MATH_ERREXCEPT)` is non-zero, then the underflow floating-point
 exception shall be raised.

## Tests

Untested

## Known bugs

None
