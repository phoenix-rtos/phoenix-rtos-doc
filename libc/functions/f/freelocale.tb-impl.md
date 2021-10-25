###Synopsis

`#include <locale.h>`

`void freelocale(locale_t locobj);`

###Description

The `freelocale()` function frees resources allocated for a locale object.

Arguments:

<u>locobj</u> - a locale object returned by a call to the `newlocale()` or `duplocale()` functions.


The `freelocale()` function causes the resources allocated for a locale object returned by a call to the `newlocale()` or `duplocale()` functions to be released.

The behaviour is undefined if the <u>locobj</u> argument is the special locale object `LC_GLOBAL_LOCALE` or is not a valid locale object handle.

Any use of a locale object that has been freed results in undefined behaviour.

###Return value

None.

###Errors

None. 
    
###Implementation tasks

 * Complete the `locale.h` file.
 * Implement the `freelocale()` function.
