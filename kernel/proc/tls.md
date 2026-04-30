# Thread-local storage

Thread-local storage (TLS) state is tracked at the process and thread levels.
The process stores the template TLS state and the global offset table pointer, and each thread stores the active
`hal_tls_t` instance used by the HAL during context switching.

## Data model

`phoenix-rtos-kernel/proc/process.h` stores process TLS fields in `process_t`:

| Field | Purpose |
| --- | --- |
| `got` | Global offset table pointer used when a thread context is created or replaced. |
| `tls` | Process-level `hal_tls_t` template copied into thread TLS storage. |

`phoenix-rtos-kernel/proc/threads.h` stores `hal_tls_t tls` in each `thread_t`.
When a selected thread has a nonzero TLS base, the scheduler calls `hal_cpuTlsSet()` before restoring the thread
context.

## Initialization and destruction

`process_tlsInit()` allocates a per-thread TLS block in the target process map with `vm_mmap()`.
The size is rounded to a page boundary.
The function copies initialized TLS data from the source template, clears the TLS BSS area, and stores a self pointer at
the aligned end of the block.

`process_tlsDestroy()` releases a TLS block with `vm_munmap()`.
The reaper path calls it for a ghost thread when the thread owns a TLS block.

`proc_threadCreate()` initializes thread TLS from the process template when the process has nonzero `tdata_sz` or
`tbss_sz`.
If the process has no TLS data, the thread TLS fields are set to zero.
The same function passes the TLS pointer to `hal_cpuCreateContext()` and sets the context GOT with `hal_cpuSetCtxGot()`.

## Process creation and execution

The ELF loading path derives process TLS from program headers and records the GOT pointer for user code.
During `vfork()`, the child initially shares the parent map and copies both process TLS and thread TLS state from the
parent.
On `exec()`, the current thread switches through the execution stack path and receives TLS and GOT state for the new
program image.

Architecture-specific HAL code defines the contents of `hal_tls_t` and programs the target TLS register.
The process subsystem treats `hal_tls_t` as an opaque HAL object except for allocation size and copy operations.
