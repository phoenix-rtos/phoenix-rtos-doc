# wctomb

## Synopsis

```c
#include <stdlib.h>

int wctomb(char *str, wchar_t wchar);
```

## Status

Declared, not implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `wctomb()` function shall determine the number of bytes needed to represent the character corresponding to the
wide-character code whose value is _wchar_ (including any change in the shift state). It shall store the character
representation (possibly multiple bytes and any special bytes to change shift state) in the array object pointed to
by _s_ (if _s_ is not a `null` pointer). At most `MB_CUR_MAX` bytes shall be stored. If _wchar_ is `0`, a `null` byte
shall be stored, preceded by any shift sequence needed to restore the initial shift state, and `wctomb()` shall be
left in the initial shift state.

The behavior of this function is affected by the `LC_CTYPE` category of the current locale. For a state-dependent
encoding, this function shall be placed into its initial state by a call for which its character pointer
argument, _s_, is a `null` pointer. Subsequent calls with _s_ as other than a `null` pointer shall cause the internal
state of the function to be altered as necessary. A call with _s_ as a `null` pointer shall cause this function to
return a non-zero value if encodings have state dependency, and `0` otherwise. Changing the `LC_CTYPE` category causes
the shift state of this function to be unspecified.

The `wctomb()` function need not be thread-safe.

The implementation shall behave as if no function defined in this volume of POSIX.1-2017 calls `wctomb()`.

## Return value

If _s_ is a `null` pointer, `wctomb()` shall return a non-zero or `0` value, if character encodings, respectively, do or
do not have state-dependent encodings. If _s_ is not a `null` pointer, `wctomb()` shall return `-1` if the value of
_wchar_ does not correspond to a valid character, or return the number of bytes that constitute the character
corresponding to the value of _wchar_.

In no case shall the value returned be greater than the value of the `MB_CUR_MAX` macro.

## Errors

The `wctomb()` function shall fail if:

* `EILSEQ` An invalid wide-character code is detected.

## Tests

Untested

## Known bugs

None
