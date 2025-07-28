# Command-line interface

Command-line interface allows user to control the booting process.

## Usage

After successful booting by Boot ROM, loader switch to the interactive mode and the prompt `(plo)%`
should be printed on the console.

```{note}
If the user defines own script which ends up with `go!` command, the plo jumps immediately
to the kernel and interactive mode will be skipped.
```

## Commands

List all the available commands in plo (some of them are available only on the specific targets):

* `alias` - sets alias to file, usage: `alias [<name> <offset> <size>]`
* `app` - loads app, usage: `app [<dev> [-x] <name> <imap1;imap2...> <dmap1;dmap2...>]`
* `bitstream - loads bitstream into PL, usage:`bitstream (dev) (name)`
* `call` - calls user's script, usage: `call <dev> <script name> <magic>`
* `console` - sets console to device, usage: `console <major.minor>`
* `copy` - copies data between devices, usage: `copy <src dev> <file/offs size> <dst dev> <file/offs size>`
* `dump` - dumps memory, usage: `dump <addr>`
* `echo` - command switch on/off information logs, usage: `echo [on/off]`
* `go!` - starts Phoenix-RTOS loaded into memory
* `help` - prints the list of available commands
* `kernel` - loads Phoenix-RTOS, usage: `kernel [<dev> [name]]`
* `map` - defines multimap, usage: `map [<name> <start> <end> <attributes>]`
* `mpu` - prints the use of MPU regions, usage: `mpu [all]`
* `phfs` - registers device in phfs, usage: `phfs [<alias> <major.minor> [protocol]]`
* `script` - shows script, usage: `script [<dev> <name> <magic>]`
* `test-ddr` - perform test DDR, usage: `test-ddr`
* `wait` - waits in milliseconds or in an infinite loop, usage: `wait [ms]`
