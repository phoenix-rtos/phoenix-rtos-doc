###Synopsis

`#include <grp.h>`

`void endgrent(void);`
`struct group *getgrent(void);`
`void setgrent(void);`

###Description

The functions operate on the group database, which contains for each users' group:

The `group` structure is defined in <`grp.h`> as follows:

           struct group {
               char   *gr_name;        /* group name */
               char   *gr_passwd;      /* group password */
               gid_t   gr_gid;         /* group ID */
               char  **gr_mem;         /* NULL-terminated array of pointers
                                          to names of group members */
           };

Arguments:
    
None.

The `getgrent()` function returns a pointer to a structure containing the broken-out fields of an entry in the group database. If the group database is not already open, `getgrent()` opens it and returns a pointer to a group structure containing the first entry in the database. Thereafter, it returns a pointer to a group structure containing the next group structure in the group database, so successive calls may be used to search the entire database.

The `setgrent()` function rewinds the group database so that the next `getgrent()` call returns the first entry, allowing repeated searches.

The `endgrent()` function closes the group database.

On error, the `setgrent()` and `endgrent()` functions set `errno` to indicate the error.

If you want to check for error situations, you should set `errno` to `0`, then call the function, then check `errno`.

These functions are not thread-safe.

###Return value

On success the `getgrent()` function returns a pointer to a `group` structure. On end-of-file, `getgrent()` returns a null pointer and does not change the setting of `errno`. On error, `getgrent()` returns a null pointer and `errno` is set to indicate the error.

The application does not modify the structure to which the return value points, nor any storage areas pointed to by pointers within the structure. The returned pointer, and pointers within the structure, might be invalidated or the structure or the storage areas might be overwritten by a subsequent call to `getgrgid()`, `getgrnam()`, or `getgrent()`. The returned pointer, and pointers within the structure, are invalidated if the calling thread is terminated.

###Errors

[`EINTR`] -  A signal was caught during the operation.
[`EIO`] - An I/O error has occurred.

[`EMFILE`] - All file descriptors available to the process are currently open.
[`ENFILE`] - The maximum allowable number of files is currently open in the system. 

###Implementation tasks

* Implement the `getgrent()` function.
* Implement the `endgrent()` function.
* Implement the `setgrent()` function.
