# POSIX layer

The `libphoenix` repository provides POSIX API enabling users to build and run portable POSIX applications. The
emulation layer is built upon Phoenix-RTOS native messaging API and a dedicated server (`posixsrv`).

The purpose of `posixsrv` is to store data that can be shared between processes, i.e.:

- keep track of file descriptors and their mapping to open files,
- manage standard IPC mechanisms: pipes, UNIX sockets,
- provide UNIX 98 pseudo-terminals,
- dispatch events for efficient `poll()`-like functions

It also registers and handles special files, such as `/dev/null` or `/dev/random`.

In the current implementation, some parts of `posixsrv` functionality is kept inside the kernel and accessed using a set
of system calls. Future implementations will instead delegate requests directly to `posixsrv`.

The source code of `posixsrv` is available on GitHub and can be obtained using the following command:

```shell
git clone https://github.com/phoenix-rtos/phoenix-rtos-posixsrv.git
```

## Blocking operations are not interruptible

A POSIX call that blocks in `posixsrv` - `sem_wait()` on a named semaphore, a read from an
empty pipe or pseudo-terminal, an event queue wait - is a message send. The calling thread
parks inside `msgSend()` in the kernel's `msg_received` state, and that wait is deliberately
uninterruptible: the kernel message descriptor is allocated on the sender's kernel stack, so
the thread cannot be unwound while a server holds the request.

This is a known deviation from IEEE Std 1003.1-2017. For the affected calls:

- they never fail with `EINTR`, whatever signal is delivered;
- they are not cancellation points, although the standard lists them as such
  (XSH 2.9.5), so `pthread_cancel()` has no effect until the call returns;
- a thread blocked on a condition that never occurs cannot be killed, and the process
  cannot be terminated until the server answers.

The deviation is a property of the messaging layer, not of any individual server, so it
applies uniformly to every blocking POSIX operation that `posixsrv` implements.

## Scheduling priorities

The kernel uses native priorities in the range `[-NPRIOS/2, NPRIOS/2 - 1]` (`[-32, 31]` by default), where a smaller
value means a more critical thread (see [Thread priorities](../kernel/proc/scheduler.md#thread-priorities)). POSIX
requires the opposite: a greater value must mean a more critical thread. Many ported tools also assume that priorities
are non-negative.

Therefore, the `sched_*()` and `pthread_*()` functions take and return POSIX priorities in the range `[0, NPRIOS - 1]`
(`[0, 63]` by default), where `NPRIOS - 1` is the most critical. libphoenix maps between the two ranges as follows:

```text
posix = (NPRIOS/2 - 1) - native
```

| Native priority | POSIX priority | Criticality |
|-----------------|----------------|-------------|
| `-32`           | `63`           | highest     |
| `0`             | `31`           |             |
| `31`            | `0`            | lowest      |

This applies to:

- `sched_get_priority_min()`, `sched_get_priority_max()`,
- `sched_setparam()`, `sched_getparam()`,
- `pthread_attr_setschedparam()`, `pthread_attr_getschedparam()`,
- `pthread_setschedparam()`, `pthread_getschedparam()`, `pthread_setschedprio()`,
- `pthread_mutexattr_setprioceiling()`, `pthread_mutexattr_getprioceiling()`,
- `pthread_mutex_setprioceiling()`, `pthread_mutex_getprioceiling()`.

These functions fail with `EINVAL` when given a priority outside the POSIX range. Use `sched_get_priority_min()` and
`sched_get_priority_max()` instead of hardcoding the bounds, because `NPRIOS` is configurable in the kernel.

The native Phoenix-RTOS API, such as [`setPriority()`](functions/sys/threads/setPriority.phrtos.md),
[`getPriority()`](functions/sys/threads/getPriority.phrtos.md), `beginthread()` or `mutexCreateWithAttr()` from
`<sys/threads.h>`, still takes native priorities.

`SCHED_RR` is the only scheduling policy that the kernel supports. POSIX states that `SCHED_RR` threads are not
affected by the nice value, so `setpriority()`, `getpriority()` and `nice()` change nothing. `setpriority()` and
`getpriority()` only validate their arguments and check that the target process or process group exists. To change
the priority of a thread, use `sched_setparam()`, `pthread_setschedprio()` or, for a native priority, `setPriority()`.

`<sys/features.h>` defines two macros that ported code can test to choose the right API:

- `__PHOENIX_SCHED_PRIO_POSIX` - the `sched_*()` and `pthread_*()` functions take POSIX priorities. Older libphoenix
  versions, which don't define it, pass native priorities through unchanged.
- `__PHOENIX_NICE_IGNORED` - `setpriority()`, `getpriority()` and `nice()` don't change the priority. Older
  libphoenix versions, which don't define it, change the priority of the calling thread.

For example:

```c
#include <sys/resource.h>
#ifdef __PHOENIX_NICE_IGNORED
#include <sys/threads.h>
#endif

#ifdef __PHOENIX_NICE_IGNORED
  setPriority(prio);
#else
  setpriority(PRIO_PROCESS, 0, prio);
#endif
```

### Portable priority setting

The example below sets the priority of the calling thread to the native Phoenix-RTOS priority `prio`, in the range
`[-NPRIOS/2, NPRIOS/2 - 1]`, and builds on Linux as well:

- on Phoenix-RTOS with `setPriority()`, it calls `setPriority()`, which takes the native priority as is,
- on older Phoenix-RTOS, it calls the deprecated `priority()`, which every libphoenix version provides and which
  always took native priorities,
- on other systems, such as Linux, it does nothing, as Linux starts threads with `SCHED_OTHER`.

```c
#ifdef __phoenix__
#include <errno.h>
#include <sys/resource.h>
#include <sys/threads.h>
#endif

static int setNativePrio(int prio)
{
#if defined(__phoenix__) && defined(__PHOENIX_NICE_IGNORED)
  return setPriority(prio) < 0 ? -1 : 0;
#elif defined(__phoenix__)
  /* priority() takes native priorities on older libphoenix */
  return priority(prio) < 0 ? -1 : 0;
#else
  /* No-op on Linux */
  (void)prio;
  return 0;
#endif
}
```

Notes:

- `__PHOENIX_NICE_IGNORED` is used to detect `setPriority()`, because every libphoenix version that defines it
  also provides `setPriority()`. `<sys/resource.h>` includes `<sys/features.h>`, which defines the macro, so it has to
  be included before the check.
- `setPriority()` and `priority()` return a negative error code instead of setting `errno`.
- `priority()` is deprecated, so the older Phoenix-RTOS branch produces a deprecation warning when compiled against a
  libphoenix that lacks `__PHOENIX_NICE_IGNORED` but already marks `priority()` as deprecated.
- In libphoenix up to v3.3.2, `priority()` returns the current priority on success, hence the `err < 0` check. The
  kernel there accepts only `[0, 7]`, with `4` as the default. These values mean the same in the current range, so keep
  `prio` in `[0, 7]` when targeting such old versions.
