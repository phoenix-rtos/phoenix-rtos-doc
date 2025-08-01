# ls

`ls` list files and directories stored in filesystem.

---

Using `ls` command with `-h` parameter prints help message as follows:

```console
usage: ls [options] [files]
  -1:  one entry per line
  -a:  do not ignore entries starting with .
  -d:  list directories themselves, not their contents
  -f:  do not sort
  -h:  prints help
  -l:  long listing format
  -r:  sort in reverse order
  -S:  sort by file size, largest first
  -t:  sort by time, newest first
```

By default, `.` (current directory) is used as `[files]`. Executing sole:

```console
ls
```

Will print all normal files and directories in current directory.

Options (excluding `-h`) may be used together, so the following command:

```console
ls -laf bin/
```

Will print all files and directories in `bin/` directory including those starting with `.`, unsorted and with one entry
per line.
