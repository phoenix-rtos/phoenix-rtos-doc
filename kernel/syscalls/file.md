# File operations

File syscall handlers unpack arguments from the user stack with `GETFROMSTACK()` and dispatch work to the POSIX
server-facing helpers in `posix_*()`.

````{function} syscalls_sys_open(ustack)
Opens a path through `posix_open()`.

:param ustack: User stack containing `const char *filename` at index `0` and `int oflag` at index `1`.
:returns: File descriptor on success or a negative error returned by `posix_open()`.
````


````{function} syscalls_sys_close(ustack)
Closes a file descriptor through `posix_close()`.

:param ustack: User stack containing `int fildes` at index `0`.
:returns: `0` on success or a negative error returned by `posix_close()`.
````

````{function} syscalls_sys_read(ustack)
Reads from a file descriptor through `posix_read()`.

:param ustack: User stack containing `int fildes`, `void *buf`, `size_t nbyte`, and `off_t offset` at indexes `0`
  through `3`.
:returns: Number of bytes read, `-EFAULT` for an invalid non-empty buffer range, or a negative error returned by
  `posix_read()`.
````

````{function} syscalls_sys_write(ustack)
Writes to a file descriptor through `posix_write()`.

:param ustack: User stack containing `int fildes`, `void *buf`, `size_t nbyte`, and `off_t offset` at indexes `0`
  through `3`.
:returns: Number of bytes written, `-EFAULT` for an invalid non-empty buffer range, or a negative error returned by
  `posix_write()`.
````

````{function} syscalls_sys_dup(ustack)
Duplicates a file descriptor through `posix_dup()`.

:param ustack: User stack containing `int fildes` at index `0`.
:returns: New file descriptor on success or a negative error returned by `posix_dup()`.
````

````{function} syscalls_sys_dup2(ustack)
Duplicates a file descriptor to a selected descriptor number through `posix_dup2()`.

:param ustack: User stack containing `int fildes` at index `0` and `int fildes2` at index `1`.
:returns: File descriptor on success or a negative error returned by `posix_dup2()`.
````

````{function} syscalls_sys_link(ustack)
Creates a hard link through `posix_link()`.

:param ustack: User stack containing `const char *path1` at index `0` and `const char *path2` at index `1`.
:returns: `0` on success or a negative error returned by `posix_link()`.
````

````{function} syscalls_sys_unlink(ustack)
Removes a path through `posix_unlink()`.

:param ustack: User stack containing `const char *pathname` at index `0`.
:returns: `0` on success or a negative error returned by `posix_unlink()`.
````

````{function} syscalls_sys_lseek(ustack)
Changes or reads a file offset through `posix_lseek()`.

:param ustack: User stack containing `int fildes`, `off_t *offset`, and `int whence` at indexes `0` through `2`.
:returns: `0` on success, `-EFAULT` when `offset` is outside the process map, or a negative error returned by
  `posix_lseek()`.
````

````{function} syscalls_sys_ftruncate(ustack)
Truncates an open file through `posix_ftruncate()`.

:param ustack: User stack containing `int fildes` at index `0` and `off_t length` at index `1`.
:returns: `0` on success or a negative error returned by `posix_ftruncate()`.
````

````{function} syscalls_sys_fcntl(ustack)
Handles file-control operations through `posix_fcntl()`.

:param ustack: User stack containing `int fd` at index `0` and `unsigned int cmd` at index `1`. Additional command
  data remains on the user stack for `posix_fcntl()`.
:returns: Command-specific result or a negative error returned by `posix_fcntl()`.
````

````{function} syscalls_sys_pipe(ustack)
Creates a pipe through `posix_pipe()`.

:param ustack: User stack containing `int *fildes` at index `0`.
:returns: `0` on success, `-EFAULT` when the two-element descriptor array is outside the process map, or a negative
  error returned by `posix_pipe()`.
````

````{function} syscalls_sys_mkfifo(ustack)
Creates a FIFO special file through `posix_mkfifo()`.

:param ustack: User stack containing `const char *path` at index `0` and `mode_t mode` at index `1`.
:returns: `0` on success or a negative error returned by `posix_mkfifo()`.
````

````{function} syscalls_sys_fstat(ustack)
Reads file status through `posix_fstat()`.

:param ustack: User stack containing `int fd` at index `0` and `struct stat *buf` at index `1`.
:returns: `0` on success, `-EFAULT` when `buf` is outside the process map, or a negative error returned by
  `posix_fstat()`.
````

````{function} syscalls_sys_statvfs(ustack)
Reads filesystem status for a path or file descriptor through `posix_statvfs()`.

:param ustack: User stack containing `const char *path`, `int fd`, and `struct statvfs *buf` at indexes `0` through
  `2`.
:returns: `0` on success, `-EFAULT` when `buf` is outside the process map, or a negative error returned by
  `posix_statvfs()`.
````

````{function} syscalls_sys_fsync(ustack)
Synchronizes an open file through `posix_fsync()`.

:param ustack: User stack containing `int fd` at index `0`.
:returns: `0` on success or a negative error returned by `posix_fsync()`.
````

````{function} syscalls_sys_chmod(ustack)
Changes path permissions through `posix_chmod()`.

:param ustack: User stack containing `const char *path` at index `0` and `mode_t mode` at index `1`.
:returns: `0` on success or a negative error returned by `posix_chmod()`.
````

````{function} syscalls_sys_ioctl(ustack)
Handles descriptor-specific control operations through `posix_ioctl()`.

:param ustack: User stack containing `int fildes` at index `0` and `unsigned long request` at index `1`. Optional
  request data remains on the user stack and is validated by `posix_ioctl()`.
:returns: Request-specific result or a negative error returned by `posix_ioctl()`.
````

````{function} syscalls_sys_poll(ustack)
Polls a file-descriptor array through `posix_poll()`.

:param ustack: User stack containing `struct pollfd *fds`, `nfds_t nfds`, and `int timeout_ms` at indexes `0`
  through `2`.
:returns: Number of ready descriptors, `-EFAULT` when the array is outside the process map, or a negative error
  returned by `posix_poll()`.
````

````{function} syscalls_sys_futimens(ustack)
Updates timestamps for an open file descriptor through `posix_futimens()`.

:param ustack: User stack containing `int fildes` at index `0` and `const struct timespec *times` at index `1`.
:returns: `0` on success, `-EFAULT` when non-`NULL` `times` is outside the process map, or a negative error returned by
  `posix_futimens()`.
````