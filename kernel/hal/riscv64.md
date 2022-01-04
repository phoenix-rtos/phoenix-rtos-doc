# HAL for RISC-V 64 based targets

HAL for RISCV64 architecture is located in `src/hal/riscv64`.

## Initialization

Kernel execution starts from `_start` symbol located in `_init.S` file.

```assembler
    _start:
        /* Mask all interrupts */
        csrw sie, zero

        /* Disable FPU */
        li t0, SR_FS
        csrc sstatus, t0
```

First instructions mask interrupts and disable FPU.

```
        /* Initialize syspage */
        la a0, syspage
        la t0, pmap_common
        li t1,  3 * SIZE_PAGE + SIZE_PAGE + SIZE_PAGE /* pdirs + stack + heap */
        add t0, t0, t1
        sd t0, (a0)
```

The next step is setting the `syspage` pointer.

```
        call dtb_parse
```

The hardware configuration is passed to kerne using Device Tree Blob (DTB). Pointer to DTB is stored in `a1` register. DTB parser extracts information necessary to kernel from tree and stores it in kernel structure. It could be used later by other components using `dtb_` functions.

```
        call _pmap_preinit
```

After evaluating hardware configuration initial kernel page tables are initialized.

```
        li a1, VADDR_KERNEL
        la a0, _start
        li t0, 0xffffffffc0000000
        and a0, a0, t0
        sub a1, a1, a0
```

The relocation offset is calculated.

```assembler
        /* Relocate stack */
        la sp, pmap_common
        li t0, 3 * SIZE_PAGE + SIZE_PAGE              /* pdirs + stack */
        add sp, sp, t0
        add sp, sp, a1

        /* Relocate syspage */
        la a0, syspage
        ld t0, (a0)
        add t0, t0, a1
        sd t0, (a0)
```

And relocation of stack and syspage is performed.

```
        /* Point stvec to virtual address of intruction after satp write */
        la a0, 1f
        add a0, a0, a1
        csrw stvec, a0

        la a0, pmap_common
        srl a0, a0, 12
        li a1, 0x8000000000000000
        or a0, a0, a1

        sfence.vma
        csrw sptbr, a0
    1:
```

The above sequence enables paging and pass execution to proper virtual address by setting the trap vector.

```
        /* Add dummy page fault trap handler */
        la a0, .Lsecondary_park
        csrw stvec, a0

        call main
        li a7, SBI_SHUTDOWN
        ecall

.Lsecondary_park:
        wfi
        j .Lsecondary_park
```