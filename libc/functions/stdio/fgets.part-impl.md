# fgets

## Synopsis

`#include <stdio.h>`

`char *fgets(char *restrict s, int n, FILE *restrict stream);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `fgets()` function shall read bytes from _stream_ into the array pointed to by _s_ until `n-1` bytes are read, or a
`<newline>` is read and transferred to _s_, or an end-of-file condition is encountered. A `null` byte shall be written
immediately after the last byte read into the array. If the end-of-file condition is encountered before any bytes are
read, the contents of the array pointed to by _s_ shall not be changed.

The `fgets()` function may mark the last data access timestamp of the file associated with _stream_ for update. The last
data access timestamp shall be marked for update by the first successful execution of `fgetc()`, `fgets()`, `fread()`,
`fscanf()`, `getc()`, `getchar()`, `getdelim()`, `getline()`, `gets()`, or `scanf()` using _stream_ that returns data
not supplied by a prior call to `ungetc()`.

## Return value

Upon successful completion, fgets() shall return _s_. If the stream is at end-of-file, the end-of-file indicator for the
stream shall be set and `fgets()` shall return a `null` pointer. If a read error occurs, the error indicator for the
stream shall be set, `fgets()` shall return a `null` pointer and shall set `errno` to indicate the error.

## Errors

Refer to [`fgetc`](./fgetc.part-impl.md).

## Tests

Untested

## Known bugs

None
