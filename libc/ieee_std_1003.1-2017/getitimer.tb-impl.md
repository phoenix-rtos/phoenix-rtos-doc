###Synopsis

`#include <sys/time.h>`

`int getitimer(int which, struct itimerval *value);`
`int setitimer(int which, const struct itimerval *restrict value,`
       `struct itimerval *restrict ovalue);`

###Description

The `getitimer()` and `setitimer()` functions get and set value of the interval timer.

Arguments:
    
<u>which</u> - the timer number.
<u>value</u> - a pointer to the structure saving the timer value.
<u>ovalue</u> - the previous value of the timer.

The `getitimer()` function stores the current value of the timer specified by <u>which</u> into the structure pointed to by <u>value</u>. 
The `setitimer()` function sets the timer specified by <u>which</u> to the value specified in the structure pointed to by <u>value</u>, and if <u>ovalue</u> is not a null pointer, stores the previous value of the timer in the structure pointed to by <u>ovalue</u>.

A timer value is defined by the `itimerval` structure, specified in `<sys/time.h>`. It includes the following members:

 * `struct timeval it_interval` ( timer interval: a value to be used in reloading it_value when the timer expires. )
 * `struct timeval it_value` (current value: the time to the next timer expiration)

Setting `it_value` to `0` disables a timer, regardless of the value of `it_interval`. 

Setting `it_interval` to `0` disables a timer after its next expiration (assuming `it_value` is non-zero).

For each interval timer, if the requested timer value requires a finer granularity than the implementation supports, the actual timer value is rounded up to the next supported value.

Each process is provided with three interval timers (defined in `<sys/time.h>`), which are indicated by the <u>which</u> argument:

 * `ITIMER_PROF` - decrements both in process virtual time and when the system is running on behalf of the process. It is designed to be used by interpreters in statistically profiling the execution of interpreted programs. Each time the `ITIMER_PROF` timer expires, the `SIGPROF` signal is delivered.
 * `ITIMER_REAL` - decrements in real time. A `SIGALRM` signal is delivered when this timer expires.
 * `ITIMER_VIRTUAL` - decrements in process virtual time. It runs only when the process is executing. A `SIGVTALRM` signal is delivered when it expires. 

###Return value

Upon successful completion, `0` is returned, otherwise  `-1` is returned and `errno` set to indicate the error.

###Errors

The `setitimer()` function fails if:

`[EINVAL]` The <u>value</u> argument is not in canonical form. (In canonical form, the number of microseconds is a non-negative integer less than `1000000` and the number of seconds is a non-negative integer.)

The `getitimer()` and `setitimer()` functions fail if:

`[EINVAL]` The <u>which</u> argument is not recognized.

###Implementation tasks

 * Put required definitions of interval timers to the `<sys/time.h>` file. 
 * Implement the `getitimer()` function.
 * Implement the `setitimer()` function.