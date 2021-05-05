###Synopsis

`#include <stdio.h>`

`int ferror(FILE *stream);`

###Description

The `ferror()` function tests the error indicator on a stream.

Arguments:

<u>stream</u> - the stream to be tested.

The `ferror()` function tests the error indicator on a stream pointed by <u>stream</u>.

###Return value

The `ferror()` function returns `1`  if and only if the error indicator is set for <u>stream</u>, otherwise it returns `0`.

###Errors

No errors are defined.

###Implementation tasks

None.