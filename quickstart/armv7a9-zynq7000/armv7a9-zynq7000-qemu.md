# Running system on <nobr>armv7a9-zynq7000-qemu</nobr>

These instructions describe how to run a Phoenix-RTOS system image for the `armv7a9-zynq7000-qemu` target architecture
using docker.

Note that, the build artifacts, including the system image, should be first provided in the `_boot` directory.

If you haven't run the `build.sh` script yet, run it for `armv7a9-zynq7000-qemu` target.

See [Building](../../building/index.md) chapter.

## Running the system image

Install Docker.

  <details>
  <summary>How to get docker (Ubuntu 22.04)</summary>

- Install required packages

  ```shell
  sudo apt-get update && \
  sudo apt-get install curl \
  ca-certificates \
  gnupg \
  lsb-release
  ```

- Make docker packages available

  ```shell
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg && \
  echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  ```

- Install docker packages

  ```shell
  sudo apt-get update && \
  sudo apt-get install docker-ce docker-ce-cli containerd.io
  ```

- Check if Docker is properly installed (version can be different):

  ```shell
  sudo docker --version
  ```

  ```
  ~$ sudo docker --version
  Docker version 20.10.12, build e91ed57
  ~$
  ```

- To make calling docker command without `sudo` possible type:

  ```shell
  sudo groupadd docker
  ```

  Even if group `docker` already exists type then:

  ```shell
  sudo usermod -aG docker $USER && \
  newgrp docker
  ```

- Check if running docker images without sudo works properly:

  ```shell
  docker run hello-world
  ```

  ```
  ~$ docker run hello-world
  Unable to find image 'hello-world:latest' locally
  latest: Pulling from library/hello-world
  2db29710123e: Pull complete
  Digest: sha256:37a0b92b08d4919615c3ee023f7ddb068d12b8387475d64c622ac30f45c29c51
  Status: Downloaded newer image for hello-world:latest

  Hello from Docker!
  This message shows that your installation appears to be working correctly.

  To generate this message, Docker took the following steps:
   1. The Docker client contacted the Docker daemon.
   2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
      (amd64)
   3. The Docker daemon created a new container from that image which runs the
      executable that produces the output you are currently reading.
   4. The Docker daemon streamed that output to the Docker client, which sent it
      to your terminal.

  To try something more ambitious, you can run an Ubuntu container with:
   $ docker run -it ubuntu bash

  Share images, automate workflows, and more with a free Docker ID:
   https://hub.docker.com/

  For more examples and ideas, visit:
   https://docs.docker.com/get-started/

  ~$
  ```

  For more details and other instructions see

  [docker.com](https://docs.docker.com/engine/install/ubuntu/)

  </details>

Now, with docker installed you can run Phoenix-RTOS using the following command:

```shell
./docker-devel.sh scripts/armv7a9-zynq7000-qemu.sh
```

After boot, the `psh` (Phoenix-RTOS shell) prompt appears.

- Note: It may take a while.

```
Phoenix-RTOS microkernel v. 2.97 rev: 10b7a77
hal: Xilinx Zynq-7000 ARMv7 Cortex-A9 r0p0
hal: ThumbEE, Thumb, ARM, Security
hal: Using GIC interrupt controller
vm: Initializing page allocator (1004+0)/131072KB, page_t=16
vm: [256x][24K][6P]H[17K][68A][127H]PPPP[773.]PPPS[31744.]
vm: Initializing memory mapper: (8097*64) 518208
vm: Initializing kernel memory allocator: (64*48) 3072
vm: Initializing memory objects
proc: Initializing thread scheduler, priorities=8
syscalls: Initializing syscall table [102]
main: Starting syspage programs: 'dummyfs;-N;devfs;-D', 'zynq7000-uart', 'psh;-i;/etc/rc.psh', 'zynq7000-flash;-r;/dev/mtd0:8388608:0x800000:jffs2;'
version 2.2. (NAND) (SUMMARY)  © 2001-2006 Red Hat, Inc.
(psh)%
```

  <details>
  <summary>Why there is no need to install qemu?</summary>

  All necessary tools including QEMU are provided in phoenix-rtos/devel docker image (run by `docker-devel.sh` script)

  If you want, you can read more about docker containerization on <https://www.docker.com/resources/what-container>

  </details>

## Using Phoenix-RTOS

Once booted, the `psh` shell prompt appears. See [Shell basics](../psh-basics.md) for an introduction to
the available shell commands, process inspection, and running programs.
