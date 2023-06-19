# Running system on `armv7a9-zynq7000-qemu` (Xilinx Zynq-7000, QEMU emulator)

These instructions describe how to run a Phoenix-RTOS system image for the `armv7a9-zynq7000-qemu` target architecture
using docker.

Note that, the build artifacts, including the system image, should be first provided in the `_boot` directory.

If you haven't run the `build.sh` script yet, run it for `armv7a9-zynq7000-qemu` target.

See [how to build the Phoenix-RTOS system image](../building/README.md).

## Running the system image

Firstly, you need to have the docker installed.

  <details>
  <summary>How to get docker (Ubuntu 20.04)</summary>

- Install required packages

  ```bash
  sudo apt-get update && \
  sudo apt-get install curl \
  ca-certificates \
  gnupg \
  lsb-release
  ```

- Make docker packages available

  ```bash
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg && \
  echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  ```

- Install docker packages

  ```bash
  sudo apt-get update && \
  sudo apt-get install docker-ce docker-ce-cli containerd.io
  ```

- Check if Docker is properly installed (version can be different):

  ```bash
  sudo docker --version
  ```

  <img src="_images/docker-version.png" width="700px">

- To make calling docker command without `sudo` possible type:

  ```bash
  sudo groupadd docker
  ```

  Even if group `docker` already exists type then:

  ```bash
  sudo usermod -aG docker $USER && \
  newgrp docker
  ```

- Check if running docker images without sudo works properly:

  ```bash
  docker run hello-world
  ```

  <img src="_images/docker-test.png" width="700px">

  For more details and other instructions see

  [docker.com](https://docs.docker.com/engine/install/ubuntu/)

  </details>

Now, with docker installed you can run Phoenix-RTOS using the following command:

```bash
./docker-devel.sh scripts/armv7a9-zynq7000-qemu.sh
```

As a result, you should see `psh` (Phoenix-RTOS shell).

- Note: It may take a while.

<img src="_images/zynq7000-emu-start.png" width="700px">

  <details>
  <summary>Why there is no need to install qemu?</summary>

  All necessary tools including QEMU are provided in phoenix-rtos/devel docker image (run by `docker-devel.sh` script)

  If you want, you can read more about docker containerization on <https://www.docker.com/resources/what-container>

  </details>

## Using Phoenix-RTOS

To get the available command list please type:

```bash
help
```

<img src="_images/zynq7000-emu-help.png" width="700px">

If you want to get the list of working processes please type:

```bash
ps
```

<img src="_images/zynq7000-emu-ps.png" width="700px">

To get the table of processes please type:

```bash
top
```

<img src="_images/zynq7000-emu-top.png" width="700px">

If you want to quit, you should click on the terminal window, press `ctrl + a`, release it, and next press the `x` key.

<img src="_images/zynq7000-emu-terminate.png" width="700px">

## See also

1. [Running system on armv7a9-zynq7000](armv7a9-zynq7000.md)
2. [Running system on armv7a9-zynq7000-zedboard](armv7a9-zynq7000-zedboard.md)
3. [Running system on armv7a9-zynq7000-zturn](armv7a9-zynq7000-zturn.md)
4. [Running system on targets](README.md)
5. [Table of Contents](../README.md)
