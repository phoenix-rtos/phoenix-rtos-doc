# Phoenix Shell (psh)

The Phoenix Shell is a compact program that enables you to control Phoenix-RTOS from the command line.

`psh` presents itself with a command line where user can enter commands to control the Phoenix-RTOS system, manage files
and processes.

## Overview

- [How to use `psh`](#usage)
- [Available commands](#applets)
- [Executing `psh`](#executing)
- [Restrictions](#restrictions)

## Usage

If the `psh` is in control of the command line each new line starts with `(psh)%` prompt. The user can then enter the
desired command. See [Applets](#applets) for a list of available commands.

If the `psh` command is run with `-h` parameter the help message is displayed as follows:

```text
usage: psh [options] [script path] or no args to run shell interactively
  -i <script path>:  selects psh script to execute
  -h: shows this help message
```

With `-i` option `psh` can execute a script - fixed set of `psh` commands saved in file.

## Applets

In `psh`, each command or set of commands is a separate applet, here's a list of the available ones:

- `bind` - binds device to directory
- [`cat`](cat.md) - concatenate file(s) to standard output
- [`cd`](cd.md)- change working directory
- [`cp`](cp.md)- copy file
- [`date`](date.md) - print/set the system date
- [`df`](df.md) - prints filesystem statistics
- [`echo`](echo.md) - display a line of text
- [`edit`](edit.md) - text editor
- [`exec`](exec.md) - replace shell with the given command
- [`exit`](exit.md) - exits shell
- [`help`](help.md) - prints this help message
- [`history`](history.md) - prints commands history
- `kill` - terminates process
- [`ls`](ls.md)- lists files in the namespace
- [`mem`](mem.md) - prints memory map
- [`mkdir`](mkdir.md)- creates directory
- `mount`- mounts a filesystem
- [`nc`](nc.md)- TCP and UDP connections and listens
- [`nslookup`](nslookup.md)- queries domain name servers
- [`ntpclient`](ntpclient.md)- set the system's date from a remote host
- `perf` - track kernel performance events
- [`ping`](ping.md) - ICMP ECHO requests
- [`pm`](pm.md)- monitors processes
- [`ps`](ps.md)- prints processes and threads
- [`pshapp`](pshapp.md) - delivers `psh` interpreter, `exit`, `pshlogin` and `history` commands
- [`pshlogin`](pshlogin.md) - launches `psh` with user authentication
- [`pwd`](pwd.md)- prints the name of current working directory
- `reboot` - restarts the machine
- `sync` - synchronizes device
- [`sysexec`](sysexec.md) - launch program from syspage using given map
- [`top`](top.md) - top utility
- [`touch`](touch.md)- changes file timestamp
- [`umount`](umount.md) - unmount a filesystem
- [`uptime`](uptime.md) - prints how long the system has been running
- [`/`](runfile.md)- executes a file

## Executing

When executing the `psh` from a name "psh" it is only possible to enter interactive mode or execute a script with `-i`.

If the `psh` is launched with a different name that corresponds to an available applet then the new `psh` executes only
that applet and then close. Executing `psh` with a different name can be achieved using symbolic links.

## Restrictions

Only one interactive session of the `psh` can be run in a scope of a `psh` process. For now, running `psh` does not
spawn a new process, so in order to invoke a second, independent shell user must execute a `psh` binary file.
See [`exec`](exec.md) or [`/`](runfile.md) for examples.

## See also

1. [Utilities](../README.md)
2. [Table of Contents](../../README.md)