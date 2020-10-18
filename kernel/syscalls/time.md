# Time management

## `syscalls_gettime`

````C
GETFROMSTACK(ustack, time_t *, praw, 0);
GETFROMSTACK(ustack, time_t *, poffs, 1);
````

Returns current time in `praw` and `poffs` variables.

## `syscalls_settime`

````C
GETFROMSTACK(ustack, time_t, offs, 0);
````

Setup system time to value given by `offs`.
