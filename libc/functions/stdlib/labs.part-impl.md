# labs

## Synopsis

```c
#include <stdlib.h>

long labs(long i);

long long llabs(long long i);
```

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `llabs()` function shall compute the absolute value of the long long integer operand _i_. If the result cannot be
represented, the behavior is undefined.

## Return value

The `labs()` function shall return the absolute value of the long integer operand.

The `llabs()` function shall return the absolute value of the long long integer operand.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None
