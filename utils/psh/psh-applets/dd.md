# dd

`dd` is a tool used for copying and converting data. It operates on blocks of data, and its behavior can be customized
with various operands. It is often used for tasks such as backing up and restoring entire
partitions, copying regions of raw device files, and converting data formats.

## Usage

```console
dd [OPERAND]...
```

### Operands

- `if=FILE`: Read from FILE instead of standard input.

- `of=FILE`: Write to FILE instead of standard output.

- `bs=BYTES`: Set both input and output block size to BYTES.

- `count=N`: Copy only N input blocks.

- `seek=N`: Skip N output blocks before writing.

- `skip=N:` Skip N input blocks before reading.

- `conv=CONVS`: Apply one or more comma-separated conversions.

### Conversions

- `nocreat`: Do not create the output file.
- `notrunc`: Do not truncate the output file.

## Examples

Copy a file with a specific block size:

```console
dd if=input.txt of=output.txt bs=1M
```

Create a disk image:

```console
dd if=/dev/sda of=disk.img bs=4M
```

Convert and copy data with no truncation

```console
dd if=input.dat of=output.dat conv=notrunc
```

## See also

1. [Feniks-RTOS shell](../index.md)
2. [Feniks-RTOS Utilities](../../index.md)
3. [Table of Contents](../../../index.md)
