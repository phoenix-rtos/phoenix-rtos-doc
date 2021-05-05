###Synopsis

`#include <unistd.h>`

`gid_t getgid(void);`

###Description

The `getgid()` function returns the effective group ID of the calling process. 

The `getgid()` function does not modify `errno`.

###Return value

The real group ID of the calling process.

###Errors

No errors are defined.

###Implementation tasks

* Implement the `getgid()` function.
