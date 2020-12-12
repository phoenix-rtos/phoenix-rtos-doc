###Synopsis

`#include <unistd.h>`

`int pipe(int *fildes);`


###Description

The `pipe()` function creates a pipe (an object that allows unidirectional data flow) and allocates a pair of file descriptors. The first descriptor connects to the read end of the pipe; the second connects to the write end.

Data written to `fildes[1]` appears on (i.e., can be read from) `fildes[0`.  This allows the output of one program to be sent to another program: the source's standard output is set up to be the write end of the pipe; the sink's standard input is set up to be the read end of the pipe.  The pipe itself persists until all of its associated descriptors are closed.

A pipe whose read or write end has been closed is considered widowed.  Writing on such a pipe causes the writing process to receive a `SIGPIPE` signal.  Widowing a pipe is the only way to deliver end-of-file to a reader: after the reader consumes any buffered data, reading a widowed pipe returns a zero count.

The generation of the `SIGPIPE` signal can be suppressed using the `F_SETNOSIGPIPE` fcntl command.

###Return value

###Errors