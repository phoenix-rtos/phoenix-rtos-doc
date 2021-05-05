###Synopsis

`#include <unistd.h>`

`uid_t geteuid(void);`

###Description

The `geteuid()` function returns the effective user ID of the calling process. 

The `geteuid()` function does not modify `errno`.

###Return value

The effective user ID.

###Errors

No errors are defined.

###Implementation tasks

* Implement the `geteuid()` function.
