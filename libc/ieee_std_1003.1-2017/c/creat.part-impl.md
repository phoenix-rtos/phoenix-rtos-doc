###Synopsis
`#include <fcntl.h>`

`creat(const char *pathname, mode_t mode);`

###Description

Creates a new file at specified <u>pathname</u> with permissions specified in <u>mode</u>.

Arguments:
<u>pathname</u> - a pathname of a new file,
<u>mode</u> - required permissions

###Return value
Returns the value `0` upon successful completion, otherwise the value `-1` is returned.

###Errors

[`EACCES`] -  Search permission is denied on a component of the path prefix, or the file exists and the permissions specified by <u>mode</u> are denied, or the file does not exist and write permission is denied for the parent directory of the file to be created, or `O_TRUNC` is specified and write permission is denied.
[EEXIST] - `O_CREAT` and `O_EXCL` are set, and the named file exists.
[EINTR] - A signal was caught during `create()`.
[EINVAL] - The implementation does not support synchronized I/O for this file or The value of the <u>mode</u> argument is not valid..
[EIO] - The <u>pathname</u> argument names a `STREAMS` file and a hangup or error occurred during the  `create()`.
[EISDIR] - The named file is a directory and <u>mode</u> includes `O_WRONLY` or `O_RDWR`, or includes `O_CREAT` without `O_DIRECTORY`.
[ELOOP] - A loop exists in symbolic links encountered during resolution of the path argument, or `O_NOFOLLOW` was specified and the <u>pathname</u> argument names a symbolic link.
[EMFILE] - All file descriptors available to the process are currently open.
[ENAMETOOLONG] - The length of a component of a <u>pathname</u> is longer than {`NAME_MAX`}.
[ENFILE] - The maximum allowable number of files is currently open in the system.
[ENOENT] or [ENOTDIR] - The <u>pathname</u> argument contains at least one non-<slash> character and ends with one or more trailing <slash> characters. If <u>pathname</u> without the trailing <slash> characters names an existing file, an [`ENOENT`] error does not occur.
[ENOSR] - The <u>pathname</u> argument names a `STREAMS`-based file and the system is unable to allocate a `STREAM`. 
[ENOSPC] - The directory or file system that would contain the new file cannot be expanded.
[ENOTDIR] - A component of the path prefix names an existing file that is neither a directory nor a symbolic link to a directory, the <u>pathname</u> argument contains at least one non- <slash> character and ends with one or more trailing <slash> characters, and the last pathname component names an existing file that is neither a directory nor a symbolic link to a directory; or `O_DIRECTORY` was specified and the <u>pathname</u> argument resolves to a non-directory file.
[ENXIO] - The named file is a character special or block special file, and the device associated with this special file does not exist.
[EOVERFLOW] - The named file is a regular file and the size of the file cannot be represented correctly in an object of type `off_t`.
[EROFS] - The named file resides on a read-only file system.
[ENOMEM] - The <u>pathname</u> argument names a `STREAMS` file and the system is unable to allocate resources.
[EOPNOTSUPP] - The <u>pathname</u> argument names a socket.
[ETXTBSY] - The file is a pure procedure (shared text) file that is being executed and <u>mode</u> is `O_WRONLY` or `O_RDWR`.

###Implementation tasks

*Implement error handling