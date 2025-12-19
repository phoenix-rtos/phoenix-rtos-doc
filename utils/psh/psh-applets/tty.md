# tty

`tty` command is a utility that allows users to print the current tty device or
change the tty device associated with the shell.

## Usage

```shell
tty [OPTION] [path_to_device]
```

- `h`: Displays help information.

- `path_to_device`: Specifies the tty device to switch to. If this argument is omitted, the current tty device is
printed.

## Examples

Print current tty device:

```shell
tty
```

Change tty device:

```shell
tty /dev/console
```
