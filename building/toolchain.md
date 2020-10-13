# Building toolchain

Phoenix-RTOS uses GNU CC toolchain for compilation.


3. Build and install toolchains for all required target architectures:

````bash
   - Build the toolchain:
	(cd phoenix-rtos-build/toolchain/ && ./build-toolchain.sh i386-pc-phoenix ~/toolchains/i386-pc-phoenix)
	(cd phoenix-rtos-build/toolchain/ && ./build-toolchain.sh arm-phoenix ~/toolchains/arm-phoenix)
	(cd phoenix-rtos-build/toolchain/ && ./build-toolchain.sh riscv64-phoenix-elf ~/toolchains/riscv64-phoenix-elf)

   - Add toolchain binaries to PATH variable:
	export PATH=$PATH:~/toolchains/i386-pc-phoenix/i386-pc-phoenix/bin/
	export PATH=$PATH:~/toolchains/arm-phoenix/arm-phoenix/bin/
	export PATH=$PATH:~/toolchains/riscv64-phoenix-elf/riscv64-phoenix-elf/bin/
````