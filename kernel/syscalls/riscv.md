# RISC-V specific

RISC-V-specific syscall IDs expose legacy SBI console calls to user space.
The kernel HAL implements the broader SBI firmware interface in `phoenix-rtos-kernel/hal/riscv64/sbi.c`.

## `syscalls_sbiPutChar` (`syscalls_sbi_putchar`)

````C
GETFROMSTACK(ustack, char, c, 0);
````

## `syscalls_sbiGetChar` (`syscalls_sbi_getchar`)

Calls the legacy SBI getchar service and returns its result.

## SBI services used by the HAL

The HAL uses SBI for firmware-backed RISC-V services:

| SBI extension | Use |
| --- | --- |
| `SBI_EXT_BASE` | SBI version and implementation discovery. |
| `SBI_EXT_TIME` | Timer programming. |
| `SBI_EXT_SRST` | System reset. |
| `SBI_EXT_IPI` | Inter-hart interrupts. |
| `SBI_EXT_HSM` | Hart state management. |
| `SBI_EXT_RFENCE` | Remote instruction and address-translation fences. |

Only `sbi_putchar` and `sbi_getchar` appear in the public syscall table.
The remaining SBI functions are HAL-internal services used for timers, reset, multicore startup, IPIs, and fences.
