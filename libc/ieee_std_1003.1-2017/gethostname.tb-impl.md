###Synopsis

`#include <unistd.h>`

`int gethostname(char *name, size_t namelen);`

###Description

The `gethostname()` function gets a name of the current host.

Arguments:
    
<u>name</u> - an array to hold the result name.
<u>namelen</u> - a size of the array.

The `gethostname()` function returns the standard host name for the current machine. The <u>namelen</u> argument specifies the size of the array pointed to by the <u>name</u> argument. The returned name is be null-terminated, except that if <u>namelen</u> is an insufficient length to hold the host name, then the returned name is truncated.

Host names are limited to `{HOST_NAME_MAX}` bytes.


###Return value

Upon successful completion, `0` is returned; otherwise  `-1` is returned.

###Errors

No errors are defined.

###Implementation tasks

* Implement the `limits.h` file containing at least the {`HOST_NAME_MAX`} constant.
* Implement the `gethostname()` function.