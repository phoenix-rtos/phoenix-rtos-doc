# condCreateWithAttr

## Synopsis

```c
#include <sys/threads.h>

int condCreateWithAttr(handle_t *h, struct condAttr *attr);
```

## Status

Implemented

## Conformance

Phoenix-RTOS specific

## Description

The `condCreateWithAttr()` function shall initialize the condition variable referenced by `h` using attributes
specified in the `attr` structure (non-`NULL`). Upon successful initialization, the state of the condition variable
shall become initialized.

Attempting to initialize an already initialized condition variable results in undefined behavior.

Attributes structure `condAttr` is defined as follows:

```c
struct condAttr {
	int clock;
	int type;
};
```

The `clock` field specifies the clock to be used for the condition variable. The following values are supported:

* `PH_CLOCK_RELATIVE` - `timeout` passed to `condWait()` is relative to the current time.
* `PH_CLOCK_REALTIME` - `timeout` passed to `condWait()` is absolute time based on the real-time clock.
* `PH_CLOCK_MONOTONIC` - `timeout` passed to `condWait()` is absolute time based on the monotonic clock.

The `type` field specifies the type of the condition variable. The following values are supported:

* `PH_COND_NORMAL` - regular condition variable, `condWait()` shall be called with a mutex locked by the calling
  thread.
* `PH_COND_UNLOCKED` - condition variable without an associated mutex. This is useful when waiting for an interrupt
  signal (see `interrupt()`), in which case a mutex would protect nothing if a single thread is waiting. It is the
  responsibility of the user to ensure that such a condition variable is used in a thread-safe manner. For interrupt
  handling the dedicated wrappers from [sys/interrupt.h](../interrupt/index.md) should be used.

## Return value

If successful, the `condCreateWithAttr()` function shall return zero; otherwise,
an error number shall be returned to indicate the error.

## Errors

The `condCreateWithAttr()` function shall fail if:

* `-ENOMEM` - Insufficient memory exists to initialize the condition variable.
* `-EINVAL` - The attributes specified in `attr` are invalid.
* `-EFAULT` - The address specified by `h` or `attr` is invalid.

These functions shall not return an error code of `EINTR`.

## Tests

Tested in [test-sys](https://github.com/phoenix-rtos/phoenix-rtos-tests/tree/master/sys)

## Known bugs

None
