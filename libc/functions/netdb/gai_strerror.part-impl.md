# gai_strerror

## Synopsis

```c
#include <netdb.h>

const char *gai_strerror(int ecode);
```

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The purpose is to address and name information error description. The `gai_strerror()` function shall return a text
string describing an error value for the `getaddrinfo()` and `getnameinfo()`
functions listed in the `<netdb.h>` header.

When the _ecode_ argument is one of the following values listed in the `<netdb.h>` header:

* `EAI_AGAIN`
* `EAI_BADFLAGS`
* `EAI_FAIL`
* `EAI_FAMILY`
* `EAI_MEMORY`
* `EAI_NONAME`
* `EAI_OVERFLOW`
* `EAI_SERVICE`
* `EAI_SOCKTYPE`
* `EAI_SYSTEM`

The function return value shall point to a string describing the error. If the argument is not one of those values, the
function shall return a pointer to a string whose contents indicate an unknown error.

## Return value

Upon successful completion, `gai_strerror()` shall return a pointer to an implementation-defined string.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None
