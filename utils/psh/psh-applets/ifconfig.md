# ifconfig

`ifconfig` is a command-line tool used to configure, control, and query TCP/IP network interface parameters.
It allows users to configure an interface's IP address, netmask, and other settings,
as well as to activate or deactivate network interfaces.

## Usage

```console
ifconfig [-a] [-h] [interface]
ifconfig <interface> [inet] <options> | <address> ...
```

### Parameters

`-a`: Display all interfaces which are currently available, even if down.

`-h`: Display help information.

`interface`: Specify the network interface to configure or query.

`inet`: Specify the use of the Internet Protocol. This is optional and mainly for compatibility.

### Options

`up`: Activate the specified interface.

`down`: Deactivate the specified interface.

`netmask <address>`: Set the subnet mask of the interface to address.

`broadcast <address>`: Set the broadcast address of the interface to address.

`mtu <N>`: Set the Maximum Transmission Unit of the interface to N.

`dstaddr <address>`: Set the destination address for a point-to-point link to address.

`pointopoint <address>`: Configure the interface as a point-to-point link with the remote endpoint address.

`multicast`: Toggle the multicast flag for the interface.

`allmulti`: Toggle the all-multicast mode, controlling whether all multicast packets are received.

`promisc`: Toggle promiscuous mode, controlling whether all packets on the network are received.

`arp`: Toggle the use of the ARP protocol on this interface.

`dynamic`: Toggle the activation of DHCP client on the interface.

## Examples

Activate an Interface:

```console
ifconfig eth0 up
```

Set IP address and subnet mask:

```console
ifconfig eth0 192.168.1.100 netmask 255.255.255.0
```

Display configuration of all interfaces:

```console
ifconfig -a
```

Setting the MTU:

```console
ifconfig eth0 mtu 1500
```

## See also

1. [Feniks-RTOS shell](../index.md)
2. [Feniks-RTOS Utilities](../../index.md)
3. [Table of Contents](../../../index.md)
