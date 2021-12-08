# ping

`ping` is a `psh` applet related to networking. It allows checking and measuring ICMP (Internet Control Message Protocol) request/response time.

---

When running `ping` with `-h` parameter the help message is displayed as follows:
```
Usage: ping [options] address
Options
  -h:  prints help
  -c:  count, number of requests to be sent, default 5
  -i:  interval in milliseconds, minimum 200 ms, default 1000
  -t:  IP Time To Live, default 64
  -s:  payload size, default 56, maximum 2040
  -W:  socket timetout, default 2000
```

## See also

1. [Phoenix-RTOS shell](psh.md)
2. [Phoenix-RTOS Utilities](README.md)
3. [Table of Contents](../README.md)
