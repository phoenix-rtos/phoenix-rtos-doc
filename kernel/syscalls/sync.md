# Thread synchronization

## `syscalls_mutexCreate`

````C
GETFROMSTACK(ustack, unsigned int *, h, 0);
````

Creates mutex and returns resource handle `h`.

## `syscalls_mutexLock` (`syscalls_phMutexLock`)

````C
GETFROMSTACK(ustack, unsigned int, h, 0);
````

Locks mutex given by handle `h`.

## `syscalls_mutexTry`

````C
GETFROMSTACK(ustack, unsigned int, h, 0);
````

Tries to lock mutex given by handle `h`.

## `syscalls_mutexUnlock`

````C
GETFROMSTACK(ustack, unsigned int, h, 0);
````

Unlocks mutex given by `h`.

## `syscalls_condCreate`

````C
GETFROMSTACK(ustack, unsigned int *, h, 0);
````

Creates conditional variable and returns its handle in variable `h`.

## `syscalls_condWait` (`syscalls_phCondWait`)

````C
GETFROMSTACK(ustack, unsigned int, h, 0);
GETFROMSTACK(ustack, unsigned int, m, 1);
GETFROMSTACK(ustack, time_t, timeout, 2);
````

Waits on conditional given by 'h' for number of microseconds given by `timeout`. Before suspending a calling thread
execution mutex identified by `m` handle is unlocked to enable other thread modifying variables used to
check conditionals after conditional signalization. When conditional variable is signaled mutex `m` is locked.

Libc wrapper:
[int condWait(handle_t h, handle_t m, time_t timeout)](../../libc/functions/sys/threads/condWait.phrtos.md)

## `syscalls_condSignal`

````C
GETFROMSTACK(ustack, unsigned int, h, 0);
````

Signals conditional given by `h`.

## `syscalls_condBroadcast`

````C
GETFROMSTACK(ustack, unsigned int, h, 0);
````

Signals conditional to all waiting threads.

## See also

1. [System calls](syscalls.md)
2. [Table of Contents](../../README.md)
