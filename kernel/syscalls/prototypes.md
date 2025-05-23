# Prototypes and definition

In Phoenix-RTOS prototypes and definitions of the system calls are located in the `libphoenix` library. A list of
all system calls is placed in a `phoenix-rtos-kernel/include/syscalls.h` header files, grouped by categories.

System call prototypes should be placed in the appropriate header file in the `libphoenix` standard library,
referring to the syscall's category.
System call definitions are placed in the `arch/$(TARGET_SUFF)/syscalls.S` file and are created based on a syscall list
via macro. Each definition triggers an exception (e.g. Supervisor Call - SVC instruction for ARM Cortex-M or Cortex-A)
with an appropriate syscall identification number handled by the kernel in the privileged mode. Arguments are passed
according to the target platform ABI (Application Binary Interface).

Handler definitions for system calls are located in the `phoenix-rtos-kernel/syscalls.c` file. Each handler should
contain an appropriate return type consistent with the prototype in `libphoenix` (in practice `int`) and take the user
stack pointer as an argument. The syscall's parameters can be obtained from the user stack using the macro
`GETFROMSTACK(stack_ptr, arg_type, var, id)`.

Phoenix-RTOS in kernel mode has access to the calling process memory, so the pointer to the data in the user space can
be passed as an argument to system call and used in the kernel space.
