# Thread management

## `syscalls_threadCreate` (`syscalls_beginthread`)

````C
GETFROMSTACK(ustack, void *, start, 0);
GETFROMSTACK(ustack, unsigned int, priority, 1);
GETFROMSTACK(ustack, void *, stack, 2);
GETFROMSTACK(ustack, unsigned int, stacksz, 3);
GETFROMSTACK(ustack, void *, arg, 4);
GETFROMSTACK(ustack, unsigned int *, id, 5);
````

Starts thread from entry point given by `start` at priority defined by `priority`. Thread stack is defined by `stack`
and `stacksz` arguments. Executed thread ID is returned in `id` variable.

## `syscalls_threadDestroy` (`syscalls_endthread`)

Terminates executing thread.

## `syscalls_threadWait` (`syscalls_threadJoin`)

````C
GETFROMSTACK(ustack, time_t, timeout, 0);
````

## `syscalls_threadSleep` (`syscalls_usleep`)

````C
GETFROMSTACK(ustack, unsigned int, us, 0);
````

Suspends thread execution for number of microseconds defined by `us`.

## `syscalls_threadGetInfo` (`syscalls_threadinfo`)

````C
GETFROMSTACK(ustack, int, n, 0);
GETFROMSTACK(ustack, threadinfo_t *, info, 1);
````

Returns thread information `info` for thread given by `n`.

## `syscalls_threadGetID` (`syscalls_gettid`)

Returns identifier of calling thread.

## `syscalls_threadSetPriority` (`syscalls_priority`)

````C
GETFROMSTACK(ustack, int, priority, 0);
````

## See also

1. [System calls](index.md)
2. [Table of Contents](../../index.md)
