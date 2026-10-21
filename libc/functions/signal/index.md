# signal.h

```{note}
**POSIX deviations:** real-time signals are not supported, therefore the `SIGRTMIN` and `SIGRTMAX` macros, required by
IEEE Std 1003.1-2017, are not defined in `<signal.h>`. Phoenix-RTOS provides the standard set of signals only, which
covers the signalling needs of the embedded applications it is designed for while keeping the signal handling in the
kernel compact.
```

```{toctree}
:maxdepth: 1
:glob:

*
```
