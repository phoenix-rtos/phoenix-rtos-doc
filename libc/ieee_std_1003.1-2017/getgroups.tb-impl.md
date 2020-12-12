###Synopsis

`#include <unistd.h>`

`int getgroups(int gidsetsize, gid_t grouplist[]);`

###Description

The `getgroups()` function gets supplementary group IDs.

Arguments:
    
<u>gidsetsize</u> - the number of elements in the array <u>grouplist</u>,
<u>grouplist</u> - the array with the current supplementary group IDs of the calling process.  

The `getgroups()` function fills in the array <u>grouplist</u> with the current supplementary group IDs of the calling process. The `getgroups()` function also returns the effective group ID in the <u>grouplist</u> array.

The <u>gidsetsize</u> argument specifies the number of elements in the array <u>grouplist</u>. The actual number of group IDs stored in the array is returned. The values of array entries with indices greater than or equal to the value returned are undefined.

If <u>gidsetsize</u> is `0`, `getgroups()` returns the number of group IDs that it would otherwise return without modifying the array pointed to by <u>grouplist</u>.

If the effective group ID of the process is returned with the supplementary group IDs, the value returned is always greater than or equal to one and less than or equal to the value of `{NGROUPS_MAX}+1`.

###Return value

The number of supplementary group IDs is returned on success. On error `-1` is returned and `errno` is set to indicate the error.

###Errors

[`EINVAL`]  The <u>gidsetsize</u> argument is non-zero and less than the number of group IDs that would have been returned.

###Implementation tasks

* Implement the `getgroups()` function.