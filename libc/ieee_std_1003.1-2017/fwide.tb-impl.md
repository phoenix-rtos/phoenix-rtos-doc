`###Synopsis`

`#include <stdio.h>`
`#include <wchar.h>`

`int fwide(FILE *stream, int mode);`

###Description

The function sets the stream orientation.

Arguments:
    
<u>stream</u> - a pointer to the stream,
<u>mode</u> - a required orientation of the stream,

The `fwide()` function determines the orientation of the stream pointed to by <u>stream</u>. If <u>mode</u> is greater than zero, the function first attempts to make the stream wide-oriented. If mode is less than zero, the function first attempts to make the stream byte-oriented. Otherwise, mode is zero and the function does not alter the orientation of the stream.

If the orientation of the stream has already been determined, `fwide()` does not change it.

Since no return value is reserved to indicate an error, an application wishing to check for error situations should set `errno` to `0`, then call `fwide()`, then check `errno`, and if it is non-zero, assume an error has occurred.

###Return value

The `fwide()` function returns a value greater than zero if, after the call, the stream has wide-orientation, a value less than zero if the stream has byte-orientation, or zero if the stream has no orientation.

###Errors

[`EBADF`] The <u>stream</u> argument is not a valid stream.

###Implementation tasks:
    
 * Implement the `fwide()` function.
