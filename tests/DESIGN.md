# Tests — Design Observations

## Three-Component Architecture

Clean separation of concerns:
1. **Binary**: Compiled C test code (Unity framework in `unity/` or custom)
2. **Python harness**: Orchestration and assertion via pexpect pattern matching (in `trunner/harness/`)
3. **YAML config**: Declarative test metadata, target filtering, timeout configuration (e.g., `psh/test.yaml`)

Supporting infrastructure: `runner.py` (top-level entry), `resolve_binaries.py`, `requirements.txt` for Python dependencies.

## Target-Aware Test Selection

YAML `targets` field enables per-SoC test filtering:
```yaml
targets:
  include: [host-generic-pc]
```
Essential for hardware-specific tests that only make sense on certain platforms.

## Python-Based Orchestration

Uses `pexpect` library for serial/console interaction. Cross-platform test execution (host QEMU, physical hardware, simulators) through consistent serial interface.

## Unity Framework Integration

Supports both custom harnesses and the Unity C testing framework. This dual approach allows low-level bare-metal tests alongside higher-level functional tests.
