# Interrupts management

## `syscalls_interrupt`

````C
GETFROMSTACK(ustack, unsigned int, n, 0);
GETFROMSTACK(ustack, void *, f, 1);
GETFROMSTACK(ustack, void *, data, 2);
GETFROMSTACK(ustack, unsigned int, cond, 3);
GETFROMSTACK(ustack, unsigned int *, handle, 4);
````

Installs interrupt handler `f` for interrupt given by `n`.

## See also

1. [System calls](README.md)
2. [Table of Contents](../../README.md)
