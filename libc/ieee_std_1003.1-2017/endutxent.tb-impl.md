###Synopsis

`#include <utmpx.h>`

`void endutxent(void);`
`struct utmpx *getutxent(void);`
`struct utmpx *getutxid(const struct utmpx *id);`
`struct utmpx *getutxline(const struct utmpx *line);`
`struct utmpx *pututxline(const struct utmpx *utmpx);`
`void setutxent(void);`

###Description

The functions provide access to user accounting database.

The information is stored in the database which is a set of `utmpx` structures defined in <`utmpx.h`>:
    
            struct utmpx {
               char            ut_user[]; /* User login name. */
               char            ut_id[];    /* Unspecified initialization process identifier. */
               char            ut_line[];  /* Device name. */
               pid_t           ut_pid;     /* Process ID., pid_t defined as int */
               short           ut_type;    /* Type of entry. */
               struct timeval  ut_tv;      /* Time entry was made. */
           }

Arguments:
    
<u>id</u> - the structure to be searched,
<u>line</u> - utmpx structure which ut_line string is matched,
<u>utmpx</u> - the structure to be put to the database.

The `getutxent()` function reads the next entry from the user accounting database opening the database if it is required. If it reaches the end of the database, it fails.

The `getutxid()` function searches forward from the current point in the database. If the `ut_type` value of the `utmpx` structure pointed to by <u>id</u> is `BOOT_TIME`, `OLD_TIME`, or `NEW_TIME`, then it stops when it finds an entry with a matching `ut_type` value. If the `ut_type` value is `INIT_PROCESS`, `LOGIN_PROCESS`, `USER_PROCESS`, or `DEAD_PROCESS`, then it shall stop when it finds an entry whose type is one of these four and whose `ut_id` member matches the `ut_id` member of the `utmpx` structure pointed to by <u>id</u>. If the end of the database is reached without a match, `getutxid()` fails.

The `getutxline()` function searche forward from the current point in the database until it finds an entry of the type `LOGIN_PROCESS` or `USER_PROCESS` which also has a `ut_line` value matching that in the `utmpx` structure pointed to by <u>line</u>. If the end of the database is reached without a match, `getutxline()` fails.

The `getutxid()` or `getutxline()` function may cache data. For this reason, to use `getutxline()` to search for multiple occurrences, the application zeroes out the static data after each success, or `getutxline()` returns a pointer to the same `utmpx` structure.

There is one exception to the rule about clearing the structure before further reads are done. The implicit read done by `pututxline()` (if it finds that it is not already at the correct place in the user accounting database) are not modify the static structure returned by getutxent(), getutxid(), or getutxline(), if the application has modified this structure and passed the pointer back to pututxline().

For all entries that match a request, the `ut_type` member indicates the type of the entry. Other members of the entry contain meaningful data based on the value of the `ut_type` member as follows:

<table>
 <tr>
    <th>ut_type Member</th>
    <th>Other Members with Meaningful Data</th>
</tr>
<tr>
    <td>EMPTY</td>
    <td>No others</td>
</tr>
<tr>
    <td>BOOT_TIME</td>
    <td>ut_tv</td>
</tr>
<tr>
    <td>OLD_TIME</td>
    <td>ut_tv</td>
</tr>
<tr>
    <td>NEW_TIME</td>
    <td>ut_tv</td>
</tr>
<tr>
    <td>USER_PROCESS</td>            
    <td>ut_id, ut_user (login name of the user), ut_line, ut_pid, ut_tv</td>
</tr>
<tr>
    <td>INIT_PROCESS</td>
    <td>ut_id, ut_pid, ut_tv</td>
</tr>
<tr>
    <td>LOGIN_PROCESS</td>
    <td>ut_id, ut_user (name of the login process), ut_line, ut_pid, ut_tv</td>
</tr>
<tr>
    <td>DEAD_PROCESS</td>            
    <td>ut_id, ut_pid, ut_tv</td>
</tr>
</table>

If the process has appropriate privileges, the `pututxline()` function writes out the structure into the user accounting database. It searches for a record as if by `getutxid()` that satisfies the request. If this search succeeds, then the entry is replaced. Otherwise, a new entry is made at the end of the user accounting database.

The `endutxent()` function closes the user accounting database.

The `setutxent()` function resets the input to the beginning of the database. This should be done before each search for a new entry if it is desired that the entire database be examined.

These functions are not thread-safe.

###Return value

On success the `getutxent()`,`getutxid()` and `getutxline()` functions return a pointer to a `utmpx` structurecontaining a copy of the requested entry in the user accounting database, otherwise a null pointer is returned. 

The return value may point to a static area which is overwritten by a subsequent call to `getutxid()` or `getutxline()`.

Upon successful completion, `pututxline()` returns a pointer to a `utmpx` structure containing a copy of the entry added to the user accounting database. Otherwise, a null pointer is returned.

The `endutxent()` and `setutxent()` functions do not return a value.

###Errors

No errors are defined  for the `endutxent()`, `getutxent()`, `getutxid()`, `getutxline()`, and `setutxent()` functions.

The `pututxline()` function may fail if:

[`EPERM`] The process does not have appropriate privileges.  

###Implementation tasks

* Implement the `getutxent` function.
* Implement the `getservent()` function.
* Implement the `getutxid()` function.
* Implement the `getutxline()` function.
* Implement the `pututxline()` function.
* Implement the `setutxent()` function.
* Implement the `endutxent` function.
