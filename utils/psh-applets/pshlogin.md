# pshogin

`psh` can be run in login mode by launching it from the name `pshlogin`. User credentials are read from `/etc/passwd` file.

---

Additional user credentials can be passed using the `PSH_DEFUSRPWDHASH` environment variable defined at compile time. `PSH_DEFUSRPWDHASH` should store only one hash of a password. Then one can also log in using:
- username: defuser
- password: (corresponding with given hash)

### Exiting `pshlogin`

It is important to know that it is impossible to completly exit the `psh` which is launched as `pshlogin`. Using the `exit` command or `EOT` character (`ctrl+D`) will only log out the user without ending the `psh` process. 

## See also

1. [Phoenix-RTOS shell](psh.md)
2. [Phoenix-RTOS Utilities](README.md)
3. [Table of Contents](../README.md)
