# Synopsis 
`#include <sys/mman.h>`</br>

` void *mmap(void *addr, size_t len, int prot, int flags, int fildes, off_t off);`</br>

## Status
Partially implemented
## Conformance
IEEE Std 1003.1-2017
## Description


The `mmap()` function shall establish a mapping between an address space of a process and a memory object.

The `mmap()` function shall be supported for the following memory objects:

* Regular files

* Shared memory objects 

* Typed memory objects 

Support for any other type of file is unspecified.

The format of the call is as follows:
```c
pa=mmap(addr, len, prot, flags, fildes, off);
```

The `mmap()` function shall establish a mapping between the address space of the process at an address pa for
_len_ bytes to the memory object represented by the file descriptor fildes at offset off for _len_ bytes.

The value of pa is an implementation-defined function of the parameter _addr_ and the values of _flags_, further
described below. A successful `mmap()` call shall return pa as its result. The address range starting at pa and
continuing for _len_ bytes shall be legitimate for the possible (not necessarily current) address space of the process. The
range of bytes starting at off and continuing for _len_ bytes shall be legitimate for the possible (not necessarily
current) offsets in the memory object represented by fildes.

If fildes represents a typed memory object opened with either the `POSIX_TYPED_MEM_ALLOCATE` flag or the
`POSIX_TYPED_MEM_ALLOCATE_CONTIG` flag, the memory object to be mapped shall be that portion of the typed memory object allocated by
the implementation as specified below. In this case, if off is non-zero, the behavior of `mmap()` is undefined. If
fildes refers to a valid typed memory object that is not accessible from the calling process, `mmap()` shall fail. 
The mapping established by `mmap()` shall replace any previous mappings for those whole pages containing any part of the
address space of the process starting at pa and continuing for _len_ bytes.

If the size of the mapped file changes after the call to `mmap()` as a result of some other operation on the mapped file,
the effect of references to portions of the mapped region that correspond to added or removed portions of the file is
unspecified.

If _len_ is zero, `mmap()` shall fail and no mapping shall be established.

The parameter _prot_ determines whether read, write, execute, or some combination of accesses are permitted to the data
being mapped. The _prot_ shall be either `PROT_NONE` or the bitwise-inclusive OR of one or more of the other flags in the
following table, defined in the `<sys/mman.h>` header.




| __Symbolic Constant__ | __Description__                |
|-------------------|----------------------------|
| `PROT_READ`         |   Data can be read.        |
|   `PROT_WRITE`      |   Data can be written.     |
|   `PROT_EXEC`       |   Data can be executed.    |
|   `PROT_NONE`       |   Data cannot be accessed. |



If an implementation cannot support the combination of access types specified by _prot_, the call to `mmap()` shall
fail.

An implementation may permit accesses other than those specified by _prot_; however, the implementation shall not permit a
write to succeed where `PROT_WRITE` has not been set and shall not permit any access where `PROT_NONE` alone has been set. The
implementation shall support at least the following values of _prot_: `PROT_NONE,` `PROT_READ,` `PROT_WRITE,` and the
bitwise-inclusive OR of `PROT_READ` and `PROT_WRITE`. The file descriptor fildes shall have been opened with read permission,
regardless of the protection options specified. If `PROT_WRITE` is specified, the application shall ensure that it has opened the
file descriptor fildes with write permission unless `MAP_PRIVATE` is specified in the _flags_ parameter as described
below.

The parameter _flags_ provides other information about the handling of the mapped data. The value of _flags_ is the
bitwise-inclusive OR of these options, defined in `<sys/mman.h>`:

| __Symbolic Constant__  |   __Description__              |
|--------------------|----------------------------|
|   `MAP_SHARED`       |   Changes are shared.      |
|   `MAP_PRIVATE`      |   Changes are private.     |
|   `MAP_FIXED`        |   Interpret _addr_ exactly.  |
|   `PROT_NONE`        |   Data cannot be accessed. |




It is implementation-defined whether `MAP_FIXED` shall be supported. 
`MAP_FIXED` shall be supported on XSI-conformant systems.

`MAP_SHARED` and `MAP_PRIVATE` describe the disposition of write references to the memory object. If `MAP_SHARED` is specified, write
references shall change the underlying object. If `MAP_PRIVATE` is specified, modifications to the mapped data by the calling process
shall be visible only to the calling process and shall not change the underlying object. It is unspecified whether modifications to
the underlying object done after the `MAP_PRIVATE` mapping is established are visible through the `MAP_PRIVATE` mapping. Either
`MAP_SHARED` or `MAP_PRIVATE` can be specified, but not both. The mapping type is retained across `fork()`.

The state of synchronization objects such as mutexes, semaphores, barriers, and conditional variables placed in shared memory
mapped with `MAP_SHARED` becomes undefined when the last region in any process containing the synchronization object is unmapped.

When fildes represents a typed memory object opened with either the `POSIX_TYPED_MEM_ALLOCATE` flag or the
`POSIX_TYPED_MEM_ALLOCATE_CONTIG` flag, `mmap()` shall, if there are enough resources available, map _len_ bytes allocated
from the corresponding typed memory object which were not previously allocated to any process in any processor that may access that
typed memory object. If there are not enough resources available, the function shall fail. If fildes represents a typed
memory object opened with the `POSIX_TYPED_MEM_ALLOCATE_CONTIG` flag, these allocated bytes shall be contiguous within the typed
memory object. If fildes represents a typed memory object opened with the `POSIX_TYPED_MEM_ALLOCATE` flag, these allocated
bytes may be composed of non-contiguous fragments within the typed memory object. If fildes represents a typed memory object
opened with neither the `POSIX_TYPED_MEM_ALLOCATE_CONTIG` flag nor the `POSIX_TYPED_MEM_ALLOCATE` flag, _len_ bytes starting at
offset off within the typed memory object are mapped, exactly as when mapping a file or shared memory object. In this case,
if two processes map an area of typed memory using the same off and _len_ values and using file descriptors that refer
to the same memory pool (either from the same port or from a different port), both processes shall map the same region of storage.

When `MAP_FIXED` is set in the _flags_ argument, the implementation is informed that the value of pa shall be
_addr_, exactly. If `MAP_FIXED` is set, `mmap()` may return `MAP_FAILED` and set errno to `EINVAL`. If a `MAP_FIXED`
request is successful, then any previous mappings [ML|MLR]   or memory locks   for those whole pages containing any part of the address range [pa,pa+_len_)
shall be removed, as if by an appropriate call to `munmap()`, before the new mapping is
established.

When `MAP_FIXED` is not set, the implementation uses _addr_ in an implementation-defined manner to arrive at pa. The
pa so chosen shall be an area of the address space that the implementation deems suitable for a mapping of _len_ bytes
to the file. All implementations interpret an _addr_ value of 0 as granting the implementation complete freedom in selecting
pa, subject to constraints described below. A non-zero value of _addr_ is taken to be a suggestion of a process address
near which the mapping should be placed. When the implementation selects a value for pa, it never places a mapping at
address 0, nor does it replace any extant mapping.

If `MAP_FIXED` is specified and _addr_ is non-zero, it shall have the same remainder as the off parameter, modulo the
page size as returned by `sysconf()` when passed `_SC_PAGESIZE` or `_SC_PAGE_SIZE`. The
implementation may require that off is a multiple of the page size. If `MAP_FIXED` is specified, the implementation may require that
_addr_ is a multiple of the page size. The system performs mapping operations over whole pages. Thus, while the parameter
_len_ need not meet a size or alignment constraint, the system shall include, in any mapping operation, any partial page
specified by the address range starting at pa and continuing for _len_ bytes.

The system shall always zero-fill any partial page at the end of an object. Further, the system shall never write out any
modified portions of the last page of an object which are beyond its end. References within the address range starting at pa
and continuing for _len_ bytes to whole pages following the end of an object shall result in delivery of a SIGBUS signal.

An implementation may generate SIGBUS signals when a reference would cause an error in the mapped object, such as out-of-space
condition.

The `mmap()` function shall add an extra reference to the file associated with the file descriptor fildes which is
not removed by a subsequent `close()` on that file descriptor. This reference shall be
removed when there are no more mappings to the file.

The last data access timestamp of the mapped file may be marked for update at any time between the `mmap()` call and the
corresponding `munmap()` call. The initial read or write reference to a mapped region
shall cause the file's last data access timestamp to be marked for update if it has not already been marked for update.

The last data modification and last file status change timestamps of a file that is mapped with `MAP_SHARED` and `PROT_WRITE` shall
be marked for update at some point in the interval between a write reference to the mapped region and the next call to `msync()` with `MS_ASYNC` or `MS_SYNC` for that portion of the file by any process. If there is no
such call and if the underlying file is modified as a result of a write reference, then these timestamps shall be marked for update
at some time after the write reference.

There may be implementation-defined limits on the number of memory regions that can be mapped (per process or per system).

If such a limit is imposed, whether the number of memory regions that can be mapped by a process is decreased by the use of `shmat()` is implementation-defined. 
If `mmap()` fails for reasons other than `EBADF`, `EINVAL`, or `ENOTSUP`, some of the mappings in the address range
starting at _addr_ and continuing for _len_ bytes may have been unmapped.


## Return value


Upon successful completion, the `mmap()` function shall return the address at which the mapping was placed (pa);
otherwise, it shall return a value of `MAP_FAILED` and set `errno` to indicate the error. The symbol `MAP_FAILED` is defined in
the `<sys/mman.h>` header. No successful return from `mmap()` shall
return the value `MAP_FAILED`.


## Errors


The `mmap()` function shall fail if:


 * `EACCES` - The fildes argument is not open for read, regardless of the protection specified, or fildes is not open for write
and `PROT_WRITE` was specified for a `MAP_SHARED` type mapping.

 * `EAGAIN` - 
The mapping could not be locked in memory, if required by `mlockall()`, due to a lack
of resources. 

 * `EBADF` - The fildes argument is not a valid open file descriptor.

 * `EINVAL` - The value of _len_ is zero.

 * `EINVAL` - The value of _flags_ is invalid (neither `MAP_PRIVATE` nor `MAP_SHARED` is set).

 * `EMFILE` - The number of mapped regions would exceed an implementation-defined limit (per process or per system).

 * `ENODEV` - The fildes argument refers to a file whose type is not supported by `mmap()`.

 * `ENOMEM` - `MAP_FIXED` was specified, and the range [_addr_,_addr_+_len_) exceeds that allowed for the address space of a
process; or, if `MAP_FIXED` was not specified and there is insufficient room in the address space to effect the mapping.

 * `ENOMEM` - 
The mapping could not be locked in memory, if required by `mlockall()`, because it
would require more space than the system is able to supply. 

 * `ENOMEM` - 
Not enough unallocated memory resources remain in the typed memory object designated by fildes to allocate _len_ bytes.


 * `ENOTSUP` - `MAP_FIXED` or `MAP_PRIVATE` was specified in the _flags_ argument and the implementation does not support this functionality.


The implementation does not support the combination of accesses requested in the _prot_ argument.


 * `ENXIO` - Addresses in the range [off,off+_len_) are invalid for the object specified by fildes.

 * `ENXIO` - `MAP_FIXED` was specified in _flags_ and the combination of _addr_, _len_, and off is invalid for the
object specified by fildes.

 * `ENXIO` - 
The fildes argument refers to a typed memory object that is not accessible from the calling process. 

 * `EOVERFLOW` - The file is a regular file and the value of off plus _len_ exceeds the offset maximum established in the open file
description associated with fildes.


The `mmap()` function may fail if:


 * `EINVAL` - The _addr_ argument (if `MAP_FIXED` was specified) or off is not a multiple of the page size as returned by `sysconf()`, or is considered invalid by the implementation.





## Tests

Untested

## Known bugs

None

## See Also 
1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
