# Network stack

Phoenix-RTOS network stack is based on LwIP. According to microkernel architecture philosophy, it works as a server on
the user level and provides a socket interface. Sockets are implemented using the native Phoenix-RTOS message passing
mechanism and are placed in the `libphoenix` library.

## Drivers

1. [PPPoU – uart/serial null-modem connection driver](lwip-pppou.md)

## Source code

The source code of the emulation server could be obtained using the following command

```console
git clone https://github.com/phoenix-rtos/phoenix-rtos-lwip.git
```

```{toctree}
:hidden:
:maxdepth: 1

lwip-pppou.md
```
