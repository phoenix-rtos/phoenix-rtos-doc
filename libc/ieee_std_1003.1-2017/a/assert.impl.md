###Synopsis

`#include <assert.h>`

`void assert(scalar expression);`

###Description

The `assert()` macro inserts diagnostics into programs; it expands to a void expression. When it is executed, if expression (which has a scalar type) is false (that is, compares equal to 0), assert() writes information about the particular call that failed on `stderr` and calls `abort()`.

The information written about the call that failed includes the text of the argument, the name of the source file, the source file line number, and the name of the enclosing function; the latter are, respectively, the values of the preprocessing macros `__FILE__` and `__LINE__` and of the identifier `__func__`.

Forcing a definition of the name `NDEBUG`, either from the compiler command line or with the preprocessor control statement `#define NDEBUG` ahead of the `#include <assert.h>` statement, stops assertions from being compiled into the program.

Arguments:
<u>expression</u> - the condition to be tested.

###Return value
The `assert()` macro does not return a value.