<!-- Documentation template to fill -->
# Synopsis 

`#include <wchar.h>`</br>

`size_t wcslen(const wchar_t *ws);`</br>

## Status

Declared, not implemented

## Conformance

IEEE Std 1003.1-2017

## Description 

The `wcslen()` function shall compute the number of wide-character codes in the wide-character string to which _`ws`_ points, not including the terminating `null` wide-character code.

The `wcsnlen()` function shall compute the smaller of the number of wide characters in the array to which _`ws`_ points, not including any terminating `null` wide-character code, and the value of `maxlen`. The `wcsnlen()` function shall never examine more than the first maxlen characters of the wide-character array pointed to by _`ws`_.

## Return value

The `wcslen()` function shall return the length of _`ws`_.

The `wcsnlen()` function shall return the number of wide characters preceding the first `null` wide-character code in the array to which _`ws`_ points, if _`ws`_ contains a `null` wide-character code within the first maxlen wide characters, otherwise, it shall return maxlen.

No return values are reserved to indicate an error.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs 

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)