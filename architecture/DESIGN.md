# Architecture — Design Observations

## Microkernel with Message Passing IPC

Phoenix-RTOS v3+ uses a pure microkernel architecture. All device drivers, file servers, and emulation layers run in user space. The kernel provides only: memory management, process/thread management, IPC primitives, and hardware abstraction.

## IPC as System Bus

Message passing is not just a communication mechanism — it serves as the system's central bus:
- File operations route through filesystem server ports
- Device I/O routes through device server ports
- Network operations route through LwIP server ports
- POSIX calls route through posixsrv ports

## Component Architecture

```
Applications
  ↓ (message passing)
Servers: posixsrv, filesystems, LwIP, device drivers
  ↓ (syscalls)
Microkernel: memory, processes, IPC, HAL
  ↓
Hardware
```

## Scalability through Modularity

Adding new functionality requires:
1. Implement a server process
2. Register a port in the namespace
3. Handle messages on that port

No kernel modification needed for new drivers, filesystems, or services.

## Dual MMU/Non-MMU Support

The architecture scales from Cortex-M (no MMU) to Cortex-A/x86/RISC-V (full MMU). Same APIs but different internal implementations, controlled by conditional compilation.

## Standards Compatibility

POSIX emulation via user-level server allows legacy application execution. The `posixsrv` process translates POSIX semantics to native microkernel message passing.
