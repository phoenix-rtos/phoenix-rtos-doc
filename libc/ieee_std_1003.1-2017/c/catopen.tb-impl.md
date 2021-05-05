###Synopsis

`#include <nl_types.h>`

`nl_catd catopen(const char *name, int oflag);`

###Description

The `catgets()` function opens a message catalogue.

Arguments:
<u>name</u> - the message catalogue name.
<u>oflag</u> - the message flag (`NL_CAT_LOCALE` or `0`).
 
The `catopen()` function opens a message catalogue and returns a message catalogue descriptor. 
The <u>name</u> argument contains the name of the message catalogue to be opened. If <u>name</u> contains a `'/'`, then it specifies a pathname for the message catalogue. Otherwise, the environment variable `NLSPATH` is used with <u>name</u> substituted for the %N conversion specification. 

If `NLSPATH` exists in the environment when the process starts, then if the process has appropriate privileges, the behaviour of `catopen()` is undefined. 
If `NLSPATH` does not exist in the environment, or if a message catalogue cannot be found in any of the components specified by `NLSPATH`, then an default path is used. This default may be affected by the setting of `LC_MESSAGES` if the value of <u>oflag</u> is `NL_CAT_LOCALE`, or the `LANG` environment variable if <u>oflag</u> is `0`.

A message catalogue descriptor remains valid in a process until that process closes it, or a successful call to one of the exec functions. A change in the setting of the `LC_MESSAGES` category may invalidate existing open catalogues.

If a file descriptor is used to implement message catalogue descriptors, the `FD_CLOEXEC` flag is set (see `<fcntl.h>`).

If the value of the <u>oflag</u> argument is `0`, the `LANG` environment variable is used to locate the catalogue without regard to the `LC_MESSAGES` category. If the <u>oflag</u> argument is `NL_CAT_LOCALE`, the `LC_MESSAGES` category is used to locate the message catalogue.

###Return value

On success a message catalogue descriptor is returned, to be used on subsequent calls to `catgets()` and `catclose()`. Otherwise, `catopen()` returns (`nl_catd`) -`1` and `errno` set to indicate the error.

###Errors

[`EACCES`] - Search permission is denied for the component of the path prefix of the message catalogue or read permission is denied for the message catalogue.
[`EMFILE`] - All file descriptors available to the process are currently open.
[`ENAMETOOLONG`] - The length of a component of a pathname is longer than {`NAME_MAX`}.
[`ENAMETOOLONG`] - The length of a pathname exceeds {`PATH_MAX`}, or pathname resolution of a symbolic link produced an intermediate result with a length that exceeds {`PATH_MAX`}.
[`ENFILE`] - Too many files are currently open in the system.
[`ENOENT`] - The message catalogue does not exist or the <u>name</u> argument points to an empty string.
[`ENOMEM`] - Insufficient storage space is available.
[`ENOTDIR`] - A component of the path prefix of the message catalogue names an existing file that is neither a directory nor a symbolic link to a directory, or the pathname of the message catalogue contains at least one non- <slash> character and ends with one or more trailing <slash> characters and the last pathname component names an existing file that is neither a directory nor a symbolic link to a directory. 

###Implementation tasks
* Implement the message catalogue type `nl_catd`.
* Implement the file `<nl_types.h>`.
* Use `malloc()` to allocate space for internal buffer areas. The `catopen()` function fails if there is insufficient storage space available to accommodate these buffers.
* Assume that message catalogue descriptors are not valid after a call to one of the `exec()` functions.
* Be aware that guidelines for the location of message catalogues have not yet been developed. Therefore you should take care to avoid conflicting with catalogues used by other applications and the standard utilities.
* To be sure that messages produced by an application running with appropriate privileges cannot be used by an attacker setting an unexpected value for `NLSPATH` in the environment to confuse a system administrator, such applications should use pathnames containing a '/' to get defined behaviour when using `catopen()` to open a message catalogue.
* Implement the function.