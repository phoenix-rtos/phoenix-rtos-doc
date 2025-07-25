# isspace

## Synopsis

```c
#include <ctype.h>

int isspace(int c);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `isspace()` function shall test whether _c_ is a character of class _space_ in the current
_locale_.

The _c_ argument is an `int`, the value of which the application shall ensure is a character representable as an
`unsigned char` or equal to the value of the macro `EOF`. If the argument has any other value, the behavior is
undefined.

## Return value

The `isspace()` function shall return non-zero if _c_ is a white-space character; otherwise, they shall return `0`.

## Errors

No errors are defined.

## Tests

Tested

## Known bugs

None
