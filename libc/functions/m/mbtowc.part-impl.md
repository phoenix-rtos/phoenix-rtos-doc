# Synopsis 
`#include <stdlib.h>`</br>
` int mbtowc(wchar_t *restrict pwc, const char *restrict s, size_t n);`</br>

## Status
Partially implemented
## Conformance
IEEE Std 1003.1-2017
## Description

If _s_ is not a _null_ pointer, `mbtowc()` shall determine the number of bytes that constitute the character pointed to
by _s_. It shall then determine the wide-character code for the value of type `wchar_t` that corresponds to that
character. (The value of the wide-character code corresponding to the _null_ byte is `0`.) If the character is valid and _pwc_ is
not a _null_ pointer, `mbtowc()` shall store the wide-character code in the object pointed to by _pwc_.

The behavior of this function is affected by the `LC_CTYPE` category of the current locale. For a state-dependent encoding,
this function is placed into its initial state by a call for which its character pointer argument, _s_, is a _null_ pointer.

Subsequent calls with _s_ as other than a _null_ pointer shall cause the internal state of the function to be altered as
necessary. A call with _s_ as a _null_ pointer shall cause this function to return a non-zero value if encodings have state
dependency, and `0` otherwise. If the implementation employs special bytes to change the shift state, these bytes shall not produce
separate wide-character codes, but shall be grouped with an adjacent character. Changing the `LC_CTYPE` category causes the
shift state of this function to be unspecified. At most _n_ bytes of the array pointed to by _s_ shall be examined.

The implementation shall behave as if no function defined in this volume of POSIX.1-2017 calls `mbtowc()`.

The
`mbtowc()` function need not be thread-safe. 


## Return value


If _s_ is a _null_ pointer, `mbtowc()` shall return a non-zero or 0 value, if character encodings, respectively, do or
do not have state-dependent encodings. If _s_ is not a _null_ pointer, `mbtowc()` shall either return `0` (if _s_ points
to the _null_ byte), or return the number of bytes that constitute the converted character (if the next _n_ or fewer bytes form
a valid character), or return `-1`    and shall set `errno` to indicate the error  (if they do not form a valid character).

In no case shall the value returned be greater than n or the value of the `MB_CUR_MAX` macro.


## Errors


The `mbtowc()` function shall fail if:


 * `EILSEQ` -   An invalid character sequence is detected. In the POSIX locale an `EILSEQ` error cannot occur since all byte values are valid
characters. 





## Tests

Untested

## Known bugs

None

## See Also 
1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
