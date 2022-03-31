# Building Phoenix-RTOS image

To create a Phoenix-RTOS image for the selected target the `phoenix-rtos-project` repository should be used. This repository aggregates all operating system modules - kernel, standard library, device drivers, filesystems, utilities, and loader. Read more about `phoenix-rtos-project` submodule repositories [here](project.md).

This chapter contains instructions on how to build a reference project and how to create the final system image.

## Host operating system

Instructions in the `Building` and `Running system on targets` chapters have been verified for the Ubuntu Linux distribution, so this is the easiest way to start working with Phoenix-RTOS. There is also the possibility to use MacOS, but it's not described in that detail for now. Using Windows isn't supported, but you can create a virtual machine with Ubuntu or try to use Docker.

## Obtaining the sources

The first step of the preparation of the final system image is repository cloning. 

To do that and make the next instructions possible, it's recommended to update currently installed packages and, if need be, install git:

```bash
sudo apt-get update && \
sudo apt-get upgrade && \
sudo apt-get install git
```

Then, the repository should be cloned **recursively** (to get the submodules):

```bash
git clone --recursive https://github.com/phoenix-rtos/phoenix-rtos-project.git
```

## Supported target platforms

The Phoenix-RTOS reference project supports the following target platforms:

* armv7m4-stm32l4x6
* armv7m7-imxrt105x
* armv7m7-imxrt106x
* armv7m7-imxrt117x
* armv7a7-imx6ull
* ia32-generic
* riscv64-spike
* riscv64-virt

To get the list of valid targets the `build.sh` script should be launched with an empty `TARGET` variable, eg:

```bash
./phoenix-rtos-build/build.sh
```

<img src="_images/available-targets.png" width="600px">

## Building using docker

This is the quickest way to start development - all necessary tools are distributed in a docker image.

Firstly, you need to have the docker installed.

  <details>
  <summary>How to get docker (Ubuntu 20.04)</summary>

  - Install required packages

  ```
  sudo apt-get update && \
  sudo apt-get install curl \
  ca-certificates \
  gnupg \
  lsb-release
  ```

  - Make docker packages available

  ```
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg && \
  echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  ```

  - Install docker packages

  ```
  sudo apt-get update && \
  sudo apt-get install docker-ce docker-ce-cli containerd.io
  ```

  - Check if Docker is properly installed (version can be different):

  ```
  sudo docker --version
  ```

  <img src="_images/docker-version.png" width="600px">

  - To make calling docker command without `sudo` possible type:

  ```
  sudo groupadd docker
  ```

  Even if group `docker` already exists type then:

  ```
  sudo usermod -aG docker $USER && \
  newgrp docker
  ```

  - Check if running docker images without sudo works properly:

  ```
  docker run hello-world
  ```

  <img src="_images/docker-test.png" width="600px">

  For more details and other instructions see

  [docker.com](https://docs.docker.com/engine/install/ubuntu/)

  </details> 

Then, to build - provide a `TARGET` via ENV variable and run the build script:

```bash
cd phoenix-rtos-project/
TARGET=ia32-generic ./docker-build.sh all
```

After the build completes, kernel and disk images will be created and placed in the `_boot` directory.

You can read more about the building script options [here](script.md).

## Building using the native toolchain

This is the method preferred when you plan to develop Phoenix-RTOS.

Firstly, you need to install some tools required for compiling the toolchain and finally create a Phoenix-RTOS system image.
There is a list of commands you can use to get them on the Ubuntu 20.04 host operating system.

```bash
sudo apt-get update && \
sudo apt-get upgrade && \
sudo apt-get install build-essential \
autoconf \
texinfo \
genext2fs \
libtool \
libhidapi-dev \
python3
```

Next, you need to compile the toolchains for all required target architectures:

```bash
cd phoenix-rtos-project
```

```bash
(cd phoenix-rtos-build/toolchain/ && ./build-toolchain.sh i386-pc-phoenix ~/toolchains/i386-pc-phoenix)
```

```bash
(cd phoenix-rtos-build/toolchain/ && ./build-toolchain.sh arm-phoenix ~/toolchains/arm-phoenix)
```

```bash
(cd phoenix-rtos-build/toolchain/ && ./build-toolchain.sh riscv64-phoenix ~/toolchains/riscv64-phoenix)
```

Toolchain binaries should be added to the PATH variable:

```bash
export PATH=$PATH:~/toolchains/i386-pc-phoenix/i386-pc-phoenix/bin/
export PATH=$PATH:~/toolchains/arm-phoenix/arm-phoenix/bin/
export PATH=$PATH:~/toolchains/riscv64-phoenix/riscv64-phoenix/bin/
```

Read more about the Phoenix-RTOS toolchain [here](toolchain.md).

To build a project - provide a `TARGET` via ENV variable:

```bash
TARGET=ia32-generic ./phoenix-rtos-build/build.sh all
```

After the build completes, kernel and disk images will be created and placed in the `_boot` directory.

You can read more about the building script options [here](script.md).

## Launching Phoenix-RTOS

To start the created image on target architecture please see [phoenix-rtos-doc/quickstart](../quickstart/README.md) guide.

## See also

1. [Phoenix-RTOS toolchain](toolchain.md)
2. [Phoenix-RTOS building script](script.md)
3. [Phoenix-RTOS reference project repository](project.md)
4. [Table of Contents](../README.md)
