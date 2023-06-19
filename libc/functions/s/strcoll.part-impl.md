# Synopsis

`#include <string.h>`

`int strcoll(const char *s1, const char *s2);`

`int strcoll_l(const char *s1, const char *s2, locale_t locale);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `strcoll()` and `strcoll_l()`
functions shall compare the string pointed to by _s1_ to the string pointed to by _s2_, both interpreted as
appropriate to the `LC_COLLATE` category of the current locale, or of the locale represented by _locale_, respectively.
The `strcoll()` and `strcoll_l()`
functions shall not change the setting of errno if successful.
Since no return value is reserved to indicate an error, an application wishing to check for error situations should set
errno to 0, then call `strcoll()`, or `strcoll_l()` then check errno.
The
behavior is undefined if the _locale_ argument to `strcoll_l()` is the special locale object `LC_GLOBAL_LOCALE` or is
not a valid locale object handle.

Upon successful completion, `strcoll()` shall return an integer greater than, equal to, or less than `0`, according to
whether the string pointed to by _s1_ is greater than, equal to, or less than the string pointed to by _s2_ when both
are interpreted as appropriate to the current locale. On error, `strcoll()` may set `errno`, but no return value is
reserved to indicate an error.

Upon successful completion, `strcoll_l()` shall return an integer greater than, equal to, or less than `0`, according to
whether the string pointed to by _s1_ is greater than, equal to, or less than the string pointed to by _s2_ when both
are interpreted as appropriate to the locale represented by _locale_. On error, `strcoll_l()` may set `errno`, but no
return value

## Return value

Upon successful completion, `strcoll()` shall return an integer greater than, equal to, or less than `0`, according to
whether the string pointed to by _s1_ is greater than, equal to, or less than the string pointed to by _s2_ when both
are interpreted as appropriate to the current locale.

On error, `strcoll()` may set `errno`, but no return
value is reserved to indicate an error.
Upon successful completion, `strcoll_l()` shall return an integer greater than, equal to, or less than `0`, according to
whether the string pointed to by _s1_ is greater than, equal to, or less than the string pointed to by _s2_ when both
are interpreted as appropriate to the locale represented by locale. On error, `strcoll_l()` may set `errno`, but no
return value is reserved to indicate an error.

## Errors

These functions may fail if:

* `EINVAL` - The _s1_ or _s2_ arguments contain characters outside the domain of the collating sequence.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
