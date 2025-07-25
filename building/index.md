# Building

To create a Phoenix-RTOS image for the selected target the `phoenix-rtos-project` repository should be used. This
repository aggregates all operating system modules - kernel, standard library, device
drivers, filesystems, utilities, and loader. Read more about `phoenix-rtos-project` submodule repositories
[here](project.md).

This chapter contains instructions on how to build a reference project and how to create the final system image.

## Contents

- [Building](#building)
  - [Contents](#contents)
  - [Host operating system](#host-operating-system)
  - [Obtaining the sources](#obtaining-the-sources)
  - [Supported target platforms](#supported-target-platforms)
  - [Building using docker](#building-using-docker)
  - [Building using the native toolchain](#building-using-the-native-toolchain)
  - [Launching Phoenix-RTOS](#launching-phoenix-rtos)

## Host operating system

Instructions in the `Building` and `Running system on targets` chapters have been verified for Ubuntu
20.04 and 22.04, so this is the easiest way to start working with Phoenix-RTOS.Windows is also supported,
by using `Cygwin` or `WSL`.

For more information follow:

- [Windows setup](windows.md)

## Obtaining the sources

The first step of the preparation of the final system image is repository cloning.

To do that and make the next instructions possible, it's recommended to update currently installed packages and, if need
be, install git:

  <details>
  <summary>Installing git on Ubuntu (click to expand)</summary>

  ```console
  sudo apt update && \
  sudo apt install -y git
  ```

  </details>

Then, the repository should be cloned **recursively** (to get the submodules):

```console
git clone --recursive https://github.com/phoenix-rtos/phoenix-rtos-project.git
```

## Supported target platforms

The Phoenix-RTOS reference project supports the following target platforms:

- aarch64a53-zynqmp-qemu
- aarch64a53-zynqmp-zcu104
- aarch64a53-zynqmp-som
- armv7a7-imx6ull-evk
- armv7a9-zynq7000-qemu
- armv7a9-zynq7000-zedboard
- armv7a9-zynq7000-zturn
- armv7m4-stm32l4x6-nucleo
- armv7m7-imxrt105x-evk
- armv7m7-imxrt106x-evk
- armv7m7-imxrt117x-evk
- armv8m33-mcxn94x-frdm
- host-generic-pc
- ia32-generic-pc
- ia32-generic-qemu
- riscv64-generic-qemu
- riscv64-generic-spike
- riscv64-grfpga-artya7
- riscv64-gr765-vcu118
- sparcv8leon-generic-qemu
- sparcv8leon-gr712rc-board
- sparcv8leon-gr716-mimas
- sparcv8leon-gr716-mini
- sparcv8leon-gr740-mini

To get the list of valid targets the `build.sh` script should be launched with an empty `TARGET` variable, eg:

```console
./phoenix-rtos-build/build.sh
```

![Image](../_static/images/building/available-targets.png)

## Building using docker

This is the quickest way to start development - all necessary tools are distributed in a docker image.

Firstly, you need to have the docker installed.

  <details>
  <summary>Installing Docker on Ubuntu (click to expand)</summary>

- Install required packages

  ```console
  sudo apt update && \
  sudo apt install -y curl \
  ca-certificates \
  gnupg \
  lsb-release
  ```

- Make docker packages available

  ```console
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg && \
  echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  ```

- Install docker packages

  ```console
  sudo apt-get update && \
  sudo apt-get install docker-ce docker-ce-cli containerd.io
  ```

- Check if Docker is properly installed (version can be different):

  ```console
  sudo docker --version
  ```

  ![Image](../_static/images/quickstart/armv7a9-zynq7000/docker-version.png)

- To make calling docker command without `sudo` possible type:

  ```console
  sudo groupadd docker
  ```

  Even if group `docker` already exists type then:

  ```console
  sudo usermod -aG docker $USER && \
  newgrp docker
  ```

- Check if running docker images without sudo works properly:

  ```console
  docker run hello-world
  ```

  ![Image](../_static/images/quickstart/armv7a9-zynq7000/docker-test.png)

  For more details and other instructions see

  [docker.com](https://docs.docker.com/engine/install/ubuntu/)

  </details>

Then, to build - provide a `TARGET` via ENV variable and run the build script:

```console
cd phoenix-rtos-project/
TARGET=ia32-generic-qemu ./docker-build.sh all
```

After the build completes, kernel and disk images will be created and placed in the `_boot` directory.

You can read more about the building script options [here](script.md).

## Building using the native toolchain

This is the method preferred when you plan to develop Phoenix-RTOS.

Firstly, you need to install some tools required for compiling the toolchain and finally create a
Phoenix-RTOS system image.
There is a list of commands you can use to get them: on both Ubuntu host operating system.

  <details>
  <summary>Installing required tools for native build on Ubuntu (click to expand)</summary>

  ```console
  sudo apt update && \
  sudo apt install -y build-essential \
  mtd-utils \
  autoconf \
  pkg-config \
  texinfo \
  genext2fs \
  libtool \
  libhidapi-dev \
  python3 \
  python3-jinja2 \
  python3-yaml
  ```

  </details>

Next, you need to compile the toolchains for all required target architectures:

```console
cd phoenix-rtos-project
```

```text
./phoenix-rtos-build/toolchain/build-toolchain.sh i386-pc-phoenix ~/toolchains/i386-pc-phoenix
./phoenix-rtos-build/toolchain/build-toolchain.sh arm-phoenix ~/toolchains/arm-phoenix
./phoenix-rtos-build/toolchain/build-toolchain.sh riscv64-phoenix ~/toolchains/riscv64-phoenix
./phoenix-rtos-build/toolchain/build-toolchain.sh sparc-phoenix ~/toolchains/sparc-phoenix
./phoenix-rtos-build/toolchain/build-toolchain.sh aarch64-phoenix ~/toolchains/aarch64-phoenix
```

<details>
<summary> Errors and warnings that may occur during the toolchain compilation </summary>
&nbsp;

If you have encountered some issue during the toolchain build - you probably interrupted a build before or the files in
the `toolchains` directory are broken for some reason. Removing a directory for a specific architecture
(arm-phoenix/i386-pc-phoenix/riscv64-phoenix/sparc-phoenix) and launching a build once again should help.

`NOTE:` Even during the correct compilation process there may be some unresolved warnings.

</details>
  &nbsp;

Toolchain binaries should be added to the PATH variable:

```console
export PATH=$PATH:$HOME/toolchains/i386-pc-phoenix/i386-pc-phoenix/bin/:$HOME/toolchains/arm-phoenix/arm-phoenix/bin/:$HOME/toolchains/riscv64-phoenix/riscv64-phoenix/bin/:$HOME/toolchains/sparc-phoenix/sparc-phoenix/bin/
```

You should keep the `PATH` variable updated. There are various methods to do that, for example you can place the export
in `.bashrc` file on `Ubuntu`:

  ```console
  echo "export PATH=$PATH:$HOME/toolchains/i386-pc-phoenix/i386-pc-phoenix/bin/:$HOME/toolchains/arm-phoenix/arm-phoenix/bin/:$HOME/toolchains/riscv64-phoenix/riscv64-phoenix/bin/:$HOME/toolchains/sparc-phoenix/sparc-phoenix/bin/" >> $HOME/.bashrc
  ```

Read more about the Phoenix-RTOS toolchain [here](toolchain.md).

To build a project - provide a `TARGET` via ENV variable:

```console
TARGET=ia32-generic-qemu ./phoenix-rtos-build/build.sh all
```

After the build completes, kernel and disk images will be created and placed in the `_boot` directory.

You can read more about the building script options [here](script.md).

## Launching Phoenix-RTOS

To start the created image on target architecture please see [phoenix-rtos-doc/quickstart](../quickstart/index.md)
guide.

```{toctree}
:hidden:
:maxdepth: 1

toolchain.md
script.md
project.md
```
