# Toolchain

Feniks-RTOS provides its toolchain, based on GNU CC. It's divided into the following parts

- arm-feniks
- i386-pc-feniks
- riscv64-feniks
- sparc-feniks
- aarch64-feniks

Each part delivers the tools required to compile the given architecture simply.
There are a few reasons why that is helpful

- You can easily compile source code for a given Feniks-RTOS platform, for example, ia32-generic-qemu:

  ```console
  i386-pc-feniks-gcc helloworld.c
  ```

- You don't need to use many of the compiler switches

- You can check if a program is compiled for Feniks-RTOS or not, using `feniks` or `__feniks__` flag

```c
#ifdef feniks
    #warning OS is Feniks-RTOS
#endif
```

## See also

1. [Building Feniks-RTOS image](index.md)
2. [Building script](script.md)
3. [Reference project](project.md)
4. [Table of Contents](../index.md)
