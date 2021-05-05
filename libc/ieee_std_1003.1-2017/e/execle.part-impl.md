###Synopsis
`#include <unistd.h>`

`int execle(const char *path, const char *arg, ...);`

###Description
`execle()` replaces current process image with a new process image. <u>const char *arg</u> can be a series of arguments describing a list of one or more arguments (pointers to null-terminated strings) available to the executed process.

###Return value
If function retunes, an error have occurred. The return value is -1. 

###Errors
On error variable <u>errno</u> is set to indicate an error.
