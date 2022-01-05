# Phoenix Shell (psh)

The Phoenix Shell is a compact program that enables you to control Phoenix-RTOS from the command line.

`psh` presents itself with a command line where user can enter commands to control the Phoenix-RTOS system, manage files and processes. 

## Overview
 - [How to use `psh`](#Usage)
 - [Available commands](#Applets)
 - [Executing `psh`](#Executing)
 - [Restrictions](#Restrictions)

## Usage
If the `psh` is in control of the command line each new line starts with `(psh)%` prompt. The user can then enter the desired command. See [Applets](#Applets) for a list of available commands.

If the `psh` command is run with `-h` parameter the help message is displayed as follows:
```
usage: psh [options] [script path] or no args to run shell interactively
  -i <script path>:  selects psh script to execute
  -h:                shows this help message
```

With `-i` option `psh` can execute a script - fixed set of `psh` commands saved in file.

## Applets

In `psh`, each command or set of commands is a separate applet, here's a list of the available ones:

* `bind`       - binds device to directory
* [`cat`](psh-applets/cat.md)        - concatenate file(s) to standard output
* [`cd`](psh-applets/cd.md)         - change working directory
* [`cp`](psh-applets/cp.md)         - copy file
* [`date`](psh-applets/date.md)        - print/set the system date
* [`df`](psh-applets/df.md) - prints filesystem statistics
* [`echo`](psh-applets/echo.md)       - display a line of text
* [`edit`](psh-applets/edit.md) - text editor
* [`exec`](psh-applets/exec.md)       - replace shell with the given command
* [`exit`](psh-applets/exit.md)       - exits shell
* [`help`](psh-applets/help.md)       - prints this help message
* [`history`](psh-applets/history.md)    - prints commands history
* `kill`       - terminates process
* [`ls`](psh-applets/ls.md)         - lists files in the namespace
* [`mem`](psh-applets/mem.md)        - prints memory map
* [`mkdir`](psh-applets/mkdir.md)      - creates directory
* `mount`      - mounts a filesystem
* [`nc`](psh-applets/nc.md)         - TCP and UDP connections and listens
* [`nslookup`](psh-applets/nslookup.md)   - queries domain name servers
* [`ntpclient`](psh-applets/ntpclient.md)   - set the system's date from a remote host
* `perf`       - track kernel performance events
* [`ping`](psh-applets/ping.md)       - ICMP ECHO requests
* [`pm`](psh-applets/pm.md)         - monitors processes
* [`ps`](psh-applets/ps.md)         - prints processes and threads
* [`pshapp`](psh-applets/pshapp.md)     - delivers `psh` interpreter, `exit`, `pshlogin` and `history` commands
* [`pshlogin`](psh-applets/pshlogin.md) - launches `psh` with user authentication
* [`pwd`](psh-applets/pwd.md)         - prints the name of current working directory
* `reboot`     - restarts the machine
* `sync`       - synchronizes device
* [`sysexec`](psh-applets/sysexec.md) - launch program from syspage using given map
* [`top`](psh-applets/top.md)        - top utility
* [`touch`](psh-applets/touch.md)      - changes file timestamp
* [`umount`](psh-applets/umount.md) - unmount a filesystem
* [`uptime`](psh-applets/uptime.md) - prints how long the system has been running
* [`/`](psh-applets/runfile.md)      - executes a file

## Executing
When executing the `psh` from a name "psh" it is only possible to enter interactive mode or execute a script with `-i`. 

If the `psh` is launched with a different name that corresponds to an available applet then the new `psh` executes only that applet and then close. Executing `psh` with a different name can be achieved using symbolic links.


## Restrictions

Only one interactive session of the `psh` can be run in a scope of a `psh` process. For now, running `psh` does not spawn a new process, so in order to invoke a second, independent shell user must execute a `psh` binary file. See [`exec`](psh-applets/exec.md) or [`/`](psh-applets/runfile.md) for examples.

## See also

1. [Utilities](README.md)
2. [Table of Contents](../README.md)
