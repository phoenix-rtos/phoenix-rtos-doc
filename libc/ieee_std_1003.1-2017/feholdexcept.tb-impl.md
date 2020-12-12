###Synopsis

`#include <fenv.h>`

`int feholdexcept(fenv_t *envp);`

###Description

The `feholdexcept()` function saves current floating-point environment.

Arguments:

<u>envp</u> - the pointer to the current floating-point environment.

The `feholdexcept()` function saves the current floating-point environment in the object of `fenv_t` and then resets the current values of all the floating point status flags.

###Return value

The `feholdexcept()` function returns zero if and only if non-stop floating-point exception handling was successfully installed, otherwise it returns -1.

###Errors

No errors are defined.

###Implementation tasks

 * Implement `fenv.h`.
 * Implement `feholdexcept()`.