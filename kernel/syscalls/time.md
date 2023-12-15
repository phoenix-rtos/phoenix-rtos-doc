# Time management

## `syscalls_timeGet` (`syscalls_gettime`)

````C
GETFROMSTACK(ustack, time_t *, praw, 0);
GETFROMSTACK(ustack, time_t *, poffs, 1);
````

Set `praw` to system time in microseconds from system boot. Set `poffs` to
offset configured in `syscalls_timeSet`. Unused arguments can be set to NULL.

## `syscalls_timeSet` (`syscalls_settime`)

````C
GETFROMSTACK(ustack, time_t, offs, 0);
````

Set offset value returned from `syscalls_timeSet`. This is shared between all
processes. It is not used for system time calculations so value interpretation
is not specified here. Default offset on boot is `0`.

## See also

1. [System calls](README.md)
2. [Table of Contents](../../README.md)

