# getgroups

## Synopsis

`#include <unistd.h>`

`int getgroups(int gidsetsize, gid_t grouplist[]);`

## Status

Declared, not implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `getgroups()` function shall fill in the array _grouplist_ with the current supplementary group IDs of the calling
 process. It is implementation-defined whether `getgroups()` also returns the effective group ID in the _grouplist_
array.

The _gidsetsize_ argument specifies the number of elements in the array _grouplist_. The actual number of group IDs
stored in the array shall be returned. The values of array entries with indices greater than or equal to the value
returned are undefined.

If _gidsetsize_ is 0, `getgroups()` shall return the number of group IDs that it would otherwise return without
modifying the array pointed to by _grouplist_.

If the effective group ID of the process is returned with the supplementary group IDs, the value returned shall always
be greater than or equal to one and less than or equal to the value of `NGROUPS_MAX`+1.

## Return value

Upon successful completion, the number of supplementary group IDs shall be returned. A return value of -1 indicates
failure and errno shall be set to indicate the error.

## Errors

The `getgroups()` function shall fail if:

* `EINVAL` - The _gidsetsize_ argument is non-zero and less than the number of group IDs that would have been returned.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../index.md)
2. [Table of Contents](../../../index.md)
