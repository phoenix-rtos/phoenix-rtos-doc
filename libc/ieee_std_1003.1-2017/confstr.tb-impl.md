### Synopsis

`#include <unistd.h>`

`size_t confstr(int name, char *buf, size_t len);`

###Description

The `confstr()` function gets configuration-defined string values.

Arguments:
<u>name</u> - the name of the system variable to be queried,
<u>buf</u> - the buffer for the return value,
<u>len</u> - the buffer length.

<u>name</u> argument is one of the following:

`_CS_PATH`
`_CS_POSIX_V7_ILP32_OFF32_CFLAGS`
`_CS_POSIX_V7_ILP32_OFF32_LDFLAGS`
`_CS_POSIX_V7_ILP32_OFF32_LIBS`
`_CS_POSIX_V7_ILP32_OFFBIG_CFLAGS`
`_CS_POSIX_V7_ILP32_OFFBIG_LDFLAGS`
`_CS_POSIX_V7_ILP32_OFFBIG_LIBS`
`_CS_POSIX_V7_LP64_OFF64_CFLAGS`
`_CS_POSIX_V7_LP64_OFF64_LDFLAGS`
`_CS_POSIX_V7_LP64_OFF64_LIBS`
`_CS_POSIX_V7_LPBIG_OFFBIG_CFLAGS`
`_CS_POSIX_V7_LPBIG_OFFBIG_LDFLAGS`
`_CS_POSIX_V7_LPBIG_OFFBIG_LIBS`
`_CS_POSIX_V7_THREADS_CFLAGS`
`_CS_POSIX_V7_THREADS_LDFLAGS`
`_CS_POSIX_V7_WIDTH_RESTRICTED_ENVS`
`_CS_V7_ENV`

`confstr()` copies that value into <u>buf</u>.   <u>len</u> is the length of the buffer unless <u>len</u> is `0` or <u>buf</u> is a null pointer. If the string to be returned is longer than <u>len</u> bytes, including the terminating null, then `confstr()` truncates the string to <u>len</u>-1 bytes and null-terminate the result. The application can detect that the string was truncated by comparing the value returned by `confstr()` with <u>len</u>.

If <u>len</u> is `0` and <u>buf</u> is a null pointer, then `confstr()` returns the integer value as defined below, but does not return a string. If <u>len</u> is `0` but <u>buf</u> is not a null pointer, the result is unspecified.

As with `sysconf()`, an application can distinguish between an invalid <u>name</u> parameter value and one that corresponds to a configurable variable that has no configuration-defined value, by checking if `errno` is modified. 

###Return value

If <u>name</u> has a configuration-defined value, the function returns the size of the buffer that would be needed to hold the entire configuration-defined value including the terminating null. If this return value is greater than <u>len</u>, the string returned in <u>buf</u> is truncated.

If <u>name</u> is invalid, `confstr()` returns `0` and sets `errno` to indicate the error.

If <u>name</u> does not have a configuration-defined value, `confstr()` returns `0` and leaves `errno` unchanged.

###Errors

[`EINVAL`] - the value of the <u>name</u> argument is invalid.

###Implementation tasks

* add necessary definitions to `<unistd.h>` file,
* implement the function.

###EXAMPLES

A call: `confstr(_CS_V7_ENV, buf, sizeof(buf));`
Result: the string stored in <u>buf</u> contains a `<space>`-separated list of the `variable=value` environment variable pairs an implementation requires as a part of specifying a conforming environment, as described in the implementations' conformance documentation.

A call: `confstr(name, (char *)NULL, (size_t)0);`
Result: the size of the buffer needed for the string value.
Then you can use `malloc()` to allocate a buffer of the required size and call `confstr()` again to get the string. Alternately, you can allocate a fixed, static buffer that is big enough to hold most answers (perhaps `512` or `1024` bytes), but then use `malloc()` to allocate a larger buffer if needed.

The `confstr()` function copies the returned string into a buffer supplied by the application instead of returning a pointer to a string. This allows a cleaner function in some implementations (such as those with lightweight threads) and resolves questions about when the application must copy the string returned.