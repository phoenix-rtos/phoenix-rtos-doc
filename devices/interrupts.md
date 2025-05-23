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
- _`cond`_ - is handle to conditional,
- _`handle`_ - points to variable which will hold new interrupt handle.

Interrupt syscall registers callback function to be executed when the interrupt number `n`  occurs and enables (if not
enabled already) this interrupt in the controller.

The callback function is invoked directly from the kernel space with interrupts globally disabled. It allows the handler
to be able to prevent the same interrupt to be executed again (e.g. when an interrupt is caused by the signal level, not
edge).

If handler returns value >= 0 then kernel performs `condSignal()` on a conditional passed when registering interrupt. If
this feature is not needed, one can pass 0 as _`cond`_.
