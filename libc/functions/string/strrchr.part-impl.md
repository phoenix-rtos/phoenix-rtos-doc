# strrchr

## Synopsis

```c
#include <string.h>

char *strrchr(const char *s, int c);
```

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `strrchr()` function shall locate the last occurrence of _c_ (converted to a char) in the string pointed to
by _s_. The terminating `NULL` character is considered to be part of the string.

## Return value

Upon successful completion, `strrchr()` shall return a pointer to the byte or a `null` pointer if _c_ does not occur in
the string.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None
