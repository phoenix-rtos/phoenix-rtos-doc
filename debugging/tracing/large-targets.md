# Large targets quick-start

Tracing quick-start for targets with plenty of storage, i.e. `ia32-generic`,
`riscv64-generic`, `armv7a7-imx6ull`, etc.

## Objectives

1. Record the trace on your target
2. Retrieve trace output directory from your target to host PC
3. Pass the directory to `convert.sh` to get a single file readable by Perfetto Trace Viewer
4. Open the trace file in the Perfetto GUI

## Prerequisites

Aside from {ref}`tracing_common_prerequisites`, you need:

* A way of transporting files from your target to host PC.

## Step 1: record the trace

You can use `libtrace` library from `phoenix-rtos-corelibs` or use psh applet
`perf`:

```text
(psh)% perf
Usage: perf -m MODE -o [stream output dir] [options]
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
(psh)% perf -m trace -o my_trace
```

This starts a trace for 3 seconds and captures it periodically (each 100 ms) to `my_trace` directory. You can fine-tune the priority of the applet with `-p`, change the sleeptime to alter periodical reads with `-s` or modify the capture buffer size.

A successful invocation:

```text
(psh)% perf -m trace -o my_trace
trace: started
trace: wrote 425/524288 bytes to channel_meta0
trace: wrote 110655/524288 bytes to channel_event0
trace: wrote 725/524288 bytes to channel_meta1
trace: wrote 201391/524288 bytes to channel_event1
trace: wrote 4737/524288 bytes to channel_meta2
trace: wrote 249235/524288 bytes to channel_event2
trace: wrote 750/524288 bytes to channel_meta3
trace: wrote 148859/524288 bytes to channel_event3
# ...
trace: stopped
trace: wrote 150/524288 bytes to channel_meta0
trace: wrote 58562/524288 bytes to channel_event0
# ...
trace: wrote 0/524288 bytes to channel_meta3
trace: wrote 0/524288 bytes to channel_event3
trace: nothing left to write, exiting
trace: finished
(psh)%
```


````{note}
If you notice something like:

```text
trace: warning: read buffer was fully utilized during perf_read - read rate may be too slow
```

This means the perf applet couldn't keep up with the rate of event emission.
Increase the buffer size `-b` (just remember that it is an exponential
parameter) or decrease the sleep time `-s`.
````

## Step 2: gather the trace from target to host

This step is mostly up to you as the means to do it are rather target-specific.
If you are gathering the trace on some QEMU target though, see RTOS-A-136548076.

Your objective here is to acquire a directory structured like the following and
have it on host PC:

```text
$ tree my_trace
my_trace
├── channel_event0
├── channel_event1
├── channel_event2
├── channel_event3
├── channel_meta0
├── channel_meta1
├── channel_meta2
└── channel_meta3
```

Example explanation: This is from `ia32-generic-qemu` target run with 4 cores,
hence 8 channels - 1 meta + 1 event per core

## Step 3: invoke convert.sh

Once you have your trace on host in a folder, say `$TRACE_DIR`, you can now
invoke:

```text
$ cd $PRTOS_PROJECT/phoenix-rtos-hostutils/trace
$ ./convert.sh $TRACE_DIR $PRTOS_PROJECT/phoenix-rtos-kernel/perf/tsdl/metadata out.pftrace
```

The resulting `out.pftrace` is ready to be opened in Perfetto.

## Step 4: view the trace in the Perfetto GUI

See {doc}`using-perfetto`.
