# Adding syscall

An example of adding a system call is conducted based on the `threadsinfo` syscall. The procedure should be performed as
follows:

1. Add syscall's declaration in `libphoenix`, e.g. `libphoenix/inlude/sys/threads.h`:

    ```c
    extern int threadsinfo(int n, threadinfo_t *info);
    ```

2. Update the syscall list in `phoenix-rtos-kernel/include/syscalls.h`. It is recommended to insert a new syscall at the
end of the list:

    ```c
    ID(threadsinfo) \
    ```

3. Create a syscall handler in `phoenix-rtos-kernel/syscalls.c`:

    ```c
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
