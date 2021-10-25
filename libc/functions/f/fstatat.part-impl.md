###Synopsis

`#include <fcntl.h>`
`#include <sys/stat.h>`

`int fstatat(int fd, const char *restrict path,
       struct stat *restrict buf, int flag);`
`int lstat(const char *restrict path, struct stat *restrict buf);`
`int stat(const char *restrict path, struct stat *restrict buf);`

###Description

The `stat()` function obtains information about the named file and writes it to the area pointed to by the <u>buf</u> argument. The <u>path</u> argument points to a pathname naming a file. Read, write, or execute permission of the named file is not required. 

Arguments:

<u>fd</u> - the file descriptor of the file of interest.
<u>path</u> - a pointer to a pathname naming a file.
<u>buf</u>  - the buffer for results - a pointer to a `stat` structure.
<u>flag</u> - a flag of a file treatment.

If the named file is a symbolic link, the `stat()` function continues pathname resolution using the contents of the symbolic link, and returns information pertaining to the resulting file if the file exists.

The <u>buf</u> argument is a pointer to a `stat` structure, as defined in the `<sys/stat.h>` header, into which information is placed concerning the file.

The `stat()` function updates any time-related fields, before writing into the `stat` structure.

If the named file is a shared memory object, the implementation updates in the `stat` structure pointed to by the <u>buf</u> argument the `st_uid`, `st_gid`, `st_size`, and `st_mode` fields, and only the `S_IRUSR`, `S_IWUSR`, `S_IRGRP`, `S_IWGRP`, `S_IROTH`, and `S_IWOTH` file permission bits need be valid.

If the named file is a typed memory object, the implementation updates in the `stat` structure pointed to by the <u>buf</u> argument the `st_uid`, `st_gid`, `st_size`, and `st_mode` fields, and only the `S_IRUSR`, `S_IWUSR`, `S_IRGRP`, `S_IWGRP`, `S_IROTH`, and `S_IWOTH` file permission bits need be valid.

For all other file types, the structure members `st_mode`, `st_ino`, `st_dev`, `st_uid`, `st_gid`, `st_atim`, `st_ctim`, and `st_mtim` have meaningful values and the value of the member `st_nlink` shall be set to the number of links to the file.

The `lstat()` function is equivalent to `stat()`, except when <u>path</u> refers to a symbolic link. In that case `lstat()` returns information about the link, while `stat()` returns information about the file the link references.

For symbolic links, the `st_mode` member contains meaningful information when used with the file type macros. The file mode bits in `st_mode` are unspecified. The structure members `st_ino`, `st_dev`, `st_uid`, `st_gid`, `st_atim`, `st_ctim`, and `st_mtim` have meaningful values and the value of the `st_nlink` member is set to the number of (hard) links to the symbolic link. The value of the `st_size` member is set to the length of the pathname contained in the symbolic link not including any terminating null byte.

The `fstatat()` function is equivalent to the `stat()` or `lstat()` function, depending on the value of <u>flag</u>, except in the case where <u>path</u> specifies a relative path. In this case the status is retrieved from a file relative to the directory associated with the file descriptor <u>fd</u> instead of the current working directory. If the access mode of the open file description associated with the file descriptor is not `O_SEARCH`, the function checks whether directory searches are permitted using the current permissions of the directory underlying the file descriptor. If the access mode is `O_SEARCH`, the function does not perform the check.

Values for <u>flag</u> are constructed by a bitwise-inclusive `OR` of flags from the following list, defined in `<fcntl.h>`: 
    
 * `AT_SYMLINK_NOFOLLOW` If <u>path</u> names a symbolic link, the status of the symbolic link is returned.

If `fstatat()` is passed the special value `AT_FDCWD` in the <u>fd</u> parameter, the current working directory is used and the behavior is identical to a call to `stat()` or `lstat()` respectively, depending on whether or not the `AT_SYMLINK_NOFOLLOW` bit is set in <u>flag</u>.

###Return value

Upon successful completion, `0` is returned. Otherwise, `-1` is returned and `errno` set to indicate the error.

###Errors

These functions fail if:

[`EACCES`] Search permission is denied for a component of the path prefix.
[`EIO`] An error occurred while reading from the file system.
[`ELOOP`] A loop exists in symbolic links encountered during resolution of the <u>path</u> argument. or
              More than {`SYMLOOP_MAX`} symbolic links were encountered during resolution of the <u>path</u> argument.
[`ENAMETOOLONG`] The length of a component of a pathname is longer than {`NAME_MAX`}. or
           The length of a pathname exceeds {`PATH_MAX`}, or pathname resolution of a symbolic link produced an intermediate result with a length that exceeds {PATH_MAX}.
[`ENOENT`] A component of <u>path</u> does not name an existing file or <u>path</u> is an empty string.
 [`ENOTDIR`] A component of the path prefix names an existing file that is neither a directory nor a symbolic link to a directory, or the <u>path</u> argument contains at least one non- <slash> character and ends with one or more trailing <slash> characters and the last pathname component names an existing file that is neither a directory nor a symbolic link to a directory.
[`EOVERFLOW`] The file size in bytes or the number of blocks allocated to the file or the file serial number cannot be represented correctly in the structure pointed to by <u>buf</u>. or
                  A value to be stored would overflow one of the members of the `stat` structure.

The `fstatat()` function fails if:

[`EACCES`] The access mode of the open file description associated with <u>fd</u> is not `O_SEARCH` and the permissions of the directory underlying <u>fd</u> do not permit directory searches.
[`EBADF`]  The <u>path</u> argument does not specify an absolute path and the <u>fd</u> argument is neither `AT_FDCWD` nor a valid file descriptor open for reading or searching.
[`ENOTDIR`] The <u>path</u> argument is not an absolute path and <u>fd</u> is a file descriptor associated with a non-directory file.
[`EINVAL`]  The value of the <u>flag</u> argument is not valid.

###Implementation tasks:
    
 * Implement error handling for the functions