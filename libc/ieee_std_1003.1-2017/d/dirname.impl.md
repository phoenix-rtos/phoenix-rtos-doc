###Synopsis

`#include <libgen.h>

char *dirname(char *path);`

###Description

The `dirname()` function returns the parent directory name of a file of a given pathname.

Arguments:
<u>path</u> - a pointer to a character string that contains a pathname.
 
The `dirname()` function takes a pointer to a character string <u>path</u> that contains a pathname, and returns a pointer to a string that is a pathname of the parent directory of that file. 
The `dirname()` function does not perform pathname resolution; the result is not affected by whether or not <u>path</u> exists or by its file type. Trailing '/' characters in the path that are not also leading '/' characters are not counted as part of the <u>path</u>.

If <u>path</u> does not contain a '/', then `dirname()` returns a pointer to the string ".". If <u>path</u> is a null pointer or points to an empty string, `dirname()` returns a pointer to the string "." .

The `dirname()` function modifies the string pointed to by <u>path</u>, and returns a pointer to static storage that is then overwritten by a subsequent call to `dirname()`.

The `dirname()` function need not be thread-safe.
 
###Return value

The `dirname()` function returns a pointer to a string as described above.

It modifies the string pointed to by <u>path</u>, and returns a pointer to internal storage. The returned pointer might be invalidated or the storage might be overwritten by a subsequent call to `dirname()`. The returned pointer is also invalidated if the calling thread is terminated.


###Errors

No errors are defined.

###Implementation tasks
