# Building script

To build Phoenix-RTOS system image build.sh script is used. The simplest way to build the image is the
following command.

```bash
TARGET=ia32-generic-qemu phoenix-rtos-build/build.sh all
```

As you can see there can be other arguments like `all`.

You can also use the `clean` argument to clean the last build artifacts.

```bash
TARGET=ia32-generic-qemu phoenix-rtos-build/build.sh clean all
```

When you want to compile only the new changes and save time you don't have to use it.

The `all` argument specifies that all system components for a given target should be compiled (excluding tests).
The available components are listed below:

- `fs` - filesystem image,

- `core` - Phoenix-RTOS core, i.e. kernel and other necessary components,

- `test` - tests,

- `ports` - phoenix-rtos-ports applications,

- `project` - project specific part (user applications),

- `image` - system image to be loaded to the target,

For example, in ia32-generic-qemu target `all` means `core fs image project ports`.</br>
For the other targets, `all` can be different components configurations. </br>
You can also choose what components you want to build, for example, the following command will build a system image
without test and ports components.
The `ports` component compiling process can take a while. If you need to build the system image quickly, you can use the
command above.

```bash
TARGET=ia32-generic-qemu phoenix-rtos-build/build.sh core fs image project test
```

For ia32-generic-qemu target, running the system in a separate window isn't the only option. There is the possibility to
run it in a terminal, in that case, you have to set a few other variables.

```bash
TARGET=ia32-generic-qemu CONSOLE=serial ./phoenix-rtos-build/build.sh all
```

After the build completes, the disk image and all files needed to run it will be created and placed in the _boot
directory.

## See also

1. [Building Phoenix-RTOS image](README.md)
2. [Toolchain](toolchain.md)
3. [Reference project](project.md)
4. [Table of Contents](../README.md)
