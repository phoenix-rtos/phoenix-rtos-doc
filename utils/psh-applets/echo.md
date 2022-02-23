# echo

The `echo` utility provided as a `psh` applet can be used to print a line of text to standard output.

---

If used with `-h` parameter it prints the help message with possible arguments and parameters as follows:

```bash
Usage: echo [options] [string]
  -h:  shows this help message
```

To print a line of text using an `echo` the text must be specified as an argument. Following command:

```bash
echo foo bar
```

The command above will concatenate and print strings `foo` and `bar` (in that order, with a space between them) to the standard output.


Exit code (of a program or an applet) can be displayed using an `echo` command:

```bash
echo $?
```

## See also

1. [Phoenix-RTOS shell](psh.md)
2. [Phoenix-RTOS Utilities](README.md)
3. [Table of Contents](../README.md)
