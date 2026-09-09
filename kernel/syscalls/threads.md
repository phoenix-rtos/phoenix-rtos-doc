# Threads management

## `syscalls_threadCreate` (`syscalls_beginthread`)

````C
GETFROMSTACK(ustack, void *, start, 0);
GETFROMSTACK(ustack, int, priority, 1);
GETFROMSTACK(ustack, void *, stack, 2);
GETFROMSTACK(ustack, unsigned int, stacksz, 3);
GETFROMSTACK(ustack, void *, arg, 4);
GETFROMSTACK(ustack, unsigned int *, id, 5);
````

Starts thread from entry point given by `start` at priority defined by `priority`. Thread stack is defined by `stack`
and `stacksz` arguments. Executed thread ID is returned in `id` variable.

The `priority` argument is signed and must fall into the `[MIN_PRIO, MAX_PRIO]` range, otherwise `-EINVAL` is returned.
See [Thread priorities](../proc/scheduler.md#thread-priorities) for the description of the priority range.

Libc wrappers: `beginthreadex()` and `beginthread()`, both declared in `sys/threads.h`.

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

## `syscalls_sys_priority`

````C
GETFROMSTACK(ustack, int, val, 0);
GETFROMSTACK(ustack, int *, res, 1);
````

Sets the base priority of the calling thread to `val` and, if `res` is not `NULL`, stores the resulting base priority
in `res`. When `val` equals `PH_GET_PRIO`, the priority is left untouched and only retrieved, in which case `res` must
not be `NULL`. `val` other than `PH_GET_PRIO` must fall into the `[MIN_PRIO, MAX_PRIO]` range, otherwise `-EINVAL` is
returned. See [Thread priorities](../proc/scheduler.md#thread-priorities) for the description of the priority range.

Because priorities are signed, the priority is reported through `res` instead of the return value - otherwise legal
negative priorities would be indistinguishable from error codes. On success `EOK` is returned.

Libc wrappers:

- [`int sys_priority(int val, int *res)`](
../../libc/functions/sys/threads/sys_priority.phrtos.md)

- [`int setPriority(int val)`](
../../libc/functions/sys/threads/setPriority.phrtos.md)

- [`int getPriority(void)`](
../../libc/functions/sys/threads/getPriority.phrtos.md)

- [`int priority(int val)`](
../../libc/functions/sys/threads/priority.phrtos.md) (deprecated)
