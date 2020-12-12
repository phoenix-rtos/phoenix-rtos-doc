###Synopsis

`#include <locale.h>`

`locale_t duplocale(locale_t locobj);`

###Description

The function duplicates a locale object. The locale is an explicit model and definition of a native-language environment. 

Arguments:
    
<u>locobj</u> - the locale object to be duplicated.

The `duplocale()` function creates a duplicate copy of the locale object <u>locobj</u>.

If the <u>locobj</u> argument is `LC_GLOBAL_LOCALE`, `duplocale()` creates a new locale object containing a copy of the global locale determined by the `setlocale()` function.

If the <u>locobj</u> argument is not a valid locale object handle, the behavior is undefined.

The use of the `duplocale()` function is recommended when a locale object is used in multiple places, and it is possible that the lifetime of the locale object might end before all uses are finished. Another reason to duplicate a locale object is if a slightly modified form is needed.

###Return value

The handle for a new locale object is returned on success, otherwise `(locale_t)0` is returned and `errno` set to indicate the error.

###Errors

[`ENOMEM`] - There is not enough memory available to create the locale object or load the locale data.

###Implementation tasks

* Implement the `duplocale()` function.