# Kernel - Processes and threads - Scheduler
The operating system scheduler controls threads execution with a predetermined policy. It is a part of Phoenix-RTOS having the most significant influence on the performance and responsiveness of the whole system.

## Scheduling policy
The scheduling algorithm is defined in the `threads_schedule` function. It is invoked by timer interrupt or voluntary reschedule (`hal_cpuReschedule`). Each function's invocation changes the context of the currently executed thread to the next one, available in a thread's ready queue. The scheduling policy determined which thread shall be chosen for the next execution. In Phoenix-RTOS a priority preempted round-robin algorithm is used. There are eight priority levels, the smallest value holds the highest priority.


The thread management unit contains an eight-element array, where each of them holds a pointer to the list of threads of the same priority. A scheduling algorithm is defined as follows:

1. The `threads_common.spinlock` is set before any operations on common data.
2. The current thread's context for the interrupted core is saved and added to the end of its priority list.
3. The next available thread with the highest priority is selected to be run and is removed from the ready thread list. If a selected thread is a ghost (a thread whose process has ended execution) and has not been executed in a supervisor mode, it is added to the ghosts list and the reaper thread is woke up.
4. For the selected thread, the following actions are performed:
    * a global pointer to the current thread is changed to the selected one,
    * a pointer to the kernel stack is updated to the stack of a new thread,
    * a memory map is changed to the map associated with the thread's process,
    * signal handlers are performed,
    * performance data is saved in a perf unit,
    * in the `hal_cpuRestore` pointer to the stack in a context of current thread is updated with a pointer to the stack of selected thread. When the scheduler finishes work, the context of selected thread restore is performed.
5. The cpu usage is updated for the current and selected thread.
6. At the end of the modification of the `threads_common.spinlock` is cleared.


## See also

1. [Kernel - Processes and threads](README.md)
2. [Kernel - Processes and threads - Management](forking.md)
3. [Kernel - Processes and threads - Synchronization primitives](scheduler.md)
4. [Kernel - Processes and threads - Message passing](msg.md)
5. [Kernel - Processes and threads - Namespace](namespace.md)
6. [Table of Contents](../../README.md)
