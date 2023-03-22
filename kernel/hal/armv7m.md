# HAL for ARMv7 Cortex-M based targets

ARMv7m HAL layer supports microcontrollers based on ARM Cortex-Mx architecture. Source code is located in `hal/armv7m` directory.

## Initialization

>
    _init_vectors:
    .word _end + 1024 + 256
    .word _start

First two words on memory address 0x00000000 define initial stack and code entrypoint. Stack is set at the end of BSS + size of the stack.

>
    .word _exceptions_dispatch /* NMI */
    .word _exceptions_dispatch /* HardFault */
    .word _exceptions_dispatch /* MemMgtFault */
    .word _exceptions_dispatch /* BusFault */
    .word _exceptions_dispatch /* UsageFault */
    .word 0
    .word 0
    .word 0
    .word 0
    .word _exceptions_dispatch /* SVC */
    .word _exceptions_dispatch /* Debug */
    .word 0
    .word _interrupts_dispatch /* PendSV */
    .word _interrupts_dispatch /* Systick */
    (..)

Next memory part defines exception and interrupt handlers.

>
    _start:
      cpsid if
      bl _stm32_init
      ldr r0, =_edata
      bl main

## See also

1. [Kernel - HAL Subsystem](README.md)
2. [Kernel - HAL for ARMv7 Cortex-A based targets](armv7a.md)
3. [Kernel - HAL for IA32 targets](ia32.md)
4. [Kernel - HAL for RISC-V 64 based targets](riscv64.md)
5. [Kernel - HAL for SPARCv8 LEON3 based targets](sparcv8leon3.md)
6. [Table of Contents](../../README.md)
