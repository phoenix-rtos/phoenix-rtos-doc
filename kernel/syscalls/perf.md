# Performance monitoring

## `syscalls_perfStart` (`syscalls_perf_start`)

````C
GETFROMSTACK(ustack, unsigned, pid, 0);
````

Starts performance monitoring for proces given by `pid`.

<br>

## `syscalls_perfRead` (`syscalls_perf_read`)

````C
GETFROMSTACK(ustack, void *, buffer, 0);
GETFROMSTACK(ustack, size_t, sz, 1);
````

Reads gathered performance monitoring events.

<br>

## `syscalls_perfFinish` (`syscalls_perf_finish`)

Finishes performance monitoring.
