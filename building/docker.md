# Building with Docker

Docker provides a reproducible build environment without installing toolchains on the host system. Two Docker
workflows are available.

## Container-Based Build (docker-build.sh)

The `docker-build.sh` script runs a self-contained build inside a Docker container using the `phoenixrtos/build` image.
The build artifacts are produced in `_boot/` on the host.

```shell
TARGET=ia32-generic-qemu ./docker-build.sh all
```

**Features:**

- Isolated build environment (no host toolchain required)
- macOS optimization: automatically adds a `tmpfs` mount for `_build/` to speed up builds on macOS Docker
- Environment variable passthrough via `.docker_env` file (place `KEY=VALUE` lines in `.docker_env` at the project root)

## Interactive Development (docker-devel.sh)

The `docker-devel.sh` script starts an interactive shell inside a Docker container using the `phoenixrtos/devel` image.
The project workspace is mounted into the container for live editing.

```shell
./docker-devel.sh
```

**Features:**

- Interactive shell with all toolchains available
- Privileged mode with USB passthrough (`/dev/bus/usb`) for hardware flashing
- Project workspace files are shared between host and container

## Environment File

Create a `.docker_env` file in the project root to pass environment variables into the Docker container:

```
CONSOLE=serial
LONG_TEST=y
```

Both `docker-build.sh` and `docker-devel.sh` read this file via the `--env-file` Docker option.
