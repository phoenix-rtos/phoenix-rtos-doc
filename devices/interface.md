# Interface

The device driver server in a Phoenix-RTOS ecosystem communicates with other processes using a message interface. In
the typical case, the driver server has one port on which all requests are placed by clients. This port can be either
registered within the native namespace or special file(s) can be created within the filesystem.

## Port creation

Port, the endpoint of the message communication, can be created using the `portCreate()` function. If zero is returned,
then creation succeeded and the variable port now contains a unique port number assigned by the kernel.

## Registering within a namespace

The freshly created port can not be seen by other processes. To allow clients to find out the server's port number, it
has to be registered within some namespace. If the device driver server wants to register more than one "file" it does
not have to create separate ports for them. The driver needs to assign each "file" ID from its private pool.

Assume we want to create an SPI server that manages 2 instances of the device - spi0 and spi1. We can manage both using
only one port by registering the same port as `/dev/spi0` with id = 1 and `/dev/spi1` with id = 2. Every message driver
receives contains information to which `oid` (object ID) it has been sent. This enables the driver to recognize to
which special file message has been addressed.

If the system does not have a root filesystem, a port can be registered within Phoenix native filesystem by using
syscall

```c
int portRegister(u32 port, const char *name, oid_t *oid);
```

where

- _`port`_ - port number acquired from portCreate,
- _`name`_ - path in the namespace, e.g. "/uart0",
- _`oid`_ - optional argument containing instance ID.

Syscall returns 0 on success.

On systems that contain filesystem special file can be created, which will point to the server's `oid`. In the first
place we need `oid` of directory which will hold our special file:

````C
    #include <sys/msg.h>

    oid_t dir;

    lookup("/dev", &dir, NULL);
````

Then we can create a new special file and register:

````C
    msg_t msg;

    msg.type = mtCreate;
    msg.i.create.dir = dir;
    msg.i.create.type = otDev;
    msg.i.create.mode = 0;
    msg.i.create.dev.port = port; /* Port number assigned by portCreate */
    msg.i.create.dev.id = id; /* Id assigned by the driver itself */
    msg.i.data = "drvfile"; /* Filename */
    msg.i.size = strlen(msg.i.data);
    msg.o.data = NULL;
    msg.o.size = 0;

    msgSend(dir.port, &msg);
````

## Message types

There are several standard types of messages, although device driver servers need to implement only a subset of them.
With every message type, there are 3 common fields:

- _`type`_ - type of message,
- _`pid`_ - process ID of sender,
- _`priority`_ - priority of sender's thread.

### mtOpen

This message type informs the server, there is a process trying to open one of its special files.

- _`i.openclose.oid`_ - `oid` of the file being opened,
- _`i.openclose.flags`_ - flags with which file is being opened.

The server can respond to this message via the o.io.err field:

- _`EOK`_ if success,
- _`ENOENT`_ if no such file exist,
- _`EPERM`_ if client has not sufficient privilege.

### mtClose

This message type informs the server, there is a process trying to close one of its special files.

- _`i.openclose.oid`_ - `oid` of the file being closed.

Server can respond to this message via o.io.err field.

### mtRead

These message-type queries are read from the device driver server.

- _`i.io.oid`_ - `oid` of the file being read from,
- _`i.io.offs`_ - offset in the file,
- _`i.io.len`_ - length of the read,
- _`i.io.mode`_ - flags with which file has been opened,
- _`o.data`_ - buffer for data,
- _`o.size`_ - length of the o.data buffer.

The operation should block the client until all requested data becomes available.

Number of read bytes or error is returned via o.io.err.

### mtWrite

These message-type queries write to the device driver server.

_`i.io.oid`_ - `oid` of the file being written to,
_`i.io.offs`_ - offset in the file,
_`i.io.len`_ - length of write,
_`i.io.mode`_ - flags with which file has been opened,
_`i.data`_ - buffer with data,
_`i.size`_ - length of the i.data buffer.

The operation should block the client until all requested data is written to the device.

Number of written bytes or error is returned via o.io.err.

### mtDevCtl

This message type allows defining an entirely custom structure for input and output to/from a device server. This
structure should be serialized/deserialized to/from message i.raw/o.raw fields. Additional data can be passed in i.data
and o.data fields.

## See also

1. [Device drivers](README.md)
2. [Access to device hardware registers](hwaccess.md)
3. [Handling interrupts](interrupts.md)
4. [Table of Contents](../README.md)
