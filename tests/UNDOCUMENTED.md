# Tests Documentation — Undocumented Areas

## 1. YAML Target Filtering

Test YAML configs support `targets: include: [...]` and `targets: exclude: [...]` for SoC-specific test selection. This critical feature for multi-target testing is not documented.

## 2. Test Directory Organization

The test repository contains organized subdirectories:
- `busybox/` — BusyBox command tests
- `proc/` — Process management tests
- `disk/` — Disk/storage tests
- `mem/` — Memory management tests
- `net/` — Networking tests
- `devices/` — Device driver tests
- `fs/` — Filesystem tests

The structure and conventions for organizing tests are not documented.

## 3. `fails/` Subdirectory

Sample tests include a `fails/` subdirectory whose purpose (expected failures, regression tracking) is not explained.

## 4. trunner Package

The test runner (`trunner/`) package internals and capabilities are not documented beyond the high-level overview. Developers extending the test framework need to understand:
- Package architecture
- Available assertion/matching primitives
- Configuration options
- How to add new test backend types

## 5. Multi-File Test Patterns

Complex tests spanning multiple source files and multiple YAML configurations are not covered. Only simple helloworld-style examples are documented.

## 6. Test Environment Variables

- `LONG_TEST=y` is documented for enabling long-running port tests
- Additional environment variables affecting test behavior are not listed
- How custom syspage configurations interact with test runs is unclear

## 7. Test Result Reporting

How test results are collected, aggregated, and reported across targets is not documented. CI/CD integration patterns are missing.
