###Synopsis

`#include <stdio.h>`

`char *ctermid(char *s);`

###Description

The `ctermid()` function generates a pathname for the controlling terminal.

Arguments:
<u>s</u> - a string or NULL.
 
The `ctermid()` function generates a string that, when used as a pathname, refers to the current controlling terminal for the current process. If `ctermid()` returns a pathname, access to the file is not guaranteed.

If the `ctermid()` function is called with a `NULL` parameter, it need not be thread-safe .

If an application uses multiple threads, it cannot call `ctermid()` with `NULL` as the parameter. If <u>s</u> is not `NULL`, the `ctermid()` function generates a string that, when used as a pathname, refers to the current controlling terminal for the current process. If <u>s</u> is `NULL`, the return value of `ctermid()` is undefined.

There is no additional burden on the programmer-changing to use a hypothetical thread-safe version of `ctermid()` along with allocating a buffer is more of a burden than merely allocating a buffer. Application code should not assume that the returned string is short, as some implementations have more than two pathname components before reaching a logical device name. 

###Return value

If <u>s</u> is a null pointer, the string is generated in the static area, the address of which is returned. The application does not modify the string returned. The returned pointer might be invalidated or the string content might be overwritten by a subsequent call to `ctermid()`. If the calling thread is terminated, the returned pointer be invalidated . If <u>s</u> is not a null pointer, <u>s</u> is assumed to point to a character array of at least `L_ctermid` bytes; the string is placed in this array and the value of <u>s</u> is returned. The symbolic constant `L_ctermid` is defined in `<stdio.h>`, and has a value greater than `0`.

if the pathname that would refer to the controlling terminal cannot be determined or if the function is unsuccessful, then the `ctermid()` function returns an empty string.

###Errors

No errors are defined.

###Implementation tasks
* Define `L_ctermid` in `<stdio.h>` file with a value greater than `0` so that array declarations using it are accepted by the compiler. The value includes the terminating null byte..
* Implement `ctermid()` function.