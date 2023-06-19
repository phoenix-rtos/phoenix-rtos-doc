# Synopsis

`#include <stdio.h>`

` char *gets(char *s); `

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The purpose is to get a string from a stdin stream. The `gets()` function shall read bytes from the standard input
stream, `stdin`, into the array pointed to by _s_, until a `<newline>` is read or an end-of-file condition is
encountered. Any `<newline>` shall be discarded and a `null` byte shall be placed immediately after the last byte
read into the array.

The `gets()` function may mark the last data access timestamp of the file associated with stream for update. The last
data access timestamp shall be marked for update by the first successful execution of `fgetc()`, `fgets()`, `fread()`,
`fscanf()`, `getc()`, `getchar()`, `getdelim()`, `getline()`, `gets()`, or `scanf()` using stream that returns data not
supplied by a prior call to `ungetc()`.

## Return value

Upon successful completion, `gets()` shall return _s_. If the end-of-file indicator for the stream is set, or if the
stream is at end-of-file, the end-of-file indicator for the stream shall be set and `gets()` shall return a `null`
pointer. If a read error occurs, the error indicator for the stream shall be set, `gets()` shall return a `null`
pointer, and set `errno` to indicate the error.

## Errors

Refer to [fgetc](../f/fgetc.part-impl.md).

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
