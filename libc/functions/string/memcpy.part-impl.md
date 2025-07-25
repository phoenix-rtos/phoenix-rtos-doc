# memcpy

## Synopsis

```c
#include <string.h>

void *memcpy(void *restrict s1, const void *restrict s2, size_t n);
```

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `memcpy()` function shall copy _n_ bytes from the object pointed to by _s2_ into the object pointed to by _s1_. If
copying takes place between objects that overlap, the behavior is undefined.

## Return value

The `memcpy()` function shall return _s1_; no return value is reserved to indicate an error.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None
