# Building

To create a Phoenix-RTOS image for the selected target the `phoenix-rtos-project` repository should be used. This
repository aggregates all operating system modules - kernel, standard library, device
drivers, filesystems, utilities, and loader.

This chapter contains instructions on how to build a reference project and how to create the final system image.

## Host operating system

Instructions in the `Building` and `Running system on targets` chapters have been verified for the Ubuntu
(20.04 and 22.04 versions) Linux distribution and macOS (tested on macOS Monterey 12.6.1), so this is the easiest way
to start working with Phoenix-RTOS. Windows is also supported, by using `Cygwin` or `WSL`.

For more information follow:
<!-- 
```{toctree}
:hidden:
:maxdepth: 1

windows.md
``` -->

See [Windows setup](windows.md)

## Obtaining the sources

The first step of the preparation of the final system image is `phoenix-rtos-project` repository cloning.

To do that and make the next instructions possible, it's recommended to update currently installed packages and, if need
be, install git:

  <details>
  <summary>Installing git on Ubuntu (click to expand)</summary>

  ```text
  sudo apt-get update && \
  sudo apt-get upgrade && \
  sudo apt-get install git
  ```

  </details>

  <details>
  <summary>Installing git on macOS (click to expand)</summary>

  You will need the command line tools for `Xcode` and `Homebrew` package, if you don't have it you can install it by
  typing:

  ```text
  xcode-select --install
  ```

  and then:

  ```text
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  ```

  Assure that brew is properly installed, by checking its version:

  ```text
  brew --version
  ```

  *The described instructions have been verified for `4.0.11` brew version.

  Then you will be ready for installing git and other required tools:

  ```text
  brew update && \
  brew upgrade && \
  brew install git
  ```

  </details>
  &nbsp;

Then, the repository should be cloned **recursively** (to get the submodules):

```text
git clone --recursive https://github.com/phoenix-rtos/phoenix-rtos-project.git
```

Read more about `phoenix-rtos-project` and its submodule repositories
[here](project.md).

## Supported target platforms

The Phoenix-RTOS reference project supports the following target platforms:

- armv7a7-imx6ull-evk
- armv7a9-zynq7000-qemu
- armv7a9-zynq7000-zedboard
- armv7a9-zynq7000-zturn
- armv7m4-stm32l4x6-nucleo
- armv7m7-imxrt105x-evk
- armv7m7-imxrt106x-evk
- armv7m7-imxrt117x-evk
- host-generic-pc
- ia32-generic-pc
- ia32-generic-qemu
- riscv64-generic-qemu
- riscv64-generic-spike
- sparcv8leon3-gr716-mini

To get the list of valid targets the `build.sh` script should be launched with an empty `TARGET` variable, eg:

```text
./phoenix-rtos-build/build.sh
```

![Image](_images/available-targets.png)

## Building using docker

This is the quickest way to start development - all necessary tools are distributed in a docker image.

Firstly, you need to have the docker installed.

  <details>
  <summary>Installing Docker on Ubuntu (click to expand)</summary>

- Install required packages

  ```text
  sudo apt-get update && \
  sudo apt-get install curl \
  ca-certificates \
  gnupg \
  lsb-release
  ```

- Make docker packages available

  ```text
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg && \
  echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  ```

- Install docker packages

  ```text
  sudo apt-get update && \
  sudo apt-get install docker-ce docker-ce-cli containerd.io
  ```

- Check if Docker is properly installed (version can be different):

  ```text
  sudo docker --version
  ```

  ![Image](_images/docker-version.png)

- To make calling docker command without `sudo` possible type:

  ```text
  sudo groupadd docker
  ```

  Even if group `docker` already exists type then:

  ```text
  sudo usermod -aG docker $USER && \
  newgrp docker
  ```

- Check if running docker images without sudo works properly:

  ```text
  docker run hello-world
  ```

  ![Image](_images/docker-test.png)

  For more details and other instructions see

  [docker.com](https://docs.docker.com/engine/install/ubuntu/)

  </details>

<details>
  <summary>Installing Docker on macOS (click to expand)</summary>

  You can find the up-to-date instructions on <https://docs.docker.com/desktop/install/mac-install/>

  To make this process simpler below is an example of installation for Mac with the Intel chip:

  Download the installer:

  ```text
  curl -o Docker.dmg "https://desktop.docker.com/mac/main/amd64/Docker.dmg?utm_source=docker&amp;utm_medium=webreferral&amp;utm_campaign=docs-driven-download-mac-amd64"
  ```

  Run the following commands to install Docker:

  ```text
  sudo hdiutil attach Docker.dmg && \
  sudo /Volumes/Docker/Docker.app/Contents/MacOS/install && \
  sudo hdiutil detach /Volumes/Docker
  ```

  Then add the path to `docker` binaries to the `PATH` environment variable:

  ```text
  export PATH="/Applications/Docker.app/Contents/Resources/bin:$PATH"
  ```

  It's recommended to place it in `.zshrc` startup script to export it every time during startup:

  ```text
  echo 'export PATH=/Applications/Docker.app/Contents/Resources/bin:$PATH' >> $HOME/.zshrc
  ```

- Check if Docker is properly installed by checking its version:

  ```text
  docker --version
  ```

- Check if running docker images without sudo works properly:

  ```text
  docker run hello-world
  ```

- If you see the following error: `ERROR: Cannot connect to the Docker daemon at unix:///var/run/docker.sock.`
  you can try to install `colima` and check once again:

  ```text
  brew install colima && \
  colima start
  ```

  </details>
  &nbsp;

Then, to build - provide a `TARGET` via ENV variable and run the build script:

```text
cd phoenix-rtos-project/
TARGET=ia32-generic-qemu ./docker-build.sh all
```

After the build completes, kernel and disk images will be created and placed in the `_boot` directory.

You can read more about the building script options [here](script.md).

## Building using the native toolchain

This is the method preferred when you plan to develop Phoenix-RTOS.

Firstly, you need to install some tools required for compiling the toolchain and finally create a
Phoenix-RTOS system image.
There is a list of commands you can use to get them: on both Ubuntu and macOS host operating systems.

  <details>
  <summary>Intalling required tools for native build on Ubuntu (click to expand)</summary>

  ```text
  sudo apt-get update && \
  sudo apt-get upgrade && \
  sudo apt-get install build-essential \
  mtd-utils \
  autoconf \
  texinfo \
  genext2fs \
  libtool \
  libhidapi-dev \
  python3
  ```

  </details>

  <details>
  <summary>Intalling required tools for native build on macOS (click to expand)</summary>

  ```text
  brew update && \
  brew upgrade && \
  brew install bash \
  coreutils \
  autoconf \
  automake \
  genext2fs \
  make \
  libelf \
  wget \
  gnu-sed \
  hidapi \
  python3
  ```

  *`bash` in version >= `4.0` and `make` in version >= `3.82` are needed (associative arrays and `undefine` used).
  They may be preinstalled, but in older versions, that's why we install it there.

  It's also required to add appropriate paths to the `PATH` environment variable:

  ```text
  export PATH=$(brew --prefix make)/libexec/gnubin:$(brew --prefix gnu-sed)/libexec/gnubin:$PATH
  ```

  and keep it updated, for example by placing the export in the startup script:

  ```text
  echo 'export PATH=$(brew --prefix make)/libexec/gnubin:$(brew --prefix gnu-sed)/libexec/gnubin:$PATH' >> $HOME/.zshrc
  ```

  *Note that you have to place the `gnubin` path that provides `make` before the `/usr/bin` in the `PATH` environment
  variable to use the `gnu` version (as it is done above).

  Phoenix-RTOS requires the `endian.h` header, which may exist, but not be visible. If during the building you discover
  the following error:
  `fatal error: 'endian.h' file not found`
  please create the symlink to this header by the given command:

  ```text
  sudo ln -s /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/machine/endian.h /usr/local/include/endian.h
  ```

  </details>
  &nbsp;

Next, you need to compile the toolchains for all required target architectures:

```text
cd phoenix-rtos-project
```

```text
(cd phoenix-rtos-build/toolchain/ && ./build-toolchain.sh i386-pc-phoenix ~/toolchains/i386-pc-phoenix)
(cd phoenix-rtos-build/toolchain/ && ./build-toolchain.sh arm-phoenix ~/toolchains/arm-phoenix)
(cd phoenix-rtos-build/toolchain/ && ./build-toolchain.sh riscv64-phoenix ~/toolchains/riscv64-phoenix)
(cd phoenix-rtos-build/toolchain/ && ./build-toolchain.sh sparc-phoenix ~/toolchains/sparc-phoenix)
```

Toolchain binaries should be added to the PATH variable:

```text
export PATH=$PATH:$HOME/toolchains/i386-pc-phoenix/i386-pc-phoenix/bin/:$HOME/toolchains/arm-phoenix/arm-phoenix/bin/:$HOME/toolchains/riscv64-phoenix/riscv64-phoenix/bin/:$HOME/toolchains/sparc-phoenix/sparc-phoenix/bin/
```

You should keep the `PATH` variable updated. There are various methods to do that, for example you can place the export
in `.bashrc` file on `Ubuntu`:

  ```text
  echo "export PATH=$PATH:$HOME/toolchains/i386-pc-phoenix/i386-pc-phoenix/bin/:$HOME/toolchains/arm-phoenix/arm-phoenix/bin/:$HOME/toolchains/riscv64-phoenix/riscv64-phoenix/bin/:$HOME/toolchains/sparc-phoenix/sparc-phoenix/bin/" >> $HOME/.bashrc
  ```

or in `.zshrc` on macOS:

  ```text
  echo 'export PATH=$PATH:$HOME/toolchains/i386-pc-phoenix/i386-pc-phoenix/bin/:$HOME/toolchains/arm-phoenix/arm-phoenix/bin/:$HOME/toolchains/riscv64-phoenix/riscv64-phoenix/bin/:$HOME/toolchains/sparc-phoenix/sparc-phoenix/bin/' >> $HOME/.zshrc
  ```

Read more about the Phoenix-RTOS toolchain [here](toolchain.md).

To build a project - provide a `TARGET` via ENV variable:

```text
TARGET=ia32-generic-qemu ./phoenix-rtos-build/build.sh all
```

After the build completes, kernel and disk images will be created and placed in the `_boot` directory.

You can read more about the building script options [here](script.md).

## Launching Phoenix-RTOS

To start the created image on target architecture please see [phoenix-rtos-doc/quickstart](../quickstart/README.md)
guide.
