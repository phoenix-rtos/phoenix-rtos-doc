# Scheduler

The operating system scheduler controls threads execution with a predetermined policy. It is a part of Phoenix-RTOS
having the most significant influence on the performance and responsiveness of the whole system.

## Scheduling policy

The scheduling algorithm is defined in the `_threads_schedule` function. It is invoked by timer interrupt or voluntary
reschedule (`hal_cpuReschedule`). Phoenix-RTOS uses a priority-preempted round-robin algorithm with 64 priority levels
(`NPRIOS`), described in [Thread priorities](#thread-priorities).

The thread management unit contains an `NPRIOS`-element array where each element holds a pointer to the list of threads
at that priority level. A 64-bit bitmask (`readyBitmask`) tracks which queues are non-empty, allowing O(1) selection of
the highest-priority ready thread (`_readyMinPrioIdx` finds the first set bit of the bitmask halves using
`hal_cpuGetFirstBit`). The scheduling algorithm is as follows:

1. `threads_common.spinlock` is held by the caller (`threads_schedule()`) before any operations on shared data.
2. The current thread's context for the interrupted core is saved and added to the end of its priority queue.
3. The next highest-priority ready thread is selected and removed from its ready
   queue. If a selected thread is a ghost (its process has ended and it has not
   been executing in supervisor mode), it is added to the ghosts list and the
   reaper thread is woken up.
4. For the selected thread:
    * the current-thread pointer is updated,
    * the kernel stack pointer is updated,
    * the address space is switched to the thread's process memory map,
    * pending signal handlers are invoked,
    * `hal_cpuRestore` switches to the selected thread's context.
5. Wait-time statistics are updated for both the preempted and selected threads.
6. `threads_common.spinlock` is cleared by the caller after `_threads_schedule()` returns.

## Thread priorities

The thread priority is a signed value (`priority_t`, defined in `proc/threads.h`) taken from the range
`[MIN_PRIO, MAX_PRIO]`, where `MIN_PRIO` equals `-NPRIOS / 2` and `MAX_PRIO` equals `NPRIOS / 2 - 1`. For the default
`NPRIOS` of 64 the range is therefore `[-32, 31]`. **The lower the numeric value, the higher the criticality of the
thread**: a thread at `MIN_PRIO` (-32) preempts every other thread, while a thread at `MAX_PRIO` (31) is scheduled only
when no other thread is ready.

The range is deliberately centered around zero instead of spanning `[0, NPRIOS - 1]`. Userspace code has historically
used the `[0, 7]` range with 4 (`PH_PRIO_DEFAULT`) as the default thread priority, so keeping those values in place and
extending the range in both directions relaxes the contention around the default priority without the need to rescale
existing code.

`NPRIOS` can be overridden at build time. It must be even and not lower than 16, and it must fit in `readyBitmask`,
which currently limits it to 64 levels. Lowering it is a way to reduce the size of the ready queue array on
memory-constrained targets.

Each thread carries two priorities:

* `priorityBase` - the priority requested for the thread (by `beginthreadex()` or `sys_priority()`),
* `priority` - the effective priority the scheduler uses.

The effective priority is the more critical (numerically lower) of `priorityBase` and the priority derived from the
locks the thread currently holds, so priority inheritance (`PH_LOCK_PROTO_INHERIT`) and the priority ceiling protocol
(`PH_LOCK_PROTO_PRIOCEILING`) can only raise a thread's criticality, never lower it below its base level.

Userspace should not hardcode the priority range. It is reported at runtime by the `schedInfo()` call (and by the POSIX
`sched_get_priority_min()` and `sched_get_priority_max()` wrappers) for the `SCHED_RR` policy.
