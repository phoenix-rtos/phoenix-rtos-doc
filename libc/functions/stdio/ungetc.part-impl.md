# ungetc

## Synopsis

`#include <stdio.h>`

`int ungetc(int c, FILE *stream);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `ungetc()` function shall push the byte specified by _c_ (converted to a `unsigned char`) back onto the input stream
pointed to by stream. The pushed-back bytes shall be returned by subsequent reads on that stream in the reverse order of
their pushing. A successful intervening call (with the stream pointed to by _stream_) to a file-positioning function
(`fseek()`, `fseeko()`, `fsetpos()`, or `rewind()`) or `fflush()` shall discard any pushed-back bytes for the stream.
The external storage corresponding to the _stream_ shall be unchanged.

One byte of push-back shall be provided. If `ungetc()` is called too many times on the same stream without an
intervening read or file-positioning operation on that stream, the operation may fail.

If the value of _c_ equals that of the macro `EOF`, the operation shall fail and the input stream shall be left
unchanged.

A successful call to `ungetc()` shall clear the end-of-file indicator for the stream. The value of the file-position
indicator for the stream after all pushed-back bytes have been read, or discarded by calling `fseek()`, `fseeko()`,
`fsetpos()`, or `rewind()` (but not `fflush()`), shall be the same as it was before the bytes were pushed back. The
file-position indicator is decremented by each successful call to `ungetc()`; if its value was `0` before a call, its
value is unspecified after the call.

## Return value

Upon successful completion, `ungetc()` shall return the byte pushed back after conversion. Otherwise, it shall return
`EOF`.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../functions.md)
2. [Table of Contents](../../../README.md)
