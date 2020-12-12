###Synopsis

`#include <pwd.h>`

`void endpwent(void);`
`struct passwd *getpwent(void);`
`void setpwent(void);`

###Description

The functions retrieve information about users.

The information is stored in the user database which is a set of `passwd` structures defined in <`pwd.h`>:
    
    struct passwd {
	char  *pw_name; /* User's login name. */
	uid_t  pw_uid;  /* Numerical user ID. */
	gid_t  pw_gid;  /* Numerical group ID. */
	char  *pw_dir;  /* Initial working directory. */ 
	char  *pw_shell; /* Program to use as shell. */
	char  *pw_passwd;  /* User's password */
	char  *pw_gecos;   /* Other user's data separated by commas. */
};

Arguments:
    
None.


These functions retrieve information about users stored in the user database.

The `getpwent()` function returns a pointer to a structure containing the broken-out fields of an entry in the user database. Each entry in the user database contains a `passwd` structure. If the user database is not already open, `getpwent()` opens it and returns a pointer to a `passwd` structure containing the first entry in the database. Thereafter, it returns a pointer to a `passwd` structure containing the next entry in the user database. Successive calls can be used to search the entire user database.

The `setpwent()` function rewinds the user database so that the next `getpwent()` call returns the first entry, allowing repeated searches.

The `endpwent()` function closes the user database.

The `setpwent()` and `endpwent()` functions does not change the setting of `errno` if successful. On error, the functions set `errno` to indicate the error.

Since no value is returned by the `setpwent()` and `endpwent()` functions, an application wishing to check for error situations should set `errno` to `0`, then call the function, then check `errno`.

The application does not modify the structure to which the return value points, nor any storage areas pointed to by pointers within the structure. The returned pointer, and pointers within the structure, might be invalidated or the structure or the storage areas might be overwritten by a subsequent call to `getpwuid()`, `getpwnam()`, or `getpwent()`. The returned pointer, and pointers within the structure, might also be invalidated if the calling thread is terminated.

These functions are not thread-safe.

###Return value

On success the `getpwent()` returns a pointer to a `passwd` structure. On end-of-file, `getpwent()` returns a null pointer and does not change the setting of `errno`. On error, `getpwent()` returns a null pointer and `errno` is set to indicate the error.

###Errors

[`EINTR`] - A signal was caught during the operation.
[`EIO`] -   An I/O error has occurred.
[`EMFILE`] -  All file descriptors available to the process are currently open.
[`ENFILE`] -  The maximum allowable number of files is currently open in the system. 

###Implementation tasks

* Implement the `getpwent` function.
* Implement the `endpwent()` function.
* Implement the `setpwent()` function.
