# isalnum

## Synopsis

```c
#include <ctype.h>

int isalnum(int c);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `isalnum()` function shall test whether _c_ is a character of class _alpha_ or _digit_ in the current locale.

The _c_ argument is an `int`, the value of which the application shall ensure is representable as an `unsigned char` or
equal to the value of the macro `EOF`. If the argument has any other value, the behavior is undefined.

## Return value

The `isalnum()` function shall return non-zero if _c_ is an alphanumeric character, otherwise shall return `0`.

## Errors

No errors are defined.

## Tests

Tested

## Known bugs

None
