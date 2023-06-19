# Synopsis

`#include <stdio.h>`

`FILE *tmpfile(void);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `tmpfile()` function shall create a temporary file and open a corresponding stream. The file shall be automatically
deleted when all references to the file are closed. The file shall be opened as in `fopen()` for update `(wb+)`,
except that implementations may restrict the permissions, either by clearing the file mode bits or setting them to the
value `S_IRUSR | S_IWUSR`.

In some implementations, a permanent file may be left behind if the process calling `tmpfile()` is killed while it is
processing a call to `tmpfile()`.

An error message may be written to standard error if the stream cannot be opened.

## Return value

Upon successful completion, `tmpfile()` shall return a pointer to the stream of the file that is created. Otherwise, it
shall return a `null` pointer and set `errno` to indicate the error.

## Errors

The `tmpfile()` function shall fail if:

* `EINTR` - a signal was caught during `tmpfile()`.

* `EMFILE` - all file descriptors available to the process are currently open.

* `EMFILE` - `STREAM_MAX` streams are currently open in the calling process.

* `ENFILE` - the maximum allowable number of files is currently open in the system.

* `ENOSPC` - the directory or file system which would contain the new file cannot be expanded.

* `EOVERFLOW` - the file is a regular file and the size of the file cannot be represented correctly in an object of type
`off_t`.

The `tmpfile()` function may fail if:

* `EMFILE` - `FOPEN_MAX` streams are currently open in the calling process.

* `ENOMEM` - insufficient storage space is available.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
