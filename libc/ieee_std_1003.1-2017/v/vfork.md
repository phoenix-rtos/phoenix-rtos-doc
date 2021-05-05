###Synopsis

`#include <unistd.h>`

`extern int vfork(void);`


###Description

vfork(), just like fork(2), creates a child process of the calling process. 
The calling thread is suspended until the child terminates (either normally, by calling _exit(2), or abnormally, after delivery of a fatal signal), or it makes a call to execve(2). Until that point, the child shares all memory with its parent, including the stack. The child must not return from the current function or call exit(3), but may call _exit(2).

As with fork(2), the child process created by vfork() inherits copies of various of the caller's process attributes (e.g., file descriptors, signal dispositions, and current working directory); the vfork() call differs only in the treatment of the virtual address space, as described above.

Signals sent to the parent arrive after the child releases the parent's memory (i.e., after the child terminates or calls execve(2)).