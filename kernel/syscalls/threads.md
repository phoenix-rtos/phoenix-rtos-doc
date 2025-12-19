# Threads management

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
GETFROMSTACK(ustack, int, tid, 0);
GETFROMSTACK(ustack, unsigned int, flags, 1);
GETFROMSTACK(ustack, int, n, 2);
GETFROMSTACK(ustack, threadinfo_t *, info, 3);
````

Returns attributes of thread referred to by `tid`. Thread attributes to retrieve
are specified in `flags` and outputted to `info`.

`tid` can contain a special value `PH_THREADINFO_THREADS_ALL` which will make
`threadsinfo` target all, present at the time of invocation, threads in the system.
In this mode, `info` is treated as an array of `threadinfo_t`, with the number of
elements specified in `n`. Otherwise, `n` must be set to 1.

`flags` is a bitmask, with following flags available:

- `PH_THREADINFO_TID`

  Returns thread's ID for queried thread in `info.tid`.

- `PH_THREADINFO_PRIO`

  Returns priority for queried thread in `info.priority`.

- `PH_THREADINFO_STATE`

  Returns current state for queried thread in `info.state`.

- `PH_THREADINFO_LOAD`

  Returns current load for queried thread in `info.load`.

- `PH_THREADINFO_CPUTIME`

  Returns time spent executing on a CPU for queried thread in `info.cpuTime`.

- `PH_THREADINFO_WAITING`

  Returns time spent waiting for queried thread in `info.wait`.

- `PH_THREADINFO_NAME`

  Returns thread's name in `info.name`.

  The actual length of thread's name can be arbitrarily long, however, the returned
  name is capped at `sizeof(info.name)`.

- `PH_THREADINFO_VMEM`

  Returns the amount of mapped virtual memory in queried thread in `info.vmem`.

- `PH_THREADINFO_PPID`

  Returns parent PID for queried thread in `info.ppid`.

- `PH_THREADINFO_ALL`

  Returns all queryable attributes

- `PH_THREADINFO_OPT_THREADCOUNT`

  Causes `threadsinfo` to ignore arguments `n` and `info`, as well as rest of
  `flags` bits and returns amount of present threads in the system at the time
  of invocation in `threadsinfo` return value.

## `syscalls_threadGetID` (`syscalls_gettid`)

Returns identifier of calling thread.

## `syscalls_threadSetPriority` (`syscalls_priority`)

````C
GETFROMSTACK(ustack, int, priority, 0);
````
