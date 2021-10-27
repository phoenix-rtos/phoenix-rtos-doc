<!-- Documentation template to fill -->
# Synopsis 

`#include <stdlib.h>`</br>
`size_t wcstombs(char *str, const wchar_t *pwcs, size_t n);`</br>

<!-- #MUST_BE: check status according to implementation -->
## Status

Declared, not implemented

<!-- #MUST_BE: if function shall be posix compliant print the standard signature  -->
## Conformance

IEEE Std 1003.1-2017 

<!-- #MUST_BE: update description from opengroup AND READ IT and check if it matches  -->
## Description 
 
`wcstombs()` - convert a wide-character string to a character string

The `wcstombs()` function shall convert the sequence of wide-character codes that are in the array pointed to by pwcs into a sequence of characters that begins in the initial shift state and store these characters into the array pointed to by _s_, stopping if a character would exceed the limit of _n_ total bytes or if a null byte is stored. Each wide-character code shall be converted as if by a call to `wctomb()`, except that the shift state of `wctomb()` shall not be affected.

The behavior of this function shall be affected by the `LC_CTYPE` category of the current locale.

No more than _n_ bytes shall be modified in the array pointed to by _s_. If copying takes place between objects that overlap, the behavior is undefined. If _s_ is a `null` pointer, `wcstombs()` shall return the length required to convert the entire array regardless of the value of _n_, but no values are stored. 

<!-- #MUST_BE: check return values by the function  -->
## Return value

If a wide-character code is encountered that does not correspond to a valid character (of one or more bytes each), `wcstombs()` shall return `(size_t)-1`. Otherwise, `wcstombs()` shall return the number of bytes stored in the character array, not including any terminating `null` byte. The array shall not be `null`-terminated if the value returned is _n_.

<!-- #MUST_BE: check what errors can cause the function to fail  -->
## Errors

The `wcstombs()` function shall fail if:

* `EILSEQ` - a wide-character code does not correspond to a valid character. 

<!-- #MUST_BE: function by default shall be untested, when tested there should be a link to test location and test command for ia32 test runner  -->
## Tests

Untested 

<!-- #MUST_BE: check for pending issues in  -->
## Known bugs 

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)