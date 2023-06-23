# Synopsis 
`#include <ioctl.h>`</br>

` int ioctl(int fildes, int request, ... /* arg */);`</br>

## Status
Partially implemented
## Conformance
IEEE Std 1003.1-2017
## Description


The `ioctl()` function shall perform a variety of control functions on devices. For _fildes_ not referring to devices, the functions performed by this call are unspecified.

The _fildes_ argument is an open file descriptor that refers to a device.

The _request_ argument selects the control function to be performed and shall depend on the device being addressed.

The _arg_ argument represents additional information that is needed by this specific device to perform the requested function. The type of _arg_ depends upon the particular control request, but it shall be either an integer or a pointer to a device-specific data structure.

In order to define driver request one should use one of the macros presented below, which are available in the `ioctl.h` header file:

- `_IOC(inout,group,num,len)` - macro which returns every possible request 

  - `inout` - use these defines: `IOC_VOID` (no data), `IOC_OUT` (read), `IOC_IN` (write), `IOC_INOUT` (read/write)
  - `group` - describe group type (collecting the ioctls in groups for a common purpose or a common driver e.g. `'S'` for sockets), 8-bit value
  - `num` - specifies serial number of request, 8 -bit value
  - `len` - how big is size of data, 14-bit value

- `_IOV(g,n)` - macro which returns no data transmission request
- `_IOR(g,n,t)` - macro which returns read request
- `_IOW(g,n,t)` - macro which returns write request
- `_IOWR(g,n,t)` - macro which returns read/write request

  - `g` - 8-bit group value
  - `n` - 8-bit serial number
  - `t` - type of data

There are also some checking macros:

- `OCPARM_LEN(x)` - returns data length
- `IOCBASECMD(x)` - returns base command value (2 least significant bytes describing group and serial number)
- `IOCGROUP(x)` - returns group type value

The resulting request will be in such form: 2 bits describe direction (`00`: none, `10`: write, `01`: read, `11`: read/write) followed by 14 size bits, followed by an 8-bit group type (collecting the ioctls in groups for a common purpose or a common driver) and an 8-bit serial number.

It is worth to note that to get data sent to driver inside message, one should use `ioctl_unapck()`.

Also, if you are willing to pass structure with pointer in _arg_ argument of `ioctl()` you
should custom pack your message in `ioctl_pack()` (see ioctl_pack() implementation).


## Return value


Upon successful completion, `ioctl()` shall return a value other than `-1` that depends on the device control function. Otherwise, it shall return `-1` and set `errno` to indicate the error.


## Errors


The `ioctl()` function may fail if:


 * `EBADF` - The _fildes_ argument is not a valid open file descriptor.

 * `ENOSYS` - Couldn't get information about calling process.

 * `EINVAL` - Tried to send message to invalid port.


## Example usage


```C
#include <ioctl.h>
#include <fcntl.h>
#include <stdio.h>

#define REQUEST _IOC(IOC_IN, 'A', 0x01, int)

int main() {
    int fd;
    int data = 4;

    if (fd = open(PATH, O_WRONLY) < 0) {
        fprintf(stderr, "Cannot open special device file\n");
    }
    
    /*
     * Send request with additional data to device server,
     * assuming device server successfully created and accept our request.
     */
    if (ioctl(fd, REQUEST, &data) < 0) {
        fprintf(stderr, "Something went wrong\n");
    }
}
```


## Tests

Tested

## Known bugs

None

## See Also 
1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
