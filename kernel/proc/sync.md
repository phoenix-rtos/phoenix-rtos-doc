# Kernel - Processes and threads - Synchronization primitives

Phoenix-RTOS kernel implements three widely used methods for synchronization of concurrently executed instruction streams.

## Spinlocks

Spinlocks are used for active synchronization of instruction streams executed parallely on multiple processing cores. They are implemented using special processor instructions allowing to atomically exchange value stored in processor register with a value stored in memory at specified linear address. These processor instructions belong to the class of so-called `set-and-test` instructions introduced especially for synchronization purposes. Their logic may a little-bit vary between specific processor architectures but the overall semantic remains consistent with atomic exchange between memory and processor register.


## Locks and mutexes

## Conditional variables


## See also

1. [Kernel - Processes and threads](README.md)
2. [Kernel - Processes and threads - Process creation](forking.md)
3. [Kernel - Processes and threads - Message passing](msg.md)
4. [Kernel - Processes and threads - Namespace](namespace.md)
5. [Table of Contents](../../README.md)

