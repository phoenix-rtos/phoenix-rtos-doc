# Obtaining trace from QEMU MBR disk image
Let `$TRACE_DIR` be a destination directory of CTF trace on host. Let
`/my_trace` be the location of recorded trace on QEMU disk image (collected,
e.g. via `perf -m trace -o /my_trace`)

## The manual way

1. Find out the disk sector size and rootfs partition start (here, start=4096,
   sector size=512):

   ```text
   $ fdisk -l $PRTOS_PROJECT/_boot/ia32-generic-qemu/hd0.disk
   Disk _boot/ia32-generic-qemu/hd0.disk: 128 MiB, 134217728 bytes, 262144 sectors
   Units: sectors of 1 * 512 = 512 bytes
   Sector size (logical/physical): 512 bytes / 512 bytes
   I/O size (minimum/optimal): 512 bytes / 512 bytes
   Disklabel type: dos
   Disk identifier: 0x00000000
   
   Device                            Boot Start    End Sectors  Size Id Type
   _boot/ia32-generic-qemu/hd0.disk1 *     4096 262143  258048  126M 83 Linux
   ```

2. Mount the QEMU image:

   ```text
   # mount -o loop,offset=$((4096*512)) _boot/ia32-generic-qemu/hd0.disk /mnt
   ```

3. Copy the recorded trace directory to host destination directory:

   ```text
   $ cp /mnt/my_trace $TRACE_DIR
   ```

4. Proceed to step 3 of RTOS-A-136548075

## The automated way using `rootfs_convert.sh`

`rootfs_convert.sh` is an end-user script that does the above steps but uses
`parted` instead (as it is more script-friendly), invokes `convert.sh`
automatically and outputs a ready to view perfetto trace. Invoke

```text
$ cd $PRTOS_PROJECT/phoenix-rtos-hostutils/trace
$ ./rootfs_convert.sh ../../_boot/ia32-generic-qemu/hd0.disk /my_trace ../../phoenix-rtos-kernel/perf/tsdl/metadata out.pftrace
```
