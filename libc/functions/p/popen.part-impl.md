# Synopsis 
`#include <stdio.h>`</br>

`FILE *popen(const char *command, const char *mode);`</br>

## Status
Implemented
## Conformance
IEEE Std 1003.1-2017
## Description

The `popen()` function shall execute the command specified by the string _command_. It shall create a pipe between the calling program and the executed command, and shall return a pointer to a stream that can be used to either read from or write to the pipe.

The environment of the executed command shall be as if a child process were created within the `popen()` call using the `fork()` function, and the child invoked the `sh` utility using the call:

`execl(shell path, "sh", "-c", command, (char *)0);`

where shell path is an unspecified pathname for the `sh` utility.

The `popen()` function shall ensure that any streams from previous `popen()` calls that remain open in the parent process are closed in the new child process.

The _mode_ argument to `popen()` is a string that specifies `I/O` mode:

 * If _mode_ is `r`, when the child process is started, its file descriptor `STDOUT_FILENO` shall be the writable end of the pipe, and the file descriptor `fileno(stream)` in the calling process, where stream is the stream pointer returned by `popen()`, shall be the readable end of the pipe.

 * If _mode_ is `w`, when the child process is started its file descriptor `STDIN_FILENO` shall be the readable end of the pipe, and the file descriptor `fileno(stream)` in the calling process, where stream is the stream pointer returned by `popen()`, shall be the writable end of the pipe.

 * If _mode_ is any other value, the result is unspecified.

After `popen()`, both the parent and the child process shall be capable of executing independently before either terminates.

Pipe streams are byte-oriented.


## Return value


Upon successful completion, `popen()` shall return a pointer to an open stream that can be used to read or write to the pipe. Otherwise, it shall return a null pointer and may set `errno` to indicate the error.


## Errors


The `popen()` function shall fail if:

 * `EMFILE` - `{STREAM_MAX}` streams are currently open in the calling process.

The popen() function may fail if:

 * `EMFILE` - `{FOPEN_MAX}` streams are currently open in the calling process.

 * `EINVAL` - The mode argument is invalid.

The `popen()` function may also set `errno` values as described by `fork` or `pipe`.


## Tests

Untested

## Known bugs

None

## See Also 
1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
