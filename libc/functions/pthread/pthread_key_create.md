# pthread_key_create

## Synopsis

```c
#include <pthread.h>

int pthread_key_create(pthread_key_t *key, void (*destructor)(void*));
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_key_create()` function shall create a thread-specific data key visible to all threads in the process. Key
values provided by `pthread_key_create()` are opaque objects used to locate thread-specific data. Although the same key
value may be used by different threads, the values bound to the key by `pthread_setspecific()` are maintained on a
per-thread basis and persist for the life of the calling thread.

Upon key creation, the value `NULL` shall be associated with the new key in all active threads. Upon thread creation,
the value `NULL` shall be associated with all defined keys in the new thread.

An optional _destructor_ function may be associated with each key value. At thread exit, if a key value has a
non-`NULL` destructor pointer, and the thread has a non-`NULL` value associated with that key, the value of the key is
set to `NULL`, and then the function pointed to is called with the previously associated value as its sole argument.
The order of destructor calls is unspecified if more than one destructor exists for a thread when it exits.

If, after all the destructors have been called for all non-`NULL` values with associated destructors, there are still
some non-`NULL` values with associated destructors, then the process is repeated. If, after at least
`PTHREAD_DESTRUCTOR_ITERATIONS` iterations of destructor calls for outstanding non-`NULL` values, there are still some
non-`NULL` values with associated destructors, implementations may stop calling destructors, or they may continue
calling destructors until no non-`NULL` values with associated destructors exist, even though this might result in an
infinite loop. Phoenix-RTOS stops calling destructors after `PTHREAD_DESTRUCTOR_ITERATIONS` iterations.

## Return value

If successful, the `pthread_key_create()` function shall store the newly created key value at _*key_ and shall return
zero. Otherwise, an error number shall be returned to indicate the error.

## Errors

The `pthread_key_create()` function shall fail if:

* `EAGAIN` - The system lacked the necessary resources to create another thread-specific data key, or the
  system-imposed limit on the total number of keys per process `PTHREAD_KEYS_MAX` has been exceeded.

* `ENOMEM` - Insufficient memory exists to create the key.

The `pthread_key_create()` function shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
