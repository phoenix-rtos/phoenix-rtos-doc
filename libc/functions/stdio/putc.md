# putc

## Synopsis

```c
#include <stdio.h>

int putc(int c, FILE *stream);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `putc()` function shall be equivalent to `fputc()`, except that if it is implemented as a macro it may evaluate
stream more than once, so the argument should never be an expression with side effects.

## Return value

Refer to fputc.

## Errors

Refer to fputc.

## POSIX deviations

The deviations described for [fputc](fputc.md#posix-deviations) apply here too.
