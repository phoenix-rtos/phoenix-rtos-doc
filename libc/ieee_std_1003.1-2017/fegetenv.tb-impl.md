###Synopsis

`#include <fenv.h>`

`int fegetenv(fenv_t *envp);`
`int fesetenv(const fenv_t *envp);`

###Description

`fegetenv()`, `fesetenv()` - get and set current floating-point environment.

Arguments:

<u>envp</u> - the pointer to the floating-point environment.

The `fegetenv()` function attempts to store the current floating-point environment in the object pointed to by <u>envp</u>.

The `fesetenv()` function attempts to establish the floating-point environment represented by the object pointed to by <u>envp</u>. The argument <u>envp</u> points to an object set by a call to `fegetenv()` or `feholdexcept()`, or equal a floating-point environment macro. The `fesetenv()` function does not raise floating-point exceptions, but only installs the state of the floating-point status flags represented through its argument.

###Return value

If the representation is successfully stored, `fegetenv()` returns zero. Otherwise, it returns `-1`. 

If the environment was successfully established, `fesetenv()` returns zero. Otherwise, it returns `-1`.

###Errors

No errors are defined.

###Implementation tasks

 * Implement `fenv.h`.
 * Implement `fegetenv()`.
 * Implement `fesetenv()`.