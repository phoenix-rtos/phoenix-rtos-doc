# cp

The `cp` utility provided as a `psh` applet can be used to copy files.

---

If used with `-h` parameter it prints the help message with possible arguments and parameters as follows:

```console
Usage: cp [options] SOURCE DESTINATION
  -p:  preserve file attributes
  -h:  shows this help message
```

To copy a file using `cp` source and destination must be specified as arguments. Following command:

```console
cp foo bar
```

Creates a file `bar` which is a copy of file `foo`. If `bar` existed it is overwritten.

To create a copy of the same name destination filename can be omitted, and only destination directory can be provided.
Following command:

```console
cp foo directory/
```

creates a file `foo` in the directory `directory`, which is a copy of an original file `foo`.
