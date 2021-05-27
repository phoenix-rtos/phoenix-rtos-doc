# Phoenix Shell (psh)

Phoenix Shell is a compact program that enables you to control the Phoenix-RTOS from the command line.

## Applets

In `psh`, each command or set of commands is a separate applet, here's a list of the available ones:

* `bind`       - binds device to directory
* `cat`        - concatenate file(s) to standard output
* `edit`       - text editor
* `exec`       - replace shell with the given command
* `exit`       - exits shell
* `help`       - prints this help message
* `history`    - prints commands history
* `kill`       - terminates process
* [`login`](psh-applets/login.md) - utility for user validation
* `ls`         - lists files in the namespace
* `mem`        - prints memory map
* `mkdir`      - creates directory
* `mount`      - mounts a filesystem
* `nc`         - TCP and UDP connections and listens
* `nslookup`   - queries domain name servers
* `perf`       - track kernel performance events
* `ping`       - ICMP ECHO requests
* `ps`         - prints processes and threads
* `pshapp`     - delivers `psh` interpreter, `exit`, `pshlogin` and `history` commands
* `reboot`     - restarts the machine
* `sync`       - synchronizes device
* [`sysexec`](psh-applets/sysexec.md) - launch program from syspage using given map
* `top`        - top utility
* `touch`      - changes file timestamp
