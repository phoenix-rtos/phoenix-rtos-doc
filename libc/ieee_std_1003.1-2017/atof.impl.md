###Synopsis

`#include <stdlib.h>`

`double atof(const char *str);`

###Description
Function converts the initial portion of the string pointed to by `str` to double representation. It is equivalent to:
    `strtod(str, (char **)NULL);`
    
Arguments
<u>str</u> - the string to be converted

###Return value
Converted `double` number.

###Errors
The function need not affect the value of `errno` on an error.