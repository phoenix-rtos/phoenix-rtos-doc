# Synopsis

`#include <stdio.h>`

`ssize_t getdelim(char **restrict lineptr, size_t *restrict n, int delimiter, FILE *restrict stream);`

` ssize_t getline(char **restrict lineptr, size_t *restrict n, FILE *restrict stream); `

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The purpose is to read a delimited record from stream. The `getdelim()` function shall read from _stream_ until it
encounters a character matching the delimiter character.

The _delimiter_ argument is a `int`, the value of which the application shall ensure is a character representable as a
`unsigned` `char` of equal value that terminates the read process. If the _delimiter_ argument has any
other value, the behavior is undefined.

The application shall ensure that _`*lineptr`_ is a valid argument that could be passed to the `free()` function. If
_`*n`_ is non-zero, the application shall ensure that _`*lineptr`_ either points to an object of size at least _`*n`_
bytes, or is a `null` pointer.

If _`*lineptr`_ is a `null` pointer or if the object pointed to by _`*lineptr`_ is of insufficient size, an object shall
be allocated as if by `malloc()` or the object shall be reallocated as if by `realloc()`, respectively, such that the
object is large enough to hold the characters to be written to it, including the terminating `NUL`, and _`*n`_ shall be
set to the new size. If the object was allocated, or if the reallocation operation moved the object, _`*lineptr`_ shall
be updated to point to the new object or new location. The characters read, including any delimiter, shall be stored in
the object, and a terminating `NUL` added when the _delimiter_ or end-of-file is encountered.

The `getline()` function shall be equivalent to the `getdelim()` function with the delimiter character equal to
the `<newline>` character.

The `getdelim()` and `getline()` functions may mark the last data access timestamp of the file associated with _stream_
for update. The last data access timestamp shall be marked for update by the first successful execution of `fgetc()`,
`fgets()`, `fread()`, `fscanf()`, `getc()`, `getchar()`, `getdelim()`, `getline()`, `gets()`, or `scanf()` using
_stream_ that returns data not supplied by a prior call to `ungetc()`.

## Return value

Upon successful completion, the `getline()` and `getdelim()` functions shall return the number of bytes written into the
buffer, including the _delimiter_ character if one was encountered before `EOF`, but excluding the terminating `NUL`
character. If the end-of-file indicator for the _stream_ is set, or if no characters were read and the _stream_ is at
end-of-file, the end-of-file indicator for the _stream_ shall be set, and the function shall return `-1`. If an error
occurs, the error indicator for the _stream_ shall be set, and the function shall return `-1` and set `errno` to
indicate the error.

## Errors

For the conditions under which the `getdelim()` and `getline()` functions shall fail and may fail, refer to
[fgetc](../f/fgetc.part-impl.md).

In addition, these functions shall fail if:

* `EINVAL` - _lineptr_ or _n_ is a `null` pointer.

* `ENOMEM` - Insufficient memory is available.

These functions may fail if:

* `EOVERFLOW` - The number of bytes to be written into the buffer, including the _delimiter_ character
 (if encountered), would exceed `SSIZE_MAX`.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
