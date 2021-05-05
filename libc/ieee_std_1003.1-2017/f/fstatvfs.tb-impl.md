###Synopsis

`#include <sys/statvfs.h>`

`int fstatvfs(int fildes, struct statvfs *buf);`
`int statvfs(const char *restrict path, struct statvfs *restrict buf);`

###Description

The `fstatvfs()` function obtains information about the statistics concerning the file system containing the file referenced by <u>fildes</u>.

The `statvfs()` function obtains information about the statistics concerning the file system containing the file named by <u>path</u>.

Arguments:

<u>fildes</u> - the file descriptor of the file of interest.
<u>path</u> - a pointer to a pathname naming a file.
<u>buf</u>  - the buffer for results - a pointer to a `statvfs` structure to be filled. Read, write, or execute permission of the named file is not required.

The following flags can be returned in the f_flag member of the `statvfs` structure:

`ST_RDONLY` Read-only file system.
`ST_NOSUID` Setuid/setgid bits ignored by exec.

###Return value

Upon successful completion, `0` is returned. Otherwise, `-1` is returned and `errno` set to indicate the error.

###Errors

The `fstatvfs()` and `statvfs()` functions fail if:

[`EIO`] An I/O error occurred while reading the file system.
[`EINTR`] A signal was caught during execution of the function.
[`EOVERFLOW`] One of the values to be returned cannot be represented correctly in the structure pointed to by <u>buf</u>.

The `fstatvfs()` function fails if:

[`EBADF`] The <u>fildes</u> argument is not an open file descriptor.

The `statvfs()` function fails if:

[`EACCES`] Search permission is denied on a component of the <u>path</u> prefix.
[`ELOOP`] A loop exists in symbolic links encountered during resolution of the <u>path</u> argument. or
        More than {`SYMLOOP_MAX`} symbolic links were encountered during resolution of the <u>path</u> argument.
[`ENAMETOOLONG`] The length of a component of a pathname is longer than {`NAME_MAX`}. or
                The length of a pathname exceeds {PATH_MAX}, or pathname resolution of a symbolic link produced an intermediate result with a length that exceeds {PATH_MAX}.
[`ENOENT`] A component of <u>path</u> does not name an existing file or <u>path</u> is an empty string.
[`ENOTDIR`] A component of the <u>path</u> prefix names an existing file that is neither a directory nor a symbolic link to a directory, or the <u>path</u> argument contains at least one non- <slash> character and ends with one or more trailing <slash> characters and the last pathname component names an existing file that is neither a directory nor a symbolic link to a directory.
        
###Implementation tasks:
    
 * Implement `sys/statvfs.h` file.
 * Implement `fstatvfs()` function.
 * Implement `statvfs()` function.