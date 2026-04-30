# Common routines

Common kernel routines are located in `phoenix-rtos-kernel/lib/`.
They provide small data structures and utility functions used by the hardware abstraction layer, process subsystem,
virtual memory subsystem, and syscall handlers.

| Component | Source files | Purpose |
| --- | --- | --- |
| Assertions | `assert.c`, `assert.h` | Kernel assertion handling. |
| Binary search | `bsearch.c`, `bsearch.h` | Generic binary search helper. |
| Circular buffers | `cbuffer.c`, `cbuffer.h` | Byte buffer storage used by kernel code that needs FIFO semantics. |
| Identifier trees | `idtree.c`, `idtree.h` | Numeric ID allocation and lookup for resources and ports. |
| Lists | `list.c`, `list.h` | Intrusive list operations. |
| Formatted output | `printf.c`, `printf.h` | Kernel formatted printing support. |
| Random numbers | `rand.c`, `rand.h` | Kernel pseudo-random number helper. |
| Red-black trees | `rb.c`, `rb.h` | Ordered intrusive tree operations. |
| String utilities | `strutil.c`, `strutil.h` | String parsing and conversion helpers. |

The umbrella header `lib.h` includes these interfaces and defines common helpers such as `min()`, `max()`, `swap()`,
`round_page()`, `lib_atomicIncrement()`, and `lib_atomicDecrement()`.

## Coverage notes

The common routines are internal kernel helpers.
Callers provide storage for intrusive nodes and buffers unless a specific helper allocates memory.
The helpers do not provide their own locking, so callers must hold the subsystem lock that protects the containing
object.

## API contracts

### `idtree`

The caller embeds `idnode_t` in the owned object and initializes the tree with `lib_idtreeInit()`.
Callers serialize access.
Allocation returns a negative error when no ID can be assigned.

### `cbuffer`

The caller owns the backing memory passed to `_cbuffer_init()`.
The buffer helper does not lock.
Read and write functions return the number of bytes processed.

### `list`

The caller embeds `next` and `prev` links in the listed object.
The list helper does not lock and does not allocate.

### `rb`

The caller embeds `rbnode_t` and supplies a comparison function.
Insert returns an error for duplicate ordering.
The tree helper does not lock.

### `strutil`

`lib_strdup()` returns an allocated copy, and callers own the returned memory.
`lib_splitname()` edits the supplied path buffer while splitting base and directory pointers.

### Atomic helpers

The caller owns the referenced object.
`lib_atomicIncrement()` uses relaxed ordering.
`lib_atomicDecrement()` uses acquire-release ordering.

The process, port, and VM subsystems wrap these helpers with their own locks and lifetime rules.
