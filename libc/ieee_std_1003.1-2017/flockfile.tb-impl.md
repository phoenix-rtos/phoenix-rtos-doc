###Synopsis

`#include <stdio.h>`

`void flockfile(FILE *file);`
`int ftrylockfile(FILE *file);`
`void funlockfile(FILE *file);`

###Description

The functions are `stdio` locking functions.

Arguments:

<u>file</u> - the pointer to `stdio` (`FILE` *) object.

These functions  provide for explicit application-level locking of stdio (`FILE` *) objects. They can be used by a thread to delineate a sequence of I/O statements that are executed as a unit.

The `flockfile()` function  acquires for a thread ownership of a (`FILE` *) object.

The `ftrylockfile()` function  acquires for a thread ownership of a (`FILE` *) object if the object is available; `ftrylockfile()` is a non-blocking version of `flockfile()`.

The `funlockfile()` function  relinquishes the ownership granted to the thread. The behaviour is undefined if a thread other than the current owner calls the `funlockfile()` function.

The functions  behave as if there is a lock count associated with each (`FILE` * ) object. This count is implicitly initialized to zero when the (`FILE` * ) object is created. The (`FILE` * ) object is unlocked when the count is zero. When the count is positive, a single thread owns the (`FILE` * ) object. When the `flockfile()` function is called, if the count is zero or if the count is positive and the caller owns the (`FILE` * ) object, the count  is incremented. Otherwise, the calling thread is suspended, waiting for the count to return to zero. Each call to `funlockfile()`  decrements the count. This allows matching calls to `flockfile()` (or successful calls to `ftrylockfile()`) and `funlockfile()` to be nested.

All functions that reference (`FILE` * ) objects, except those with names ending in `_unlocked`,  behave as if they use `flockfile()` and `funlockfile()` internally to obtain ownership of these (`FILE` * ) objects.

###Return value

For `flockfile()` and `funlockfile()` - none.
The `ftrylockfile()` function  returns `0` on success and `-1` when the lock cannot be acquired.

###Errors

No errors are defined.

###Implementation tasks

 * Implement the `flockfile()` function.
 * Implement the `funlockfile()` function.
 * Implement the `ftrylockfile()` function.