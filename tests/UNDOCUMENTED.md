# Tests Documentation — Undocumented Areas

## 1. YAML Target Filtering

Test YAML configs support `targets: include: [...]` and `targets: exclude: [...]` for SoC-specific test selection. Used extensively, e.g., `psh/test.yaml` (lines 2, 18, 50, 67, 82) contains multiple target filter blocks. This critical feature for multi-target testing is not documented.

## 2. Test Directory Organization

The test repository contains 30+ organized subdirectories including:
- `busybox/` — BusyBox command tests
- `proc/` — Process management tests
- `disk/` — Disk/storage tests
- `mem/` — Memory management tests
- `net/` — Networking tests
- `devices/` — Device driver tests
- `fs/` — Filesystem tests
- `libc/` — C library tests
- `psh/` — PSH shell tests
- `virtio/` — VirtIO tests
- Library tests: `libalgo/`, `libcache/`, `libtinyaes/`, `libtrace/`, `libuuid/`
- Framework tests: `mbedtls/`, `micropython/`, `coremark_pro/`
- Additional: `cpp/`, `gfx/`, `ioctl/`, `meterfs/`, `port/`, `stdio/`, `sys/`, `thread-local/`, `waitpid/`, `initfini/`, `setjmp/`, `lsb_vsx/`

The structure and conventions for organizing tests are not documented.

## 3. `fails/` Subdirectory

The `sample/test/fails/` directory exists in the test repository. Its purpose (expected failures, regression tracking, negative test examples) is not explained. Appears to be part of the sample/template test structure.

## 4. trunner Package

The test runner (`trunner/`) package contains:
- `test_runner.py` — Main test runner
- `ctx.py` — Test context management
- `dut.py` — Device Under Test abstraction
- `host.py` — Host-side operations
- `config.py` — Configuration handling
- `types.py` — Type definitions
- `text.py` — Text processing utilities
- `extensions.py` — Extension system
- `tools/` — Utility tools
- `harness/` — Test harness implementations
- `target/` — Target abstractions

Internals and capabilities are not documented beyond the high-level overview.

## 5. Multi-File Test Patterns

Complex tests spanning multiple source files and multiple YAML configurations are not covered. Only simple helloworld-style examples are documented.

## 6. Test Environment Variables

- `LONG_TEST=y` is documented for enabling long-running port tests
- Additional environment variables affecting test behavior are not listed
- How custom syspage configurations interact with test runs is unclear

## 7. Test Result Reporting

How test results are collected, aggregated, and reported across targets is not documented. CI/CD integration patterns are missing.
