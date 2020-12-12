###Synopsis

`#include <grp.h>`

`struct group *getgrnam(const char *name);`
`int getgrnam_r(const char *name, struct group *grp, char *buffer,
       size_t bufsize, struct group **result);`

###Description

The `getgrnam()` and `getgrnam_r()` functions return the group database entry for the group name. 

Arguments:
    
<u>name</u> - the group name,
<u>grp</u> - a pointer to the group structure,  
<u>buffer</u> - a pointer to the memory provided,  
<u>bufsize</u> - a size of the provided memory,
<u>result</u> - the updated group structure.

The `getgrnam()` function searches the group database for an entry with a matching name. It is not thread-safe.

Applications wishing to check for error situations should set `errno` to `0` before calling `getgrnam()`. If `getgrnam()` returns a null pointer and `errno` is set to non-zero, an error occurred.

The `getgrnam_r()` function updates the group structure pointed to by <u>grp</u> and stores a pointer to that structure at the location pointed to by <u>result</u>. The structure contains an entry from the group database with a matching name. Storage referenced by the `group` structure is allocated from the memory provided with the <u>buffer</u> parameter, which is <u>bufsize</u> bytes in size. A call to `sysconf(_SC_GETGR_R_SIZE_MAX)` returns either `-1` without changing `errno` or an initial value suggested for the size of this buffer. A null pointer is returned at the location pointed to by <u>result</u> on error or if the requested entry is not found.

The `getgrnam_r()` function is thread-safe and returns values in a user-supplied <u>buffer</u> instead of possibly using a `static` data area that may be overwritten by each call.

###Return value

The `getgrnam()` function returns a pointer to a struct `group` with the structure defined in `<grp.h>` with a matching entry if one is found. The `getgrnam()` function returns a null pointer if either the requested entry was not found, or an error occurred. If the requested entry was not found, `errno` is not changed. On error, `errno` is set to indicate the error.

The application does not modify the structure to which the return value points, nor any storage areas pointed to by pointers within the structure. The returned pointer, and pointers within the structure, might be invalidated or the structure or the storage areas might be overwritten by a subsequent call to `getgrent()`, `getgrgid()`, or `getgrnam()`. If the calling thread is terminated, the returned pointer, and pointers within the structure, might also be invalidated .

The `getgrnam_r()` function returns zero on success or if the requested entry was not found and no error has occurred. If any error has occurred, an error number is returned to indicate the error.

###Errors

[`EIO`]  An I/O error has occurred.
[`EINTR`] A signal was caught during ``getgrnam()``.
[`EMFILE`] All file descriptors available to the process are currently open.
[`ENFILE`] The maximum allowable number of files is currently open in the system.

The `getgrnam_r()` function fails if:

[`ERANGE`] Insufficient storage was supplied via <u>buffer</u> and <u>bufsize</u> to contain the data to be referenced by the resulting `group` structure.

###Implementation tasks

* Implement the `getgrnam()` function.
* Implement the `getgrnam_r()` function.