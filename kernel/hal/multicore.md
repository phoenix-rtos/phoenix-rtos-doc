# Multicore synchronization

Multicore synchronization combines HAL spinlocks, interrupt control, processor barriers, and inter-processor
interrupts (IPIs).
The kernel does not publish a separate userspace memory model in these sources.
The documented guarantees here describe source-visible kernel mechanisms.

## Spinlocks and barriers

Kernel subsystems use `hal_spinlockSet()` and `hal_spinlockClear()` around shared data structures such as scheduler,
interrupt, timer, process, VM, and device state.
The exact primitive is architecture-specific:

| Architecture family | Source-visible synchronization |
| --- | --- |
| AArch64 | Interrupt masking paths use `dsb ish` and `isb`; spinlocks are implemented in `hal/aarch64/spinlock.c`. |
| ARM | Shared barrier helpers provide `dmb`, `dsb`, and `isb`; ARMv7-R spinlocks use `dmb`. |
| IA32 | Local APIC paths provide IPIs, and atomic instructions provide the lock primitive. |
| RISC-V | SBI IPI, timer, HSM, and RFENCE calls provide firmware-backed multicore services. |
| SPARCv8 LEON | Gaisler interrupt controllers provide broadcast IPI support on supported targets. |

The kernel code documents ordering at the synchronization primitive level.
Callers rely on the HAL implementation for the required architecture barriers.

## Inter-processor interrupts

The HAL exports `hal_cpuBroadcastIPI()` for sending an interrupt to other cores.
Some architectures also implement target-specific send paths, such as IA32 `hal_cpuSendIPI()`.
RISC-V uses the SBI IPI extension (`SBI_EXT_IPI`) through `hal_sbiSendIPI()`.
SPARCv8 LEON targets use Gaisler IRQMP or IRQAMP interrupt controllers.

IPIs are used for scheduling and cross-core coordination.
The concrete interrupt controller path depends on the target HAL.

## RISC-V firmware services

`phoenix-rtos-kernel/hal/riscv64/sbi.c` implements SBI calls for:

| Extension | Use |
| --- | --- |
| `SBI_EXT_BASE` | SBI version and implementation discovery. |
| `SBI_EXT_TIME` | Timer programming. |
| `SBI_EXT_SRST` | System reset. |
| `SBI_EXT_IPI` | Inter-hart interrupts. |
| `SBI_EXT_HSM` | Hart state management. |
| `SBI_EXT_RFENCE` | Remote instruction and address-translation fences. |

The legacy SBI console calls are also exposed through `hal_sbiPutchar()` and `hal_sbiGetchar()`.
