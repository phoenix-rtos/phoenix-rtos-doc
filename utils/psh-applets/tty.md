# tty

`tty` command is a utility that allows users to print the current tty device or
change the tty device associated with the shell.

## Usage

```text
tty [OPTION] [path_to_device]
```

- `h`: Displays help information.

- `path_to_device`: Specifies the tty device to switch to. If this argument is omitted, the current tty device is
printed.

## Examples

Print current tty device:

```text
tty
```

Change tty device:

```text
tty /dev/console
```

## See also

1. [Phoenix-RTOS shell](../psh.md)
2. [Phoenix-RTOS Utilities](../README.md)
3. [Table of Contents](../../README.md)
