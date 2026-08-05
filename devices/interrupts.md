# Handling interrupts

It is often necessary to handle hardware interrupts when creating a device driver. To enable the userspace server to do
so, Phoenix-RTOS provides a special callback mechanism. Driver registers interrupt handler via syscall:

````C
int interrupt(unsigned int n, int (*f)(unsigned int, void *), void *arg,
              unsigned int cond, unsigned int *handle);
````

where:

- _`n`_ - is platform dependent interrupt number,
- _`f`_ - is an interrupt handler,
- _`arg`_ - is passed to the handler during call,
- _`cond`_ - is handle to conditional (or interrupt queue, see below),
- _`handle`_ - points to variable which will hold new interrupt handle.

Interrupt syscall registers callback function to be executed when the interrupt number `n`  occurs and enables (if not
enabled already) this interrupt in the controller.

The callback function is invoked directly from the kernel space with interrupts globally disabled. It allows the handler
to be able to prevent the same interrupt to be executed again (e.g. when an interrupt is caused by the signal level, not
edge).

If handler returns value >= 0 then kernel performs `condBroadcast()` on a conditional passed when registering
interrupt. If this feature is not needed, one can pass 0 as _`cond`_.

To unregister the interrupt, `resourceDestroy()` should be called on the _`handle`_ variable.

## Interrupt queues

A regular conditional variable requires a mutex to be held while calling `condWait()`. When a thread only waits for an
interrupt to be signaled, such a mutex protects nothing, introduces a performance penalty, allocates unnecessary
resources and obscures the code. For this reason libphoenix provides a set of thin wrappers declared in
`<sys/interrupt.h>`, which present the conditional passed to `interrupt()` as an _interrupt queue_:

- [`interrupt_queueCreate()`](../libc/functions/sys/interrupt/interrupt_queueCreate.phrtos.md) - creates a queue that
  is waited on without any mutex,
- [`interrupt_queueCreateLocked()`](../libc/functions/sys/interrupt/interrupt_queueCreateLocked.phrtos.md) - creates a
  queue that is waited on with a mutex held,
- [`interrupt_queueWait()`](../libc/functions/sys/interrupt/interrupt_queueWait.phrtos.md) - waits on a queue created
  with `interrupt_queueCreate()`,
- [`interrupt_queueWaitLocked()`](../libc/functions/sys/interrupt/interrupt_queueWaitLocked.phrtos.md) - waits on a
  queue created with `interrupt_queueCreateLocked()`,
- [`interrupt_queueSignal()`](../libc/functions/sys/interrupt/interrupt_queueSignal.phrtos.md) - wakes up a thread
  waiting on a queue from the thread context,
- [`interrupt_queueBroadcast()`](../libc/functions/sys/interrupt/interrupt_queueBroadcast.phrtos.md) - wakes up all
  threads waiting on a queue from the thread context.

The handle returned by either of the create functions is passed as the _`cond`_ argument of `interrupt()`, so an
interrupt queue may be used instead of a normal conditional variable.

```{note}
The unlocked queue may only be used when exactly one thread waits for the interrupt. If multiple threads wait on the
same interrupt, or the predicate checked after the wake-up is shared between threads, the locked version
(`interrupt_queueCreateLocked()` together with `interrupt_queueWaitLocked()`) must still be used.

With an unlocked queue, the predicate is the only synchronization with the interrupt handler. When the predicate is
already true, the waiter never enters the kernel, so no memory barrier is executed.
```

A typical usage looks as follows:

````C
#include <stdatomic.h>
#include <sys/interrupt.h>

static handle_t queue;
static handle_t irq;
static atomic_int irqFlag;

static int irq_handler(unsigned int n, void *arg)
{
    /* acknowledge/mask the interrupt here */
    irqFlag = 1;
    /* return >= 0 to wake up the queue */
    return 0;
}

void driver_init(void)
{
    interrupt_queueCreate(&queue, PH_CLOCK_RELATIVE);
    interrupt(IRQ_NUMBER, irq_handler, NULL, queue, &irq);
}

void driver_thread(void)
{
    for (;;) {
        while (atomic_exchange(&irqFlag, 0) == 0) {  
            interrupt_queueWait(queue, 0);
        }
        /* handle the interrupt */
    }
}
````
