###Synopsis

`#include <sys/stat.h>
`int futimens(int fd, const struct timespec times[2]);`

`#include <fcntl.h>`
`int utimensat(int fd, const char *path, const struct timespec times[2],
       int flag);`

`#include <sys/time.h>`
`int utimes(const char *path, const struct timeval times[2]); `

###Description

The functions set file access and modification times for the file argument.

The structures used by functions are defined as follows:

`struct timespec {`
`  time_t tv_sec; 	/* whole seconds (valid values are >= `0`) */`
`  long tv_nsec;	/* nanoseconds (valid values are [`0`, `999999999`]) */`
`};`

`struct timeval {`
`  time_t tv_sec ;	/* whole seconds (valid values are >= `0`) */`
`  suseconds_t tv_usec; 	/* microseconds */`
`};`

Arguments:
    
<u>fd</u> - a file descriptor of the file,
<u>path</u> - a path to the file,
<u>times</u> - an array of two `timespec` structures. The first array member represents the date and time of last access, and the second member represents the date and time of last modification. The times in the `timespec` structure are measured in seconds and nanoseconds since the Epoch. The file's relevant timestamp is set to the greatest value supported by the file system that is not greater than the specified time.
<u>flag</u> - `0` or  `AT_SYMLINK_NOFOLLOW`, what means that if <u>path</u> names a symbolic link, then the access and modification times of the symbolic link are changed rather than the file to which it refers.

The `futimens()` and `utimensat()` functions set the access and modification times of a file to the values of the <u>times</u> argument. The `futimens()` function changes the times of the file associated with the file descriptor <u>fd</u>. The `utimensat()` function changes the times of the file pointed to by the <u>path</u> argument, relative to the directory associated with the file descriptor <u>fd</u>. Both functions allow time specifications accurate to the nanosecond.

For `futimens()` and `utimensat()`, the <u>times</u> argument is an array of two `timespec` structures. The first array member represents the date and time of last access, and the second member represents the date and time of last modification. The <u>times</u> in the timespec structure are measured in seconds and nanoseconds since the Epoch. The file's relevant timestamp is set to the greatest value supported by the file system that is not greater than the specified time.

If the `tv_nsec` field of a `timespec` structure has the special value `UTIME_NOW`, the file's relevant timestamp is set to the greatest value supported by the file system that is not greater than the current time. If the `tv_nsec` field has the special value `UTIME_OMIT`, the file's relevant timestamp is not changed. In either case, the `tv_sec` field is ignored.

If the <u>times</u> argument is a null pointer, both the access and modification timestamps are set to the greatest value supported by the file system that is not greater than the current time. If `utimensat()` is passed a relative path in the <u>path</u> argument, the file to be used is relative to the directory associated with the file descriptor <u>fd</u> instead of the current working directory. If the access mode of the open file description associated with the file descriptor is not `O_SEARCH`, the function checks whether directory searches are permitted using the current permissions of the directory underlying the file descriptor. If the access mode is `O_SEARCH`, the function does not perform the check.

If `utimensat()` is passed the special value `AT_FDCWD` in the <u>fd</u> parameter, the current working directory is used.

Only a process with the effective user ID equal to the user ID of the file, or with write access to the file, or with appropriate privileges may use `futimens()` or `utimensat()` with a null pointer as the <u>times</u> argument or with both `tv_nsec` fields set to the special value `UTIME_NOW`. Only a process with the effective user ID equal to the user ID of the file or with appropriate privileges may use `futimens()` or `utimensat()` with a non-null <u>times</u> argument that does not have both `tv_nsec` fields set to `UTIME_NOW` and does not have both `tv_nsec` fields set to `UTIME_OMIT`. If both `tv_nsec` fields are set to `UTIME_OMIT`, no ownership or permissions check is performed for the file, but other error conditions may still be detected (including `[EACCES]` errors related to the path prefix).

Upon successful completion, `futimens()` and `utimensat()` mark the last file status change timestamp for update, with the exception that if both `tv_nsec` fields are set to `UTIME_OMIT`, the file status change timestamp need not be marked for update.

The `utimes()` function is equivalent to the `utimensat()` function with the special value `AT_FDCWD` as the <u>fd</u> argument and the flag argument set to zero, except that the <u>times</u> argument is a `timeval` structure rather than a `timespec` structure, and accuracy is only to the microsecond, not nanosecond, and rounding towards the nearest second may occur.

###Return value

Upon successful completion, the functions return `0`, otherwise  the return `-1` and set `errno` to indicate the error. If `-1` is returned, the file times are not affected.

###Errors

[`EACCES`] The <u>times</u> argument is a null pointer, or both `tv_nsec` values are `UTIME_NOW`, and the effective user ID of the process does not match the owner of the file and write access is denied.
[`EINVAL`] Either of the <u>times</u> argument structures specified a `tv_nsec` value that was neither `UTIME_NOW` nor `UTIME_OMIT`, and was a value less than zero or greater than or equal to `1000` million.
[`EINVAL`] A new file timestamp would be a value whose `tv_sec` component is not a value supported by the file system.
[`EPERM`] The <u>times</u> argument is not a null pointer, does not have both `tv_nsec` fields set to `UTIME_NOW`, does not have both `tv_nsec` fields set to `UTIME_OMIT`, the calling process' effective user ID does not match the owner of the file, and the calling process does not have appropriate privileges.
[`EROFS`] The file system containing the file is read-only.

The `futimens()` function fails if:

[`EBADF`] The <u>fd</u> argument is not a valid file descriptor.

The `utimensat()` function fails if:

[`EACCES`] The access mode of the open file description associated with <u>fd</u> is not `O_SEARCH` and the permissions of the directory underlying <u>fd</u> do not permit directory searches.
[`EBADF`]  The <u>path</u> argument does not specify an absolute path and the <u>fd</u> argument is neither `AT_FDCWD` nor a valid file descriptor open for reading or searching.
[`ENOTDIR`] The <u>path</u> argument is not an absolute path and <u>fd</u> is a file descriptor associated with a non-directory file.

The `utimensat()` and utimes() functions fail if:

[`EACCES`] Search permission is denied by a component of the path prefix.
[`EINVAL`] The value of the <u>flag</u> argument is not valid. 
[`ELOOP`]  A loop exists in symbolic links or more than {`SYMLOOP_MAX`} symbolic links are encountered during resolution of the <u>path</u> argument.
[`ENAMETOOLONG`] The length of a component of a pathname is longer than {`NAME_MAX`} or
    the length of a pathname exceeds {`PATH_MAX`}, or 
    pathname resolution of a symbolic link produced an intermediate result with a length that exceeds {`PATH_MAX`}.
[`ENOENT`] A component of <u>path</u> does not name an existing file or <u>path</u> is an empty string.
[`ENOTDIR`]A component of the path prefix names an existing file that is neither a directory nor a symbolic link to a directory, or the <u>path</u> argument contains at least one non- <slash> character and ends with one or more trailing <slash> characters and the last pathname component names an existing file that is neither a directory nor a symbolic link to a directory.
 
###Implementation tasks:
    
 * Implement the `futimens()` function.
 * Implement the `utimensat()` function.
 * Implement the `utimes()` function.