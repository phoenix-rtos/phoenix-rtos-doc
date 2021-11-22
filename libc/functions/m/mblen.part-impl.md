# Synopsis 
`#include <stdlib.h>`</br>

` int mblen(const char *s, size_t n);`</br>

## Status
Partially implemented
## Conformance
IEEE Std 1003.1-2017
## Description

If _s_ is not a `null` pointer, `mblen()` shall determine the number of bytes constituting the character pointed to by
_s_. Except that the shift state of `mbtowc()` is not affected, it shall be
equivalent to: 
```c
mbtowc((wchar_t *)0, s, n);
```


The implementation shall behave as if no function defined in this volume of POSIX.1-2017 calls `mblen()`.

The behavior of this function is affected by the `LC_CTYPE` category of the current locale. For a state-dependent encoding,
this function shall be placed into its initial state by a call for which its character pointer argument, _s_, is a `null`
pointer. Subsequent calls with s as other than a `null` pointer shall cause the internal state of the function to be altered
as necessary. A call with _s_ as a `null` pointer shall cause this function to return a non-zero value if encodings have state
dependency, and 0 otherwise. If the implementation employs special bytes to change the shift state, these bytes shall not produce
separate wide-character codes, but shall be grouped with an adjacent character. Changing the `LC_CTYPE` category causes the
shift state of this function to be unspecified.
The
`mblen()` function need not be thread-safe. 


## Return value


If _s_ is a `null` pointer, `mblen()` shall return a non-zero or `0` value, if character encodings, respectively, do or do
not have state-dependent encodings. If _s_ is not a `null` pointer, `mblen()` shall either return `0` (if s points to
the `null` byte), or return the number of bytes that constitute the character (if the next n or fewer bytes form a valid
character), or return `-1` (if they do not form a valid character)    and may set `errno` to indicate the error.  In no case shall the value returned be greater than n or the value of
the `MB_CUR_MAX` macro.


## Errors


The `mblen()` function may fail if:


 * `EILSEQ` -   An invalid character sequence is detected. In the POSIX locale an `EILSEQ` error cannot occur since all byte values are valid
characters. 





## Tests

Untested

## Known bugs

None

## See Also 
1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
