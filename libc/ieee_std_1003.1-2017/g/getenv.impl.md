###Synopsis

`#include <stdlib.h>`

`char *getenv(const char *name);`

###Description

Function searches for the environment string pointed to by <u>name</u> and returns the associated value of the string.

Arguments:
<u>name</u> - the name of the environment variable to be found.

The returned string pointer might be invalidated or the string content might be overwritten by a subsequent call to `getenv()`, `setenv()`, `unsetenv()`, or `putenv()` but they are not affected by a call to any other function.
The returned string pointer might also be invalidated if the calling thread is terminated.

The `getenv()` function is not thread-safe.

###Return value

A pointer to a string containing the value for the specified <u>name</u>. 
If the specified name cannot be found in the environment of the calling process, a null pointer is returned.

###Errors

No errors are defined.

###Implementation tasks

* None.
