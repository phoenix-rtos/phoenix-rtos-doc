# pipe

## Synopsis

`#include <unistd.h>`

`int pipe(int fildes[2]);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pipe()` function shall create a pipe and place two file descriptors, one each into the arguments _fildes[0]_ and
_fildes[1]_, that refer to the open file descriptions for the read and write ends of the pipe. The file descriptors
shall be allocated as described in File Descriptor Allocation. The `O_NONBLOCK` and `FD_CLOEXEC` flags shall be clear
on both file descriptors. (The `fcntl()` function can be used to set both these flags.)

Data can be written to the file descriptor _fildes[1]_ and read from the file descriptor _fildes[0]_. A read on the file
descriptor _fildes[0]_ shall access data written to the file descriptor _fildes[1]_ on a first-in-first-out basis.

It is unspecified whether _fildes[0]_ is also open for writing and whether _fildes[1]_ is also open for reading.

A process has the pipe open for reading (correspondingly writing) if it has a file descriptor open that refers to the
read end, _fildes[0]_ (write end, _fildes[1]_).

The pipe's user ID shall be set to the effective user ID of the calling process.

The pipe's group ID shall be set to the effective group ID of the calling process.

Upon successful completion, `pipe()` shall mark for update the last data access, last data modification, and last file
status change timestamps of the pipe.

## Return value

Upon successful completion, `0` shall be returned; otherwise, `-1` shall be returned and `errno` set to indicate the
error, no file descriptors shall be allocated and the contents of fildes shall be left unmodified.

## Errors

The `pipe()` function shall fail if:

* [`EMFILE`] - All, or all but one, of the file descriptors available to the process are currently open.
* [`ENFILE`] - The number of simultaneously open files in the system would exceed a system-imposed limit.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../functions.md)
2. [Table of Contents](../../../README.md)
