---
nosearch: True
---

# System calls

System call (commonly abbreviated to syscall) is an entry point to execute a specific user program's request to a
service from the kernel. The operating system kernel runs in a privileged mode to protect sensitive software and
hardware parts from the other software components. A user application executing in an unprivileged mode does not have
access to the protected data. Performing a hardware interrupt or conducting a trap handled by the kernel, the user
application can obtain sensitive data from the kernel, e.g. information about all processes running in the system.

## Prototypes and definition

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

## Adding syscall

An example of adding a system call is conducted based on the `threadsinfo` syscall. The procedure should be performed as
follows:

1. Add syscall's declaration in `libphoenix`, e.g. `libphoenix/inlude/sys/threads.h`:

    ```C
        extern int threadsinfo(int n, threadinfo_t *info);
    ```

2. Update the syscall list in `phoenix-rtos-kernel/include/syscalls.h`. It is recommended to insert a new syscall at the
end of the list:

    ```C
        ID(threadsinfo) \
    ```

3. Create a syscall handler in `phoenix-rtos-kernel/syscalls.c`:

    ```C
        int syscalls_threadsinfo(void *ustack)
        {
            int n, i;
            pid_t ppid;
            threadinfo_t *info;
    
            /* Get input arguments from stack according to order in the syscall prototype.
               GETFROMSTACK macro modifies value of stack pointer. The order of its invocation has to be compliant with arguments put on stack.
               GETFROMSTACK arguments:
                1st arg - stack pointer
                2nd arg - type of data put on stack
                3rd arg - variable name
                4th arg - id order on stack (start from 0) */
            GETFROMSTACK(ustack, int, n, 0);
            GETFROMSTACK(ustack, threadinfo_t *, info, 1);
    
            /* Get thread's list from kernel's submodule */
            n = proc_threadsList(n, info);
    
            /* Assign parent process id */
            for (i = 0; i < n; ++i) {
                if ((ppid = posix_getppid(info[i].pid)) > 0)
                    info[i].ppid = ppid;
            }
    
            return n;
        }
    ```

4. The system call can be invoked in user application by including `sys/threads.h` header. This example syscall is used
by the `ps` applet in the `psh` (Phoenix-Shell).

## See also

1. [Kernel](../README.md)
2. [System calls - Debug](debug.md)
3. [System calls - Memory management](mem.md)
4. [System calls - Processes management](proc.md)
5. [System calls - Threads management](threads.md)
6. [System calls - Threads synchronization](sync.md)
7. [System calls - Inter-process communication](ipc.md)
8. [System calls - File operations](file.md)
9. [System calls - Socket operations](socket.md)
10. [System calls - Interrupts management](interrupts.md)
11. [System calls - Performance monitoring](perf.md)
12. [System calls - Time management](time.md)
13. [System calls - Platform management](platform.md)
14. [System calls - RISC-V specific](riscv.md)
15. [Table of Contents](../../README.md)
