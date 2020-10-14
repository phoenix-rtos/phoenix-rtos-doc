# Building Phoenix-RTOS image

To create Phoenix-RTOS image for selected target the `phoenix-rtos-project` repository should be used. This repository aggregates all operating system modules.

## Cloning and initializing repository

Clone the repository and `cd` into it:

````bash
git clone https://github.com/phoenix-rtos/phoenix-rtos-project.git
cd phoenix-rtos-project/
````
Initialize and update git submodules:
```bash
git submodule update --init --recursive