# rmdir

`rmdir` command is used to remove empty directories.

## Usage

```text
rmdir [-p] DIRECTORY...
```

### Options

- `p`: Removes parent directories as well, provided they are also empty.
This option allows for the removal of a directory hierarchy if all directories in the path are empty.

### Arguments

- `DIRECTORY...`: Specifies one or more directories to be removed.
These directories must be empty for the operation to succeed.

## Examples

Remove a Single Empty Directory:

```text
rmdir dir
```

Remove a Directory and Its Empty Parents:

```text
rmdir -p dir/emptydir/anotheremptydir
```

## See also

1. [Phoenix-RTOS shell](psh.md)
2. [Phoenix-RTOS Utilities](../README.md)
3. [Table of Contents](../../README.md)
