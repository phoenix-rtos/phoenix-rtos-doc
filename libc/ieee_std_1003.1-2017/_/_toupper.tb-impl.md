###Synopsis
`#include <ctype.h>`

`int _toupper(int c);`

###Description
The `_toupper()` macro is equivalent to `toupper()` except that the application ensures that the argument <u>c </u> is an lowercase letter.

Arguments:
<u>c </u> - a letter to be transliterated to uppercase.

###Return value
Upon successful completion, `_toupper()` returns the uppercase letter corresponding to the argument passed.

###Errors
No errors are defined.

###Comments
Applications should use the `toupper()` function instead of the obsolescent `_toupper()` function.
The `_toupper()` function may be removed in a future version.
