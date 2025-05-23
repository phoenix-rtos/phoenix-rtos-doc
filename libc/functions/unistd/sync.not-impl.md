# sync

## Synopsis

```c
#include <unistd.h>

void sync(void);
```

## Status

Declared, not implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `sync()` function shall cause all information in memory that updates file systems to be scheduled for writing out to
all file systems.

The writing, although scheduled, is not necessarily complete upon return from `sync()`.

## Return value

The `sync()` function shall not return a value.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None
