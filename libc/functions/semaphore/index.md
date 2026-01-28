# semaphore.h

## Description

This header contains interfaces to standard POSIX semaphores.

`libphoenix` implements named and unnamed semaphores; both of which are
'fair' such that if a thread "up's" a semaphore, which is currently waited on
by more than one thread, the waiting threads are woken up with respect to the
first-in, first-out order of semaphore "down's".

## Notes

* Unnamed semaphores are a kernel resource which is process bound, meaning that
   they cannot be shared between different processes.

* Named semaphores are implemented as a part of POSIX emulation server.
   They are created as character devices in `/dev/posix/sem` directory.

## Functions

```{toctree}
:maxdepth: 1
:glob:

*
```
