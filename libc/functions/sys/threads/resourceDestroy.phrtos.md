# resourceDestroy

## Synopsis

```c
#include <sys/threads.h>

int resourceDestroy(handle_t h);
```

## Status

Implemented

## Conformance

Phoenix-RTOS specific

## Description

Deletes the resource given by `h` from current process. Has additional effects depending on the resource.

If the deleted resource is a mutex, it is unlocked and memory allocated to it is freed.

If the deleted resource is a conditional variable, `condBroadcast()` is called with the handle _`h`_, and then memory
allocated to it is freed.

If the deleted resource is an interrupt handle, the handler function is unregistered, the conditional variable related
to the handle is disposed (as described above) and memory allocated to the handle is freed.

## Return value

If successful, the `resourceDestroy()` function shall return zero; otherwise, an
error number shall be returned to indicate the error.

## Errors

The `resourceDestroy()` function may fail if:

* `-EINVAL` - The provided handle _`h`_ does not point to a valid resource.

## Tests

Tested in [test-sys](https://github.com/phoenix-rtos/phoenix-rtos-tests/tree/master/sys)

## Known bugs

None
