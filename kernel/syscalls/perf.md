# Performance monitoring

## `syscalls_perfStart` (`syscalls_perf_start`)

````C
GETFROMSTACK(ustack, unsigned, pid, 0);
````

Starts performance monitoring for process given by `pid`.

## `syscalls_perfRead` (`syscalls_perf_read`)

````C
GETFROMSTACK(ustack, void *, buffer, 0);
GETFROMSTACK(ustack, size_t, sz, 1);
````

Reads gathered performance monitoring events.

## `syscalls_perfFinish` (`syscalls_perf_finish`)

Finishes performance monitoring.

## See also

1. [System calls](syscalls.md)
2. [Table of Contents](../../README.md)
