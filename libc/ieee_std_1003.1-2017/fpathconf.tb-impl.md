###Synopsis

`#include <unistd.h>`

`long fpathconf(int fildes, int name);`
`long pathconf(const char *path, int name);`

###Description

The functions determine the current value of a configurable limit or option (variable) that is associated with a file or directory.

Arguments:
<u>fildes</u> - an open file descriptor.
<u>path</u> - the pathname of a file or directory.
<u>name</u> - the variable to be queried relative to that file or directory.

The following variables are supported:

 * `_PC_FILESIZEBITS`- {`FILESIZEBITS`}
 * `_PC_LINK_MAX`- {`LINK_MAX`}
 * `_PC_MAX_CANON`- {`MAX_CANON`} 
 * `_PC_MAX_INPUT`- {`MAX_INPUT`}
 * `_PC_NAME_MAX`- {`NAME_MAX`}
 * `_PC_PATH_MAX`- {`PATH_MAX`}
 * `_PC_PIPE_BUF`- {`PIPE_BUF`}
 * `_PC_2_SYMLINKS`- {`POSIX2_SYMLINKS`}
 * `_PC_ALLOC_SIZE_MIN`- {`POSIX_ALLOC_SIZE_MIN`}
 * `_PC_REC_INCR_XFER_SIZE`- {`POSIX_REC_INCR_XFER_SIZE`}
 * `_PC_REC_MAX_XFER_SIZE`- {`POSIX_REC_MAX_XFER_SIZE`}
 * `_PC_REC_MIN_XFER_SIZE`- {`POSIX_REC_MIN_XFER_SIZE`}
 * `_PC_REC_XFER_ALIGN`- {`POSIX_REC_XFER_ALIGN`}
 * `_PC_SYMLINK_MAX`- {`SYMLINK_MAX`}
 * `_PC_CHOWN_RESTRICTED` - `_POSIX_CHOWN_RESTRICTED`
 * `_PC_NO_TRUNC` - `_POSIX_NO_TRUNC`
 * `_PC_VDISABLE` - `_POSIX_VDISABLE`
 * `_PC_ASYNC_IO` - `_POSIX_ASYNC_IO`
 * `_PC_PRIO_IO` - `_POSIX_PRIO_IO`
 * `_PC_SYNC_IO` - `_POSIX_SYNC_IO`
 * `_PC_TIMESTAMP_RESOLUTION` - `_POSIX_TIMESTAMP_RESOLUTION`
 
 <b>Requirements</b>

 * If <u>path</u> or <u>fildes</u> refers to a directory, the value returned applies to the directory itself.

 * If <u>path</u> or <u>fildes</u> does not refer to a terminal file,  an association of the variable name with the specified file is  supported.

 * If <u>path</u> or <u>fildes</u> refers to a directory, the value returned applies to filenames within the directory.

 * If <u>path</u> or <u>fildes</u> refers to a directory, the value returned is the maximum length of a relative pathname that would not cross any mount points when the specified directory is the working directory.

 * If <u>path</u> refers to a `FIFO`, or <u>fildes</u> refers to a pipe or `FIFO`, the value returned applies to the referenced object. If <u>path</u> or <u>fildes</u> refers to a directory, the value returned applies to any `FIFO` that exists or can be created within the directory. 

 * If <u>path</u> or <u>fildes</u> refers to a directory, the value returned applies to any files, other than directories, that exist or can be created within the directory.

 * If <u>path</u> or <u>fildes</u> refers to a directory, an implementation supports an association of the variable name with the specified file.

 * If <u>path</u> or <u>fildes</u> refers to a directory, the value returned is the maximum length of the string that a symbolic link in that directory can contain.

 * If <u>path</u> or <u>fildes</u> des does not refer to a regular file, an implementation supports an association of the variable name with the specified file. 

###Return value

If <u>name</u> is an invalid value, both `pathconf()` and `fpathconf()` return `-1` and set `errno` to indicate the error.

If the variable corresponding to <u>name</u> is described in <`limits.h`> as a maximum or minimum value and the variable has no limit for the path or file descriptor, both `pathconf()` and `fpathconf()` return `-1` without changing `errno`. 

Otherwise, `pathconf()` or `fpathconf()` return the current variable value for the file or directory without changing `errno`. The value returned is not more restrictive than the corresponding value available to the application when it was compiled with the implementation's <`limits.h`> or <`unistd.h`>.

If the variable corresponding to <u>name</u> is dependent on an unsupported option, the results are unspecified.

###Errors

<b>For `pathconf()`:</b>

[`EINVAL`]  The value of name is not valid.
[`EOVERFLOW`] The value of name is `_PC_TIMESTAMP_RESOLUTION` and the resolution is larger than {`LONG_MAX`}.
[`EACCES`] Search permission is denied for a component of the path prefix.
[`EINVAL`] The implementation does not support an association of the variable name with the specified file.
[`ELOOP`]  A loop exists in symbolic links encountered during resolution of the <u>path</u> argument.
[`ELOOP`]  More than {`SYMLOOP_MAX`} symbolic links were encountered during resolution of the <u>path</u> argument.
[`ENAMETOOLONG`] The length of a component of a pathname is longer than {`NAME_MAX`}.
[`ENAMETOOLONG`] The length of a pathname exceeds {`PATH_MAX`}, or pathname resolution of a symbolic link produced an intermediate result with a length that exceeds {`PATH_MAX`}.
[`ENOENT`] A component of <u>path</u> does not name an existing file or <u>path</u> is an empty string.
[`ENOTDIR`] A component of the path prefix names an existing file that is neither a directory nor a symbolic link to a directory, or the path argument contains at least one non- <slash> character and ends with one or more trailing <slash> characters and the last pathname component names an existing file that is neither a directory nor a symbolic link to a directory.

<b>For `fpathconf()`:</b>

[`EINVAL`] The value of <u>name</u> is not valid.
[`EOVERFLOW`] The value of name is `_PC_TIMESTAMP_RESOLUTION` and the resolution is larger than {`LONG_MAX`}.
[`EBADF`] The <u>fildes</u> argument is not a valid file descriptor.
[`EINVAL`] The implementation does not support an association of the variable name with the specified file.

###Implementation tasks

* Implement `fpathconf()`.
* Implement `pathconf()`.