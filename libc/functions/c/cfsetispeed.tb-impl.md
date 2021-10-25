###Synopsis
`#include <termios.h>`

`int cfsetispeed(struct termios *termios_p, speed_t speed)`

###Description
`cfsetispeed()` function provided for setting the baud rate value in the `termios` structure. The function sets <u>speed</u> value to input bound rate in the `termios` structure <u>termios_p</u>.

Arguments:
<u>termios_p</u> - the pointer to the `termios` structure,
<u>speed</u> - the input baud rate.

###Return value
Returns the value `0` upon successful completion, otherwise the value `-1` is returned and `errno` is set to the applicable error code.

###Errors

[`EINVAL`] - the speed value is not a valid baud rate or the value of speed is outside the range of possible speed values as specified in <`termios.h`>. 