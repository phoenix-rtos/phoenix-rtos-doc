###Synopsis
`#include <dirent.h>`

`int closedir(DIR *dirp);`

###Description

`closedir` closes the directory and frees the structure associated with <u>dirp</u> pointer.

Arguments:
<u>dirp</u> - a pointer to the directory structure

Upon return, the value of <u>dirp</u> does no longer point to an accessible object of the type `DIR`. A file descriptor used to implement type `DIR` is closed.

###Return value

Returns the value 0 upon successful completion, otherwise the value -1 is returned and `errno` set.

###Errors

[`EBADF`] - the <u>dirp</u> argument does not refer to an open directory stream.
[`EINTR`] - the closedir() function was interrupted by a signal. 

###Implementation tasks

* implement error handling and error return value