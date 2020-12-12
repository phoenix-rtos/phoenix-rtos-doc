### Synopsis

`#include <unistd.h>`

`int close(int fildes);`

###Compliance
IEEE Std 1003.1-2001

###Description
Closes the file descriptor. 

After this action:

* the descriptor is available for future allocations (especially subsequent calls of `open()`),

* all record locks owned by the process on the file associated with the file descriptor are unlocked,

* when all file descriptors associated with a pipe or FIFO special file are closed, any data remaining in the pipe or FIFO is discarded,

* when all file descriptors associated with an open file description have been closed, the open file description is freed.

* if the link count of the file is `0`, when all file descriptors associated with the file are closed, the space occupied by the file is freed and the file is no longer accessible. 

* if a `STREAMS-based` <u>fildes</u> is closed:
     * if the calling process was previously registered to receive a `SIGPOLL` signal for events associated with that `STREAM`, the calling process is unregistered for events associated with the `STREAM`. 
     * the last `close()` for a `STREAM` causes the `STREAM` associated with <u>fildes</u> to be dismantled. 
     * if `O_NONBLOCK` is not set and there have been no signals posted for the `STREAM`, and if there is data on the module's write queue, `close()` waits for an unspecified time (for each module and driver) for any output to drain before dismantling the `STREAM`.
     * the time delay can be changed via an `I_SETCLTIME` `ioctl()` request. 
     * if the `O_NONBLOCK` flag is set, or if there are any pending signals, `close()` does not wait for output to drain, and dismantles the `STREAM` immediately.

* for `STREAMS-based` pipes, when <u>fildes</u> is associated with one end of a pipe:
     * the last `close()` causes a hangup to occur on the other end of the pipe. 
     * if the other end of the pipe has been named by `fattach()`, then the last `close()` forces the named end to be detached by `fdetach()`. 
     * if the named end has no open file descriptors associated with it and gets detached, the `STREAM` associated with that end shall also be dismantled.

* for pseudo-terminals:
     * if <u>fildes</u> refers to the master side of a pseudo-terminal, and this is the last close a `SIGHUP` signal is sent to the controlling process, if any, for which the slave side of the pseudo-terminal is the controlling terminal. 
     * closing the master side of the pseudo-terminal flushes all queued input and output.
     * if <u>fildes</u> refers to the slave side of a `STREAMS`-based pseudo-terminal, a zero-length message is sent to the master.

* for cancelable asynchronous I/O operation against <u>fildes</u>: when `close()` is called, the I/O operation is cancelled. An I/O operation that is not cancelled completes as if the `close()` operation had not yet occurred. All operations that are not cancelled are completed as if the `close()` blocked until the operations completed. The `close()` operation itself need not block awaiting such I/O completion. 

* if a memory mapped file or a shared memory object remains referenced at the last close (that is, a process has it mapped), then the entire contents of the memory object persists until the memory object becomes unreferenced. If this is the last close of a memory mapped file or a shared memory object and the close results in the memory object becoming unreferenced, and the memory object has been unlinked, then the memory object is removed.

* if <u>fildes</u> refers to a socket, `close()` causes the socket to be destroyed. If the socket is in connection-mode, and the `SO_LINGER` option is set for the socket with non-zero linger time, and the socket has untransmitted data, then `close()` blocks for up to the current linger interval until all data is transmitted.      

###Return value
`0` - upon success, `-1` otherwise (`errno` is set then to the appropriate error).

###Errors

[`EBADF`] - the <u>fildes</u> argument is not a open file descriptor.
[`EINTR`] - the `close()` function was interrupted by a signal.
[`EIO`] - an I/O error occurred while reading from or writing to the file system. 

###Implementation tasks
* implement `STREAM` files, pipes (STREAM as a method of implementing network services and other character-based input/output mechanisms, with the `STREAM` being a full-duplex connection between a process and a device. )
* implement pseudo-terminals specifying that closing the master side of the pseudo-terminal flushes all queued input and output. 
* decide and implement whether any I/O operation is cancelled, and which I/O operation is cancelled upon `close()`.
* implement memory mapped files,
* implement shared memory objects,
* implement error detection as listed above.