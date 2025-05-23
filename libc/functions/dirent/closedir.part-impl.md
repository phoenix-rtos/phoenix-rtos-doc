# closedir

## Synopsis

`#include <dirent.h>`

`int closedir(DIR *dirp);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `closedir()` function shall close the directory stream referred to by the argument _dirp_. Upon return, the value
of _dirp_ may no longer point to an accessible object of the type `DIR`. If a file descriptor is used to implement type
`DIR`, that file descriptor shall be closed.

## Return value

Upon successful completion, `closedir()` shall return `0`, otherwise, `-1` shall be returned and `errno`
set to indicate the error.

## Errors

The `closedir()` function may fail if:

* `EBADF` - The _dirp_ argument does not refer to an open directory stream.

* `EINTR` - The `closedir()` function was interrupted by a signal.

## Tests

Untested

## Known bugs

None
