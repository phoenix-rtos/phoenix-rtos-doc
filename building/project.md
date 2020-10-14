# Build the project for selected target

To build Phoenix-RTOS for selected platform you should edit build.project file and set TARGET variable to define target processor architecture and target board.

## Available target platforms

* armv7m3-stm32l152xd
* armv7m3-stm32l152xe
* armv7m4-stm32l4x6
* armv7m7-imxrt105x
* armv7m7-imxrt106x
* armv7m7-imxrt117x
* armv7a7-imx6ull
* ia32-generic
* riscv64-spike
* riscv64-virt




## Running build.sh script

```
	./phoenix-rtos-build/build.sh clean all
```
After the build successfully completes, kernel and disk images will be created and placed in the *_boot* directory.
