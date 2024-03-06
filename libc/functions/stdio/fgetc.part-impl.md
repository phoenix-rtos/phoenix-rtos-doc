# fgetc

## Synopsis

`#include <stdio.h>`

`int fgetc(FILE *stream);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

If the end-of-file indicator for the input stream pointed to by _stream_ is not set and a next byte is present, the
`fgetc()` function shall obtain the next byte as an unsigned char converted to an int, from the input stream pointed
to by _stream_, and advance the associated file position indicator for the stream (if defined). Since `fgetc()`
operates on bytes, reading a character consisting of multiple bytes (or "a multibyte character") may require multiple
calls to `fgetc()`.

The `fgetc()` function may mark the last data access timestamp of the file associated with _stream_ for update. The
last data access timestamp shall be marked for update by the first successful execution of `fgetc()`, `fgets()`,
`fread()`, `fscanf()`, `getc()`, `getchar()`, `getdelim()`, `getline()`, `gets()`, or `scanf()` using _stream_ that
returns data not supplied by a prior call to `ungetc()`.

## Return value

Upon successful completion, `fgetc()` shall return the next byte from the input stream pointed to by _stream_.
If the end-of-file indicator for the stream is set, or if the stream is at end-of-file, the end-of-file indicator
for the stream shall be set and `fgetc()` shall return `EOF`. If a read error occurs, the error indicator for the
stream shall be set, `fgetc()` shall return `EOF` and shall set `errno` to indicate the error.

## Errors

The `fgetc()` function shall fail if data needs to be read and:

* `EAGAIN` - The `O_NONBLOCK` flag is set for the file descriptor underlying _stream_ and the thread would be delayed
 in the `fgetc()`
operation.

* `EBADF` - The file descriptor underlying _stream_ is not a valid file descriptor open for reading.

* `EINTR` - The read operation was terminated due to the receipt of a signal, and no data was transferred.

* `EIO` - A physical `I/O` error has occurred, or the process is in a background process group attempting to read from
 its controlling terminal, and either the calling thread is blocking `SIGTTIN` or the process is ignoring `SIGTTIN` or
 the process group of the process is orphaned. This error may also be generated for implementation-defined reasons.

* `EOVERFLOW` - The file is a regular file and an attempt was made to read at or beyond the offset maximum associated
 with the corresponding stream.

The `fgetc()` function may fail if:

* `ENOMEM` - Insufficient storage space is available.

* `ENXIO` - A request was made of a nonexistent device, or the request was outside the capabilities of the device.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
