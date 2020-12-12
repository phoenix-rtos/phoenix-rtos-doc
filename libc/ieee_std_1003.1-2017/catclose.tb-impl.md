###Synopsis

`#include <nl_types.h>`

`int catclose(nl_catd catd);`

###Description

The function closes the message catalogue identified by <u>catd</u>. If a file descriptor is used to implement the type `nl_catd`, that file descriptor is closed.

Arguments
<u>catd</u> - the message catalogue.
 
###Return value

`0` - success,
`-1` - on error (`errno` is set appropriately).

###Errors

`[EBADF]` - The catalogue descriptor is not valid.
`[EINTR]` - The `catclose()` function was interrupted by a signal. 

###Implementation tasks
* Implement the `catopen()` function.
* Implement the `catclose()` function.