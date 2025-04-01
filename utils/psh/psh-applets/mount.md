# mount

`mount` is used to mount filesystems to a specified directory in the file system hierarchy.
This tool is fundamental for accessing the contents of different storage devices or filesystem images
within the system's directory structure.

## Usage

```console
mount <source> <target> <fstype> <mode> [data]
```

- `<source>`: Specifies the device or filesystem image to be mounted.

- `<target>`: The directory onto which the filesystem will be mounted. This directory must already exist.

- `<fstype>`: The type of filesystem to be mounted.

- `<mode>`: Mount flags specified as a numerical value, which control various mount options.

- `[data]`: Optional. Filesystem-specific data that may be required for some types of mounts, such as mount options.

## See also

1. [Feniks-RTOS shell](../index.md)
2. [Feniks-RTOS Utilities](../../index.md)
3. [Table of Contents](../../../index.md)
