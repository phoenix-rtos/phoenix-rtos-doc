# strcat

## Synopsis

```c
#include <string.h>

char *strcat(char *restrict s1, const char *restrict s2);
```

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `strcat()` function shall append a copy of the string pointed to by _s2_ (including the terminating `NUL` character)
to the end of the string pointed to by _s1_. The initial byte of _s2_ overwrites the `NUL` character at the end of
_s1_. If copying takes place between objects that overlap, the behavior is undefined.

## Return value

The `strcat()` function shall return _s1_; no return value is reserved to indicate an error.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None
