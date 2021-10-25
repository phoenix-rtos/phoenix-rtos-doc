###Synopsis

`#include <stropts.h>`

`int fattach(int fildes, const char *path);`

###Description

The function attaches a STREAMS-based file descriptor to a file in the file system name space.

Arguments:

<u>fildes</u> - the file descriptor.
<u>path</u> - a pathname of an existing file. 

The `fattach()` function attaches a STREAMS-based file descriptor to a file, effectively associating a pathname with <u>fildes</u>. The application ensures that the <u>fildes</u> argument is a valid open file descriptor associated with a STREAMS file. The <u>path</u> argument points to a pathname of an existing file. The application has appropriate privileges or is the owner of the file named by <u>path</u> and has write permission. A successful call to `fattach` causes all pathnames that name the file named by <u>path</u> to name the STREAMS file associated with <u>fildes</u>, until the STREAMS file is detached from the file. A STREAMS file can be attached to more than one file and can have several pathnames associated with it.

The attributes of the named STREAMS file are initialized as follows: the permissions, user ID, group ID, and times are set to those of the file named by <u>path</u>, the number of links is set to `1`, and the size and device identifier are set to those of the STREAMS file associated with <u>fildes</u>. If any attributes of the named STREAMS file are subsequently changed (for example, by `chmod()`), neither the attributes of the underlying file nor the attributes of the STREAMS file to which <u>fildes</u> refers are affected.

File descriptors referring to the underlying file, opened prior to an `fattach()` call, continue to refer to the underlying file.

###Return value

Upon successful completion, `fattach()` returns `0`. Otherwise, `-1` is returned and `errno` set to indicate the error.

###Errors

[`EACCES`] Search permission is denied for a component of the path prefix, or the process is the owner of path but does not have write permissions on the file named by <u>path</u>.
[`EBADF`] The <u>fildes</u> argument is not a valid open file descriptor.
[`EBUSY`] The file named by path is currently a mount point or has a STREAMS file attached to it.
[`ELOOP`] A loop exists in symbolic links encountered during resolution of the path argument.
[`ENAMETOOLONG`] The length of a component of a pathname is longer than {`NAME_MAX`}.
[`ENOENT`] A component of <u>path</u> does not name an existing file or path is an empty string.
[`ENOTDIR`] A component of the path prefix names an existing file that is neither a directory nor a symbolic link to a directory, or the <u>path</u> argument contains at least one non- <slash> character and ends with one or more trailing <slash> characters.
[`EPERM`] The effective user ID of the process is not the owner of the file named by <u>path</u> and the process does not have appropriate privileges.

[`EINVAL`] The <u>fildes</u> argument does not refer to a STREAMS file.
[`ELOOP`] More than {`SYMLOOP_MAX`} symbolic links were encountered during resolution of the <u>path</u> argument.
[`ENAMETOOLONG`] The length of a pathname exceeds {`PATH_MAX`}, or pathname resolution of a symbolic link produced an intermediate result with a length that exceeds {`PATH_MAX`}.
[`EXDEV`] A link to a file on another file system was attempted.

###Implementation tasks

 * Implement the `stropts.h` file
 * Implement `fattach()`