# strlen

## Synopsis

`#include <string.h>`

`size_t strlen(const char *s);`

`size_t strnlen(const char *s, size_t maxlen);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `strlen()` function shall compute the number of bytes in the string to which _s_ points, not including the
terminating `NUL` character.
The
`strnlen()` function shall compute the smallest of the number of bytes in the array to which _s_ points, not including
any terminating `NUL` character, or the value of the _maxlen_ argument. The `strnlen()` function shall never examine
more than _maxlen_ bytes of the array pointed to by _s_.

## Return value

The `strlen()` function shall return the length of _s_; no return value shall be reserved to indicate an error.
The
`strnlen()` function shall return the number of bytes preceding the first null byte in the array to which _s_ points, if
_s_ contains a `null` byte within the first _maxlen_ bytes; otherwise, it shall return _maxlen_.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../functions.md)
2. [Table of Contents](../../../README.md)
