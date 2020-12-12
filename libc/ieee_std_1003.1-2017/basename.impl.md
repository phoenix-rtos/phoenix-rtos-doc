###Synopsis
`#include <libgen.h>`

`char *basename(char *path);`

###Description

The `basename()` function takes the pathname pointed to by <u>path</u> and returns a pointer to the final component of the pathname, deleting any trailing '/' characters.

Arguments:
<u>path</u> - the pathname to be stripped.

If the string pointed to by <u>path</u> consists entirely of the '/' character, `basename()` returns a pointer to the string "/". If the string pointed to by <u>path</u> is exactly "//", "/" is returned.

If <u>path</u> is a null pointer or points to an empty string, `basename()` returns a pointer to the string ".".

###Return value
The basename() function shall return a pointer to the final component of <u>path</u>.

###Errors

No errors are defined.
