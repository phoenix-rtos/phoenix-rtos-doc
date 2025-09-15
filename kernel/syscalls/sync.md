# Threads synchronization

## `syscalls_phMutexCreate`

````C
GETFROMSTACK(ustack, handle_t *, h, 0);
GETFROMSTACK(ustack, const struct lockAttr *, attr, 1);
````

Creates mutex and returns resource handle `h`. Mutex attributes are specified in `attr` structure.

Libc wrappers:

- [`int phMutexCreate(handle_t *h, const struct lockAttr *attr)`](
../../libc/functions/sys/threads/mutexCreateWithAttr.phrtos.md)

- [`int mutexCreateWithAttr(handle_t *h, const struct lockAttr *attr)`](
../../libc/functions/sys/threads/mutexCreateWithAttr.phrtos.md)

- [`int mutexCreate(handle_t *h)`](
../../libc/functions/sys/threads/mutexCreate.phrtos.md)

## `syscalls_mutexLock` (`syscalls_phMutexLock`)

````C
GETFROMSTACK(ustack, handle_t, h, 0);
````

Locks mutex given by handle `h`. If it is already locked, blocks until it becomes available.

Libc wrappers:

- [`int mutexLock(handle_t h)`](
../../libc/functions/sys/threads/mutexLock.phrtos.md)

- [`int phMutexLock(handle_t h)`](
../../libc/functions/sys/threads/mutexLock.phrtos.md)

## `syscalls_mutexTry`

````C
GETFROMSTACK(ustack, handle_t, h, 0);
````

Tries once to lock mutex given by handle `h`. If it is already locked, fails with -EBUSY.

Libc wrapper:
[`int mutexTry(handle_t h)`](
../../libc/functions/sys/threads/mutexTry.phrtos.md)

## `syscalls_mutexUnlock`

````C
GETFROMSTACK(ustack, handle_t, h, 0);
````

Unlocks mutex given by `h`.

Libc wrapper:
[`int mutexUnlock(handle_t h)`](
../../libc/functions/sys/threads/mutexUnlock.phrtos.md)

## `syscalls_phCondCreate`

````C
GETFROMSTACK(ustack, handle_t *, h, 0);
GETFROMSTACK(ustack, const struct condAttr *, attr, 1);
````

Creates conditional variable and returns its handle in variable `h`. Conditional variable attributes are specified in
`attr` structure.

Libc wrappers:

- [`int condCreate(handle_t *h)`](
../../libc/functions/sys/threads/condCreate.phrtos.md)

- [`int phCondCreate(handle_t *h, const struct condAttr *attr)`](
../../libc/functions/sys/threads/condCreateWithAttr.phrtos.md)

- [`int condCreateWithAttr(handle_t *h, const struct condAttr *attr)`](
../../libc/functions/sys/threads/condCreateWithAttr.phrtos.md)

## `syscalls_condWait` (`syscalls_phCondWait`)

````C
GETFROMSTACK(ustack, handle_t, h, 0);
GETFROMSTACK(ustack, handle_t, m, 1);
GETFROMSTACK(ustack, time_t, timeout, 2);
````

Waits on conditional given by 'h' for number of microseconds given by `timeout`. Before suspending a calling thread
execution mutex identified by `m` handle is unlocked to enable other thread modifying variables used to
check conditionals after conditional signalization. When conditional variable is signaled mutex `m` is locked.

Libc wrapper:
[`int condWait(handle_t h, handle_t m, time_t timeout)`](
../../libc/functions/sys/threads/condWait.phrtos.md)

## `syscalls_condSignal`

````C
GETFROMSTACK(ustack, handle_t, h, 0);
````

Signals conditional given by `h` to at least one waiting thread.

Libc wrapper:
[`int condSignal(handle_t h)`](
../../libc/functions/sys/threads/condSignal.phrtos.md)

## `syscalls_condBroadcast`

````C
GETFROMSTACK(ustack, handle_t, h, 0);
````

Signals conditional given by `h` to all waiting threads.

Libc wrapper:
[`int condBroadcast(handle_t h)`](
../../libc/functions/sys/threads/condSignal.phrtos.md)

## `syscalls_resourceDestroy`

````C
GETFROMSTACK(ustack, handle_t, h, 0);
````

Deletes the resource given by `h` from process. Has additional effects depending on the resource.

Libc wrapper:
[`int resourceDestroy(handle_t h)`](
../../libc/functions/sys/threads/resourceDestroy.phrtos.md)
