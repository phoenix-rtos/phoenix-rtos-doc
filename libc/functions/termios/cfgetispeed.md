# cfgetispeed

## Synopsis

```c
#include <termios.h>

speed_t cfgetispeed(const struct termios *termios_p);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `cfgetispeed()` function shall extract the input baud rate from the `termios` structure to which the
_termios_p_ argument points.

This function shall return exactly the value in the `termios` data structure, without interpretation.

## Return value

Upon successful completion, `cfgetispeed()` shall return a value of type `speed_t` representing the input baud
rate.

## Errors

No errors are defined.

## POSIX deviations

No POSIX deviations discovered.
