###Synopsis

`#include <stdio.h>`

`FILE *freopen(const char *filename, const char *mode, FILE *stream);`

###Description

The `freopen()` function associates a new filename with the given open stream and at the same time closes the old file in stream.

Arguments:

<u>filename</u> - a pathname to the file to be opened,
<u>mode</u> - the required mode of the file,
<u>stream</u> - the pointer to a `FILE` object that identifies the stream to be reopened

The `freopen()` function first attempts to flush the stream associated with <u>stream</u> as if by a call to `fflush(stream)`. Failure to flush the stream successfully is ignored. If <u>filename</u> is not a null pointer, `freopen()` closes any file descriptor associated with stream. Failure to close the file descriptor successfully is ignored. The error and end-of-file indicators for the stream are cleared.

The `freopen()` function opens the file whose filename is the string pointed to by <u>filename</u> and associates the stream pointed to by <u>stream</u> with it. The <u>mode</u> argument is used just as in `fopen()`.

The original stream is closed regardless of whether the subsequent open succeeds.

If <u>filename</u> is a null pointer, the `freopen()` function attempts to change the mode of the stream to that specified by <u>mode</u>, as if the name of the file currently associated with the stream had been used. In this case, the file descriptor associated with the stream need not be closed if the call to `freopen()` succeeds. 

After a successful call to the `freopen()` function, the orientation of the stream is cleared, the encoding rule is cleared, and the associated `mbstate_t` object is set to describe an initial conversion state.

If <u>filename</u> is not a null pointer, or if <u>filename</u> is a null pointer and the specified mode change necessitates the file descriptor associated with the stream to be closed and reopened, the file descriptor associated with the reopened stream is allocated and opened as if by a call to `open()` with the following flags:
<table style="width:100%">
  <tr>
    <th>`freopen()` Mode</th>
    <th>`open()` Flags</th>
  </tr>
  <tr>
    <td>r or rb</td>
    <td>O_RDONLY</td>
  </tr>
  <tr>
    <td>w or wb</td>
    <td>O_WRONLY|O_CREAT|O_TRUNC</td>
  </tr>
  <tr>
    <td>a or ab</td>
    <td>O_WRONLY|O_CREAT|O_APPEND</td>
  </tr>
  <tr>
    <td>r+ or rb+ or r+b</td>
    <td>O_RDWR</td>
  </tr>
    <tr>
    <td>w+ or wb+ or w+b</td>
    <td>O_RDWR|O_CREAT|O_TRUNC</td>
  </tr>
    <tr>
    <td>a+ or ab+ or a+b</td>
    <td>O_RDWR|O_CREAT|O_APPEND</td>
  </tr>
</table> 

###Return value

The value of <u>stream</u> on success.  Otherwise, a null pointer is returned, and `errno` is set to indicate the error. 

###Errors

[`EACCES`] Search permission is denied on a component of the path prefix, or the file exists and the permissions specified by mode are denied, or the file does not exist and write permission is denied for the parent directory of the file to be created.
[`EBADF`] The file descriptor underlying the stream is not a valid file descriptor when pathname is a null pointer.
    [`EINTR`] A signal was caught during `freopen()`.
    [`EISDIR`] The named file is a directory and <u>mode</u> requires write access.
    [`ELOOP`] A loop exists in symbolic links encountered during resolution of the <u>filename</u> argument.
    [`EMFILE`] All file descriptors available to the process are currently open.
    [`ENAMETOOLONG`] The length of a component of a <u>filename</u> is longer than {`NAME_MAX`}.
    [`ENFILE`] The maximum allowable number of files is currently open in the system.
    [`ENOENT`] The <u>mode</u> string begins with 'r' and a component of <u>filename</u> does not name an existing file, or <u>mode</u> begins with 'w' or 'a' and a component of the path prefix of pathname does not name an existing file, or pathname is an empty string.
    [`ENOENT`] or [`ENOTDIR`] The <u>filename</u> argument contains at least one non- <slash> character and ends with one or more trailing <slash> characters. If <u>filename</u> without the trailing <slash> characters would name an existing file, an [`ENOENT`] error does not occur.
    [`ENOSPC`] The directory or file system that would contain the new file cannot be expanded, the file does not exist, and it was to be created.
    [`ENOTDIR`] A component of the path prefix names an existing file that is neither a directory nor a symbolic link to a directory, or the <u>filename</u> argument contains at least one non- <slash> character and ends with one or more trailing <slash> characters and the last <u>filename</u> component names an existing file that is neither a directory nor a symbolic link to a directory.
    [`ENXIO`] The named file is a character special or block special file, and the device associated with this special file does not exist.
    [`EOVERFLOW`] The named file is a regular file and the size of the file cannot be represented correctly in an object of type `off_t`.
    [`EROFS`] The named file resides on a read-only file system and <u>mode</u> requires write access.
    [`EBADF`] The mode with which the file descriptor underlying the stream was opened does not support the requested mode when <u>filename</u> is a null pointer.
    [`EINVAL`] The value of the <u>mode</u> argument is not valid.
    [`ELOOP`] More than {`SYMLOOP_MAX`} symbolic links were encountered during resolution of the <u>file</u> argument.
    [`ENAMETOOLONG`] The length of a <u>filename</u> exceeds {`PATH_MAX`}, or pathname resolution of a symbolic link produced an intermediate result with a length that exceeds {`PATH_MAX`}.
    [`ENOMEM`] Insufficient storage space is available.
    [`ENXIO`] A request was made of a nonexistent device, or the request was outside the capabilities of the device.
    [`ETXTBSY`] The file is a pure procedure (shared text) file that is being executed and <u>mode</u> requires write access.

###Implementation tasks

 * Implement error handling for the function.