###Synopsis

`#include <math.h>`

`int fpclassify(real-floating x);`
 
###Description

The `fpclassify()` macro classifies its argument value as `NaN`, infinite, normal, subnormal or zero. First, an argument represented in a format wider than its semantic type is converted to its semantic type. Then classification is based on the type of the argument.

Arguments:

<u>x</u> - a number to be classified.

###Return value

The `fpclassify()` returns the value of the number classification macro appropriate to the value of its argument.

###Errors

No errors are defined.

###Implementation tasks

 * Complete `math.h` with following constants:
     `FP_INFINITE` (Positive or negative infinity (overflow))
     `FP_NAN` (Not-A-Number)
     `FP_NORMAL` (Normal value)
     `FP_SUBNORMAL` (Sub-normal value (underflow))
     `FP_ZERO` (Value of zero).
 * Implement the `fpclassify()`.