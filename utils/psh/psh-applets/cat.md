# cat

The `cat` utility provided as a `psh` applet can be used to concatenate files and print their content to standard
output.

---

If used with `-h` parameter it prints the help message with possible arguments and parameters as follows:

```shell
Usage: cat [options] [files]
  -h:  shows this help message
```

To print a file using `cat` the filename must be specified as an argument. Following command:

```shell
cat file1 file2
```

The command above will concatenate and print files `file1` and `file2` (in that order) to standard output.
