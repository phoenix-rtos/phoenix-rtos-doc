# cfsetospeed

## Synopsis

```c
#include <termios.h>

int cfsetospeed(struct termios *termios_p, speed_t speed);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `cfsetospeed()` function shall set the output baud rate stored in the structure pointed to by _termios_p_ to
_speed_.

There shall be no effect on the baud rates set in the hardware until a subsequent successful call to `tcsetattr()` with
the same `termios` structure. Similarly, errors resulting from attempts to set baud rates not supported by the terminal
device need not be detected until the `tcsetattr()` function is called.

The value of _speed_ is not validated: the speed constants defined in `<termios.h>` are equal to the baud rates they
name (for example `B9600` is `9600`).

## Return value

Upon successful completion, `cfsetospeed()` shall return `0`; otherwise, it shall return `-1` and `errno` may be set to
indicate the error.

## Errors

The `cfsetospeed()` function may fail if:

* `EINVAL` - The _speed_ value is not a valid baud rate.

* `EINVAL` - The value of _speed_ is outside the range of possible speed values as specified in `<termios.h>`.

## POSIX deviations

No POSIX deviations discovered.
