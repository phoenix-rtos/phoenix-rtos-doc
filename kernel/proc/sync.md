# Synchronization primitives

Phoenix-RTOS kernel implements three widely used methods for synchronization of concurrently executed instruction
streams.

## Spinlocks

Spinlocks are used in kernel for active synchronization of instruction streams executed in parallel on multiple
processing cores. They are implemented using special processor instruction allowing to atomically exchange value stored
in processor register with a value stored in a memory at specified linear address. This processor instruction belongs
to the class of so-called `test-and-set` instructions introduced especially for synchronization purposes. Their logic
may slightly vary between specific processor architectures, but the overall semantics remains consistent with atomic
exchange between memory and processor register.

Spinlocks are the basic method of synchronization used to implement mechanisms based on the thread scheduling. They are
used to synchronizing access to scheduler thread lists or to synchronize access before thread scheduler is initialized
or when data is shared among threads and interrupt handlers.

Spinlock logic is quite simple. When program tries to enter into the critical section which should be executed
exclusively by only one instruction stream it checks the spinlock value in memory by exchanging it with the value 0
meaning that access to the critical section has been granted. If the spinlock value read from memory and swapped
atomically with 0 was greater than 0, processor can start the further instruction stream execution. If not it should
repeat previous exchange until it checks that access was not granted before the check (spinlock value gathered from
memory during the swap was 1).

Spinlocks are widely used to synchronize memory access between synchronous code executed as main instruction stream and
asynchronous code executed as interrupt/exception handlers so before spinlock `test-and-set` operation, interrupts on
the current processing core should be disabled and the processor state connected with interrupt handling should be
preserved.

Overall spinlock lock implementation has been presented below in C using preprocessor macros to represent blocks of
processor-specific assembly code.

```c
    SAVE_INTERRUPTS_STATE(CURRENT_CPU, state);
    DISABLE_INTERRUPTS;

    while (!TEST_AND_SET(0, spinlock));
```

Spinlock unlocking operation is quite simple. Processor atomically changes spinlock value in memory to non-zero and
restores its interrupt state based on state saved in spinlock. It is worth adding that operation on spinlock should
save and restore processor state from the variable assigned specifically for this particular processor.

```c
    TEST_AND_SET(1, spinlock);
    RESTORE_INTERRUPTS_STATE(CURRENT_CPU, state);
```

## Locks and mutexes

Locks are used to synchronize access to critical sections inside kernel using scheduling mechanism. The main difference
between locks and spinlocks is that they use passive waiting (removal from scheduler queues) instead of active waiting
(iterations until spinlock value becomes non-zero). Locks can be used only when process subsystem is initialized and
scheduler is working.

Each lock consists of spinlock, state variable and waiting queue.

## Conditional variables
