# sched_yield

## Synopsis

```c
#include <sched.h>

int sched_yield(void);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `sched_yield()` function shall force the running thread to relinquish the processor until it again becomes the head
of its thread list. It takes no arguments.

## Return value

The `sched_yield()` function shall return `0` if it completes successfully; otherwise, it shall return a value of `-1`
and set `errno` to indicate the error.

## Errors

No errors are defined.

## POSIX deviations

No POSIX deviations discovered.
