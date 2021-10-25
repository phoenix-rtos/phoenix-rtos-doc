###Synopsis

`#include <stdio.h>`

`FILE *fopen(const char *filename, const char *mode);`

###Description

Opens the file with a name pointed to by <u>filename</u> using the given <u>mode</u>.

Arguments:
<u>filename</u> - the string saving the file's pathname
<u>mode</u> - the string defining the file mode; it should be one of the following:

`r` - open the file for reading.
`w` - truncate to zero length or create file for writing.
`a` - append; open or create file for writing at end-of-file.
`r+`- open file for update (reading and writing).
`w+`- truncate to zero length or create file for update.
`a+`- append; open or create file for update, writing at end-of-file.

Opening a file with append mode (a as the first character in the mode argument) causes all subsequent writes to the file to be forced to the then current end-of-file, regardless of intervening calls to `fseek()`.

When a file is opened with update mode ( '+' as the second or third character in the mode argument), both input and output may be performed on the associated stream. However, the application ensures that output is not directly followed by input without an intervening call to `fflush()` or to a file positioning function (`fseek()`, `fsetpos()`, or `rewind()`), and input is not directly followed by output without an intervening call to a file positioning function, unless the input operation encounters end-of-file.

When opened, a stream is fully buffered if and only if it can be determined not to refer to an interactive device. The error and end-of-file indicators for the stream are cleared.

If mode is `w`, `a`, `w+` or `a+`:

 * the file did not previously exist, upon successful completion, `fopen()` marks the last data access, last data modification, and last file status change timestamps of the file and the last file status change and last data modification timestamps of the parent directory.

 * the file did not previously exist, the for update `fopen()` function creates a file as if it called the `creat()` function with a value appropriate for the path argument interpreted from pathname and a value of `S_IRUSR | S_IWUSR | S_IRGRP | S_IWGRP | S_IROTH | S_IWOTH` for the <u>mode</u> argument.

If mode is `w`, `a`, `w+` and the file did previously exist, upon successful completion, `fopen()` marks for update the last data modification and last file status change timestamps of the file.

After a successful call to the `fopen()` function, the orientation of the stream is cleared, the encoding rule is cleared, and the associated `mbstate_t` object is set to describe an initial conversion state.

###Return value

A pointer to the object controlling the stream on success, otherwise a null pointer is returned, and `errno` is set to indicate the error. 
    
###Errors

[`EACCES`] Search permission is denied on a component of the path prefix, or the file exists and the permissions specified by <u>mode</u> are denied, or the file does not exist and write permission is denied for the parent directory of the file to be created.
[`EINTR`]  A signal was caught during `fopen()`.
[`EISDIR`] The named file is a directory and <u>mode</u> requires write access.
[`ELOOP`]  A loop exists in symbolic links encountered during resolution of the <u>path</u> argument.
[`EMFILE`] All file descriptors available to the process are currently open.
[`EMFILE`] {`STREAM_MAX`} streams are currently open in the calling process.
[`ENAMETOOLONG`] The length of a <u>pathname</u> exceeds {`PATH_MAX`}, or pathname resolution of a symbolic link produced an intermediate result with a length that exceeds {`PATH_MAX`}.
[`ENFILE`] The maximum allowable number of files is currently open in the system.
[`ENOENT`] The mode string begins with 'r' and a component of <u>pathname</u> does not name an existing file, or mode begins with 'w' or 'a' and a component of the path prefix of <u>pathname</u> does not name an existing file, or <u>pathname</u> is an empty string.
[`ENOENT`] or [`ENOTDIR`] The <u>pathname</u> argument contains at least one non- <slash> character and ends with one or more trailing <slash> characters. If <u>pathname</u> without the trailing <slash> characters would name an existing file, an [`ENOENT`] error shall not occur.
[`ENOSPC`] The directory or file system that would contain the new file cannot be expanded, the file does not exist, and the file was to be created.
[`ENOTDIR`] A component of the path prefix names an existing file that is neither a directory nor a symbolic link to a directory, or the <u>pathname</u> argument contains at least one non- <slash> character and ends with one or more trailing <slash> characters and the last pathname component names an existing file that is neither a directory nor a symbolic link to a directory.
[`ENXIO`]   The named file is a character special or block special file, and the device associated with this special file does not exist.
[`EOVERFLOW`] The named file is a regular file and the size of the file cannot be represented correctly in an object of type `off_t`.
[`EROFS`] The named file resides on a read-only file system and <u>mode</u> requires write access.
[`EINVAL`] The value of the <u>mode</u> argument is not valid.
    [`ELOOP`]  More than {`SYMLOOP_MAX`} symbolic links were encountered during resolution of the <u>path</u> argument.
    [`EMFILE`] {`FOPEN_MAX`} streams are currently open in the calling process.
    [`ENAMETOOLONG`] The length of a component of a pathname is longer than {`NAME_MAX`}.
    [`ENOMEM`] Insufficient storage space is available.
    [`ETXTBSY`] The file is a pure procedure (shared text) file that is being executed and <u>mode</u> requires write access.

###Implementation tasks

 * Implement error handling for the `fopen()` function.
 
