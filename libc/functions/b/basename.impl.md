### Synopsis

`#include <libgen.h>`

`char *basename(char *path);`

### Description

The `basename()` function takes the pathname pointed to by _path_ and returns a pointer to the final component of
the pathname, deleting any trailing '/' characters.

Arguments:
_path_ - the pathname to be stripped.

If the string pointed to by _path_ consists entirely of the '/' character, `basename()` returns a pointer to the
string "/". If the string pointed to by _path_ is exactly "//", "/" is returned.

If _path_ is a null pointer or points to an empty string, `basename()` returns a pointer to the string ".".

### Return value

The basename() function shall return a pointer to the final component of _path_.

### Errors

No errors are defined.
