# fstat

## Synopsis

```c
#include <sys/stat.h>

int fstat(int fildes, struct stat *buf);
```

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

The `fstat()` function shall update any time-related fields, before writing into the stat structure. For a pipe, a FIFO,
a socket, the kernel console, and the `/dev/null`, `/dev/zero`, `/dev/full` and `/dev/urandom` special files the
`st_atim`, `st_mtim` and `st_ctim` fields are set to zero (see POSIX deviations).

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

## POSIX deviations

For an open file descriptor that refers to a pipe, a FIFO, a socket or the kernel console (the terminal set up by the
kernel as the standard streams of the first process), `fstat()` does not query the server handling the file, and the
`st_atim`, `st_mtim` and `st_ctim` fields are set to zero. The kernel also treats the `/dev/null`, `/dev/zero`,
`/dev/full` and `/dev/urandom` special files as pipes, so `fstat()` reports zero timestamps and the `S_IFIFO` file type
for them.

For other files the timestamps are reported by the server handling the file, and whether they are updated by I/O
operations depends on that server. Servers without a built-in filesystem (`posixsrv` and most device drivers) do not
update them, as this would require an additional message to the filesystem server on every `read()` and `write()`, which
adds latency to I/O operations that is not acceptable on a real-time system. `dummyfs` does not update `st_mtim` and
`st_ctim` of a regular file on `write()`.
