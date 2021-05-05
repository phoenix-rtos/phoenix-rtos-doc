###Synopsis

`#include <unistd.h>`

`char *getcwd(char *buf, size_t size);`

###Description

The `getcwd()` function gets the pathname of the current working directory

Arguments:

<u>buf</u> - the result buffer, to which the pathname is put,
<u>size</u> - the size (in bytes) of the buffer.

The `getcwd()` function places an absolute pathname of the current working directory in the array pointed to by <u>buf</u>, and returns <u>buf</u>. The pathname contains no components that are dot or dot-dot, or are symbolic links.

If there are multiple pathnames that `getcwd()` could place in the array pointed to by <u>buf</u>, one beginning with a single <slash> character and one or more beginning with two <slash> characters, then `getcwd()` places the pathname beginning with a single <slash> character in the array. The pathname does not contain any unnecessary <slash> characters after the leading one or two <slash> characters.

The <u>size</u> argument is the size in bytes of the character array pointed to by the <u>buf</u> argument. If <u>buf</u> is a null pointer, the behavior of `getcwd()` is unspecified.

###Return value

Upon successful completion, `getcwd()` returns the <u>buf</u> argument. Otherwise, `getcwd()` returns a null pointer and sets `errno` to indicate the error. The contents of the array pointed to by <u>buf</u> are then undefined.

###Errors

[`EINVAL`] The <u>size</u> argument is 0. 
[`ERANGE`] The <u>size</u> argument is greater than 0, but is smaller than the length of the string +1. 
[`EACCES`] Search permission was denied for the current directory, or read or search permission was denied for a directory above the current directory in the file hierarchy.
[`ENOMEM`] Insufficient storage space is available. 

###Implementation tasks

* Implement error handling for the [`EACCES`] error.
