###Synopsis

`#include <ftw.h>`

`int ftw(const char *path, int (*fn)(const char *,
       const struct stat *ptr, int flag), int ndirs); `

###Description

The `ftw()` function traverses (walk) a file tree

Arguments:
    
<u>path</u> - a path to the root of the directory hierarchy.
<u>fn</u> - a pointer to the function executed for each object of the hierarchy.
<u>ndirs</u> - the maximum number of directory streams or file descriptors or both available for use by `ftw()` while traversing the tree. It should be in the range [`1`, {`OPEN_MAX`}].



The `ftw()` function recursively descends the directory hierarchy rooted in <u>path</u>. For each object in the hierarchy, `ftw()` calls the function pointed to by <u>fn</u>, passing it a pointer to a null-terminated character string containing the name of the object, a pointer to a `stat` structure containing information about the object, filled in as if `stat()` or `lstat()` had been called to retrieve the information. Possible values of the integer, defined in the `<ftw.h>` header, are:

`FTW_D` a directory.
`FTW_DNR` a directory that cannot be read.
`FTW_F` a non-directory file.
`FTW_SL` a symbolic link (but see also `FTW_NS` below).
`FTW_NS` an object other than a symbolic link on which `stat()` could not successfully be executed. If the object is a symbolic link and `stat()` failed, `ftw()` passes `FTW_SL` or `FTW_NS` to the user-supplied function.

If the integer is `FTW_DNR`, descendants of that directory are not processed. If the integer is `FTW_NS`, the `stat` structure contains undefined values. An example of an object that would cause `FTW_NS` to be passed to the function pointed to by <u>fn</u> would be a file in a directory with read but without execute (search) permission.

The `ftw()` function visits a directory before visiting any of its descendants. It uses at most one file descriptor for each level in the tree.

The tree traversal continues until either the tree is exhausted, an invocation of <u>fn</u> returns a non-zero value, or some error, other than [`EACCES`], is detected within `ftw()`.

The <u>ndirs</u> argument specifies the maximum number of directory streams or file descriptors or both available for use by `ftw()` while traversing the tree. When `ftw()` returns it closes any directory streams and file descriptors it uses not counting any opened by the application-supplied <u>fn</u> function.

The results are unspecified if the application-supplied <u>fn</u> function does not preserve the current working directory.

The `ftw()` function is not thread-safe.

###Return value

Upon successful completion, if the tree is exhausted,`ftw()` returns `0`; If the function pointed to by <u>fn</u> returns a non-zero value, `ftw()` stops its tree traversal and returns whatever value was returned by the function pointed to by <u>fn</u>. If `ftw()` detects an error, it returns `-1` and sets `errno` to indicate the error.

If `ftw()` encounters an error other than [`EACCES`], it returns `-1` and sets `errno` to indicate the error. The external variable `errno` may contain any error value that is possible when a directory is opened or when one of the `stat` functions is executed on a directory or file.

###Errors

[`EACCES`] Search permission is denied for any component of <u>path</u> or read permission is denied for <u>path</u>.
[`ELOOP`]  A loop exists in symbolic links encountered during resolution of the <u>path</u> argument.
[`ENAMETOOLONG`] The length of a component of a pathname is longer than {`NAME_MAX`}.
[`ENOENT`] A component of <u>path</u> does not name an existing file or <u>path</u> is an empty string.
[`ENOTDIR`] A component of <u>path</u> names an existing file that is neither a directory nor a symbolic link to a directory.
[`EOVERFLOW`] A field in the `stat` structure cannot be represented correctly in the current programming environment for one or more files found in the file hierarchy.
[`EINVAL`] The value of the <u>ndirs</u> argument is invalid.
[`ELOOP`] More than {`SYMLOOP_MAX`} symbolic links were encountered during resolution of the <u>path</u> argument.
[`ENAMETOOLONG`] The length of a pathname exceeds {`PATH_MAX`}, or pathname resolution of a symbolic link produced an intermediate result with a length that exceeds {`PATH_MAX`}.

###Implementation tasks:
    
 * Implement the `ftw.h` file.
 * Implement the `ftw()` function.
 