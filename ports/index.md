# Ports

Open-source tools adapted to Phoenix-RTOS are called ports. A source code of each port is downloaded from its official
website as an archive file. Next, the file is unpacked and compiled using the appropriate toolchain.
All these steps are performed during a building process when the ports component is specified. Read more about
building components in the [Building](../building/index.md) chapter.

The [phoenix-rtos-ports](https://github.com/phoenix-rtos/phoenix-rtos-ports) repository mostly consists of specific
building scripts and patches for each tool.
If you don't know what are `phoenix-rtos` repositories you can check the [Project repository](../project/index.md)
chapter.

## Components

Following ports are possible to use:

- `busybox` - application suite that provides several UN*X utilities,
- `curl` - command-line tool for transferring data using various network protocols,
- `dropbear` - package that provides SSH-compatible server and client,
- `jansson` - library for encoding, decoding and manipulating JSON data,
- `libevent`- library that provides asynchronous event notification,
- `lighttpd`- web server optimized for speed-critical environments,
- `lua` - programming language designed primarily for embedded use in applications,
- `lzo` - portable lossless data compression library,
- `mbedtls` - an open source, portable, easy to use SSL library,
- `micropython` - lean and efficient implementation of the Python 3 programming language,
- `openssl`- toolkit for general-purpose cryptography and secure communication,
- `openvpn`- open source connection protocol used to facilitate a secure tunnel between two points in a network,
- `pcre` - library that implements regular expression pattern matching using the same syntax and semantics as Perl 5,
- `scep` - client-only implementation of the `SCEP` (Cisco System's Simple Certificate Enrollment Protocol),
- `wpa_supplicant` - Wi-Fi Protected Access client and `IEEE 802.1X` supplicant
- `azure_sdk` - Azure IoT C Software Development Kit

```{toctree}
:maxdepth: 1

mbedtls.md
azure_sdk.md
```

<!-- #TODO: add chapters on how to use each of these tools -->
