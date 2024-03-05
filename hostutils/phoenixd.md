# Phoenix Daemon (phoenixd)

`phoenixd` is a component responsible for managing communication channels and facilitating the boot process.
It provides functionality for handling various types of requests, including kernel and program loading,
over different communication interfaces such as serial ports, pipes, UDP, and TCP.
Operates as a background service, listening for incoming requests and responding accordingly.

## Usage

```bash
phoenixd [-1] [-k kernel] [-s bindir] [-p serial_device] [-m pipe_file] [-i udp_ip_addr:port] [-t tcp_ip_addr:port] [-u load_addr[:jump_addr]] [-b baudrate] [-o output_file]
```

### Arguments

- `-1`: Enable BSP mode
- `-k, --kernel PATH`: Specify the path to the kernel image
- `-s, --sysdir PATH`: Specify the path to the system directory
- `-p, --serial SERIAL_DEVICE`: Specify serial device(s) for communication
- `-m, --pipe PIPE_FILE`: Specify pipe file(s) for communication
- `-i, --udp UDP_IP_ADDR:PORT`: Specify UDP IP address and port for communication
- `-t, --tcp TCP_IP_ADDR:PORT`: Specify TCP IP address and port for communication
- `-u, --usb LOAD_ADDR[:JUMP_ADDR]`: Specify USB load address and optional jump address
- `-b, --baudrate RATE`: Specify the baud rate for serial communication
- `-a, --append ARGS`: Specify arguments for appending to initrd
- `-x, --execute ARGS`: Specify arguments for execution after initrd
- `-c, --console PATH`: Specify the console server path
- `-I, --initrd PATH`: Specify the initrd server path
- `-o, --output PATH`: Specify the output file path
- `-h, --help`: Display usage information

### Modes

- `--sdp`: For creating images without plugins, suitable for older kernel versions. Limited to 68KB image size.
- `--plugin`: For creating images with all modules in syspage for kernels with plugins. Limited to 4MB image size.
In this mode arguments are passed only to kernel e.g. <kernel_path>="app1;arg1;arg2 app2;arg1;arg2".
- `--upload`: Similar to SDP mode but for kernels with plugins. Limited to 4MB image size.

## See also

1. [Phoenix-RTOS disk tool](psdisk.md)
2. [Phoenix-RTOS serial uploader](psu.md)
3. [Phoenix-RTOS Host Utilities](README.md)
4. [Table of Contents](../README.md)
