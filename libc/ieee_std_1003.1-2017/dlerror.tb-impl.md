###Synopsis

`#include <dlfcn.h>`

`char *dlerror(void);`

###Description

The `dlerror()` function gets diagnostic information.

Arguments:
None.
 
The `dlerror()` function returns a null-terminated character string describing the last error that occurred during dynamic linking processing. If no dynamic linking errors have occurred since the last call of `dlerror()`, it returns `NULL`.

The `dlerror()` function is thread-safe. It returns only errors that occured on the current thread.

Depending on the application environment with respect to asynchronous execution events, such as signals or other asynchronous computation sharing the address space, applications should use a critical sections to retrieve the error pointer and buffer.
 
###Return value

On success, `dlerror()` returns a null-terminated character string; otherwise, `NULL` is returned.

The application does not modify the string returned. 

The returned pointer might be invalidated or the string content might be overwritten by a subsequent call to `dlerror()` in the same thread. The returned pointer might also be invalidated if the calling thread is terminated.

###Errors

No errors are defined.

###Implementation tasks

* Implement the `dlerror()` function.