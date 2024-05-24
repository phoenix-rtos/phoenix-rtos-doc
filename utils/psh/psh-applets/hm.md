# hm

`hm` (health monitor) spawn and oversee the execution of specified applications. Its primary function is to ensure that
these applications remain active, automatically respawning them if they terminate unexpectedly.

## Usage

```console
hm progname1[@argv[0]@argv[1]@...argv[n]] [progname2...]
```

### Parameters

- `progname`: The name of the program to be monitored. This is usually the path to the executable.

- `@argv[i]`: Optional arguments for the program, separated by the @ symbol.

## See also

1. [Phoenix-RTOS shell](../index.md)
2. [Phoenix-RTOS Utilities](../../index.md)
3. [Table of Contents](../../../index.md)
