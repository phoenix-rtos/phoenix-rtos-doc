# Exception reporting

Exception reporting records the HAL exception context, writes it to the console and standard error, and marks the
faulting thread for termination.
The implementation is centered on `process_dumpException()` and `process_exception()` in
`phoenix-rtos-kernel/proc/process.c`.

## Dump contents

`process_dumpException()` calls `hal_exceptionsDumpContext()` to format architecture-specific register state into a
fixed-size buffer.
It prints the same buffer to the kernel console and to file descriptor `2` with `posix_write()`.

After the HAL context dump, the function writes one of these source-derived location lines:

| Context | Reported data |
| --- | --- |
| User interrupt handler | Interrupt number, owning process path, and owning process ID. |
| Kernel thread | Kernel thread ID. |
| Process thread | Thread ID, process path, and process ID. |

The exact register dump format is architecture-specific because each HAL implementation provides its own
`hal_exceptionsDumpContext()`.

## Fault handling

`process_exception()` calls `process_dumpException()` for the current exception.
If the current thread has no process, the kernel halts the CPU.
For process threads, the handler posts `signal_kill`, sets `thread->exit` to `THREAD_END_NOW`, and reschedules so that
the thread does not return to user mode.

The virtual memory fault paths in `vm/map.c` also call `process_dumpException()` before reporting invalid mapping,
invalid address, or unaligned access cases.

## Undefined instructions

The HAL installs `process_illegal()` as the handler for `EXC_UNDEFINED`.
For process threads, that handler posts `signal_illegal` to the current thread.
If the exception occurs without a current process, the CPU is halted.
