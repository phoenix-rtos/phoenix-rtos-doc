# fstat

## Synopsis

`#include <sys/stat.h>`

`int fstat(int fildes, struct stat *buf);`

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `fstat()` function shall obtain information about an open file associated with the file descriptor _fildes_, and
shall write it to the area pointed to by _buf_.

If _fildes_ references a shared memory object, the implementation shall update in the stat structure pointed to by the
_buf_ argument the `st_uid`, `st_gid`, `st_size`, and `st_mode` fields, and only the `S_IRUSR`, `S_IWUSR`, `S_IRGRP`,
`S_IWGRP`, `S_IROTH`, and `S_IWOTH` file permission bits need be valid. The implementation may update other fields
and flags.

If _fildes_ references a typed memory object, the implementation shall update in the stat structure pointed to by the
_buf_ argument the `st_uid`, `st_gid`, `st_size`, and `st_mode` fields, and only the `S_IRUSR`, `S_IWUSR`, `S_IRGRP`,
`S_IWGRP`, `S_IROTH`, and `S_IWOTH` file permission bits need be valid. The implementation may update other fields and
flags.

The _buf_ argument is a pointer to a stat structure, as defined in `<sys/stat.h>`, into which information is placed
concerning the file.

For all other file types defined in this volume of `POSIX.1-2017`, the structure members `st_mode`, `st_ino`, `st_dev`,
`st_uid`, `st_gid`, `st_atim`, `st_ctim`, and `st_mtim` shall have meaningful values and the value of the `st_nlink`
member shall be set to the number of links to the file.

An implementation that provides additional or alternative file access control mechanisms may, under
implementation-defined conditions, cause `fstat()` to fail.

The `fstat()` function shall update any time-related fields, before writing into the stat structure.

## Return value

Upon successful completion, `0` shall be returned. Otherwise, `-1` shall be returned and `errno` set to indicate the
error.

## Errors

The `fstat()` function shall fail if:

- `[EBADF]` - The _fildes_ argument is not a valid file descriptor.

- `[EIO]` - An `I/O` error occurred while reading from the file system.

- `[EOVERFLOW]` - The file size in bytes or the number of blocks allocated to the file or the file serial number cannot
be represented correctly in the structure pointed to by _buf_.

The `fstat()` function may fail if:

- `[EOVERFLOW]`- One of the values is too large to store into the structure pointed to by the _buf_ argument.

## Tests

Tested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
