###Synopsis

`#include <grp.h>`

`struct group *getgrgid(gid_t gid);`

`int getgrgid_r(gid_t gid, struct group *grp, char *buffer,
       size_t bufsize, struct group **result);`

###Description

The `getgrgid()` and `getgrgid_r()` functions return the group database entry for the group ID. 

Arguments:
    
<u>gid</u> - the group ID,
<u>grp</u> - a pointer to the group structure,  
<u>buffer</u> - a pointer to the memory provided,  
<u>bufsize</u> - a size of the provided memory,
<u>result</u> - the updated group structure.

The `getgrgid()` function searches the group database for an entry with a matching <u>gid</u>. The `getgrgid()` function is not thread-safe.

To check for error situations you must set `errno` to `0` before calling `getgrgid()`. If `getgrgid()` returns a null pointer and `errno` is set to non-zero, an error occurred.

The `getgrgid_r()` function updates the group structure pointed to by <u>grp</u> and stores a pointer to that structure at the location pointed to by <u>result</u>. The structure contains an entry from the group database with a matching <u>gid</u>. Storage referenced by the group structure is allocated from the memory provided with the <u>buffer</u> parameter, which is <u>bufsize</u> bytes in size. A call to `sysconf(_SC_GETGR_R_SIZE_MAX)` returns either `-1` without changing `errno` or an initial value suggested for the size of this buffer. A null pointer is returned at the location pointed to by <u>result</u> on error or if the requested entry is not found.

The `getgrgid_r()` function is thread-safe and returns values in a user-supplied buffer instead of possibly using a static data area that may be overwritten by each call.

Portable applications should take into account that it is usual for an implementation to return `-1` from `sysconf()` indicating that there is no maximum for `_SC_GETGR_R_SIZE_MAX`.

###Return value

Upon successful completion, `getgrgid()` returns a pointer to a `struct group` with the structure defined in `<grp.h>` with a matching entry if one is found. The `getgrgid()` function returns a null pointer if either the requested entry was not found, or an error occurred. If the requested entry was not found, `errno` is not changed. On error, `errno` is set to indicate the error.

The application does not modify the structure to which the return value points, nor any storage areas pointed to by pointers within the structure. The returned pointer, and pointers within the structure, might be invalidated or the structure or the storage areas might be overwritten by a subsequent call to `getgrent()`, `getgrgid()`, or `getgrnam()`. The returned pointer, and pointers within the structure, might also be invalidated if the calling thread is terminated.

If successful, the `getgrgid_r()` function returns zero; otherwise, an error number is returned to indicate the error.

###Errors

[`EIO`]  An I/O error has occurred.
[`EINTR`] A signal was caught during `getgrgid()`.
[`EMFILE`] All file descriptors available to the process are currently open.
[`ENFILE`] The maximum allowable number of files is currently open in the system.

The `getgrgid_r()` function fails if:

[`ERANGE`] Insufficient storage was supplied via <u>buffer</u> and <u>bufsize</u> to contain the data to be referenced by the resulting `group` structure.

###Implementation tasks

* Implement the `getgrgid()` function.
* Implement the `getgrgid_r()` function.