###Synopsis
`#include <unistd.h>`

`int chdir(const char *path);`

###Compliance
IEEE Std 1003.1-2001

###Description

`chdir` changes the working directory of the current process to the one specified in <u>path</u>.

Arguments:
<u>path</u> - the path of thr new current working directory.

###Return value
Returns `0` upon successful completion, otherwise the value `-1` is returned and `errno` set to the relevant error.

###Errors

[`EACCES`] - search permission is denied for any component of the pathname pointed to by <u>path</u>.
[`ELOOP`] - a loop exists in symbolic links encountered during resolution of the <u>path</u> argument or more than {`SYMLOOP_MAX`} symbolic links were encountered during resolution of the <u>path</u> argument.
[`ENAMETOOLONG`] - the length of a component of a pathname is longer than {`NAME_MAX`} or  the length of a pathname exceeds {`PATH_MAX`}, or pathname resolution of a symbolic link produced an intermediate result with a length that exceeds {`PATH_MAX`}. 
[`ENOENT`] - a component of <u>path</u> does not name an existing directory or <u>path</u> is an empty string.
[`ENOTDIR`] - a component of the pathname names an existing file that is neither a directory nor a symbolic link to a directory.

###Implementation tasks

* Error detection and error codes setting due to above errors.

###Tests

======

###EXAMPLES
None.
