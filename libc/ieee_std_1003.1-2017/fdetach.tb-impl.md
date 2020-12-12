###Synopsis

`#include <stropts.h>`

`int fdetach(const char *path);`

###Description

The `fdetach()` function detaches a name from a STREAMS-based file descriptor. 

Arguments:

<u>path</u> - the pathname of the attached STREAMS file.

The `fdetach()` function detaches a STREAMS-based file from the file to which it was attached by a previous call to `fattach()`. The process has appropriate privileges or is the owner of the file. A successful call to `fdetach()` causes all pathnames that named the attached STREAMS file to again name the file to which the STREAMS file was attached. All subsequent operations on <u>path</u> operate on the underlying file and not on the STREAMS file.

All open file descriptions established while the STREAMS file was attached to the file referenced by <u>path</u> still refer to the STREAMS file after the `fdetach()` has taken effect.

If there are no open file descriptors or other references to the STREAMS file, then a successful call to `fdetach()` is equivalent to performing the last `close()` on the attached file.

The `fdetach()` function may be removed in a future version. It is marked obsolescent.
 
###Return value

Upon successful completion, the `fdetach()` function returns `0`, otherwise, `-1` is returned and `errno` set to indicate the error.

###Errors

[`EACCES`] - Search permission is denied on a component of the path prefix.
[`EINVAL`] - The <u>path</u> argument names a file that is not currently attached.
[`ELOOP`] -  A loop exists in symbolic links encountered during resolution of the <u>path</u> argument.
[`ENAMETOOLONG`] - The length of a component of a pathname is longer than {`NAME_MAX`}.
[`ENOENT`] - A component of <u>path</u> does not name an existing file or <u>path</u> is an empty string.
[`ENOTDIR`] - A component of the path prefix names an existing file that is neither a directory nor a symbolic link to a directory, or the <u>path</u> argument contains at least one non- <slash> character and ends with one or more trailing <slash> characters and the last pathname component names an existing file that is neither a directory nor a symbolic link to a directory.
[`EPERM`] - The effective user ID is not the owner of <u>path</u> and the process does not have appropriate privileges.
[`ELOOP`] - More than {`SYMLOOP_MAX`} symbolic links were encountered during resolution of the <u>path</u> argument.
[`ENAMETOOLONG`] - The length of a pathname exceeds {`PATH_MAX`}, or pathname resolution of a symbolic link produced an intermediate result with a length that exceeds {`PATH_MAX`}. 

###Implementation tasks

 * Implement the `stropts.h`
 * Implement the `fdetach()` function.