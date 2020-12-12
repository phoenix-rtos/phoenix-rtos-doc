###Synopsis
`#include <termios.h>`

`speed_t cfgetospeed(const struct termios *termios_p)`

###Description
`cfgetospeed()` function is provided for getting the output baud rate value from the `termios` structure.

Arguments:
<u>termios_p</u> - a pointer to the ` termios` structure of interest.

The function does not interpret the returned value in any way.

###Return value
Returns the output baud rate in the <u>termios_p</u> ` termios` structure.

###Errors
No errors are defined.