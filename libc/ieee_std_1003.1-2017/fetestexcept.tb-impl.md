###Synopsis

`#include <fenv.h>`

`int fetestexcept(int excepts);`

###Description

The `fetestexcept()` function determines which of a specified subset of the floating-point exception flags is currently set. 

Arguments:

<u>excepts</u> - the floating-point status flags to be queried.

###Return value

The `fetestexcept()` function returns the value of the bitwise-inclusive OR of the floating-point exception macros corresponding to the currently set floating-point exceptions included in <u>excepts</u>.

###Errors

No errors are defined.

###Example

The following example calls function `f()` if an invalid exception is set, and then function `g()` if an overflow exception is set:

    #include <fenv.h>
    /* ... */
    {
        #pragma STDC FENV_ACCESS ON
        int set_excepts;
        feclearexcept(FE_INVALID | FE_OVERFLOW);
        // maybe raise exceptions
        set_excepts = fetestexcept(FE_INVALID | FE_OVERFLOW);
        if (set_excepts & FE_INVALID) f();
        if (set_excepts & FE_OVERFLOW) g();
        /* ... */
    }

###Implementation tasks

* Implement the `fetestexcept()` function