# sockatmark

## Synopsis

```c
#include <sys/socket.h>

int sockatmark(int s);
```

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `sockatmark()` function shall determine whether the socket specified by the descriptor _s_ is at the out-of-band
data mark. If the protocol for the socket supports out-of-band data by marking the stream with an out-of-band data
mark, the `sockatmark()` function shall return `1` when all data preceding the mark has been read and the out-of-band
data mark is the first element in the receive queue. The `sockatmark()` function shall not remove the mark from the
stream.

## Return value

Upon successful completion, the `sockatmark()` function shall return a value indicating whether the socket is at an
out-of-band data mark. If the protocol has marked the data stream and all data preceding the mark has been read, the
return value shall be `1`; if there is no mark, or if data precedes the mark in the receive queue, the `sockatmark()`
function shall return `0`. Otherwise, it shall return a value of `-1` and set `errno` to indicate the error.

## Errors

The `sockatmark()` function shall fail if:

* `EBADF` - The _s_ argument is not a valid file descriptor.

* `ENOTTY` - The file associated with the _s_ argument is not a socket.

## POSIX deviations

No POSIX deviations discovered.
