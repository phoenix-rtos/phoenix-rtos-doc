# SHA-256 library (libsha256)

SHA-256 message digest (`FIPS 180-4`) for callers that need a hash without pulling in a TLS stack, for example to verify
what has been written back to flash or to check a firmware payload before applying it.

The implementation is a single-file extract from [libtomcrypt](https://github.com/libtom/libtomcrypt), kept in the
upstream formatting so that it stays diffable against the original. The snapshot it was taken from is recorded in
`libsha256/sbom.json`.

## Application interface

### Data types

- `sha256_ctx_t` - hashing state, allocated by the caller and initialized by `sha256_init`. Its contents are internal
to the library.

  ```c
  typedef union {
      struct sha256_state {
          uint64_t length;
          uint32_t state[8], curlen;
          unsigned char buf[SHA256_BLOCK_SIZE];
      } sha256;
  } sha256_ctx_t;
  ```

### Constants

- `SHA256_DIGEST_SIZE` - digest length in bytes (32),
- `SHA256_BLOCK_SIZE` - compression function block length in bytes (64).

### Functions

All functions return `0` on success and a non-zero value on failure (invalid arguments, or a message longer than the
algorithm allows).

- `sha256_init` - Initializes the hashing state `md`. Has to be called before any other operation on it.

  ```c
  int sha256_init(sha256_ctx_t *md);
  ```

- `sha256_process` - Processes `inlen` bytes of `in` through the hash. The API is streaming, so it can be called any
number of times and the message never has to be held in memory as a whole.

  ```c
  int sha256_process(sha256_ctx_t *md, const unsigned char *in, unsigned long inlen);
  ```

- `sha256_done` - Terminates the hash, writing `SHA256_DIGEST_SIZE` bytes of digest to `out`. The state must not be
used afterward without re-initializing it.

  ```c
  int sha256_done(sha256_ctx_t *md, unsigned char *out);
  ```

- `mem_neq` - Compares `len` bytes of `a` and `b` in constant time, returning `0` when they are equal and non-zero when
they are not. Use it wherever inequality means a wrong key or a forged digest - a plain `memcmp()` leaks the position of
the first mismatch through its execution time. Test the result against `0` and never against `1`: a `NULL` argument is
reported with a different non-zero value, so `if (mem_neq(...) == 1)` would accept what it was meant to reject.

  ```c
  int mem_neq(const void *a, const void *b, size_t len);
  ```

## Using libsha256

Add the library to the `LIBS` variable in the `Makefile` and include the header:

- Makefile - linking with the `libsha256` library.

  ```make
  NAME := fwverify
  LOCAL_SRCS := main.c
  LIBS := libsha256

  include $(binary.mk)
  ```

- `main.c` - hashing a file without holding it in memory.

  ```c
  #include <fcntl.h>
  #include <stdio.h>
  #include <unistd.h>

  #include <libsha256.h>

  int main(int argc, char *argv[])
  {
      sha256_ctx_t ctx;
      unsigned char digest[SHA256_DIGEST_SIZE], buf[512];
      ssize_t n;
      int fd, i;

      fd = open(argv[1], O_RDONLY);
      if (fd < 0) {
          return 1;
      }

      sha256_init(&ctx);
      while ((n = read(fd, buf, sizeof(buf))) > 0) {
          sha256_process(&ctx, buf, n);
      }
      close(fd);

      sha256_done(&ctx, digest);
      for (i = 0; i < SHA256_DIGEST_SIZE; i++) {
          printf("%02x", digest[i]);
      }
      printf("\n");

      return 0;
  }
  ```

## Tests

The library is covered by unit tests placed next to it, which are built and run by the build system - see
[Unit tests placed next to the code](../tests/index.md#unit-tests-placed-next-to-the-code).
