# strtok

## Synopsis

`#include <string.h>`

`char *strtok(char *restrict s, const char *restrict sep);`

`char *strtok_r(char *restrict s, const char *restrict sep, char **restrict state);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

A sequence of calls to `strtok()` breaks the string pointed to by _s_ into a sequence of tokens, each of which is
delimited by a byte from the string pointed to by _sep_. The first call in the sequence has _s_ as its first argument,
and is followed by calls with a `null` pointer as their first argument. The separator string pointed to by _sep_ may be
different from call to call.

The first call in the sequence searches the string pointed to by _s_ for the first byte that is not contained in the
current separator string pointed to by _sep_. If no such byte is found, then there are no tokens in the string pointed
to by _s_ and `strtok()` shall return a `null` pointer. If such a byte is found, it is the start of the first token. The
`strtok()` function then searches from there for a byte that is contained in the current separator string. If no such
byte is found, the current token extends to the end of the string pointed to by _s_, and subsequent searches for a token
shall return a `null` pointer. If such a byte is found, it is overwritten by a `NUL` character, which terminates the
current token.

The `strtok()` function saves a pointer to the following byte, from which the next search for a token shall start.

Each subsequent call, with a `null` pointer as the value of the first argument, starts searching from the saved pointer
and behaves as described above.

The implementation shall behave as if no function defined in this volume of POSIX.1-2017 calls `strtok()`.

The
`strtok()` function need not be thread-safe.

The `strtok_r()` function shall be equivalent to `strtok()`, except that `strtok_r()` shall be thread-safe and the
argument state points to a user-provided pointer that allows `strtok_r()` to maintain state between calls which scan
the same string. The application shall ensure that the pointer pointed to by state is unique for each string (_s_)
being processed concurrently by `strtok_r()` calls. The application need not initialize the pointer pointed to by state
to any particular value. The implementation shall not update the pointer pointed to by state to point (directly or
indirectly) to resources, other than within the string _s_, that need to be freed or released by the caller.

## Return value

Upon successful completion, `strtok()` shall return a pointer to the first byte of a token. Otherwise, if there is no
token, `strtok()` shall return a `null` pointer.

The `strtok_r()` function shall return a pointer to the token found, or a `null` pointer when no token is found.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None
