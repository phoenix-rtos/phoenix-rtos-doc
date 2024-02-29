# msgrespond

## Synopsis

`#include <sys/msg.h>`

`int msgRespond(uint32_t port, msg_t *m, unsigned long int rid);`

## Status

Implemented

## Conformance

Phoenix-RTOS specific

## Description

Finishes the communication between processes by responding to sender of initial message _msg_ with modified output
buffer to _port_ from which the message was read. Response ID _rid_ specifies message context and should be passed from
_rid_ acquired via `msgRecv()` call.

This function is part of interprocess communication mechanisms in Phoenix-RTOS. For more information about messaging
process and `msg_t` message structure please refer to [Message Passing](../../../kernel/proc/msg.md).

## Return value

If an error occurs during a function call an error value shall be returned. Otherwise, returns `0`.

## Errors

This function shall fall if:

* `-EINVAL` - _port_ does not name an existing port, or _port_ is closed

## Tests

Untested

## Known bugs

* Does not check if message pointer _m_ is not `NULL`.

## See Also

1. [IPC mechanisms in Phoenix-RTOS](../../../architecture.md#interprocess-communication)
2. [Standard library functions](../README.md)
3. [Table of Contents](../../../README.md)
