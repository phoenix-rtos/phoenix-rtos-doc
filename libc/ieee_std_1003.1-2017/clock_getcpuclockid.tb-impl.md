###Synopsis

`#include <time.h>`

`int clock_getcpuclockid(pid_t pid, clockid_t *clock_id);`

###Description

The `clock_getcpuclockid()` function returns the clock ID of the CPU-time clock of the process specified by <u>pid</u>. If the process described by <u>pid</u> exists and the calling process has permission, the clock ID of this clock shall be returned in <u>clock_id</u>.

Arguments:
<u>pid</u> - the ID of the process of interest,
<u>clock_id</u> - (output value) the CPU-time clock ID of the process making the call.

If <u>pid</u> is zero, the function returns the clock ID of the CPU-time clock of the process making the call, in <u>clock_id</u>.

###Return value

`0` on success, error number otherwise.

###Errors

[`EPERM`] - the requesting process does not have permission to access the CPU-time clock for the process.
[`ESRCH`] - no process can be found corresponding to the process specified by <u>pid</u>. 

###Implementation tasks
* Define the conditions under which one process has permission to obtain the CPU-time clock ID of other processes.
* Implement the function.

