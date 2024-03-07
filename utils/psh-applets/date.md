# date

The `date` utility provided as a `psh` applet can be used to print or set system date and time.

---

If used with `-h` parameter it prints the help message with possible arguments and parameters as follows:

```bash
Usage: date [-h] [-s EPOCH] [-d @EPOCH] [+FORMAT]
  -h:  shows this help message
  -s:  set system time described by EPOCH (POSIX time format)
  -d:  display time described by EPOCH (POSIX time format)
  FORMAT: string with POSIX date formatting characters
NOTE: FORMAT string not supported by options: '-s', '-d'
```

## Date printing

To print current system date execute command without parameters. Default format of date is
`<dayname, dd monthname yy hh:mm:ss>`:

```bash
(psh)% date
Thu, 01 Jan 70 00:00:01
(psh)%
```

Printing accepts `FORMAT` string that describes how or what part of date should be printed. Available formats are listed
further in this document. Format string should start with `+` sign.

``` bash
(psh)% date +%H:%M:%S
00:02:34
(psh)%
```

## Date setting

To set date execute command with option `-s` and pass time in standard POSIX format
(seconds since `Thu, 01 Jan 70 00:00:00`). Successful set of date prints newly set date.

```bash
(psh)% date -s 1630000000
Thu, 26 Aug 21 17:46:41
(psh)% date
Thu, 26 Aug 21 17:46:42
(psh)%
```

__Note:__ `-s` option temporarily does not support `FORMAT` string, and it accepts

## Date parsing

To parse and print date without setting it execute command with option `-d` and pass `@EPOCH` parameter which is in
standard POSIX time.

```bash
(psh)% date -d @1630000000
Thu, 26 Aug 21 17:46:41
(psh)%
```

## See also

1. [Phoenix-RTOS shell](psh.md)
2. [Phoenix-RTOS Utilities](README.md)
3. [Table of Contents](../README.md)
