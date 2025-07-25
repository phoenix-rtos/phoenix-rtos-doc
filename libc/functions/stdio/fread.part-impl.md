# fread

## Synopsis

```c
#include <stdio.h>

size_t fread(void *restrict ptr, size_t size,
             size_t nitems, FILE *restrict stream);
```

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `fread()` function shall read into the array pointed to by _ptr_ up to _nitems_ elements whose size is specified by
_size_ in bytes, from the stream pointed to by _stream_. For each object, size calls shall be made to the `fgetc()`
function and the results stored, in the order read, in an array of unsigned char exactly overlaying the object. The
file position indicator for the stream (if defined) shall be advanced by the number of bytes successfully read. If an
error occurs, the resulting value of the file position indicator for the stream is unspecified. If a partial element is
read, its value is unspecified.

The `fread()` function may mark the last data access timestamp of the file associated with _stream_ for update. The last
data access timestamp shall be marked for update by the first successful execution of `fgetc()`, `fgets()`, `fread()`,
`fscanf()`, `getc()`, `getchar()`, `getdelim()`, `getline()`, `gets()`, or `scanf()` using _stream_ that returns data
not supplied by a prior call to `ungetc()`.

## Return value

Upon successful completion, `fread()` shall return the number of elements successfully read which is less than _nitems_
only if a read error or end-of-file is encountered. If _size_ or _nitems_ is `0`, `fread()` shall return `0` and the
contents of the array and the state of the stream remain unchanged. Otherwise, if a read error occurs, the error
indicator for the stream shall be set and `errno` shall be set to indicate the error.

## Errors

Refer to [fgetc](fgetc.part-impl.md)

## Tests

Untested

## Known bugs

None
