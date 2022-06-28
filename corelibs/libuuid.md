Universally Unique identifiers library
===================

Linux libuuid compliant library used to generate unique identifiers for objects that may be accessible beyond the system.
According to `RFC 4122` and `DCE 1.1` (Distributed Computing Environment) currently supported UUID format is variant 1, version 4 (randomly/pseudo-randomly generated).

## Contents

- [General information](#general-information)
- [Using libuuid](#using-libuuid)
- [Running tests](#running-tests)

## General information

Linux libuuid compliant library used to generate unique identifiers for objects that may be accessible beyond the system.
According to `RFC 4122` and `DCE 1.1` (Distributed Computing Environment) currently supported UUID format is variant 1, version 4 (randomly/pseudo-randomly generated).

## Using libuuid

To use functions provided by `libuuid` please add the library to the `LIBS` variable in `Makefile` and include the required header file. Below is a simple example, which could be placed in `_user` directory:

 - Makefile - linking with `libbuid` library.
  ```
  NAME := uuidgen
  LOCAL_SRCS := main.c
  LIBS := libuuid

  include $(binary.mk)
  ```

 - Source code:

  ```C
  #include <stdio.h>
  #include <uuid/uuid.h>

  int main(void)
  {
    uuid_t uu;
    char uuStr[37];

    uuid_generate(uu);
    uuid_unparse(uu, uuStr);

    printf("Generated identifier: %s\n", uuStr);

    return 0;
  }
  ```

 - Sample result:

  ```
  (psh)% /usr/bin/uuidgen
  Generated identifier: 81fb691c-fb2d-4546-54ef-231edff56a7f
  (psh)% 

  ```

  ## Running tests

  Phoenix-RTOS UUID Library provides the basic set of unit tests, which is available in [phoenix-rtos-tests](https://github.com/phoenix-rtos/phoenix-rtos-tests/tree/master). It can be run for different platforms, here is the example for the `ia32-generic-qemu` target:

  ```
  python3 phoenix-rtos-tests/runner.py -T ia32-generic-qemu -t phoenix-rtos-tests/libuuid/
  ```
