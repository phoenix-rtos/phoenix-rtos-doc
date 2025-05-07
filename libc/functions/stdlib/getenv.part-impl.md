# getenv

## Synopsis

```c
#include <stdlib.h>

int getenv(const char *name);
```

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `getenv()` function shall search the environment of the calling process (see XBD Environment Variables) for the
environment variable name if it exists and return a pointer to the value of the environment variable. If the specified
environment variable cannot be found, a null pointer shall be returned. The application shall ensure that it does not
modify the string pointed to by the `getenv()` function.

The returned string pointer might be invalidated, or the string content might be overwritten by a subsequent call to
`getenv()`,`setenv()`,`unsetenv()`, or `putenv()`, but they shall not be affected by a call to any other function in
this volume of `POSIX.1-2017`.

## Return value

Upon successful completion, `getenv()` shall return a pointer to a string containing the value for the specified name.
If the specified name cannot be found in the environment of the calling process, a null pointer shall be returned.

## Errors

No errors are defined.

## Tests

Tested

## Known bugs

None
