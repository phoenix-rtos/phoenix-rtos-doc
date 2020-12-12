###Synopsis

`#include <fenv.h>`

`int fegetround(void);`
`int fesetround(int round);`

###Description

`fegetround()`, `fesetround()` - get and set current rounding direction.

Arguments:

<u>round</u> - the rounding direction to be set.

The `fegetround()` function gets the current rounding direction.

The `fesetround()` function establishes the rounding direction (in the program's floating-point environment) represented by its argument <u>round</u>. If the argument is not equal to the value of a rounding direction macro, the rounding direction is not changed. Recognized values of the argument are given by macros in the following list, defined in `fenv.h` as integer constants:
`FE_DOWNWARD` Round down to the next lower integer.
`FE_UPWARD`   Round up to the next greater integer.
`FE_TONEAREST` Round up or down toward whichever integer is nearest.
`FE_TOWARDZERO` Round positive values downward and negative values upward.

###Return value

The `fegetround()` function returns the value of the rounding direction macro representing the current rounding direction or `-1` if there is no such rounding direction macro or the current rounding direction is not determinable.

The `fesetround()` function returns a zero value if and only if the requested rounding direction was established, otherwise it returns `-1`.

###Errors

No errors are defined.

###Implementation tasks

 * Implement `fenv.h`.
 * Implement `fegetround()`.
 * Implement `fesetround()`.