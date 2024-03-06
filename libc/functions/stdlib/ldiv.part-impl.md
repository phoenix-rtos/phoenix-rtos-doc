# ldiv

## Synopsis

`#include <stdlib.h>`

`ldiv_t ldiv(long numer, long denom);`

`lldiv_t lldiv(long long numer, long long denom);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

These functions shall compute the quotient and remainder of the division of the numerator _numer_ by the denominator
_denom_. If the division is inexact, the resulting quotient is the long integer (for the `ldiv()` function) or
long integer (for the `lldiv()` function) of lesser magnitude that is the nearest to the algebraic quotient. If the
result cannot be represented, the behavior is undefined; otherwise, quot * denom+rem shall equal _numer_.

## Return value

The `ldiv()` function shall return a structure of type `ldiv_t`, comprising both the quotient and the remainder.
The structure shall include the following members, in any order:

```c
long   quot;    /* Quotient */
long   rem;     /* Remainder */
```

The `lldiv()` function shall return a structure of type `lldiv_t`, comprising both the quotient and the remainder.
The structure shall include the following members, in any order:

```c
long long   quot;    /* Quotient */
long long   rem;     /* Remainder */
```

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
