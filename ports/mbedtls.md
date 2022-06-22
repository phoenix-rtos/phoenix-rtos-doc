Mbed TLS Port
===================

## Contents

- [General information](#general-information)
- [Supported version](#supported-version)
- [Using mbedtls](#using-mbedtls)
- [Running tests](#running-tests)
- [Known bugs](#known-bugs)

## General information

There are stored adaptations needed to run `mbedtls` on Phoenix-RTOS.

Mbed TLS is a C library that implements cryptographic primitives, X.509 certificate manipulation, and the SSL/TLS and DTLS protocols. Its small code footprint makes it suitable for embedded systems. For more information please visit the [Mbed TLS Github](https://github.com/Mbed-TLS).

## Supported version

The supported version is [v2.28.0](https://github.com/Mbed-TLS/mbedtls/tree/v2.28.0).
## Using mbedtls

To use functions provided by `mbedtls` please place the specific `mbedtls` library in `LIBS` variable in `Makefile` and include the required header file. Below is the example of using `mbedtls_aes_init()` in user program `hello`:

 - Makefile - linking with all provided mbedtls libraries, You can use only required ones here.
  ```
  NAME := hello
  LOCAL_SRCS := main.c
  LIBS := libmbedtls libmbedx509 libmbedcrypto

  include $(binary.mk)
  ```

 - Source code:

  ```C
  #include <stdio.h>
  #include <mbedtls/aes.h>

  int main(void)
  {
    mbedtls_aes_context ctx;

    mbedtls_aes_init( &ctx );
    printf("Hello World!!\n");
  
    return 0;
  }
  ```

- Note: Please remember that `PORTS_MBEDTLS` should be set to `y` in the specific building script in `_projects` directory or using an environment variable.

## Running tests

To build `mbedtls` tests please set `LONG_TEST=y` environment variable before calling `build.sh`.

In order to run the specific test please type in psh: `/bin/test_name mbedtls_test_configs/test_name.datax`, for example:

```
/bin/test_suite_ssl mbedtls_test_configs/test_suite_ssl.datax
```

 - Running all tests and parsing results isn't supported in Phoenix-RTOS Test Runner yet.

 - The following tests require setting current date before running(using `date` command in psh, for example: `date -s @1653990793`), because of certificates' creation date:
   - `test_suite_ssl`
   - `test_suite_x509`

 - Because tests use `.datax` files and most of them use `data_files` directory running tests is supported only on `rootfs` platforms.

## Known bugs

Currently, there are 3/2695 unresolved failing test cases in `test_suite_ssl`:
 - `DTLS renegotiation: no legacy renegotiation`,

 - `DTLS renegotiation: legacy renegotiation`,

 - `DTLS renegotiation: legacy break handshake`

There are also failing test cases not related strictly to problems with `mbedtls`:

 - `net_poll beyond FD_SETSIZE` in `test_suite_net` - https://github.com/phoenix-rtos/phoenix-rtos-project/issues/408

 - `Overwrite 0 -> 3` in `test_suite_psa_its` - https://github.com/phoenix-rtos/phoenix-rtos-project/issues/409
