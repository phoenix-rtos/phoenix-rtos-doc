###Synopsis

`#include <stdlib.h>`

`div_t div(int numer, int denom);`

###Description

The function divides <u>numer</u> (numerator) by <u>denom</u> (denominator).

The returned structure includes the following members, in any order:

`int  quot;  /* quotient */`
`int  rem;   /* remainder */`

If the result cannot be represented, the behavior is undefined; otherwise, `quot`* <u>denom</u>+ `rem` equals <u>numer</u>.

###Return value

The function returns a structure of type `div_t`, comprising both the quotient and the remainder. 

###Errors

No errors are defined.