###Synopsis
`#include <ctype.h>`

`int _tolower(int c);`

###Description
The `_tolower()` macro is equivalent to `tolower(c)` except that the application ensures that the argument <u>c </u> is an uppercase letter.

Arguments:
<u>c </u> - a letter to be transliterate to lowercase.

###Return value
Upon successful completion, `_tolower()` returns the lowercase letter corresponding to the argument passed.

###Errors
No errors are defined.

###Comments
Applications should use the tolower() function instead of the obsolescent `_tolower()` function.
The `_tolower()` function may be removed in a future version.