# killpg

## Synopsis

```c
#include <signal.h>

int killpg(pid_t pgrp, int sig);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `killpg()` function shall send the signal specified by _sig_ to the process group specified by _pgrp_.

If _pgrp_ is greater than `1`, `killpg(pgrp, sig)` shall be equivalent to `kill(-pgrp, sig)`. If _pgrp_ is less than
or equal to `1`, the behavior of `killpg()` is undefined.

If _pgrp_ is `0`, the signal is sent to the process group of the calling process. If _pgrp_ is negative, `killpg()`
fails with `EINVAL`. If _pgrp_ is `1`, the call is equivalent to `kill(-1, sig)`, which sends the signal to all
processes in the session of the calling process, so process group `1` cannot be signalled by `killpg()`.

## Return value

Upon successful completion, `0` shall be returned. Otherwise, `-1` shall be returned and `errno` set to indicate the
error.

## Errors

The `killpg()` function shall fail if:

* `EINVAL` - The value of the _sig_ argument is an invalid or unsupported signal number.

* `EPERM` - The process does not have permission to send the signal to any receiving process.

* `ESRCH` - No process or process group can be found corresponding to that specified by _pgrp_.

## POSIX deviations

The default actions of the job control signals are not implemented: `SIGSTOP`, `SIGTSTP`, `SIGTTIN` and `SIGTTOU` do not
stop the processes of the group and `SIGCONT` does not continue them (see the deviations of `kill()`).

Permission to send a signal is not verified. Phoenix-RTOS does not keep user and group IDs of processes, so every
process is privileged to send a signal to any other user process and `killpg()` does not fail with `EPERM` due to the
user IDs of the sending and receiving processes (see the deviations of `kill()`).
