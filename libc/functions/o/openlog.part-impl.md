# Synopsis 
`#include <syslog.h>`</br>
` void closelog(void);`</br>
` void openlog(const char *ident, int logopt, int facility);`</br>
` int setlogmask(int maskpri);`</br>
` void syslog(int priority, const char *message, ... /* arguments */); `</br>

## Status
Partially implemented
## Conformance
IEEE Std 1003.1-2017
## Description


The `syslog()` function shall send a message to an implementation-defined logging facility, which may log it in an
implementation-defined system log, write it to the system console, forward it to a list of users, or forward it to the logging
facility on another host over the network. The logged message shall include a message header and a message body. The message header
contains at least a timestamp and a tag string.

The message body is generated from the message and following arguments in the same manner as if these were arguments to
`printf()`, except that the additional conversion specification `%m` shall be
recognized; it shall convert no arguments, shall cause the output of the error message string associated with the value of
`errno` on entry to `syslog()`, and may be mixed with argument specifications of the `%n$` form.

If a complete conversion specification with the m conversion specifier character is not just `%m`, the behavior is
undefined. A trailing `<newline>` may be added if needed.

Values of the _priority_ argument are formed by OR'ing together a severity-level value and an optional _facility_ value. If
no _facility_ value is specified, the current default facility value is used.

Possible values of severity level include:

 * `LOG_EMERG` - A panic condition.

 * `LOG_ALERT`A condition that should be corrected immediately, such as a corrupted system database.

 * `LOG_CRIT` - Critical conditions, such as hard device errors.

 * `LOG_ERR` - Errors.

 * `LOG_WARNING` - Warning messages.

 * `LOG_NOTICE` - Conditions that are not error conditions, but that may require special handling.

 * `LOG_INFO` - Informational messages.

 * `LOG_DEBUG` - Messages that contain information normally of use only when debugging a program.

The _facility_ indicates the application or system component generating the message. Possible _facility_ values include:

 * `LOG_USER` - Messages generated by arbitrary processes. This is the default facility identifier if none is specified.

 * `LOG_LOCAL0` - Reserved for local use.

 * `LOG_LOCAL1` - Reserved for local use.

 * `LOG_LOCAL2` - Reserved for local use.

 * `LOG_LOCAL3` - Reserved for local use.

 * `LOG_LOCAL4` - Reserved for local use.

 * `LOG_LOCAL5` - Reserved for local use.

 * `LOG_LOCAL6` - Reserved for local use.

 * `LOG_LOCAL7` - Reserved for local use.

The `openlog()` function shall set process attributes that affect subsequent calls to `syslog()`. The _ident_
argument is a string that is prepended to every message. The _logopt_ argument indicates logging options. Values for
_logopt_ are constructed by a bitwise-inclusive OR of zero or more of the following:

 * `LOG_PID` - Log the process ID with each message. This is useful for identifying specific processes.

 * `LOG_CONS` - Write messages to the system console if they cannot be sent to the logging facility. The `syslog()` function ensures that
the process does not acquire the console as a controlling terminal in the process of writing the message.

 * `LOG_NDELAY` - Open the connection to the logging facility immediately. Normally the open is delayed until the first message is logged. This
is useful for programs that need to manage the order in which file descriptors are allocated.

 * `LOG_ODELAY` - Delay open until `syslog()` is called.

 * `LOG_NOWAIT` - Do not wait for child processes that may have been created during the course of logging the message. This option should be used
by processes that enable notification of child termination using `SIGCHLD`, since `syslog()` may otherwise block waiting for a
child whose exit status has already been collected.

The _facility_ argument encodes a default facility to be assigned to all messages that do not have an explicit facility
already encoded. The initial default facility is `LOG_USER`.

The `openlog()` and `syslog()` functions may allocate a file descriptor. It is not necessary to call `openlog()`
prior to calling `syslog()`.

The `closelog()` function shall close any open file descriptors allocated by previous calls to `openlog()` or
`syslog()`.

The `setlogmask()` function shall set the log priority mask for the current process to _maskpri_ and return the
previous mask. If the _maskpri_ argument is 0, the current log mask is not modified. Calls by the current process to
`syslog()` with a priority not set in _maskpri_ shall be rejected. The default log mask allows all priorities to be
logged. A call to `openlog()` is not required prior to calling `setlogmask()`.

Symbolic constants for use as values of the _logopt_, _facility_, _priority_, and _maskpri_ arguments are
defined in the `<syslog.h>` header.


## Return value


The `setlogmask()` function shall return the previous log _priority_ mask. The `closelog()`, `openlog()`, and
`syslog()` functions shall not return a value.


## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None

## See Also 
1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)