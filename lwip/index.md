# Network stack

Feniks-RTOS network stack is based on LwIP. According to microkernel architecture philosophy, it works as a server on
the user level and provides a socket interface. Sockets are implemented using the native Feniks-RTOS message passing
mechanism and are placed in the `libfeniks` library.

## Drivers

1. [PPPoU – uart/serial null-modem connection driver](lwip-pppou.md)

## Source code

The source code of the emulation server could be obtained using the following command

```console
git clone http://git.feniks-rtos.com/feniks-rtos-lwip
```

## See also

1. [Table of Contents](../index.md)

```{toctree}
:hidden:
:maxdepth: 1

lwip-pppou.md
```
