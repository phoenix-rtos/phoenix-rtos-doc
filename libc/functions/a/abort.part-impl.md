# Synopsis

`#include <stdlib.h>`

`void abort(void);`

## Status

Partially implemented

## Description

The `abort()` function causes abnormal program termination to occur. Any open streams are flushed and closed. The `abort()` function is thread-safe. 

## Return value

The `abort()` function never returns.

## Errors

No errors are defined.

## Implementation tasks

* The abort() function overrides blocking or ignoring the SIGABRT signal.

## Tests

======

## EXAMPLES

None.
