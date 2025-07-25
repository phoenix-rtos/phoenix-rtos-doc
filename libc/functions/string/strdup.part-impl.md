# strdup

## Synopsis

```c
#include <string.h>

char *strdup(const char *s);

char *strndup(const char *s, size_t size);
```

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `strdup()` function shall return a pointer to a new string, which is a duplicate of the string pointed to by _s_.
The returned pointer can be passed to `free()`. A `null` pointer is returned if the new string cannot be created.

The `strndup()` function shall be equivalent to the `strdup()` function, duplicating the provided _s_ in a new block of
memory allocated as if by using `malloc()`, with the exception being that `strndup()` copies at most _size_ plus one
byte into the newly allocated memory, terminating the new string with a `NUL` character.

If the length of _s_ is larger than _size_, only _size_ bytes shall be duplicated.

If _size_ is larger than the length of _s_, all bytes in _s_ shall be copied into the new memory buffer, including the
terminating `NUL` character.

The newly created string shall always be properly terminated.

## Return value

The `strdup()` function shall return a pointer to a new string on success. Otherwise, it shall return a null pointer and
set errno to indicate the error.

Upon successful completion, the `strndup()` function shall return a pointer to the newly allocated memory containing the
duplicated string. Otherwise, it shall return a null pointer and set errno to indicate the error.

## Errors

These functions shall fail if:

- `[ENOMEM]` - Storage space available is insufficient.

## Tests

Tested

## Known bugs

None
