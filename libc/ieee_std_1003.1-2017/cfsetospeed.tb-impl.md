###Synopsis
`#include <termios.h>`

`int cfsetospeed(struct termios *termios_p, speed_t speed)`

###Compliance
POSIX.1-1988

###Description
`cfsetospeed()` function provided for setting the baud rate value in the `termios` structure. The function sets <u>speed</u> value to output bound rate in the `termios` structure <u>termios_p</u>.

Arguments:
<u>termios_p</u> - the pointer to the `termios` structure,
<u>speed</u> - the output baud rate.

###Return value
Returns the value `0` upon successful completion, otherwise the value `-1` is returned.

###Errors

[`EINVAL`] - the <u>speed</u> value is not a valid baud rate or the value of <u>speed</u> is outside the range of possible speed values as specified in <`termios.h`>. 