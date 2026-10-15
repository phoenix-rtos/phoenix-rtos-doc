# getpgrp

## Synopsis

```c
#include <unistd.h>

pid_t getpgrp(void);
```

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `getpgrp()` function shall return the process group ID of the calling process.

## Return value

The `getpgrp()` function shall always be successful, and no return value is reserved to indicate an error.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None
