# File operations

## DEPRECATED `syscalls_fileAdd` ⇾ `syscalls_fileOpen`

````C
GETFROMSTACK(ustack, unsigned int *, h, 0);
GETFROMSTACK(ustack, oid_t *, oid, 1);
GETFROMSTACK(ustack, unsigned int, mode, 2);
````

Adds file given by `oid` to process resources. Added process resource is identified by handle returned in `h` variable.
The access mode is set to `mode`.

## `syscalls_fileOpen` (`syscalls_sys_open`)

````C
GETFROMSTACK(ustack, const char *, filename, 0);
GETFROMSTACK(ustack, int, oflag, 1);
````

## DEPRECATED `syscalls_fileSet` ⇾ `syscalls_fileRead`, `syscalls_fileWrite`

````C
GETFROMSTACK(ustack, unsigned int, h, 0);
GETFROMSTACK(ustack, char, flags, 1);
GETFROMSTACK(ustack, oid_t *, oid, 2);
GETFROMSTACK(ustack, offs_t, offs, 3);
GETFROMSTACK(ustack, unsigned, mode, 4);
````

Updates file parameters for file given by resource handle `h`.

## DEPRECATED `syscalls_fileGet` ⇾ `syscalls_fileRead`, `syscalls_fileWrite`

````C
GETFROMSTACK(ustack, unsigned int, h, 0);
GETFROMSTACK(ustack, int, flags, 1);
GETFROMSTACK(ustack, oid_t *, oid, 2);
GETFROMSTACK(ustack, offs_t *, offs, 3);
GETFROMSTACK(ustack, unsigned *, mode, 4);
````

Retrieves file parameters for file given by resource handle `h`.

## DEPRECATED `syscalls_fileRemove` ⇾ `syscalls_fileClose`

````C
GETFROMSTACK(ustack, unsigned int, h, 0);
````

Removes file given by `h` from resources of calling process.

## DEPRECATED `syscalls_resourceDestroy` ⇾ `syscalls_fileClose`, `syscalls_mutexDestroy`, `syscalls_condDestroy`

````C
GETFROMSTACK(ustack, unsigned int, h, 0);
````

Destroys resource given by `h`.

## `syscalls_fileRead` (`syscalls_sys_read`)

````C
GETFROMSTACK(ustack, int, fildes, 0);
GETFROMSTACK(ustack, void *, buf, 1);
GETFROMSTACK(ustack, size_t, nbyte, 2);
````

## `syscalls_fileWrite` (`syscalls_sys_write`)

````C
GETFROMSTACK(ustack, int, fildes, 0);
GETFROMSTACK(ustack, void *, buf, 1);
GETFROMSTACK(ustack, size_t, nbyte, 2);
````

## `syscalls_fileClose` (`syscalls_sys_close`)

````C
GETFROMSTACK(ustack, int, fildes, 0);
````

## `syscalls_fileLink` (`syscalls_sys_link`)

````C
GETFROMSTACK(ustack, const char *, path1, 0);
GETFROMSTACK(ustack, const char *, path2, 1);
````

## `syscalls_fileUnlink` (`syscalls_sys_unlink`)

````C
GETFROMSTACK(ustack, const char *, pathname, 0);
````

## `syscalls_fileCtl` (`syscalls_sys_fcntl`)

````C
GETFROMSTACK(ustack, unsigned int, fd, 0);
GETFROMSTACK(ustack, unsigned int, cmd, 1);
````

## `syscalls_fileTrunc` (`syscalls_sys_ftruncate`)

````C
GETFROMSTACK(ustack, int, fildes, 0);
GETFROMSTACK(ustack, off_t, length, 1);
````

## `syscalls_fileSeek` (`syscalls_sys_lseek`)

````C
GETFROMSTACK(ustack, int, fildes, 0);
GETFROMSTACK(ustack, off_t, offset, 1);
GETFROMSTACK(ustack, int, whence, 2);
````

## `syscalls_fileDup` (`syscalls_sys_dup`)

````C
GETFROMSTACK(ustack, int, fildes, 0);
````

## `syscalls_fileDup2` (`syscalls_sys_dup2`)

````C
GETFROMSTACK(ustack, int, fildes, 0);
GETFROMSTACK(ustack, int, fildes2, 1);
````

## `syscalls_filePipe` (`syscalls_sys_pipe`)

````C
GETFROMSTACK(ustack, int *, fildes, 0);
````

## `syscalls_fileMakeFifo` (`syscalls_sys_mkfifo`)

````C
GETFROMSTACK(ustack, const char *, path, 0);
GETFROMSTACK(ustack, mode_t, mode, 1);
````

## `syscalls_fileChangeMode` (`syscalls_sys_chmod`)

````C
GETFROMSTACK(ustack, const char *, path, 0);
GETFROMSTACK(ustack, mode_t, mode, 1);
````

## `syscalls_fileStat` (`syscalls_sys_fstat`)

````C
GETFROMSTACK(ustack, int, fd, 0);
GETFROMSTACK(ustack, struct stat *, buf, 1);
````

## `syscalls_fileIoCtl` (`syscalls_sys_ioctl`)

````C
GETFROMSTACK(ustack, int, fildes, 0);
GETFROMSTACK(ustack, unsigned long, request, 1);
````

## `syscalls_fileTimes` (`syscalls_sys_utimes`)

````C
GETFROMSTACK(ustack, const char *, filename, 0);
GETFROMSTACK(ustack, const struct timeval *, times, 1);
````

## `syscalls_filePoll` (`syscalls_sys_poll`)

````C
GETFROMSTACK(ustack, struct pollfd *, fds, 0);
GETFROMSTACK(ustack, nfds_t, nfds, 1);
GETFROMSTACK(ustack, int, timeout_ms, 2);
````

## See also

1. [System calls](README.md)
2. [Table of Contents](../../README.md)
