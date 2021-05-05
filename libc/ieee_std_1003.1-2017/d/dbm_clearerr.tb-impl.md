###Synopsis

`#include <ndbm.h>`

`int dbm_clearerr(DBM *db);`
`void dbm_close(DBM *db);`
`int dbm_delete(DBM *db, datum key);`
`int dbm_error(DBM *db);`
`datum dbm_fetch(DBM *db, datum key);`
`datum dbm_firstkey(DBM *db);`
`datum dbm_nextkey(DBM *db);`
`DBM *dbm_open(const char *file, int open_flags, mode_t file_mode);`
`int dbm_store(DBM *db, datum key, datum content, int store_mode);`

###Description

The functions operate on key-value databases consisting of `datum` structures including the following members:

`void   *dptr` - a pointer to the application's data (of any type: binary as well as character strings). 
`size_t  dsize` - the size of the object pointed to by `dptr`. 
 
Arguments:
<u>db</u> - a pointer to the database.

<u>key</u> - a structure with the database element.
<u>file</u> - a pathname to the file containing the database.
<u>open_flags</u> - flags for a file opening.
<u>file_mode</u> - a file access mode.

<u>content</u> - a structure with element to be put to the database.
<u>store_mode</u> - a mode of the insertion of the record ( new - `DBM_INSERT`, existing - `DBM_REPLACE`)controls whether `dbm_store()` replaces any pre-existing record that has the same key that is specified by the <u>key</u> argument. The application sets <u>store_mode</u> to either `DBM_INSERT` or `DBM_REPLACE`. If the database contains a record that matches the <u>key</u> argument and <u>store_mode</u> is `DBM_REPLACE`, the existing record is replaced with the new record. If the database contains a record that matches the <u>key</u> argument and <u>store_mode</u> is `DBM_INSERT`, the existing record is left unchanged and the new record is ignored. If the database does not contain a record that matches the <u>key</u> argument and <u>store_mode</u> is either `DBM_INSERT` or `DBM_REPLACE`, the new record is inserted in the database.
 
A database is stored in the file, which name is formed by appending the suffix `.db` to the <u>file</u> argument given to `dbm_open()`. 
Its internal block size is `1024` bytes.

The `dbm_open()` function opens or creates a database located in the <u>file</u> without extension(`pathname` of the database). The <u>open_flags</u> control whether database can be read from, written to or both. 
The file pathname need not be longer then {`PATH_MAX`}-`4` bytes (including the terminating null), or its last component need not be longer than {`NAME_MAX`}-`4` bytes (excluding the terminating null).

The `dbm_close()` function closes a database. The application ensures that argument <u>db</u> is a pointer to a `dbm` structure that has been returned from a call to `dbm_open()`.

The `dbm_fetch()` function reads a record from a database. The argument <u>db</u> is a pointer to a database structure returned from a call to `dbm_open()`. The argument <u>key</u> is a datum that has been initialized by the application to the value of the <u>key</u> that matches the key of the record the program is fetching.

The `dbm_store()` function writes a record to a database. The argument <u>db</u> is a pointer to a database structure that has been returned from a call to `dbm_open()`. The argument <u>key</u> is a `datum` that has been initialized by the application to the value of the key that identifies (for subsequent reading, writing, or deleting) the record the application is writing. The argument content is a `datum` that has been initialized by the application to the value of the record the program is writing. The argument <u>store_mode</u> controls whether `dbm_store()` replaces any pre-existing record that has the same key that is specified by the <u>key</u> argument. The application sets <u>store_mode</u> to either `DBM_INSERT` or `DBM_REPLACE`. If the database contains a record that matches the <u>key</u> argument and <u>store_mode</u> is `DBM_REPLACE`, the existing record is replaced with the new record. If the database contains a record that matches the <u>key</u> argument and <u>store_mode</u> is `DBM_INSERT`, the existing record is left unchanged and the new record is ignored. If the database does not contain a record that matches the <u>key</u> argument and <u>store_mode</u> is either `DBM_INSERT` or `DBM_REPLACE`, the new record is inserted in the database.

If the sum of a <u>key</u> / <u>content</u> pair exceeds the internal block size, the result is unspecified. Moreover, the application ensures that all <u>key</u> / <u>content</u> pairs that hash together fit on a single block. The `dbm_store()` function returns an error in the event that a disk block fills with inseparable data.

The `dbm_delete()` function deletes the record and its key from the database. The argument <u>db</u> is a pointer to a database structure that has been returned from a call to `dbm_open()`. The argument <u>key</u> is a datum that has been initialized by the application to the value of the key that identifies the record the program is deleting.

The `dbm_firstkey()` function returns the first key in the database. The argument <u>db</u> is a pointer to a database structure that has been returned from a call to `dbm_open()`.

The `dbm_nextkey()` function returns the next key in the database. The argument <u>db</u> is a pointer to a database structure that has been returned from a call to `dbm_open()`. The application ensures that the `dbm_firstkey()` function is called before calling `dbm_nextkey()`. Subsequent calls to `dbm_nextkey()` return the next key until all of the keys in the database have been returned.

The `dbm_error()` function returns the error condition of the database. The argument <u>db</u> is a pointer to a database structure that has been returned from a call to `dbm_open()`.

The `dbm_clearerr()` function clears the error condition of the database. The argument <u>db</u> is a pointer to a database structure that has been returned from a call to `dbm_open()`.

The `dptr` pointers returned by these functions point into static storage that may be changed by subsequent calls.

These functions are not thread-safe.

###Return value

The `dbm_store()` function returns `0` when it succeeds and a negative value when it fails. It returns `1` if it is called with a <u>flags</u> value of `DBM_INSERT` and the function finds an existing record with the same key.
The `dbm_delete()` function returns `0` when it succeeds and a negative value when it fails.
The `dbm_error()` function  returns `0` if the error condition is not set and returns `1` if the error condition is set.
The return value of `dbm_clearerr()` is `0`.
The `dbm_firstkey()` and `dbm_nextkey()` functions  return a key `datum`. When the end of the database is reached, the `dptr` member of the key is a null pointer. If an error is detected, the `dptr` member of the key  is a null pointer and the error condition of the database is set.
The `dbm_fetch()` function  returns a content `datum`. If no record in the database matches the <u>key</u> or if an error condition has been detected in the database, the `dptr` member of the content is a null pointer.
The `dbm_open()` function  returns a pointer to a database structure. If an error is detected during the operation, `dbm_open()` returns a `(DBM *)0`.

###Errors

No errors are defined.

###Examples

Traversing the database:
for(key = dbm_firstkey(db); key.dptr != NULL; key = dbm_nextkey(db));

###Implementation tasks
* Define the `DBM` and `datum` types.
* Define the `<ndbm.h>` file
* Implement the functions.