###Synopsis
`#include <sys/stat.h>`

`int fstat(int fildes, struct stat *buf);`

###Description

The `fstat()` function obtains information about an open file associated with the file descriptor <u>fildes</u>, and writes it to the area pointed to by <u>buf</u>.
   
Arguments:

<u>fildes</u> - the file descriptor of the file of interest.
<u>buf</u>  - the buffer for results.

If <u>fildes</u> references a shared memory object, the implementation updates in the `stat` structure pointed to by the <u>buf</u> argument the `st_uid`, `st_gid`, `st_size`, and `st_mode` fields, and only the `S_IRUSR`, `S_IWUSR`, `S_IRGRP`, `S_IWGRP`, `S_IROTH`, and `S_IWOTH` file permission bits need be valid. 

If <u>fildes</u> references a typed memory object, the implementation updates in the `stat` structure pointed to by the <u>buf</u> argument the `st_uid`, `st_gid`, `st_size`, and `st_mode` fields, and only the `S_IRUSR`, `S_IWUSR`, `S_IRGRP`, `S_IWGRP`, `S_IROTH`, and `S_IWOTH` file permission bits need be valid.

The <u>buf</u> argument is a pointer to a `stat` structure, as defined in <`sys/stat.h`>, into which concerning the file information is placed.

The `fstat()` function updates any time-related fields, before writing into the `stat` structure.

###Return value

Upon successful completion, `0` is returned. Otherwise, `-1` is returned and `errno` set to indicate the error.

###Errors

[`EBADF`] The <u>fildes</u> argument is not a valid file descriptor.
[`EIO`] An I/O error occurred while reading from the file system.
[`EOVERFLOW`] The file size in bytes or the number of blocks allocated to the file or the file serial number cannot be represented correctly in the structure pointed to by <u>buf</u>.
[`EOVERFLOW`] One of the values is too large to store into the structure pointed to by the <u>buf</u> argument.

###Implementation tasks
 
* Implement error handling for `fstat()`