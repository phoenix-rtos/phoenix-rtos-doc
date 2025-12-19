# bind

`bind` is used to bind a device to a directory, effectively linking a device node to a specific filesystem location.

## Usage

```shell
bind <source> <target>
```

- `source`: Specifies the device node to be bound. This is typically a path in the device hierarchy, such as /dev/sda.
- `target`: Specifies the directory to which the source device will be bound. This must be an existing directory.
