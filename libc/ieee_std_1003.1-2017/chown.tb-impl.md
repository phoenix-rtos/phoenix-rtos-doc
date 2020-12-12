###Synopsis
`#include <unistd.h>`
`int chown(const char *path, uid_t owner, gid_t group);`

`#include <fcntl.h>`
`int fchownat(int fd, const char *path, uid_t owner, gid_t group, int flag);`

###Description
The `chown()` function changes ownership of the file (the user and the group). 
The `fchownat()` function works identically unless the case when <u>path</u> is a relative path. 

Arguments:
<u>path</u> - the pathname of the file,
<u>owner</u> - the user identifier of a new owner of the file,
<u>group</u> - the user group identifier of a new owner of the file,

<u>fd</u> - file descriptor of the directory,
<u>flag</u> - `0` or `AT_SYMLINK_NOFOLLOW` (ownership of the file is changed for <u>path</u> naming a symbolic link).

The ownership of a file may be changed only by processes with the effective user IDs equal to the user ID of the file or with appropriate privileges. 
If `_POSIX_CHOWN_RESTRICTED` is in effect for <u>path</u>:
 * Changing the user ID is restricted to processes with appropriate privileges.
 * Changing the group ID is permitted to a process with an effective user ID equal to the user ID of the file, but without appropriate privileges, if and only if <u>owner</u> is equal to the file's user ID or (uid_t)-1 and <u>group</u> is equal either to the calling process' effective group ID or to one of its supplementary group IDs.

For <u>path</u> naming a regular file, one or more of the `S_IXUSR`, `S_IXGRP`, or `S_IXOTH` bits of the file mode are set, and the process does not have appropriate privileges, the set-user-ID (`S_ISUID`) and set-group-ID (`S_ISGID`) bits of the file mode are cleared upon successful return from `chown()`. If the specified file is a regular file, one or more of the `S_IXUSR`, `S_IXGRP`, or `S_IXOTH` bits of the file mode are set, and the process has appropriate privileges, it is implementation-defined whether the set-user-ID and set-group-ID bits are altered. If the `chown()` function is successfully invoked on a file that is not a regular file and one or more of the `S_IXUSR`, `S_IXGRP`, or `S_IXOTH` bits of the file mode are set, the set-user-ID and set-group-ID bits may be cleared.

If <u>owner</u> or <u>group</u> is specified as (uid_t)-1 or (gid_t)-1, respectively, the corresponding ID of the file are not changed.

Upon successful completion, `chown()` marks for update the last file status change timestamp of the file, except that if <u>owner</u> is (uid_t)-1 and <u>group</u> is (gid_t)-1, the file status change timestamp need not be marked for update.

The `fchownat()` function is equivalent to the `chown()` and `lchown()` functions except in the case where <u>path</u> specifies a relative path. In this case the file to be changed is determined relative to the directory associated with the file descriptor <u>fd</u> instead of the current working directory. If the access mode of the open file description associated with the file descriptor is not `O_SEARCH`, the function checks whether directory searches are permitted using the current permissions of the directory underlying the file descriptor. If the access mode is `O_SEARCH`, the function does not perform the check.

Values for <u>flag</u> are constructed by a bitwise-inclusive `OR` of flags from the following list, defined in <fcntl.h>:

`AT_SYMLINK_NOFOLLOW` - if <u>path</u> names a symbolic link, ownership of the symbolic link is changed.

If `fchownat()` is passed the special value `AT_FDCWD` in the <u>fd</u> parameter, the current working directory is used and the behavior is identical to a call to `chown()` or `lchown()` respectively, depending on whether or not the `AT_SYMLINK_NOFOLLOW` bit is set in the flag argument.

###Return value

`0` - successful completion,
`-1` - otherwise (`errno` is set to the error); no changes are made in the user ID and group ID of the file.

###Errors

[`EACCES`] - search permission is denied on a component of the <u>path</u> prefix
           - (for fchownat())the access mode of the open file description associated with <u>fd</u> is not `O_SEARCH` and the permissions of the directory underlying <u>fd</u> do not permit directory searches.
[`ELOOP`] - a loop exists in symbolic links encountered during resolution of the <u>path</u> argument.
          - (for `fchownat()`) more than {`SYMLOOP_MAX`} symbolic links were encountered during resolution of the <u>path</u> argument.
[`ENAMETOOLONG`] - the length of a component of a pathname is longer than {`NAME_MAX`}
                 - the length of a pathname exceeds {`PATH_MAX`}, or pathname resolution of a symbolic link produced an intermediate result with a length that exceeds {`PATH_MAX`}.
[`ENOENT`] - a component of <u>path</u> does not name an existing file or <u>path</u> is an empty string.
[`ENOTDIR`] - a component of the <u>path</u> prefix names an existing file that is neither a directory nor a symbolic link to a directory, or the <u>path</u> argument contains at least one non- <slash> character and ends with one or more trailing <slash> characters and the last pathname component names an existing file that is neither a directory nor a symbolic link to a directory .
            - (for fchownat()) the <u>path</u> argument is not an absolute path and u>fd</u> is a file descriptor associated with a non-directory file.
[`EPERM`] - the effective user ID does not match the owner of the file, or the calling process does not have appropriate privileges and `_POSIX_CHOWN_RESTRICTED` indicates that such privilege is required.
[`EROFS`] - the named file resides on a read-only file system.

[`EBADF`] - the <u>path</u> argument does not specify an absolute path and the <u>fd</u> argument is neither `AT_FDCWD` nor a valid file descriptor open for reading or searching.

[`EIO`] - an I/O error occurred while reading or writing to the file system.
[`EINTR`] - the `chown()` function was interrupted by a signal which was caught.
[`EINVAL`] - the owner or group ID supplied is not a value supported by the implementation 
           - (for `fchownat()`)the value of the <u>flag</u> argument is not valid.

