###Synopsis

`#include <sys/ipc.h>`

`key_t ftok(const char *path, int id);`

###Description

The `ftok()` function generates an IPC key.

Arguments:
    
<u>path</u> - the pathname of an existing file.
<u>id</u> - a nonzero number of which the least significant `8` bits will be used to generate the key.

The `ftok()` function returns a key based on <u>path</u> and <u>id</u> that is usable in subsequent calls to `msgget()`, `semget()`, and `shmget()`. The application must ensure that the <u>path</u> argument is the pathname of an existing file that the process is able to `stat()`, with the exception that if `stat()` would fail with [`EOVERFLOW`] due to file size, `ftok()` still succeeds.

The `ftok()` function returns the same key value for all paths that name the same file, when called with the same <u>id</u> value, and should return different key values when called with different <u>id</u> values or with paths that name different files existing on the same file system at the same time.

Only the low-order `8`-bits of <u>id</u> are significant. They must form the nonzero number.


###Return value

Upon successful completion, `ftok()` returns an IPC key.
Otherwise, `ftok()` returns `(key_t)-1`, and sets `errno` to indicate the error.

###Errors

[`EACCES`] Search permission is denied for a component of the path prefix.
[`EIO`] An error occurred while reading from the file system.
[`ELOOP`] A loop exists in symbolic links encountered during resolution of the <u>path</u> argument or
          more than {`SYMLOOP_MAX`} symbolic links were encountered during resolution of the <u>path</u> argument.
[`ENAMETOOLONG`]  The length of a component of a pathname is longer than {`NAME_MAX`}  or
        the length of a pathname exceeds {`PATH_MAX`}, or pathname resolution of a symbolic link produced an intermediate result with a length that exceeds {`PATH_MAX`}. 
[`ENOENT`]  A component of <u>path</u> does not name an existing file or <u>path</u> is an empty string.
[`ENOTDIR`] A component of the <u>path</u> prefix names an existing file that is neither a directory nor a symbolic link to a directory, or the <u>path</u> argument contains at least one non- <slash> character and ends with one or more trailing <slash> characters and the last pathname component names an existing file that is neither a directory nor a symbolic link to a directory.
    
###Implementation tasks:
    
 * Implement the `ftok()` function.
 