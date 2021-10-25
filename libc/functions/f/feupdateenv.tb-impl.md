###Synopsis

`#include <fenv.h>`

`int feupdateenv(const fenv_t *envp);`

###Description

The `feupdateenv()` function saves the currently raised floating-point exceptions in its automatic storage, attempts to install the floating-point environment represented by the object pointed to by <u>envp</u>, and then attempts to raise the saved floating-point exceptions. 

Arguments:

<u>envp</u> - The pointer to an object set by a call to `feholdexcept()` or `fegetenv()`, or equal a floating-point environment macro.

###Return value

`0` on success, otherwise '-1'.

###Errors

No errors are defined.

###Implementation tasks

* Implement the `feupdateenv()` function.