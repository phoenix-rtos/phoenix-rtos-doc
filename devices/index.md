# Device drivers

Feniks-RTOS implements device drivers as device servers running on the user level. The communication with drivers is
done via message passing using a well-defined interface for exchanging data between programs and drivers.

To control the device, two mechanisms are necessary and should be provided by the operating system kernel: access to
device hardware registers and method of handling interrupts triggered by it. The architecture of these Feniks-RTOS
mechanisms has been presented in the chapter’s subsections.

## Generic driver architecture

Each typical driver in Feniks-RTOS consists of the main function which typically parses command line parameters,
creates a driver communication port, registers it in the operating system, namespace, initializes a device, and starts
processing the incoming messages.

The message is fetched from the queue using the `msgRecv` syscall. This syscall blocks the thread until a message is
available, so the device server should implement a thread pool to process the incoming request. The client is blocked
until the server responds to the message using the `msgRespond` syscall. There are two approaches to message
processing - concurrent processing and iterative processing.

## Concurrent processing

Messages which can be processed instantly may be serviced by one of the main loop threads.

## Iterative processing

If delays are expected (e.g. waiting for I/O) message should be inserted into the server's internal queue and processed
by the internal thread.

## Source code

The source code of Feniks-RTOS device drivers could be obtained using the following command

```console
git clone http://git.feniks-rtos.com/feniks-rtos-devices
```

The documentation of a particular driver is provided within its source code repository.

## See also

1. [Access to device hardware registers](hwaccess.md)
2. [Handling interrupts](interrupts.md)
3. [Message interface](interface.md)
4. [Table of Contents](../index.md)

```{toctree}
:hidden:
:maxdepth: 1

interface.md
hwaccess.md
interrupts.md
libsdio.md
sensors/simsensors.md
```
