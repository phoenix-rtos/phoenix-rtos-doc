# Phoenix-RTOS loader (plo)

Phoenix-RTOS uses its own operating system loader - plo (Phoenix LOader).

Loader was initially implemented for IA32 but currently supports other architectures as well. It should be used when target device doesn't support execution of the code from FLASH or ROM and the code should be loaded into the RAM.

Loader is highly recommended for advanced projects where remote upgrade functionality is required. It enables to check the firmware consistency before operating system and application are started.

## Source code
The source code of the libphoenix could be obtained using the following command

>
    git clone http://git.phoenix-rtos.com/plo

## See also

1. [Table of Contents](../README.md)