# cfsetispeed

## Synopsis

```c
#include <termios.h>

int cfsetispeed(struct termios *termios_p, speed_t speed);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `cfsetispeed()` function shall set the input baud rate stored in the structure pointed to by _termios_p_ to
_speed_.

There shall be no effect on the baud rates set in the hardware until a subsequent successful call to `tcsetattr()` with
the same `termios` structure. Similarly, errors resulting from attempts to set baud rates not supported by the terminal
device need not be detected until the `tcsetattr()` function is called.

If _speed_ is `0` (`B0`), the input baud rate is set to the output baud rate stored in the structure, so that a
subsequent call to `tcsetattr()` sets the input baud rate to the output baud rate. The value of _speed_ is not
validated: the speed constants defined in `<termios.h>` are equal to the baud rates they name (for example `B9600` is
`9600`).

## Return value

Upon successful completion, `cfsetispeed()` shall return `0`; otherwise, `-1` shall be returned, and `errno` may be set
to indicate the error.

## Errors

The `cfsetispeed()` function may fail if:

* `EINVAL` - The _speed_ value is not a valid baud rate.

* `EINVAL` - The value of _speed_ is outside the range of possible speed values as specified in `<termios.h>`.

## POSIX deviations

No POSIX deviations discovered.
