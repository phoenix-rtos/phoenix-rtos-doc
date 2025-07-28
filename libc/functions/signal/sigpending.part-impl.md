# sigpending

## Synopsis

```c
#include <signal.h>

int sigpending(sigset_t *set);
```

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `sigpending()` function shall store, in the location referenced by the _set_ argument, the set of signals that are
blocked from delivery to the calling thread and that are pending on the process or the calling thread.

## Return value

Upon successful completion, `sigpending()` shall return `0`; otherwise, `-1` shall be returned and `errno` set to
indicate the error.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None
