# Adding custom kernel events
All events emitted by the kernel are declared in
`phoenix-rtos-kernel/perf/trace-events.h`. First, there is an event ID
declaration in enum:

```c
enum {
	/* ... */
	PERF_EVENT_SYSCALL_ENTER = 0x28,
	/* ... */
};
```

Underneath is a probe definition:

```c
static inline void trace_eventSyscallEnter(u8 n, u16 tid)
{
	struct {
		u8 n;
		u16 tid;
	} __attribute__((packed)) ev;

	PERF_EVENT_BODY(PERF_EVENT_SYSCALL_ENTER, ev, NULL, {
		ev.n = n;
		ev.tid = tid;
	});
}
```

The `trace_eventXXX()` probe can then be used anywhere in the kernel, for
example:

```c
#include "perf/trace-events.h"
/* ... */
void *syscalls_dispatch(int n, char *ustack, cpu_context_t *ctx)
{
	/* ... */
	trace_eventSyscallEnter(n, tid);

	retval = ((void *(*)(char *))syscalls[n])(ustack);

	trace_eventSyscallExit(n, tid);
	/* ... */
	return retval;
}
```

These declarations reflect the structure of events contained in the
`phoenix-rtos-kernel/perf/tsdl/metadata` file:

```
event {
	name = syscall_enter;
	id = 0x28;
	fields := struct {
		u8 n;
		u16 tid;
	};
};
```

The `tsdl/metadata` file is a CTF metadata stream conforming to [CTF 1.8](
https://diamon.org/ctf/v1.8.3/). It is a contract to the outside world about the
events understandable by the kernel. The kernel emits events in binary form and
the `tsdl/metadata` is the only source of information about the structure of our
events that the babeltrace2 has when parsing the binary streams (this is what
happens under the hood in `ctf_to_proto.py` which is under the hood of
`convert.sh`).

```{warning}
When adding custom events, you must ensure `events.h` matches `tsdl/metadata`,
**otherwise the trace will be impossible to parse by the host utilities.**
```
