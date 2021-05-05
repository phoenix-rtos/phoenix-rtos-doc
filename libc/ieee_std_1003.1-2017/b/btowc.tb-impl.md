###Synopsis

`#include <stdio.h>`
`#include <wchar.h>`

`wint_t btowc(int c);`

###Description

The function transforms a single byte to a wide character.

Arguments
<u>c</u> - a character to be transformed.
 
The behavior of this function is affected by the `LC_CTYPE` category of the current locale.
 
###Return value

The wide-character representation of that character <u>c</u>.
`WEOF` - if <u>c</u> is equal `EOF` or if (unsigned char) c does not constitute a valid (one-byte) character in the initial shift state. 

`btowc()` does not return `WEOF` if <u>c</u> has a value in the range `0` to `255` inclusive.

###Errors

No errors are defined.