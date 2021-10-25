# Synopsis

`#include <stdlib.h>`

`void abort(void);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `abort()` function causes abnormal program termination to occur. Any open streams are flushed and closed. The `abort()` function is thread-safe.

## Return value

The `abort()` function never returns.

## Errors

No errors are defined.

## Tests
