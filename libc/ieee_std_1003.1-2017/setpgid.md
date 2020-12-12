### Synopsis
`#include <unistd.h>`

`int setpgid(pid_t pid, pid_t pgid);`

###Description

`setpgid()` sets the process group of the specified process `pid` to the specified `pgid`.  If `pid` is zero, then the call applies to the current process.

If the invoker is not the super-user, then the affected process must have the same effective user-id as the invoker or be a descendant of the invoking process.

###Return value

###Errors