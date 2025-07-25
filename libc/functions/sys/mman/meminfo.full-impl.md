# meminfo

## Synopsis

```c
#include <sys/mman.h>

void meminfo(meminfo_t *info);
```

## Description

The `meminfo()` function shall assign values for a `meminfo_t` structure. The `meminfo_t` implementation is presented
below.

```C
typedef struct _meminfo_t {
    struct {
        unsigned int alloc, free, boot, sz;
        int mapsz;
        pageinfo_t *map;
    } page;

    struct {
        unsigned int pid, total, free, sz;
        int mapsz, kmapsz;
        entryinfo_t *kmap, *map;
    } entry;
} meminfo_t;
```

The structure consists of two following parts: `page` and `entry`.

The page, in general, is a representation of RAM physical memory's part. For more information about paging technique
please refer to the [`Memory management chapter`](../../../../kernel/vm/../index.md) and
[`Page allocator chapter`](../../../../kernel/vm/page.md).

Each of the structure's elements has been briefly described:

* `alloc` - Size of allocated pages in bytes,
* `free` - Size of free pages in bytes,
* `boot` - Size of pages reserved by the internal boot firmware in bytes,
* `sz` - Size of the `page_t` structure which describes each physical page available,
* `mapsz` - Number of all available pages, both free and allocated. It only applies to target architectures with `MMU`
(memory management unit).
* `map` - Array (in fact pointer to an array) with information about each of the available pages in `pageinfo_t` format.

If `mapsz` has been passed to the `meminfo()` function with `-1` value `mapsz` and `map` won't be changed.

An entry describes one memory segment, and it's one abstraction layer higher than a page. Entries compose a memory map
which is address space, for example, intended for kernel. Read more about memory mapping in
[`Memory mapper chapter`](../../../../kernel/vm/mapper.md).

The `entry` structure consists of following elements:

* `pid` - Mapper process ID,
* `total` - Size of all available entries in bytes,
* `free` - Size of free entries in bytes,
* `sz` - Size of the `map_entry_t` structure which describes an entry,
* `mapsz` - Number of all available entries,
* `kmapsz` - Number of entries associated with kernel,
* `kmap` - Array (in fact pointer to an array) with information about each of the entry associated with kernel in
`entryinfo_t` format.
* `map` - Array (in fact pointer to an array) with information about each of the available entries in `entryinfo_t`
format.

If `mapsz` has been passed to the `meminfo()` function with `-1` value `mapsz` and `map` won't be changed.

Similarly to `mapsz`, if `kmapsz` has been passed to the `meminfo()` function with `-1` value `kmapsz` and `kmap`
won't be changed.

## Return value

The `meminfo()` function doesn't return anything.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None
