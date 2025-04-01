# tty

`tty` command is a utility that allows users to print the current tty device or
change the tty device associated with the shell.

## Usage

```console
tty [OPTION] [path_to_device]
```

- `h`: Displays help information.

- `path_to_device`: Specifies the tty device to switch to. If this argument is omitted, the current tty device is
printed.

## Examples

Print current tty device:

```console
tty
```

Change tty device:

```console
tty /dev/console
```

## See also

1. [Feniks-RTOS shell](../index.md)
2. [Feniks-RTOS Utilities](../../index.md)
3. [Table of Contents](../../../index.md)
