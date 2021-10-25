###Synopsis

`#include <nl_types.h>`

`int catgets(nl_catd catd, int set_id, int msg_id, const char *s);`

###Description

The `catgets()` function attempts to read a given message in a given set from the given message catalogue.

Arguments
<u>catd</u> - the message catalogue.
<u>set_id</u> - the message set.
<u>msg_id</u> - the message identifier.
<u>s</u> - the message text.
 
The <u>catd</u> argument is a message catalogue descriptor returned from an earlier call to `catopen()`. If <u>catd</u> is not a value returned by `catopen()` for a message catalogue still open in the process, then the results are undefined. 
The <u>s</u> argument points to a default message string which is returned by `catgets()` if it cannot retrieve the identified message.
 
The `catgets()` function need not be thread-safe.
 
###Return value

On success a pointer to an internal buffer area containing the null-terminated message string is returned, otherwise <u>s</u> is returned and `errno` set to indicate the error.

###Errors

[`EINTR`] - The read operation was terminated by a signal and no data was transferred.
[`ENOMSG`] - The message identified by <u>set_id</u> and <u>msg_id</u> is not in the message catalogue.
[`EBADF`] - The <u>catd</u> argument is not a valid message catalogue descriptor open for reading.
[`EBADMSG`] - The message identified by <u>set_id</u> and <u>msg_id</u> in the specified message catalogue did not satisfy security criteria.
[`EINVAL`] - The message catalogue identified by <u>catd</u> is corrupted. 

###Implementation tasks
* Implement the `catopen()` function.
* Implement the `catgets()` function.