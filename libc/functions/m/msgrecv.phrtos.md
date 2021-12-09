# Synopsis 
`#include <sys/msg.h>`

`int msgRecv(uint32_t port, msg_t *m, unsigned long int *rid);`

## Status
Implemented
## Conformance
Phoenix-RTOS specific
## Description

This function should read a message from _port_ and store its contents in `msg_t` structure pointed by _m_. _rid_ parameter specifies receiving context and should be passed to `msgRespond()`.

Upon calling `msgRecv()` the receiving thread is suspended until one of the following occurs:
 - a new message is received
 - port is closed
 - an error occurs

 `msgRecv()` does not finish the communication between sender and receiver and is only used to get contents of a message. To properly finish the communication `msgRespond()` shall be called with appropriate `*rid` value to respond to the message and end communication between processes. If no `msgRespond()` is called the message sender will wait indefinetely for a response.


This function is part of interprocess communicaition mechanisms in Phoenix-RTOS. For more information about messaging process and `msg_t` message structure please refer to [Message Passing](../../../kernel/proc/msg.md).


## Return value

If an error occurred during a function call an error value shall be returned. Otherwise returns `0`.

## Errors

This function shall fall if:

 * `-EINVAL` - _port_ does not name an existing port, or _port_ is closed

## Tests

Untested

## Known bugs

None

## See Also 
1. [IPC mechanisms in Phoenix-RTOS](../../../architecture.md#interprocess-communication) 
2. [Standard library functions](../README.md)
3. [Table of Contents](../../../README.md)
