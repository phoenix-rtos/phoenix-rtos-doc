# crypt

## Synopsis

`#include <unistd.h>`

`char *crypt(const char *key, const char *salt);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `crypt()` function is a string encoding function. The algorithm is implementation-defined.

The _key_ argument points to a string to be encoded. The _salt_ argument shall be a string of at least two bytes in
length not including the `null` character chosen from the set:

```c
a b c d e f g h i j k l m n o p q r s t u v w x y z
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
0 1 2 3 4 5 6 7 8 9 . /
```

The first two bytes of this string may be used to perturb the encoding algorithm.

The return value of `crypt()` points to static data that is overwritten by each call.

The `crypt()` function need not be thread-safe.

## Return value

Upon successful completion, `crypt()` shall return a pointer to the encoded string. The first two bytes of the returned
value shall be those of the _salt_ argument. Otherwise, it shall return a null pointer and set `errno` to indicate the
error.

## Errors

The `crypt()` function shall fail if:

* `ENOSYS` - The functionality is not supported in this implementation.

## Tests

Untested

## Known bugs

None
