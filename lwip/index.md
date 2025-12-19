# Network stack

Phoenix-RTOS network stack is based on LwIP. According to microkernel architecture philosophy, it works as a server on
the user level and provides a socket interface. Sockets are implemented using the native Phoenix-RTOS message passing
mechanism and are placed in the `libphoenix` library.

The source code of the emulation server could be obtained using the following command

```shell
git clone https://github.com/phoenix-rtos/phoenix-rtos-lwip.git
```

```{toctree}
:maxdepth: 1

lwip-pppou.md
```
