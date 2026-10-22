# WebAssembly Micro Runtime Port

## General information

There are stored adaptations needed to run `wamr` on Phoenix-RTOS.

WebAssembly Micro Runtime (WAMR) is a lightweight standalone WebAssembly
runtime with small footprint, high performance and highly configurable features
for applications ranging from embedded, IoT, edge to Trusted Execution Environment,
smart contract, cloud native.

## Supported version

The supported version is [2.4.2](https://github.com/wasm-micro-runtime/wasm-micro-runtime/tree/WAMR-2.4.2)

## Quickstart for ia32-generic-qemu

`wamr` port is not built by default on `ia32-generic-qemu` platform. To build it, it must be added
to your targets/projects port list in `_project/ia32-generic-qemu/ports.yaml`.

The image used for emulation can be built with:

```sh
TARGET=ia32-generic-qemu ./phoenix-rtos-build/build.sh clean all
```

The port builds the interpreter executable and a static library for use with external projects.
Additionally, the port allows the developer to add native functions that will be exported for use in the
WebAssembly environment.

## Running the interpreter

The WAMR interpreter binary is located in `/usr/bin/iwasm`. Refer to `/usr/bin/iwasm --help` for usage.

## Using wamr as a library

WAMR can be embedded into projects as a static library. In order to use it, a project must link it by including
`libiwasm` in `LIBS` variable in its Makefile.

Here is a sample Makefile, linking `libiwasm`:

```makefile
NAME := hello
LOCAL_SRCS := main.c
LIBS := libiwasm

include $(binary.mk)
```

Refer to [WAMR documentation](https://github.com/wasm-micro-runtime/wasm-micro-runtime/blob/WAMR-2.4.2/doc/embed_wamr.md#the-runtime-initialization) for usage of the library.

## Adding native calls to WASM environment

The Phoenix-RTOS WAMR port has a builtin mechanism for compiling added native functions into WAMR runtime.
Those functions can be later called by a WASM app running in the WAMR runtime.

Below is an example source code implementing and exporting a simple native function for WAMR

```c
#include <wasm_export.h>

int foo1(wasm_exec_env_t exec_env, int a, int b)
{
	return a * b + 3;
}

NativeSymbol native_symbols[] = {
	{ "foo1", foo1, "(ii)i", NULL },
};

int n_native_symbols = sizeof(native_symbols) / sizeof(*native_symbols);
```

Such file would have to be saved under any file name in `phoenix-rtos-ports/wamr/native_libs/` directory.

Full example in our ports is located in `phoenix-rtos-ports/wamr/native_libs_example/` directory.

For native function implementation guidelines, refer to [WAMR documentation](https://github.com/wasm-micro-runtime/wasm-micro-runtime/blob/WAMR-2.4.2/doc/export_native_api.md)
