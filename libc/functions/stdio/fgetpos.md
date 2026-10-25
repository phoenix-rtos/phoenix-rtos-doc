# fgetpos

## Synopsis

```c
#include <stdio.h>

int fgetpos(FILE *restrict stream, fpos_t *restrict pos);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `fgetpos()` function shall store the current values of the parse state (if any) and file position indicator for
the stream pointed to by _stream_ in the object pointed to by _pos_. The value stored contains unspecified information
usable by `fsetpos()` for repositioning the stream to its position at the time of the call to `fgetpos()`.

The `fpos_t` type is defined as `off_t`, and the value stored is the file position indicator of the stream, as returned
by `ftello()`.

The `fgetpos()` function shall not change the setting of `errno` if successful.

## Return value

Upon successful completion, `fgetpos()` shall return `0`; otherwise, it shall return a non-zero value and set `errno`
to indicate the error.

## Errors

The `fgetpos()` function shall fail if:

* `EBADF` - The file descriptor underlying _stream_ is not valid.

* `EOVERFLOW` - The current value of the file position cannot be represented correctly in an object of type `fpos_t`.

* `ESPIPE` - The file descriptor underlying _stream_ is associated with a pipe, FIFO, or socket.

## POSIX deviations

No POSIX deviations discovered.
