###Synopsis

`#include <dirent.h>`

`int dirfd(DIR *dirp);`

###Description

The `dirfd()` function computes a file descriptor referring to the same directory as the <u>dirp</u> argument. This file descriptor is closed by a call to `closedir()`. 
The file descriptor, or the state of the associated description, can be modified only by: `closedir()`, `readdir()`, `readdir_r()`, `rewinddir()`, or `seekdir()`. After attempt to close this descriptor another way, the behaviour is undefined.

Arguments:
<u>dirp</u> - a pointer to the DIR data  structure.
 
###Return value

On success an integer containing a file descriptor for the directory pointed to by <u>dirp</u>,
otherwise `-1` is returned and `errno` set to indicate the error.

###Errors

[`EINVAL`] - the <u>dirp</u> argument does not refer to a valid directory stream.

###Implementation tasks

* Implement the `dirfd()` function.