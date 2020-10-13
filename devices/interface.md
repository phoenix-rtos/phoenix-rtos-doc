# Interface

Device driver server in the Phoenix-RTOS ecosystem communicate with other processes using message interface. In the typical case driver server have one port on which all request are placed by clients. This port can be either registered within native namespace or special file(s) can be created within the filesystem.

##Port creation

Port, endpoint of the message communication, can be created using

>
int portCreate(u32 *port);

syscall. If zero is returned, then creation succeeded and variable port now contains unique port number assigned by the kernel.

##Registering within namespace

Freshly created port can not be seen by other processes. To allow clients to find out servers port number, it has to be registered within some namespace. If device driver server wants to register more than one "file" it do not have create separate ports for them. Driver needs to assign each "file" id from it's private pool.

Assume we want to create SPI server which manages 2 instances of device - spi0 and spi1. We can manage both using only one port by registering the same port as <i>/dev/spi0</i> with id = 1 and <i>/dev/spi1</i> with id = 2. Every message driver receives contain information to which oid it has been sent. This enables driver to recognize to which special file message has been adressed to.

If system does not have root filesystem, port can be registered within Phoenix native filesystem by using syscall

>
    int portRegister(u32 port, const char *name, oid_t *oid);

where

- <b>port</b> - port number aquired from portCreate,
- <b>name</b> - path in the namespace, e.g. "/uart0",
- <b>oid</b> - optional argument containing instance id.

Syscall returns 0 on success.

On systems that contain filesystem special file can be created, which will point to the server's oid. In the first place we need oid of directory which will hold our special file:

>
    #include <sys/msg.h>
>
    oid_t dir;
>
    lookup("/dev", &dir, NULL);

Then we can create new special file and register:

>
    msg_t msg;
>
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
>
    msgSend(dir.port, &msg);
<p>
##Message types

There are several standart types of messages, although device driver servers need to implement only subset of them. With every message type there are 3 common fields:

- <b>type</b> - type of message,
- <b>pid</b> - process id of sender,
- <b>priority</b> - priority of sender's thread.
</p><p>
###mtOpen

This message type informs server, there is process trying to open one of it's special files.

- <b>i.openclose.oid</b> - oid of the file being opened,
- <b>i.openclose.flags</b> - flags with which file is being opened.

Server can respond to this message via o.io.err field:

- <b>EOK</b> if success,
- <b>ENOENT</b> if no such file exist, 
- <b>EPERM</b> if client has not sufficient privilege.
</p><p>
###mtClose

This message type informs server, there is process trying to close one of it's special files.

- <b>i.openclose.oid</b> - oid of the file being closed.

Server can respond to this message via o.io.err field.
</p><p>
###mtRead

This message type queries read from the device driver server.

- <b>i.io.oid</b> - oid of the file being read from,
- <b>i.io.offs</b> - offset in the file,
- <b>i.io.len</b> - length of the read,
- <b>i.io.mode</b> - flags with which file has been opened,
- <b>o.data</b> - buffer for data,
- <b>o.size</b> - length of the o.data buffer.

Operation should block client until all requested data becomes available.

Number of read bytes or error is returned via o.io.err.
</p><p>
###mtWrite

This message type queries write to the device driver server.

<b>i.io.oid</b> - oid of the file being written to,
<b>i.io.offs</b> - offset in the file,
<b>i.io.len</b> - length of the write,
<b>i.io.mode</b> - flags with which file has been opened,
<b>i.data</b> - buffer with data,
<b>i.size</b> - length of the i.data buffer.

Operation should block client until all requested data is written to the device.

Number of written bytes or error is returned via o.io.err.
</p><p>
###mtDevCtl

This message type allows to define entirely custom structure for input and output to/from a device server. This structure should be serialized/deserialized to/from message i.raw/o.raw fields. Additional data can be passed in i.data and o.data fields.
</p>