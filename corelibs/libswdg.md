# Software watchdog library (libswdg)

`libswdg` provides a multichannel software watchdog for applications that need process-level timeout supervision.

## Application interface

### Data types

`swdg_callback_t`
: Callback invoked when a watchdog channel times out. The `channel` argument identifies the expired channel, so one
  callback can handle multiple channels.

  ```c
  typedef void (*swdg_callback_t)(int channel);
  ```

### Functions

````{function} swdg_reload(no)
Reloads the timer for watchdog channel `no`.

:param no: Channel number. Values outside the configured channel range are ignored.
:returns: Nothing.
````

````{function} swdg_disable(no)
Disables watchdog channel `no` without changing its callback or timeout configuration.

:param no: Channel number. Values outside the configured channel range are ignored.
:returns: Nothing.
````

````{function} swdg_enable(no)
Enables watchdog channel `no` and reloads it before signaling the watchdog thread.

:param no: Channel number. Values outside the configured channel range are ignored.
:returns: Nothing.
````

````{function} swdg_chanConfig(no, callback, limit)
Configures watchdog channel `no` with a timeout callback and deadline.

:param no: Channel number. Values outside the configured channel range are ignored.
:param callback: Callback executed by the watchdog thread when the channel times out.
:param limit: Timeout value in microseconds.
:returns: Nothing.
````

````{function} swdg_init(chanCount, priority)
Initializes the library with `chanCount` channels and starts the watchdog thread at `priority`.

:param chanCount: Number of watchdog channels. The value must be greater than `0`.
:param priority: Watchdog thread priority. The implementation accepts values from `0` through `6`.
:returns: `0` on success, `-EINVAL` for invalid arguments, `-ENOMEM` when channel allocation fails, or a negative
  error returned by `mutexCreate()`, `condCreate()`, or `beginthread()`.
````

### Notes

- All channels start disabled.
- Channel configuration does not enable a disabled channel.
- A timeout callback must not call `libswdg` functions, because the watchdog thread holds the library lock while it
  invokes callbacks.

## Using libswdg

The following example configures one channel with a 30 second timeout.

```c
void callback(int no)
{
    systemReboot();
}

int main()
{
    swdg_init(1, 3);
    swdg_chanConfig(0, callback, 30 * 1000 * 1000);
    swdg_enable(0);

    while (1) {
        doAppStuff();
        swdg_reload(0);
    }

    return 0;
}
```

If `doAppStuff()` blocks or crashes for more than 30 seconds, the watchdog callback resets the system.
