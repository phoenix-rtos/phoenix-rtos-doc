# Phoenix Shell (psh)

Phoenix Shell is a compact program that enables you to control the Phoenix-RTOS from the command line.

`psh` presents itself with a commandline where user can enter commands to control the Phoenix-RTOS system, manage files and processes. 

## Overview
 - [How to use `psh`](#Usage)
 - [Available commands](#Applets)
 - [Executing `psh`](#Executing)
 - [Restrictions](#Restrictions)

## Usage
If psh is in control of the commandline each new line starts with `(psh)%` prompt. User can then enter desired command. See [Applets](#Applets) for list of available commands.

If `psh` command is run with `-h` parameter the help message is displayed as follows:
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
* [`edit`](psh-applets/edit.md) - text editor
* [`exec`](psh-applets/exec.md)       - replace shell with the given command
* [`exit`](psh-applets/exit.md)       - exits shell
* [`help`](psh-applets/help.md)       - prints this help message
* [`history`](psh-applets/history.md)    - prints commands history
* `kill`       - terminates process
* [`ls`](psh-applets/ls.md)         - lists files in the namespace
* `mem`        - prints memory map
* [`mkdir`](psh-applets/mkdir.md)      - creates directory
* `mount`      - mounts a filesystem
* [`nc`](psh-applets/nc.md)         - TCP and UDP connections and listens
* [`nslookup`](psh-applets/nslookup.md)   - queries domain name servers
* `perf`       - track kernel performance events
* [`ping`](psh-applets/ping.md)       - ICMP ECHO requests
* [`ps`](psh-applets/ps.md)         - prints processes and threads
* [`pshapp`](psh-applets/pshapp.md)     - delivers `psh` interpreter, `exit`, `pshlogin` and `history` commands
* [`pshlogin`](psh-applets/pshlogin.md) - launches `psh` with user authentication
* `reboot`     - restarts the machine
* `sync`       - synchronizes device
* [`sysexec`](psh-applets/sysexec.md) - launch program from syspage using given map
* [`top`](psh-applets/top.md)        - top utility
* [`touch`](psh-applets/touch.md)      - changes file timestamp
* [`/`](psh-applets/runfile.md)      - executes a file

## Executing
When executing `psh` from a name "psh" it is only possible to enter interactive mode or executa a script with `-i`. 

If `psh` is launched with different name that corresponds to an available applet then the new psh executes only that applet and then close. Executing `psh` with different name can be achieved using symbolic links.


## Restrictions

Only one interactive session of `psh` can be run in a scope of a `psh` process. For now running `psh` does not spawn new process, so in order to invoke a second, independent shell user must execute a `psh` binary file. See [`exec`](psh-applets/exec.md) or [`/`](psh-applets/runfile.md) for examples.