# getc

## Synopsis

```c
#include <stdio.h>

int getc(FILE *stream);
```

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The purpose is to get a byte from a stream. The `getc()` function shall be equivalent to `fgetc`, except that if it is
implemented as a macro it may evaluate stream more than once, so the argument should never be an expression with
side effects.

## Return value

Refer to [fgetc](../stdio/fgetc.part-impl.md).

## Errors

Refer to [fgetc](../stdio/fgetc.part-impl.md).

## Tests

Untested

## Known bugs

None
