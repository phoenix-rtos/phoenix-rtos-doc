# Synopsis 
`#include <threads.h>`

`int condCreate(handle_t *h);`

## Status
Implemented
## Conformance
Phoenix-RTOS specific
## Description

The `condCreate()` function shall initialize the condition variable referenced by _h_. Upon successful initialization, the state of the
condition variable shall become initialized.

Attempting to initialize an already initialized condition variable results in undefined behavior.

## Return value

If successful, the `condCreate()` function shall return zero; otherwise, an error number shall be returned to indicate the error.


## Errors


The `condCreate()` function shall fail if:

 * `-ENOMEM` - Insufficient memory exists to initialize the condition variable.

These functions shall not return an error code of `EINTR`.

## Tests

Untested

## Known bugs

None

## See Also 
1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
