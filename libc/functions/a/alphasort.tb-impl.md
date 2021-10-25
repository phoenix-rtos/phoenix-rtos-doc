###Synopsis
`#include <dirent.h>`

`int alphasort(const struct dirent **d1, const struct dirent **d2);`

`int scandir(const char *dir, struct dirent ***namelist,
       int (*sel)(const struct dirent *),
       int (*compar)(const struct dirent **, const struct dirent **));`

###Description

The `alphasort()` function can be used as the comparison function for the `scandir()` function to sort the directory entries, <u>d1</u> and <u>d2</u>, into alphabetical order. Sorting happens as if by calling the `strcoll()` function on the `d_name` element of the `dirent` structures passed as the two parameters. If the `strcoll()` function fails, the return value of `alphasort()` is unspecified.

Arguments:

For `alphasort()`:
<u>d1</u>, <u>d2</u>  - directory entries to be compared.

For `scandir()`:
<u>dir</u> - the directory to be scanned,
<u>namelist</u> - a resulting array which is allocated as if by a call to `malloc()`,
<u>sel</u> - a pointer to the function to be called on each directory entry,
<u>compar</u> - the comparison function.

If <u>sel</u> is a null pointer, all entries are selected.
If the comparison function <u>compar</u> does not provide total ordering, the order in which the directory entries are stored is unspecified.

###Return value

Upon successful completion, the `alphasort()` function returns greater than, equal to, or less than `0`, according to whether the name of the directory entry pointed to by <u>d1</u> is lexically greater than, equal to, or less than the directory pointed to by <u>d2</u> when both are interpreted as appropriate to the current locale. There is no return value reserved to indicate an error.

Upon successful completion, the `scandir()` function returns the number of entries in the array and a pointer to the array through the parameter <u>namelist</u>. Otherwise, the `scandir()` function returns `-1`.

###Errors
No errors are defined for the `alphasort()` function.

The `scandir()` function fails if
    [`EACCES`] -  search permission is denied for the component of the path prefix of <u>dir</u> or read permission is denied for <u>dir</u>.
    [`ELOOP`] - a loop exists in symbolic links encountered during resolution of the <u>dir</u> argument.
    [`ENAMETOOLONG`] - The length of a component of a pathname is longer than {`NAME_MAX`}.
    [`ENOENT`] - A component of <u>dir</u> does not name an existing directory or <u>dir</u> is an empty string.
    [`ENOMEM`] - Insufficient storage space is available.
    [`ENOTDIR`] - A component of <u>dir</u> names an existing file that is neither a directory nor a symbolic link to a directory.
    [`EOVERFLOW`] - One of the values to be returned or passed to a callback function cannot be represented correctly.
    [`ELOOP`] - More than {`SYMLOOP_MAX`} symbolic links were encountered during resolution of the <u>dir</u> argument.
    [`EMFILE`] - All file descriptors available to the process are currently open.
    [`ENAMETOOLONG`] - The length of a <u>pathname</u> exceeds {`PATH_MAX`}, or <u>pathname</u> resolution of a symbolic link produced an intermediate result with a length that exceeds {`PATH_MAX`}.
    [`ENFILE`] - Too many files are currently open in the system.

###Comments
The `alphasort()` function does not change the setting of `errno` if successful. Since no return value is reserved to indicate an error, an application wishing to check for error situations should set `errno` to `0`, then call `alphasort()`, then check `errno`.
