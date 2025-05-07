# System calls

System call (commonly abbreviated to syscall) is an entry point to execute a specific user program's request to a
service from the kernel. The operating system kernel runs in a privileged mode to protect sensitive software and
hardware parts from the other software components. A user application executing in an unprivileged mode does not have
access to the protected data. Performing a hardware interrupt or conducting a trap handled by the kernel, the user
application can obtain sensitive data from the kernel, e.g. information about all processes running in the system.

```{toctree}
:maxdepth: 1

prototypes.md
add.md
debug.md
mem.md
proc.md
threads.md
sync.md
ipc.md
file.md
socket.md
interrupts.md
perf.md
time.md
platform.md
riscv.md
```
