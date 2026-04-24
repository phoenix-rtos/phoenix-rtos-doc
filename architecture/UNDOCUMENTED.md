# Architecture Documentation — Undocumented Areas

## 1. Memory Copy Minimization in Message Passing

The architecture uses three strategies for IPC efficiency:
- **Inline**: Small messages (< ~64 bytes) carried in the message structure
- **Shared mapping**: Larger buffers mapped into receiver's address space
- **Zero-copy**: Page-aligned buffers transferred without copying

These optimizations are critical to the architecture's performance but not documented.

## 2. Virtual Memory Sharing Mechanism

How physical memory pages are shared between processes during message passing:
- Page table entry sharing for mapped regions
- Copy-on-write for fork()
- Wrapper pages for partial-page transfers

## 3. System Call Instructions Per Architecture

Each architecture uses different privilege transition mechanisms:
- ARM: SVC instruction
- x86: INT/SYSENTER
- RISC-V: ECALL
- SPARC: trap instructions

The specific system call ABI per architecture is not documented.

## 4. Namespace Structure

The port-based namespace and object identifier system is mentioned but not specified:
- How ports map to filesystem paths
- Resolution order for overlapping registrations
- Namespace hierarchy and traversal

## 5. Memory Management Policies

MMU configuration, page table format, address space layout, and memory protection policies vary by architecture but are undocumented.

## 6. Thread Context Switching

The actual context switch mechanism (saving/restoring CPU state, switching address spaces, updating TLB) is architecturally significant but not described.

## 7. POSIX Emulation Architecture

The POSIX server's role in providing POSIX-compatible interfaces over the microkernel's message passing is mentioned but the architectural details are missing.

## 8. Multi-core Architecture

Multi-core support (per-core scheduling, IPI, spinlock coordination) is implemented but the architectural model is not documented.
