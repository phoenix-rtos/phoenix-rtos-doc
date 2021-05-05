###Synopsis

`include <time.h>`

`int clock_nanosleep(clockid_t clock_id, int flags,
       const struct timespec *rqtp, struct timespec *rmtp); `

###Description

The function executes the high resolution sleep for the specified clock.

Arguments:

<u>clock_id</u> - the identifier of the clock under interest,
<u>flags</u> - flags defining the way of action of the function,
<u>rqtp</u> - the requested time interval (to sleep),
<u>rmtp</u> - the `timespec` structure specifying the actual amount of time remaining in the specified time interval.

The action of the function depends of the value of the flag `TIMER_ABSTIME` in <u>flags</u> argument.

   *  The flag `TIMER_ABSTIME` is not set - the function causes the current thread to be suspended until either the time interval specified by the <u>rqtp</u> argument has elapsed, or a signal is delivered to the calling thread and its action is to invoke a signal-catching function, or the process is terminated. The clock used to measure the time is the clock specified by <u>clock_id</u>.
   *  The flag `TIMER_ABSTIME` is set - the function causes the current thread to be suspended until one of beneath conditions is fulfilled:
        * the time value of the clock specified by <u>clock_id</u> reaches the absolute time specified by the <u>rqtp</u> argument,
        * a signal is delivered to the calling thread and its action is to invoke a signal-catching function, 
        * the process is terminated. 
    If, at the time of the call, the time value specified by <u>rqtp</u> is less than or equal to the time value of the specified clock, then `clock_nanosleep()` shall return immediately and the calling process shall not be suspended.

  The suspension time caused by this function may be longer than requested because the argument value is rounded up to an integer multiple of the sleep resolution, or because of the scheduling of other activity by the system. But, except for the case of being interrupted by a signal, the suspension time for the relative `clock_nanosleep()` function (that is, with the `TIMER_ABSTIME` flag not set) shall not be less than the time interval specified by <u>rqtp</u>, as measured by the corresponding clock. The suspension for the absolute clock_nanosleep() function (that is, with the  `TIMER_ABSTIME` flag set) shall be in effect at least until the value of the corresponding clock reaches the absolute time specified by <u>rqtp</u>, except for the case of being interrupted by a signal.

The `clock_nanosleep()` function does not block any signal.

If the <u>clock_id</u> argument refers to the CPU-time clock of the calling thread, the `clock_nanosleep()` function fails. 

###Return value

`0` - the requested time elapsed.

The corresponding error value, when:
   * the function fails,
   * the function was interrupted by a signal,
   * if the <u>rmtp</u> argument is non-NULL, the `timespec` structure referenced by it is updated to contain the amount of time remaining in the interval (the requested time minus the time actually slept). The <u>rqtp</u> and <u>rmtp</u> arguments can point to the same object. If the <u>rmtp</u> argument is `NULL`, the remaining time is not returned. The absolute `clock_nanosleep()` function has no effect on the structure referenced by <u>rmtp</u>.

###Errors

[`EINTR`] - the `clock_nanosleep()` function was interrupted by a signal.

[`EINVAL`] 
    - the <u>rqtp</u> argument specified a nanosecond value less than zero or greater than or equal to `1000` million; 
     - the `TIMER_ABSTIME` flag was specified in flags and the <u>rqtp</u> argument is outside the range for the clock specified by <u>clock_id</u>; or the <u>clock_id</u> argument does not specify a known clock, or specifies the CPU-time clock of the calling thread.

[`ENOTSUP`] - the <u>clock_id</u> argument specifies a clock for which `clock_nanosleep()` is not supported, such as a CPU-time clock. 

###Implementation tasks

* Decide whether <u>clock_id</u> values of other CPU-time clocks are allowed.
* Implement the function.

###Tests

======

###EXAMPLES




