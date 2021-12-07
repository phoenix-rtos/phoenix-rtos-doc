# Toolchain

Phoenix-RTOS provides its toolchain, based on GNU CC. It's divided into the following parts

- arm-phoenix
- i386-pc-phoenix
- riscv64-phoenix

Each part delivers the tools required to compile for the given architecture simply.
There are a few reasons why that is helpful

- You can easily compile source code for a given Phoenix-RTOS platform, for example, ia32-generic:

  ```bash
  i386-pc-phoenix-gcc helloworld.c
  ```

- You don't need to use many of the compiler switches

- You can check if a program is compiled for Phoenix-RTOS or not, using `phoenix` or `__phoenix__` flag

```c
#ifdef phoenix
    #warning OS is Phoenix-RTOS
#endif
```

## See also

1. [Phoenix-RTOS building script](script.md)
2. [Phoenix-RTOS reference project repository](project.md)
3. [Table of Contents](../README.md)

