###Synopsis

`#include <fmtmsg.h>`

`int fmtmsg(long classification, const char *label, int severity, const char *text, const char *action, const char *tag);`

###Description

The `fmtmsg()` function displays messages in a specified format instead of the traditional `printf()` function.

Arguments:

<u>classification</u> - the source of the message and direction of the display of the formatted message.
<u>label</u> - the source of the message.
<u>severity</u> - the seriousness of the condition.
<u>text</u> - the error condition that produced the message.
<u>action</u> - the first step to be taken in the error-recovery process. It is preceded with the prefix: "TO FIX:". The action string is not limited to a specific size.
<u>tag</u> - an identifier that references on-line documentation for the message. 

Based on a message's classification component, `fmtmsg()` writes a formatted message either to standard error, to the console, or to both.

A formatted message consists of up to five components (`fmtmsg()` arguments)as defined below. The component <u>classification</u> is not part of a message displayed to the user, but defines the source of the message and directs the display of the formatted message.

<b><u>classification</u></b> contains the sum of identifying values constructed from the constants defined below. Each identifier from a subclass may be used in combination with a single identifier from a different subclass. Two or more identifiers from the same subclass should not be used together, with the exception of identifiers from the display subclass. (Both display subclass identifiers may be used so that messages can be displayed to both standard error and the system console.)

<b>Major Classifications</b> - the source of the condition. Identifiers are: 
        
 * `MM_HARD` (hardware), 
 * `MM_SOFT` (software), 
 * `MM_FIRM` (firmware).
        
<b>Message Source Subclassifications</b> - the type of software in which the problem is detected. Identifiers are: 
        
 * `MM_APPL` (application), 
 * `MM_UTIL` (utility), 
 * `MM_OPSYS` (operating system).
        
<b>Display Subclassifications</b> - the place where the message is to be displayed. Identifiers are: 
        
 * `MM_PRINT` (the standard error stream), 
 * `MM_CONSOLE` (the system console). 
        
One or both identifiers may be used.
        
<b>Status Subclassifications</b> - the possibility of recovery from the condition. Identifiers are: 
        
 * `MM_RECOVER` (recoverable), 
 * `MM_NRECOV` (non-recoverable).
 * `MM_NULLMC` (no classification component is supplied for the message).
        
<u>label</u> - the source of the message. The format is two fields separated by a <colon>:
        * the first field is up to 10 bytes, 
        * the second is up to 14 bytes.
    
<u>severity</u> - the seriousness of the condition. Identifiers for the levels of severity are:

  * `MM_HALT` - the application has encountered a severe fault and is halting. Produces the string "HALT".
  * `MM_ERROR` - the application has detected a fault. Produces the string "ERROR".
  * `MM_WARNING` - a condition that is out of the ordinary, that might be a problem, and should be watched. Produces the string "WARNING".
  * `MM_INFO` - information about a condition that is not in error. Produces the string "INFO".
  * `MM_NOSEV` - no severity level is supplied for the message.

<u>text</u> - the error condition that produced the message. The character string is not limited to a specific size. If the character string is empty, then the text produced is unspecified.
    
<u>action</u> - the first step to be taken in the error-recovery process. The `fmtmsg()` function precedes the action string with the prefix: "TO FIX:". The action string is not limited to a specific size.
    
<u>tag</u> - an identifier that references on-line documentation for the message. Suggested usage is that <u>tag</u> includes the label and a unique identifying number. A sample tag is "XSI:cat:146".

The `MSGVERB` environment variable (for message verbosity) determines for `fmtmsg()` which message components are to select when writing messages to standard error. The value of `MSGVERB` is a <colon>-separated list of optional keywords. Valid keywords are: 

 * label, 
 * severity, 
 * text,
 * action,
 * tag. 
        
If `MSGVERB` contains a keyword for a component and the component's value is not the component's null value, `fmtmsg()` includes that component in the message when writing the message to standard error. If `MSGVERB` does not include a keyword for a message component, that component is not included in the display of the message. The keywords may appear in any order. If `MSGVERB` is not defined, if its value is the null string, if its value is not of the correct format, or if it contains keywords other than the valid ones listed above, `fmtmsg()` selects all components.

`MSGVERB` determines which components are selected for display to standard error. All message components are included in console messages.

###Return value

One of the following values:

`MM_OK` - The function succeeded.
`MM_NOTOK` - The function failed completely.
`MM_NOMSG` - The function was unable to generate a message on standard error, but otherwise succeeded.
`MM_NOCON` - The function was unable to generate a console message, but otherwise succeeded. 
    
###Errors

No errors are defined.

###Implementation tasks

 * Implement `fmtmsg.h` file.
 * Implement the `fmtmsg` function.
 