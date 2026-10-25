# setpgrp

## Synopsis

```c
#include <unistd.h>

pid_t setpgrp(void);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

If the calling process is not already a session leader, `setpgrp()` sets the process group ID of the calling process
to the process ID of the calling process. If `setpgrp()` creates a new session, then the new session has no controlling
terminal.

The `setpgrp()` function has no effect when the calling process is a session leader.

The `setpgrp()` function behaves as `setpgid(0, 0)`: it creates a new process group in the session of the calling
process and doesn't create a new session.

## Return value

Upon completion, `setpgrp()` shall return the process group ID.

## Errors

No errors are defined.

## POSIX deviations

No POSIX deviations discovered.
