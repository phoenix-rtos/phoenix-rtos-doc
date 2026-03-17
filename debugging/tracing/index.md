# Tracing

(tracing_common_prerequisites)=

## Common prerequisites
* Phoenix-RTOS 3.4
* Host dependencies for hostutils (Ubuntu):
  ```bash
  sudo apt install babeltrace2 python3-bt2 protobuf-compiler python3-protobuf
  ```

```{toctree}
:maxdepth: 1

large-targets.md
small-targets.md
obtaining-trace-from-qemu.md
using-perfetto.md
custom-events.md
```
