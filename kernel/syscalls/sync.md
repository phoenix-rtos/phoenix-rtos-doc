# Thread synchronization

## `syscalls_mutexCreate`

````C
GETFROMSTACK(ustack, unsigned int *, h, 0);
````

Creates mutex and returns resource handle `h`.

## `syscalls_phMutexLock`

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

## `syscalls_phCondWait`

````C
GETFROMSTACK(ustack, unsigned int, h, 0);
GETFROMSTACK(ustack, unsigned int, m, 1);
GETFROMSTACK(ustack, time_t, timeout, 2);
````

Waits on conditional given by 'h' for number of microseconds giveb by `timeout`. Before suspending a calling thread execution mutex identified by `m` handle is unlocked to enable other thread modifying variables used to check condtionals after conditional signalisation. When conditional variable is signaled mutex `m` is locked.

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