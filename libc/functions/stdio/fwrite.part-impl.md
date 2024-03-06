# fwrite

## Synopsis

`#include <stdio.h>`

`size_t fwrite(const void *restrict ptr, size_t size, size_t nitems, FILE *restrict stream);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `fwrite()` function shall write, from the array pointed to by _ptr_, up to _nitems_ elements whose size is specified
by _size_, to the stream pointed to by _stream_. For each object, size calls shall be made to the `fputc()` function,
taking the values (in order) from an array of unsigned char exactly overlaying the object. The file-position indicator
for the stream (if defined) shall be advanced by the number of bytes successfully written. If an error occurs, the
resulting value of the file-position indicator for the stream is unspecified.

The last data modification and last file status change timestamps of the file shall be marked for update between the
successful execution of `fwrite()` and the next successful completion of a call to `fflush()` or `fclose()` on the same
stream, or a call to `exit()` or `abort()`.

## Return value

The `fwrite()` function shall return the number of elements successfully written, which may be less than _nitems_ if a
write error is encountered. If _size_ or _nitems_ is `0`, `fwrite()` shall return `0` and the state of the stream
remains unchanged. Otherwise, if a write error occurs, the error indicator for the stream shall be set, and `errno`
shall be set to indicate the error.

## Errors

Refer to fputc.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
