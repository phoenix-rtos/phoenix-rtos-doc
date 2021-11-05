# Synopsis 
`#include <stdio.h>`</br>
` int fputs(const char *restrict s, FILE *restrict stream);`</br>

## Status
Partially implemented
## Conformance
IEEE Std 1003.1-2017
## Description


The `fputs()` function shall write the null-terminated string pointed to by s to the stream pointed to by
stream. The terminating null byte shall not be written.
The
last data modification and last file status change timestamps of the file shall be marked for update between the successful
execution of `fputs()` and the next successful completion of a call to `fflush()`
or `fclose()` on the same stream or a call to `exit()` or `abort()`. 


## Return value

Upon successful completion, `fputs()` shall return a non-negative number. Otherwise, it shall return `EOF`, set an error indicator for the stream and set `errno` to indicate the error.

## Errors

Refer to [fputc](/fputc.part-impl.md)


## Tests

Untested

## Known bugs

None

## See Also 
1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
