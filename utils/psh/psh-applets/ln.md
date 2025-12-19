# ln

`ln` is used to create links between files. It supports the creation of both hard links and symbolic links,
enabling users to create multiple references to a single file or directory.

## Usage

```shell
ln [-s] TARGET LINK_NAME
ln TARGET... LINK_NAME
```

- `-s`: Create a symbolic link instead of a hard link.
- `TARGET`: The target file or directory to which the link refers.
- `LINK_NAME`: The name of the newly created link.

### Description

`ln` can create two types of links:

- Hard links: Create an additional directory entry for a file. Hard links cannot span file systems
and cannot link to directories.

- Symbolic links: Create a special type of file that serves as a reference or pointer to another file or directory,
which can span file systems and can link to directories.
