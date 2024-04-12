# kill

`kill` is used to send signals to processes. It allows users to terminate processes, stop and continue their execution,
and send other types of signals for various purposes.

## Usage

```console
kill [-s signal | -signal] <pid [...]>
```

- `-s signal`: Specifies the signal to send by name. The SIG prefix is optional (e.g., TERM or SIGTERM).
- `-signal`: Specifies the signal to send by its name without the -s option and with a mandatory - prefix
(e.g., -TERM or -SIGTERM).
- `<pid>`: The process ID(s) to which the signal should be sent. Multiple PIDs can be specified, separated by spaces.

## Description

`kill` is commonly used to manage process execution. By default, if no signal is specified, `SIGTERM` is sent,
which requests the termination of the process. The utility can send almost any signal,
allowing for nuanced process control.

## Signals

Commonly used signals include:

`SIGTERM`: Gracefully terminate the process.
`SIGKILL`: Immediately terminate the process. Cannot be ignored.
`SIGSTOP`: Stop the process's execution.
`SIGCONT`: Continue the process if it is currently stopped.

## See also

1. [Phoenix-RTOS shell](../psh.md)
2. [Phoenix-RTOS Utilities](../../utils.md)
3. [Table of Contents](../../../README.md)
