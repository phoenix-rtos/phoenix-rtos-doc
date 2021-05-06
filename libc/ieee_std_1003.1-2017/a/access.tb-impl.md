# Synopsis
`#include <unistd.h>`

`int access(const char *pathname, int amode);`

`#include <fcntl.h>`

`int faccessat(int fd, const char *path, int amode, int flag);`

## Status

To be implemented

## Description

`access()` checks for file accessibility.

Arguments:

<u>pathname</u> - path to the file.
<u>amode</u> - access permission to be checked.
<u>flag</u> - access flag.

The `access()` function checks the file named by the <u>pathname</u> pointed to by the path argument for accessibility according to the bit pattern contained in <u>amode</u>. The checks for accessibility (including directory permissions checked during pathname resolution) are performed using the real user ID in place of the effective user ID and the real group ID in place of the effective group ID.

The value of <u>amode</u> is either the bitwise-inclusive `OR` of the access permissions to be checked (`R_OK`, `W_OK`, `X_OK`) or the existence test (`F_OK`).

If any access permissions are checked, each is checked individually, except that where that description refers to execute permission for a process with appropriate privileges, an implementation may indicate success for `X_OK` even if execute permission is not granted to any user.

The `faccessat()` function, when called with a <u>flag</u> value of zero, is equivalent to the `access()` function, except in the case where path specifies a relative path. In this case the file whose accessibility is to be determined is located relative to the directory associated with the file descriptor fd instead of the current working directory. If the access mode of the open file description associated with the file descriptor is not `O_SEARCH`, the function check whether directory searches are permitted using the current permissions of the directory underlying the file descriptor. If the access mode is O_SEARCH, the function does not perform the check.

If `faccessat()` is passed the special value `AT_FDCWD` in the <u>fd</u> parameter, the current working directory is used and, if flag is zero, the behavior is identical to a call to `access`().

Values for <u>flag</u> are constructed by a bitwise-inclusive `OR` of flags from the following list, defined in <`fcntl.h`>: `AT_EACCESS`

The checks for accessibility (including directory permissions checked during pathname resolution) is performed using the effective user ID and the group ID instead of the real user ID and group ID as required in a call to `access()`.

## Return value

`0` upon successful completion,

`-1` otherwise.

## Errors

[`EACCES`] - Permission bits of the file mode do not permit the requested access, or search permission is denied on a component of the path prefix.

[`ELOOP`] - A loop exists in symbolic links encountered during resolution of the path argument.

[`ENAMETOOLONG`] - The length of a component of a pathname is longer than {NAME_MAX}.

[`ENOENT`] - A component of path does not name an existing file or path is an empty string.

[`ENOTDIR`] - A component of the path prefix names an existing file that is neither a directory nor a symbolic link to a directory, or the path argument contains at least one non- <slash> character and ends with one or more trailing <slash> characters and the last pathname component names an existing file that is neither a directory nor a symbolic link to a directory.

[`EROFS`] - Write access is requested for a file on a read-only file system.

The `faccessat()` function fails if:

[`EACCES`] - The access mode of the open file description associated with fd is not O_SEARCH and the permissions of the directory underlying fd do not permit directory searches.

[`EBADF`] -  The path argument does not specify an absolute path and the fd argument is neither AT_FDCWD nor a valid file descriptor open for reading or searching.

[`ENOTDIR`] - The path argument is not an absolute path and fd is a file descriptor associated with a non-directory file.

These functions may fail if:

[`EINVAL`] - The value of the <u>amode</u> argument is invalid.

[`ELOOP`] - More than {`SYMLOOP_MAX`} symbolic links were encountered during resolution of the path argument.

[`ENAMETOOLONG`] - The length of a <u>pathname</u> exceeds {`PATH_MAX`}, or pathname resolution of a symbolic link produced an intermediate result with a length that exceeds {PATH_MAX}.

[`ETXTBSY`] - Write access is requested for a pure procedure (shared text) file that is being executed.

The `faccessat()` function may fail if:

[`EINVAL`] - The value of the flag argument is not valid.
