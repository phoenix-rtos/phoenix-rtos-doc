###Synopsis

`#include <unistd.h>`

`char *crypt(const char *key, const char *salt);`

###Description

The `crypt()` function is a string encoding function.

Arguments:
<u>key</u> - a string to be encoded.
<u>salt</u> - a string of at least two bytes in length not including the null character chosen from the set of letters (small and capital), digits, point and slash.

The first two bytes of the salt string are used to perturb the encoding algorithm.

The return value of `crypt()` points to static data that is overwritten by each call.

The use of `crypt()` for anything other than password hashing is not recommended.
 
###Return value

On success this function returns a pointer to the encoded string. The first two bytes of the returned value are those of the salt argument. 
Otherwise, the function returns a null pointer and sets `errno` to indicate the error.

###Errors

[`ENOSYS`] - The functionality is not supported on this implementation. 

###Implementation tasks
* Implement error detection.