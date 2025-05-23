# setvbuf

## Synopsis

```c
#include <stdio.h>

int setvbuf(FILE *restrict stream,
            char *restrict buf, int type,
            size_t size);
```

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `setvbuf()` function may be used after the stream pointed to by _stream_ is associated with an open file but
before any other operation (other than an unsuccessful call to `setvbuf()`) is performed on the stream. The argument
type determines how stream shall be buffered, as follows:

* `_IOFB` shall cause input/output to be fully buffered.

* `_IOLB` shall cause input/output to be line buffered.

* `_IONB` shall cause input/output to be unbuffered.

If _buf_ is not a `null` pointer, the array it points to may be used instead of a buffer allocated by `setvbuf()` and
the argument size specifies the size of the array; otherwise, size may determine the size of a buffer allocated by
the `setvbuf()` function. The contents of the array at any time are unspecified.
For information about streams, see Standard I/O Streams.

## Return value

Upon successful completion, `setvbuf()` shall return `0`. Otherwise, it shall return a non-zero value if an invalid
value is given for type or if the request cannot be honored,  and may set `errno` to indicate the error.

## Errors

The `setvbuf()` function may fail if:

* `EBADF` - The file descriptor underlying stream is not valid.

The following sections are informative.

## Tests

Untested

## Known bugs

None
