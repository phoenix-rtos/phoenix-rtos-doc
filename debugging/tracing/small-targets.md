# Small (RTT) targets quick-start

Tracing quick-start for targets with constrained resources that support RTT
transfer over J-Link (i.e. `armv7m7-imxrt117x`).

```{warning}
Currently, only single-core targets are supported. It can be fairly easily
extended to multi-core if you expose additional buffers in
`plo/devices/pipe-rtt/rtt.c`.
```

## Objectives

1. Ensure RTT tracing back-end is correctly set up on your target
2. Record a trace on your target and gather it on host over RTT
3. Pass the directory to `convert.sh` to get a single file readable by Perfetto Trace Viewer
4. Open the trace file in the Perfetto GUI

## Prerequisites

Aside from {ref}`tracing_common_prerequisites`, you need:

* A working RTT transfer on your target (`.rtt` map, ID 2 and ID 3 TX channels
  of at least 1024 B and similar channels for subsequent IDs if your target is
  multi-core)

## Step 1: ensure RTT tracing back-end is set up correctly

In the `board_config.h` for your target, ensure the following options are set:

```c
#define RTT_ENABLED      1
#define RTT_ENABLED_PLO  1
#define PERF_RTT_ENABLED 1
#define RTT_PERF_BUFFERS 1
```

## Step 2: record the trace and gather it on host over RTT

On host, run `collect_rtt_trace.py` from `phoenix-rtos-hostutils/trace` with a
path to your OpenOCD config, say `$MY_OCD_CONFIG`, and a destination folder, say
`$TRACE_DIR`:

```text
$ cd $PRTOS_PROJECT/phoenix-rtos-hostutils/trace
$ ./collect_rtt_trace.py $MY_OCD_CONFIG $TRACE_DIR
```

A successful invocation:

```text
$ ./collect_rtt_trace.py ../../evkb_common/ocd/imxrt_wip.cfg output
OpenOCD started
Open On-Chip Debugger 0.12.0+dev-01784-gae4877c57 (2025-06-27-10:45)
Licensed under GNU GPL v2
For bug reports, read
        http://openocd.org/doc/doxygen/bugs.html
Warn : Interface already configured, ignoring
DEPRECATED! use 'gdb breakpoint_override', not 'gdb_breakpoint_override'
force hard breakpoints
Info : J-Link V9 compiled May  7 2021 16:26:12
Info : Hardware version: 9.60
Info : VTarget = 3.327 V
Info : clock speed 4000 kHz
Info : SWD DPIDR 0x6ba02477
Info : [imxrt.cpu] Cortex-M7 r1p2 processor detected
Warn : [imxrt.cpu] Erratum 3092511: Cortex-M7 can halt in an incorrect address when breakpoint and exception occurs simultaneously
Info : The erratum 3092511 workaround will resume after an incorrect halt
Info : [imxrt.cpu] target has 8 breakpoints, 4 watchpoints
Info : [imxrt.cpu] Examination succeed
Info : [imxrt.cpu] starting gdb server on 3333
Info : Listening on port 3333 for gdb connections
Info : Listening on port 18021 for rtt connections
Info : Listening on port 18022 for rtt connections
Info : Listening on port 18023 for rtt connections
Info : Listening on port 18024 for rtt connections
Info : rtt: Searching for control block 'SEGGER RTT'
Info : rtt: Control block found at 0x2003ff00
Info : Listening on port 6666 for tcl connections
Info : Listening on port 4444 for telnet connections
Info : accepting 'rtt' connection on tcp/18023
Info : accepting 'rtt' connection on tcp/18024
Connected to 2 channels
Saving traces to /home/adam/prtos/perf/phoenix-rtos-hostutils/trace/output
Ready to gather events. Do ^C when the trace has finished
```

Now, start the trace on your target. You can use `libtrace` library from
`phoenix-rtos-corelibs` or use psh applet `perf`:

```text
(psh)% perf
Usage: perf -m MODE [options]
Modes:
  trace - kernel tracing
Options:
  -t [timeout] (default: 3000 ms)
  -b [bufsize exp] (default: 18 -> (2 << 18) B)
  -s [sleeptime] (default: 100 ms)]
  -j [start | stop] - just start/stop perf and exit
  -p [prio]
```

The minimal invocation is:

```text
(psh)% perf -m trace
```

This starts a trace for 3 seconds and emits it over RTT.

A successful invocation:

```text
(psh)% perf -m trace
trace: started
trace: stopped
trace: nothing left to write, exiting
trace: finished
(psh)%
```

While the trace is gathering, the log from `collect_rtt_trace.py` should display
the current transfer rate and the amount of data read so far:

```text
Rate: 29.89 KB/s
channel_meta0: 2.45 KB
channel_event0: 91.19 KB
```

Once the trace is finished, terminate `collect_rtt_trace.py` with ^C (SIGINT).

````{note}
If you notice something like:

```text
kernel (perf_traceFinish:312): event delay detected 2 times - event receiver couldn't keep up
kernel (perf_traceFinish:313): start ts=913491309 delay ts=915280482 stop ts=916571720
```

This means the RTT receiver couldn't keep up with the rate of event emission.
The events were still captured, but the kernel was unable to put the events into
the RTT buffer immediately and it had to actively wait. This may be a concern to
you or not, depending on how many times the delay has occured and how long it
was. Usually delays are caught when the rate of event emission drastically
changes. This is still being investigated.
````

## Step 3: invoke convert.sh

Once you have your trace on host in a folder, say `$TRACE_DIR`, you can now invoke:

```text
$ cd $PRTOS_PROJECT/phoenix-rtos-hostutils/trace
$ ./convert.sh $TRACE_DIR $PRTOS_PROJECT/phoenix-rtos-kernel/perf/tsdl/metadata out.pftrace
```

The resulting `out.pftrace` is ready to be opened in Perfetto.

## Step 4: view the trace in the Perfetto GUI

See {doc}`using-perfetto`.
