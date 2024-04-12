# lseek

## Synopsis

`#include <unistd.h>`

`off_t lseek(int fildes, off_t offset, int whence);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `lseek()` function shall set the file offset for the open file description associated with the file descriptor
_fildes_, as follows:

* If _whence_ is `SEEK_SET,` the file offset shall be set to _offset_ bytes.

* If _whence_ is `SEEK_CUR,` the file offset shall be set to its current location plus _offset_.

* If _whence_ is `SEEK_END,` the file offset shall be set to the size of the file plus _offset_.

The symbolic constants `SEEK_SET,` `SEEK_CUR,` and `SEEK_END` are defined in `<unistd.h>`.

The behavior of `lseek()` on devices which are incapable of seeking is implementation-defined. The value of the file
offset associated with such a device is undefined.

The `lseek()` function shall allow the file offset to be set beyond the end of the existing data in the file. If data
is later written at this point, subsequent reads of data in the gap shall return bytes with the value 0 until data is
actually written into the gap.

The `lseek()` function shall not, by itself, extend the size of a file.

If _fildes_ refers to a shared memory object, the result of the `lseek()` function is unspecified.

If _fildes_ refers to a typed memory object, the result of the `lseek()` function is unspecified.

## Return value

Upon successful completion, the resulting offset, as measured in bytes from the beginning of the
file, shall be returned.

Otherwise, -1 shall be returned, errno shall be set to indicate the error, and the file offset shall remain unchanged.

## Errors

The `lseek()` function shall fail if:

* `EBADF` - The _fildes_ argument is not an open file descriptor.

* `EINVAL` - The _whence_ argument is not a proper value, or the resulting file offset would be negative for a regular
 file, block special file, or directory.

* `EOVERFLOW` - The resulting file offset would be a value which cannot be represented correctly in an object of type
 `off_t`.

* `ESPIPE` - The _fildes_ argument is associated with a pipe, `FIFO`, or socket.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../functions.md)
2. [Table of Contents](../../../README.md)
