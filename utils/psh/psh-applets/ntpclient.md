# ntpclient

The `ntpclient` is a `psh` applet related to networking, which allows to
set the system's date in UTC from a remote host.

---

Running `ntpclient` with `-h` argument prints help message as follows:

```shell
Usage: ntpclient [options]
  -h:  prints help
  -s:  specify ntp server address
```

By default, `ntpclient` assumes `ntp.pool.org` as the address of time-server.
Specifying the custom address of the time-server to query for the current time
is optional and may be achieved using the `-s` switch, as in the example below,
where `time.coi.pw.edu.pl` was chosen as the address of the time-server:

```shell
(psh)% ntpclient -s time.coi.pw.edu.pl
Using NTP server: time.coi.pw.edu.pl
System time in UTC was Fri Aug 5 17:29:48 2022
System time set to UTC Fri Aug 5 17:29:48 2022
```
