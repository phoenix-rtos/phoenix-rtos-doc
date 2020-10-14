# Interrupts

It is often necessary to handle hardware interrupts when creating device driver. To enable user space server to do so, Phoenix-RTOS provides special callback mechanism. Driver registers interrupt handler via syscall:

````C
    int interrupt(unsigned int n, int (*f)(unsigned int, void *), void *arg, unsigned int cond, unsigned int *handle);
````
where:

- <b>n</b> is platform dependent interrupt number,
- <b>f</b>  is an interrupt handler,
- <b>arg</b>  is passed to the handler during call,
- <b>cond</b>  is handle to conditional,
- <b>handle</b>  points to variable which will hold new interrupt handle.

Interrupt syscall registers callback function to be executed when the interrupt number <b>n</b>  occurs and enables (if not enabled already) this interrupt in the controller.

Callback function is invoked directly from the kernel space with interrupts globally disabled. It allows handler to be able to prevent the same interrupt to be executed again (e.g. when interrupt is caused by signal level, not edge).

If handler returns value > 0 then kernel performs <i>condSignal()</i> on a conditional passed when registering interrupt. If this feature is not needed, one can pass 0 as <i>cond</i>.