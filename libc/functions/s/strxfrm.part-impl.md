# Synopsis 
`#include <string.h>`</br>

` size_t strxfrm(char *restrict s1, const char *restrict s2, size_t n);`</br>

` size_t strxfrm_l(char *restrict s1, const char *restrict s2,`</br>
`        size_t n, locale_t locale); `</br>

## Status
Partially implemented
## Conformance
IEEE Std 1003.1-2017
## Description


The `strxfrm()`    and `strxfrm_l()` 
functions shall transform the string pointed to by _s2_ and place the resulting string into the array pointed to by
_s1_. The transformation is such that if `strcmp()` is applied to two transformed
strings, it shall return a value greater than, equal to, or less than `0`, corresponding to the result of `strcoll()`    or `strcoll_l()`,
respectively, applied to the same two original strings
with the same locale. No more than n bytes are
placed into the resulting array pointed to by _s1_, including the terminating `NUL` character. If _n_ is `0`, _s1_ is
permitted to be a null pointer. If copying takes place between objects that overlap, the behavior is undefined.

The
`strxfrm()` and `strxfrm_l()` functions shall not change the setting of `errno` if successful. 
Since no return value is reserved to indicate an error, an application wishing to check for error situations should set
`errno` to `0`, then call `strxfrm()`    or `strxfrm_l()`,   then check `errno`.
The
behavior is undefined if the locale argument to `strxfrm_l()` is the special locale object `LC_GLOBAL_LOCALE` or is not a
valid locale object handle. 


## Return value


Upon successful completion, `strxfrm()`    and `strxfrm_l()`   shall return the length of the transformed string (not including the terminating `NUL` character).
If the value returned is _n_ or more, the contents of the array pointed to by _s1_ are unspecified.
On error, `strxfrm()`    and `strxfrm_l()`   may
set `errno` but no return value is reserved to indicate an error.


## Errors


These functions may fail if:


 * `EINVAL` - The string pointed to by the _s2_ argument contains characters outside the domain of the collating sequence. 



## Tests

Untested

## Known bugs

None

## See Also 
1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
