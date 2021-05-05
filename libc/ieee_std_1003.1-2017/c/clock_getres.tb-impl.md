###Synopsis

`#include <time.h>`

`int clock_getres(clockid_t clock_id, struct timespec *res);`
`int clock_gettime(clockid_t clock_id, struct timespec *tp);`
`int clock_settime(clockid_t clock_id, const struct timespec *tp);`

###Description

The `clock_getres()` function calculates the resolution of the given clock unless the <u>res</u> argument is `NULL`.
The `clock_gettime()` function gets the time value (pointed to by <u>tp</u>) of the specified clock.
The `clock_settime()` function sets the specified clock to the specified value (pointed to by <u>tp</u>). Time values that are between two consecutive non-negative integer multiples of the resolution of the specified clock shall be truncated down to the smaller multiple of the resolution. If the <u>time</u> argument of `clock_settime()` is not a multiple of <u>res</u>, then the value is truncated to a multiple of <u>res</u>.

Arguments:
<u>clock_id</u> - the ID of the specified clock.
<u>res</u> - the resolution (implementation defined)of the given clock,
<u>tp</u> - the pointer to the suitable `timespec` structure.

A <u>clock_id</u> of `CLOCK_REALTIME` is defined in <`time.h`>. This clock represents the clock measuring real time for the system. For this clock, the values returned by `clock_gettime()` and specified by `clock_settime()` represent the amount of time (in seconds and nanoseconds) since the begining of the `Epoch`. An implementation may also support additional clocks. The interpretation of time values for these clocks is unspecified.

If the value of the `CLOCK_REALTIME` clock is set via `clock_settime()`, the new value of the clock is used to determine the time of expiration for absolute time services based upon the `CLOCK_REALTIME` clock. This applies to the time at which armed absolute timers expire. If the absolute time requested at the invocation of such a time service is before the new value of the clock, the time service expires immediately as if the clock had reached the requested time normally.

Setting the value of the `CLOCK_REALTIME` clock via `clock_settime()` has no effect neither on threads that are blocked waiting for a relative time service based upon this clock (including the `nanosleep()` function), nor on the expiration of relative timers based upon this clock. Consequently, these time services shall expire when the requested relative interval elapses, independently of the new or old value of the clock.`CLOCK_REALTIME` as defined in <`time.h`>. This clock represents the clock measuring real time for the system. For this clock, the values returned by `clock_gettime()` and specified by `clock_settime()` represent the amount of time (in seconds and nanoseconds) since the Epoch. An implementation may also support additional clocks. The interpretation of time values for these clocks is unspecified.

While the `Monotonic Clock` option is supported, the implementation supports a <u>clock_id</u> of `CLOCK_MONOTONIC` defined in <`time.h`>. This clock represents the monotonic clock for the system. For this clock, the value returned by `clock_gettime()` represents the amount of time (in seconds and nanoseconds) since the Epoch. This point does not change after system start-up time. The value of the `CLOCK_MONOTONIC` clock cannot be set via `clock_settime()`, which will fail being invoked with a <u>clock_id</u> argument of `CLOCK_MONOTONIC`.

If the value of the `CLOCK_REALTIME` clock is set via `clock_settime()`, the new value of the clock is used to determine the time at which the system awakes a thread blocked on an absolute `clock_nanosleep()` call based upon the `CLOCK_REALTIME` clock. If the absolute time requested at the invocation of such a time service is before the new value of the clock, the call returns immediately as if the clock had reached the requested time normally.

Setting the value of the `CLOCK_REALTIME` clock via `clock_settime()` has no effect on any thread that is blocked on a relative `clock_nanosleep()` call. Consequently, the call returns when the requested relative interval elapses, independently of the new or old value of the clock.

While `_POSIX_CPUTIME` is defined, implementation supports `clock ID` values obtained by invoking `clock_getcpuclockid()`, which represent the CPU-time clock of a given process. Implementation also supports the special `clockid_t` value `CLOCK_PROCESS_CPUTIME_ID`, which represents the CPU-time clock of the calling process when invoking one of the `clock_*`() or `timer_*`() functions. For these clock IDs, the values returned by `clock_gettime()` and specified by `clock_settime()` represent the amount of execution time of the process associated with the clock. Changing the value of a CPU-time clock via `clock_settime()` has no effect on the behavior of the sporadic server scheduling policy.

If `_POSIX_THREAD_CPUTIME` is defined, implementation supports:
 * `clock ID`  values obtained by invoking `pthread_getcpuclockid()`, which represent the CPU-time clock of a given thread,
 * `CLOCK_THREAD_CPUTIME_ID` ( the special `clockid_t` value ), which represents the CPU-time clock of the calling thread when invoking one of the `clock_*()` or `timer_*()` functions. For these clock IDs, the values returned by `clock_gettime()` and specified by `clock_settime()` represent the amount of execution time of the thread associated with the clock. Changing the value of a CPU-time clock via `clock_settime()` has no effect on the behavior of the sporadic server scheduling policy.

###Return value

`0` on success, `-1` otherwise (`errno` is then set to indicate the corresponding error).

###Errors

[`EINVAL`] - the clock_id argument does not specify a known clock.

[`EOVERFLOW`] (for the `clock_gettime()` function) - the number of seconds will not fit in an object of type `time_t`.

[`EINVAL`] (for the `clock_settime()` function)
    *  The <u>tp</u> argument to `clock_settime()` is outside the range for the given clock ID.
    *  The <u>tp</u> argument specified a nanosecond value less than zero or greater than or equal to `1000` million.
    *  The value of the <u>clock_id</u> argument is `CLOCK_MONOTONIC`. 

[`EPERM`] (for the `clock_settime()` function) - the requesting process does not have appropriate privileges to set the specified clock. 

###Implementation tasks

While implementing the functions you must make the following decisions (define appropriate constants): 
  * Decide if the clock is visible to all processes or per-process (measuring time that is meaningful only within a process). 
  * Define the clock resolution
  * Decide if additional clocks are supported and, if yes, how their time values would be interpreted.
  * Decide what would be the effect of setting a clock via `clock_settime()` on armed per-process timers associated with a clock other than `CLOCK_REALTIME` (if there are any).
  * Define privileges that are needed to set a particular clock.
  * Decide if `_POSIX_CPUTIME` is defined.
  * Decide if `_POSIX_THREAD_CPUTIME` is defined.