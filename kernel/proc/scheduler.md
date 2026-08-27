# Scheduler

The operating system scheduler controls threads execution with a predetermined policy. It is a part of Phoenix-RTOS
having the most significant influence on the performance and responsiveness of the whole system.

## Scheduling policy

The scheduling algorithm is defined in the `_threads_schedule` function. It is invoked by timer interrupt or voluntary
reschedule (`hal_cpuReschedule`). Phoenix-RTOS uses a priority-preempted round-robin algorithm with 64 priority levels
(`NPRIOS`). The priority range is `[-32, 31]`: `MIN_PRIO` (-32) is the highest criticality; `MAX_PRIO` (31) is the
lowest.

The thread management unit contains a 64-element array where each element holds a pointer to the list of threads at
that priority level. A 64-bit bitmask (`readyBitmask`) tracks which queues are non-empty, allowing O(1) selection of
the highest-priority ready thread (e.g. via `__builtin_ctzll`). The scheduling algorithm is as follows:

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
