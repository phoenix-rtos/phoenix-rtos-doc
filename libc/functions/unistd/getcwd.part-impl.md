# getcwd

## Synopsis

```c
#include <unistd.h>

char *getcwd(char *buf, size_t size);
```

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The purpose is to get the `pathname` of the current working directory. The `getcwd()` function shall place an absolute
`pathname` of the current working directory in the array pointed to by _buf_, and return _buf_. The `pathname` shall
contain no components that are dot or dot-dot, or are symbolic links.

If there are multiple `pathnames` that `getcwd()` could place in the array pointed to by _buf_, one beginning with a
single `<slash>` character and one or more beginning with two `<slash>` characters, then `getcwd()` shall place the
`pathname` beginning with a single `<slash>` character in the array. The `pathname` shall not contain any unnecessary
`<slash>` characters after the leading one or two `<slash>` characters.

The _size_ argument is the size in bytes of the character array pointed to by the _buf_ argument. If _buf_ is a `null`
pointer, the behavior of `getcwd()` is unspecified.

## Return value

Upon successful completion, `getcwd()` shall return the _buf_ argument. Otherwise, `getcwd()` shall return a `null`
pointer and set `errno` to indicate the error. The contents of the array pointed to by _buf_ are then undefined.

## Errors

The `getcwd()` function shall fail if:

* [`EINVAL`] - The _size_ argument is `0`.
* [`ERANGE`] - The _size_ argument is greater than `0`, but is smaller than the length of the `string + 1`.

The `getcwd()` function may fail if:

* [`EACCES`] - Search permission was denied for the current directory, or read, or search permission was denied for a
 directory above the current directory in the file hierarchy.
* [`ENOMEM`] - Insufficient storage space is available.

## Tests

Untested

## Known bugs

None
