# Software watchdog library (libswdg)

Software multichannel watchdog implementation.

## Contents

- [Application interface](#application-interface)
  - [Data types](#data-types)
  - [Functions](#functions)
  - [Notes](#notes)
- [Using libswdg](#using-libswdg)

## Application interface

### Data types

```c
typedef void (*swdg_callback_t)(int channel);
```

Callback function to be provided to be executed in the event of channel timeout. `channel` param conveys information
which channel timeout has occurred, this allows one callback to be used for all channels.

### Functions

```c
void swdg_reload(int no);
```

Reloads selected watchdog channel `no` timer. This causes channel deadline to be set to value set in configuration.

```c
void swdg_disable(int no);
```

Disables selected watchdog channel `no` timer. Configuration is kept, so channel can be re-enabled without additional
steps.

```c
void swdg_enable(int no);
```

Enables selected watchdog channel `no` timer. Channel is refreshed on enable, so no spurious timeout can occur.

```c
void swdg_chanConfig(int no, swdg_callback_t callback, time_t limit);
```

Configures selected watchdog channel `no` with desired `callback` function and `limit` (in microseconds) deadline.

```c
void swdg_init(size_t chanCount, int priority);
```

Initialize library with `chanCount` channels and watchdog thread with priority `priority`. Needs to be called before any
other operation. `chanCount` has to be greater than zero, `priority` has to be greater or equal to zero
(the highest priority) and less than 7.

### Notes

- All channels start disabled,
- Channel configuration does not change its state, channel needs to be enabled if it was not prior,
- Callback function **must not** call any libswdg functions! Deadlock will occur.

## Using libswdg

Normal usage example - one channel active with 30 seconds timeout.

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
		swdg_reaload(0);
	}

	return 0;
}
```

Should `doAppStuff()` function hang/crash for more than 30 seconds, the system will reset.
