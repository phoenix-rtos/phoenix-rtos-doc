# Phoenix Serial Uploader (psu)

`psu` is a tool for loading firmware onto Phoenix-RTOS devices using the SDP (Serial Download Protocol) or MCUBoot
protocol. It executes scripts containing firmware upload commands, targeting NXP devices such as `imxrt106x`,
`imxrt117x`, and `imx6ull`.

## Usage

```shell
psu [OPTIONS] script_path
```

Options:

- `-t` — Set timeout for the wait command (default is 10 seconds)
- `-h` — Display help

## Example Usage

```shell
psu -t 15 script.sdp
```

## SDP Script Syntax

Script files contain one command per line. The following commands are supported:

| Command | Syntax | Description |
|---|---|---|
| `WAIT` | `WAIT <vid> <pid>` | Wait for a HID device with specified USB vendor/product ID |
| `WRITE_FILE` | `WRITE_FILE F/S <path> [address] [format] [offset] [size]` | Transfer a file to the target. `F` for file, `S` for syspage. |
| `WRITE_REGISTER` | `WRITE_REGISTER <address> <value>` | Write a value to a memory-mapped register |
| `JUMP_ADDRESS` | `JUMP_ADDRESS <address>` | Jump to the specified address on the target |

### Example Script

```
WAIT 1fc9 0135
WRITE_FILE F _boot/armv7m7-imxrt106x-evk/phoenix.disk 0x70000000
JUMP_ADDRESS 0x70000400
```

For the full script syntax reference, see the
[psu README](https://github.com/phoenix-rtos/phoenix-rtos-hostutils/tree/master/psu).
