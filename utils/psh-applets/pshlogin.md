# pshogin

`psh` can be run in login mode by launching it from name `pshlogin`. User credentials are read from `/etc/passwd` file.

---

Additional user credentials can be passed using the `PSH_DEFUSRPWDHASH` environment variable defined at compile time. `PSH_DEFUSRPWDHASH` should store only one hash of a password. Then one can also log in using:
- username: defuser
- password: (corresponding with given hash)

### Exiting `pshlogin`

It is important to know that it is impossible to completly exit the `psh` which is launched as `pshlogin`. Using `exit` command or `EOT` character (`ctrl+D`) will only logout the user without ending the `psh` process. 
