# putchar

## Synopsis

```c
#include <stdio.h>

int putchar(int c);
```

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

`putchar()` - put a byte on a stdout stream

The function call `putchar(c)` shall be equivalent to `putc(c,stdout)`.

## Return value

Refer to fputc.

## Errors

Refer to fputc.

## Tests

Untested

## Known bugs

None
