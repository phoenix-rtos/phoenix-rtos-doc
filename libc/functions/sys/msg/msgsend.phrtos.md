# msgSend

## Synopsis

```c
#include <sys/msg.h>

int msgSend(uint32_t port, msg_t *m);
```

## Status

Implemented

## Conformance

Phoenix-RTOS specific

## Description

This function sends a message _m_ to specified _port_. An _m_ should point to a `msg_t` structure that stores
message data.

After calling the `msgSend()` function the sending thread is suspended until the receiving thread executes `msgRecv()`
function, reads data from input buffer, writes the final answer to the output buffer and executes `msgRespond()`.

This function ensures that either message was processed by a recipient or that it was not sent at all.

This function is part of interprocess communication mechanisms in Phoenix-RTOS. For more information about messaging
process and `msg_t` message structure please refer to [Message Passing](../../../../kernel/proc/msg.md).

## Return value

If an error occurred during a function call an error value shall be returned. Otherwise, it returns `0`.

## Errors

This function shall fall if:

* `-EINVAL` - _port_ does not name an existing port, or _port_ is closed, or _m_ points to an uninitialized message
 structure.

This function may fall if:

* `-EINTR` - calling thread was woken up by signal before the message was received by the server.

## Tests

Untested

## Known bugs

None
