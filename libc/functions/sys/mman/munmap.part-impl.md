# munmap

## Synopsis

`#include <sys/mman.h>`

`int munmap(void *addr, size_t len);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `munmap()` function shall remove any mappings for those entire pages containing any part of the address space of the
process starting at _addr_ and continuing for _len_ bytes. Further, references to these pages shall result in the
generation of a `SIGSEGV` signal to the process. If there are no mappings in the specified address range, then
`munmap()` has no effect.

The implementation may require that _addr_ be a multiple of the page size as returned by `sysconf()`.

If a mapping to be removed was private, any modifications made in this address range shall be discarded.

Any memory locks (see `mlock()` and `mlockall()`) associated with this address range shall be removed, as if by an
appropriate call to `munlock()`.

If a mapping removed from a typed memory object causes the corresponding address range of the memory pool to be
inaccessible by any process in the system except through allocatable mappings (that is, mappings of typed memory objects
opened with the `POSIX_TYPED_MEM_MAP_ALLOCATABLE` flag), then that range of the memory pool shall become deallocated and
may become available to satisfy future typed memory allocation requests.

A mapping removed from a typed memory object opened with the `POSIX_TYPED_MEM_MAP_ALLOCATABLE` flag shall not affect in
any way the availability of that typed memory for allocation.
The behavior of this function is unspecified if the mapping was not established by a call to `mmap()`.

## Return value

Upon successful completion, `munmap()` shall return `0`; otherwise, it shall return `-1` and set `errno` to indicate the
error.

## Errors

The `munmap()` function shall fail if:

* `EINVAL` - Addresses in the range (_addr_, _addr_ + _len_) are outside the valid range for the address space of a
process.

* `EINVAL` - The _len_ argument is `0`.

The `munmap()` function may fail if:

* `EINVAL` - The _addr_ argument is not a multiple of the page size as returned by `sysconf()`.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../../functions.md)
2. [Table of Contents](../../../../README.md)
