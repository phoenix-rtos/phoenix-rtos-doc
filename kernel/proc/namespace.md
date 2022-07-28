# Kernel - Processes and threads - Namespace

The namespace and port registering functionality is used by operating system servers (e.g. device drivers, file servers) as a basic method of integration with the other operating system components. For example if a thread working in the process context opens the file given by specific path, it indirectly lookups for the port of the file server handling this object and finally receives the `oid_t`(port, id) structure identifying the file on the server. It is done because the file server handling particular file during start registers its port in the namespace handled by the other server or by the kernel. File server mount its namespace to the existing namespace handled by existing file servers. The namespace mounting functionality is presented on the following picture.

<img src="_images/proc-namespace.png" style=" width: 450px">

In case of device drivers they registers special names in the namespace and associate them with the specific `oids`. 
When program opens the file registered by a device driver it receives `oid` pointed directly to the device driver server, so all communication is redirected to this server. This idea has been briefly presented on following figure.

<img src="_images/proc-namespace2.png" style=" width: 450px">

1. [Kernel](../README.md)
2. [Kernel - Processes and threads - Process creation](forking.md)
3. [Kernel - Processes and threads - Synchronization primitives](sync.md)
4. [Kernel - Processes and threads - Message passing](msg.md)
5. [Table of Contents](../../README.md)
