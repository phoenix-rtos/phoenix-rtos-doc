# Phoenix Shell (psh)

The Phoenix Shell is a compact program that enables you to control Phoenix-RTOS from the command line.

`psh` presents itself with a command line where user can enter commands to control the Phoenix-RTOS system, manage files
and processes.

## Usage

If the `psh` is in control of the command line each new line starts with `(psh)%` prompt. The user can then enter the
desired command. See [Applets](#applets) for a list of available commands.

If the `psh` command is run with `-h` parameter the help message is displayed as follows:

```shell
usage: psh [options] [script path] or no args to run shell interactively
  -i <script path>:  selects psh script to execute
  -h: shows this help message
```

With `-i` option `psh` can execute a script - fixed set of `psh` commands saved in file.

## Applets

In `psh`, each command or set of commands is a separate applet. The basic usage of the majority of these applets is
compatible with POSIX standards. For example, `ls` works like the `ls` user command on Ubuntu
(or other Linux distribution), except for particular arguments that are not supported.
The Phoenix Shell is in ongoing development, which means its behavior can slightly vary,
particularly as new features are introduced.
Here's a list of the available applets:

- [`bind`](psh-applets/bind.md) - binds device to directory
- [`cat`](psh-applets/cat.md) - concatenate file(s) to standard output
- [`cd`](psh-applets/cd.md) - change working directory
- `chmod` - change file permissions
- [`clear`](psh-applets/clear.md) - clear the terminal screen
- [`cp`](psh-applets/cp.md) - copy file
- [`date`](psh-applets/date.md) - print/set the system date
- [`dd`](psh-applets/dd.md) - copy a file according to the operands
- [`df`](psh-applets/df.md) - prints filesystem statistics
- [`dmesg`](psh-applets/dmesg.md) - read kernel ring buffer
- [`echo`](psh-applets/echo.md) - display a line of text
- [`edit`](psh-applets/edit.md) - text editor
- [`exec`](psh-applets/exec.md) - replace shell with the given command
- [`exit`](psh-applets/exit.md) - exits shell (built-in)
- [`export`](psh-applets/export.md) - set and export variables list to environment (built-in)
- `hd` - hex dump
- [`help`](psh-applets/help.md) - prints this help message
- [`history`](psh-applets/history.md) - prints commands history (built-in)
- [`hm`](psh-applets/hm.md) - health monitor, spawns apps and keeps them alive
- [`ifconfig`](psh-applets/ifconfig.md) - configures network interfaces
- [`kill`](psh-applets/kill.md) - terminates process
- [`ln`](psh-applets/ln.md) - make links between files
- [`ls`](psh-applets/ls.md)- lists files in the namespace
- [`mem`](psh-applets/mem.md) - prints memory map
- [`mkdir`](psh-applets/mkdir.md)- creates directory
- [`mount`](psh-applets/mount.md) - mounts a filesystem
- [`nc`](psh-applets/nc.md)- TCP and UDP connections and listens
- [`nslookup`](psh-applets/nslookup.md)- queries domain name servers
- [`ntpclient`](psh-applets/ntpclient.md)- set the system's date from a remote host
- [`perf`](psh-applets/perf.md) - track kernel performance events
- [`ping`](psh-applets/ping.md) - ICMP ECHO requests
- [`pm`](psh-applets/pm.md)- monitors processes
- [`printenv`](psh-applets/printenv.md) - print all or part of environment
- [`ps`](psh-applets/ps.md)- prints processes and threads
- [`pshapp`](psh-applets/pshapp.md) - delivers `psh` interpreter, `exit`, `pshlogin` and `history` commands
- [`pshlogin`](psh-applets/pshlogin.md) - launches `psh` with user authentication
- [`pwd`](psh-applets/pwd.md)- prints the name of current working directory
- [`reboot`](psh-applets/reboot.md) - restarts the machine
- [`reset`](psh-applets/reset.md) - restore terminal from abnormal state
- [`rm`](psh-applets/rm.md) - unlink files or remove empty directories
- [`rmdir`](psh-applets/rmdir.md) - remove empty directories
- `route` - display/modify routing table
- [`sync`](psh-applets/sync.md) - synchronizes device
- [`sysexec`](psh-applets/sysexec.md) - launch program from syspage using given map
- [`top`](psh-applets/top.md) - top utility
- [`touch`](psh-applets/touch.md)- changes file timestamp
- [`tty`](psh-applets/tty.md) - print or replace interactive shell tty device
- [`umount`](psh-applets/umount.md) - unmount a filesystem
- [`unset`](psh-applets/unset.md) - unset list of environment variables
- [`uptime`](psh-applets/uptime.md) - prints how long the system has been running
- [`wget`](psh-applets/wget.md) - downloads a file using http
- [`/`](psh-applets/runfile.md)- executes a file

```{toctree}
:glob:
:hidden:
:maxdepth: 1

psh-applets/*
```

## Executing

When executing the `psh` from a name "psh" it is only possible to enter interactive mode or execute a script with `-i`.

If the `psh` is launched with a different name that corresponds to an available applet then the new `psh` executes only
that applet and then close. Executing `psh` with a different name can be achieved using symbolic links.

## Restrictions

Only one interactive session of the `psh` can be run in a scope of a `psh` process. For now, running `psh` does not
spawn a new process, so in order to invoke a second, independent shell user must execute a `psh` binary file.
See [`exec`](psh-applets/exec.md) or [`/`](psh-applets/runfile.md) for examples.

Applets like `ps` and `top` query process information via [System Calls](../../kernel/syscalls/index.md).

## Architecture

### Applet Registration

Each applet registers itself at load time using the `__attribute__((constructor))` GCC extension. This means no
hardcoded command table is needed  -  applets self-register when the binary is loaded.

```c
void __attribute__((constructor)) cat_registerapp(void) {
    static psh_appentry_t app = { .name = "cat", ... };
    psh_registerapp(&app);
}
```

### Applet Function Conventions

Each applet provides two functions:

- `void psh_<cmd>info(void)`  -  prints a brief description for help output
- `int psh_<cmd>(int argc, char **argv)`  -  main entry point

### Build-Time Applet Selection

The set of compiled-in applets is controlled by a Makefile variable:

```makefile
PSH_COMMANDS ?= $(PSH_ALLCOMMANDS)      # Default: all applets
PSH_PROJECT_DEPS = ...                    # Project-specific additions
```

This allows resource-constrained targets to include only needed commands.

### Symlink Invocation

PSH can be invoked via symlinks. The binary checks `argv[0]` to determine which applet to run. This allows individual
commands to appear as standalone executables in the filesystem.

### Built-in vs Standalone Commands

Some commands listed above are built-in shell functions rather than standalone applets:

- `clear`, `exit`, `reset`, `history`  -  internal shell commands in `pshapp/`
- `export`, `unset`  -  environment management in `pshapp/env.c`
- `pshlogin`  -  authentication handler

These are always available regardless of `PSH_COMMANDS` selection.
