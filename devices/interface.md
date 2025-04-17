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
    msg.oid = dir;
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

Interprocess communication by message queues is described in detail in the
[Message passing](../kernel/proc/msg.md) document.
