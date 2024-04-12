---
orphan: True
---
# PPPoU driver

In the era of IoT, when the goal is to address every device on the Internet
with IP, even on the simplest microcontroller, may face a barrier in the form
of the lack of a proper interface (Ethernet, Wi-Fi) the use of uart in
conjunction with an appropriate adapter, be it USB, Bluetooth or
optical/infrared uart may be the easiest to connect both worlds.

Almost every microcontroller has at least one uart, and may not have Ethernet MAC,
Wi-Fi or Bluetooth, but uart/serial null-modem connection is possible always and
the most legitimate and proven protocol to deliver IP world is PPP.

## Build and set up the device

Before you start [building Phoenix RTOS](../building/building.md) with
[network stack — LwIP](/lwip/lwip.md), you need to adjust the custom
build.project script, in function `b_build_project()` add the following lines:

```console
b_log "Builing phoenix-rtos-lwip"
(cd phoenix-rtos-lwip && make $MAKEFLAGS $CLEAN all)
```

some targets may require adding also

```console
b_install "$PREFIX_PROG_STRIPPED/lwip" /sbin
```

next it is required to add `lwip` to syspage programs with `PROGS` variable,
e.g.:

```console
PROGS=("dummyfs" "imxrt-multi" "lwip" "psh")
```

If `phoenix-rtos-build` builds`phoenix-rtos-lwip` correctly, you can start the
null-modem point-to-point connection in the Phoenix RTOS system.  To enable the
driver and up the interface just after Phoenix RTOS kernel starts, add e.g. the
following line to the `plo` script:

```console
app flash0 -x @lwip;/dev/uart3:115200:up xip1 ocram2
```

It is important that the entry is added with the `imxrt-multi` driver or with
the appropriate platform serial driver. Driver that is used in the example is
`imxrt-multi` available for `imxrt` targets, it will create an entry in `/dev`
directory e.g. `uart3` corresponding to the auxiliary uart port instance on
i.MX RT1064-EVK board, where uart1 is already used for the systems console.

The configuration field `:115200:` is optional and represents the connection
speed (value of 115200 bauds is the default baud rate and can be omitted).  Of
course, you can set other speeds, e.g. 9600, 230400 or 460800. Other connection
parameters, such as parity and stop bits, are fixed to 8N1, because nowadays,
other values are rarely used, especially for serial PPP connections.

### Default route

By default, `pppou` driver will add the `default route` via itself. If the
`default route` is not to be added, use the optional `nodefault` parameter,
as in the example below.

```console
app flash0 -x @lwip;pppou:/dev/uart3:115200:nodefault:up xip1
```

## Setup device side

For example, on the `imxrt` platforms _(memory map used in example is for i.MX
RT1064)_ the plo script might look like this:

```console
map itcm 0 58000 R+E
map dtcm 20000000 20028000 R+W
map ocram2 20200000 20280000 R+W+E
map xip1 70000000 70400000 R+E
kernel flash0
app flash0 -x @dummyfs xip1 dtcm
app flash0 -x @imxrt-multi xip1 dtcm
app flash0 -x @lwip;pppou:/dev/uart3:460800:up xip1 ocram2
app flash0 -x @psh xip1 ocram2
go!
```

Alternatively, `phoenix-rtos-lwip` can also be started with the command `psh`
sysexec (NON-MMU targets) at any time:

```console
sysexec ocram2 lwip pppou:/dev/uart3:115200:up
```

If provided the LwIP server has not already been running, and on MMU architectures
either using the `exec` command or directly in `psh` command prompt.

Once the `phoenix-rtos-lwip` server has started, you can make sure by issuing
the command `ps`, which should show that the `lwip` with the correct arguments
is already running, in the example figure below you can see that the baud rate
460800 was used.

![ps showing LwIP server is running](_images/lwip-pppou-ps.png)

## Setup host side

As what has been done above and both the device and host have been connected
with a null-modem cable or using any uart-ttl-usb adapter, then on the host
side you must also configure the connection, if it is Linux or BSD, you can
use, for example this command (prepend `pppd` with `sudo`, `doas` or `su`
command if `root` user rights are required):

```console
pppd /dev/ttyUSB0 460800 10.0.0.1:10.0.0.2 lock local noauth nocrtscts nodefaultroute maxfail 0 persist
```

The device entry `/dev/ttyUSB0` may differ between systems, the address pair
`10.0.0.1:10.0.0.2` means `local:remote` that the host will get `10.0.0.1`
address and the remote device with `phoenix-rtos-lwip` running will get
`10.0.0.2` address, the ppp daemon will run in the background and wait
continuously (`maxfail 0 persist`) for connections.

To check if the connection has been successfully established, use `ping`
command on the host side:

![ping the phenix-rtos device](_images/lwip-pppou-ping.png)

Additional `/dev` entries will be created like `ifstatus`, `route` and `pf`.

## Enabling IPv6 (dual stack)

Add the following line at the top of file `phoenix-rtos-lwip/include/default-opts/lwipopts.h` and rebuild.

```c
#define LWIP_IPV6 1
```

Re-run `pppd` with `+ipv6` flag, the remote side may be assigned with
link-local address like `fe80::55a0:6c87:7de3:611b`

![ping the phenix-rtos device](_images/lwip-pppou-ping6.png)

## Debugging

Compile `phoenix-rtos-lwip` pppou driver with logging enabled, and then on host
use the following command that enable full `pppd` debugging

```console
pppd /dev/ttyUSB0 <speed> 10.0.0.1:10.0.0.2 lock local nodetach noauth debug dump nocrtscts nodefaultroute maxfail 0 holdoff 1
```

Replace `<speed>` with the baud rate of remote side and supported by the
system, e.g. 9600, 115200, 230400 or 460800.
