###Synopsis
`#include <termios.h>`

`speed_t cfgetispeed(const struct termios *termios_p)`

###Description

`cfgetispeed()` function is provided for getting the baud rate value in the `termios` structure.
The function extracts the input baud rate from the `termios` structure to which the <u>termios_p</u> argument points.

Arguments:
<u>termios_p</u> - the pointer to the `termios` under interest. 

###Return value
Returns the input baud rate in the <u>termios_p</u> termios structure. It does not interpret the value, but returns it as it is. The returned value is of type `speed_t` representing the input baud rate.
Only a limited set of possible rates is at all portable, and this constrains the application to that set.

###Errors
No errors are defined.