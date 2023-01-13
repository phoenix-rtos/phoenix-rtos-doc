<!-- Documentation template to fill -->
# Synopsis 

`#include <stdarg.h>`</br>
`#include <stdio.h>`</br>

`int vdprintf(int fildes, const char *restrict format, va_list ap);`</br>

`int vfprintf(FILE *restrict stream, const char *restrict format, va_list ap);`</br>

`int vprintf(const char *restrict format, va_list ap);`</br>

`int vsnprintf(char *restrict s, size_t n, const char *restrict format, va_list ap);`</br>

`int vsprintf(char *restrict s, const char *restrict format, va_list ap);`</br>

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017 

<!-- #MUST_BE: update description from opengroup AND READ IT and check if it matches  -->
## Description 
 
The `vdprintf()`, `vfprintf()`, `vprintf()`, `vsnprintf()`, and `vsprintf()` functions shall be equivalent to the `dprintf()`, `fprintf()`, `printf()`, `snprintf()`, and `sprintf()` functions respectively, except that instead of being called with a variable number of arguments, they are called with an argument list as defined by `<stdarg.h>`.

These functions shall not invoke the va_end macro. As these functions invoke the va_arg macro, the value of ap after the return is unspecified.

## Return value

Upon successful completion, functions shall return the number of bytes transmitted.

If an output error was encountered, these functions shall return a negative value and set errno to indicate the error.

## Errors

These functions shall fail if either the stream is unbuffered or the stream's buffer needs to be flushed, and:

* `EAGAIN` - The `O_NONBLOCK` flag is set for the file descriptor underlying stream and the thread would be delayed in the write operation.

* `EBADF` - The file descriptor underlying stream is not a valid file descriptor open for writing.

* `EFBIG` - An attempt was made to write to a file that exceeds the maximum file size.

* `EFBIG` - An attempt was made to write to a file that exceeds the file size limit of the process.

* `EFBIG` - The file is a regular file and an attempt was made to write at or beyond the offset maximum.

* `EINTR` - The write operation was terminated due to the receipt of a signal, and no data was transferred.

* `EIO` - A physical I/O error has occurred, or the process is a member of a background process group attempting to write to its controlling terminal, `TOSTOP` is set, the calling thread is not blocking `SIGTTOU`, the process is not ignoring `SIGTTOU`, and the process group of the process is orphaned. This error may also be returned under implementation-defined conditions.

* `ENOSPC` - There was no free space remaining on the device containing the file.

* `EPIPE` - An attempt is made to write to a pipe or `FIFO` that is not open for reading by any process. A `SIGPIPE` signal shall also be sent to 
the thread. 

* `EILSEQ` - A wide-character code that does not correspond to a valid character has been detected.

* `EOVERFLOW` - he value to be returned is greater than `INT_MAX`. 


These functions may fall if:

 * `ENOMEM` - Insufficient storage space is available. 

 * `ENXIO` - A request was made of a nonexistent device, or the request was outside the capabilities of the device.

<!-- #MUST_BE: function by default shall be untested, when tested there should be a link to test location and test command for ia32 test runner  -->
## Tests

Untested 

<!-- #MUST_BE: check for pending issues in  -->
## Known bugs 

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)