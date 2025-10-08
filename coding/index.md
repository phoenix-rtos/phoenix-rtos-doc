# Coding Standard
This is the Coding Standard, which shall be used during the implementation of files of Phoenix-RTOS.  
It consists of sections that group coding rules by topic.  
Coding rules are identified with ID of such format: `PS-CODE-XXX`.  
Rule numbering does not have to be sequential and should not be changed once assigned.
If a new rule is added in any section, it should be assigned the next available number after the highest existing rule number.

Rules are formulated using these special statements:
- `shall` indicates mandatory rule or action  
- `should` indicates recommended rule or action
- `could` indicates possibility or an option that is not necessarily recommended.


## C language standard
### PS-CODE-001
The code shall be compliant with C99 (without GNU extensions) standard.

## MISRA C 2023 (2012)
### PS-CODE-002
The code should be compliant with the set of MISRA C 2023 (2012) defined in [Phoenix RTOS MISRA C Profile](./misracprofile.md)  

### PS-CODE-003
Any deviations from the MISRA C 2023 (2012) mandatory and required rules shall be justified within TBD.

## File label
### PS-CODE-004 
Each operating system source file shall be marked with label with the following structure:  
```c
/*
 * <Project name>
 *
 * <Name of the software module, optional>
 *
 * <Brief file description>
 *
 * Copyright <Years of active development> Phoenix Systems
 * Author: <List of authors>
 *
 * %LICENSE%
 */
```

### PS-CODE-005
Main label blocks shall be separated by an empty line.

### PS-CODE-006
The consecutive label blocks, in that order, shall:
- inform that file is the part of Phoenix-RTOS operating system
- provide the information about the operating system 
- describe the file functionality 
- present copyright notices for the file, with the newest copyrights at the top and authors sorted according to the importance of their contribution
- provide license information with %LICENSE% macro

#### Example: 
In this example, the file belongs to operating system kernel. The file implements `pmap` interface - the hardware dependent 
part of memory management subsystem for managing the MMU or MPU (part of HAL). 
The file was developed in years 2014-2015 and in the earlier period of 2005-2006. It has three
authors sorted according to the importance of their contribution. All names are presented. 
The %LICENSE% macro is used to inject the license conditions.  
```c
/*
 * Phoenix-RTOS
 *
 * Operating system kernel
 *
 * pmap - machine dependent part of VM subsystem (ARM)
 *
 * Copyright 2014-2015 Phoenix Systems
 * Copyright 2005-2006 Pawel Pisarczyk
 * Author: Pawel Pisarczyk, Radoslaw F. Wawrzusiak, Jacek Popko
 *
 * %LICENSE%
 */
```

## Indentation
### PS-CODE-007
The Tab character shall be used as code indentation.

#### Note:
It is not allowed to make an indentation with space character. The source code
used for development tests (e.g. printf debug) should be entered without indentation. The following code presents
correctly formatted code with one line (`lib_printf`) entered for debug purposes. The inserted line should be removed
in the final code.

#### Example:  
```c
int main(void)
{
    _hal_init();
    hal_consolePrint(ATTR_BOLD, "Phoenix-RTOS microkernel v. " VERSION "\n");

    _vm_init(&main_common.kmap, &main_common.kernel);
    _proc_init(&main_common.kmap, &main_common.kernel);
    _syscalls_init();

    lib_printf("DEBUG: starting first process...\n");

    /* Start init process */
    proc_start(main_initthr, NULL, (const char *)"init");

    /* Start scheduling, leave current stack */
    hal_cpuEnableInterrupts();
    hal_cpuReschedule();

    return 0;
}
```

## Source files
### PS-CODE-008
Separate source files shall be created for each operating system module. 

### PS-CODE-009
Source files shall be grouped in directories which names correspond to the names of subsystems.

## Functions
### PS-CODE-010
Functions should be short and not too complex in terms of logic.

### PS-CODE-011
The function should do one thing only.

### PS-CODE-012
Functions should be separated with two newline characters.

## Function names  
### PS-CODE-013  
Function names shall be created according to the following schema `[_]<subsystem>_<functionality>` where:
- `<subsystem>`is the name of subsystem or file to which function belongs
- `<functionality>` is the brief sentence explaining the implemented functionality. 

### PS-CODE-014  
The subsystem name should be a one word.

### PS-CODE-015  
The subsystem name shall not contain the underscore characters

### PS-CODE-016  
The subsystem name shall be written in camelCase if more the one word is used.

### Example: 
The function for kernel space memory allocation could be named `vm_kmalloc()`. 
The function for creating a newthread could be named `proc_threadCreate()`.

### Note:
The underscore character at the start of the function name means that function is not sAn underscore character at the start of the function name indicates that the function is not synchronized, and its usage by two parallel threads requires external synchronization. A good example of such function is the internal function for adding
the node to the red-black tree or the internal function for adding the item to the list.

### PS-CODE-017
Functions used internally in C file shall be declared as static. 

### PS-CODE-018
Functions used only inside the selected subsystem shall be named with the name of the module instead of the name of subsystem. 

### PS-CODE-019
Functions exported outside the subsystem shall be named with subsystem name only.

### PS-CODE-020
All external (i.e. non-static) symbols (including functions) of a library shall be prefixed with a library name.

### Example
Let's say we have library `libfoo` and it's function called `init`. This function must be prefixed with
either `foo` or `libfoo` - prefix has to be unique and be consistent within the library:

```c
int libfoo_init(void);

/* or */

int foo_init(void);
```

### PS-CODE-021
If a library consists of submodules (i.e. well separated modules within one library) then second underscore can be used
to separate library from submodule and from functionality names. 

#### Note:
Please note that in general such functions shouldn't be a part of API, but need to adhere to namespace rules as can not be `static` also. 

#### Example
```c
int libfoo_bar_start();
```

## Function length
### PS-CODE-022
Function shall be not longer than 200 lines of code and not shorter than 10 lines of code.

## Variables
### PS-CODE-023
Variables should be named with one short word without the underscore characters. 

### PS-CODE-024
For variable names, longer than one word, the camelCase shall be used. 

### PS-CODE-025
When defining a variable, it shall be assigned with a value (do not assume that its value is zero).

#### Note:
**In the kernel code always initialize global/static variables in runtime.** There's not `.bss` and `.data` initialization in
the kernel.

### PS-CODE-026
`const` should be used whenever it is not expected or prohibited for value to change.

## Local variables - kernel
### PS-CODE-027
Local variables shall be defined before the function code in the kernel.

### PS-CODE-028
The stack usage and number of local variables should be minimized in the kernel.

### PS-CODE-029
Static local variables shall not be used in the kernel.

### Example
```c
void *_kmalloc_alloc(u8 hdridx, u8 idx)
{
    void *b;
    vm_zone_t *z = kmalloc_common.sizes[idx];

    b = _vm_zalloc(z, NULL);
    kmalloc_common.allocsz += (1 << idx);

    if (idx == hdridx) {
        kmalloc_common.hdrblocks--;
    }

    if (z->used == z->blocks) {
        _vm_zoneRemove(&kmalloc_common.sizes[idx], z);
        _vm_zoneAdd(&kmalloc_common.used, z);
    }

    return b;
}
```

## Local variables - libphoenix, userspace
### PS-CODE-030
Scope of local variables should be minimalized in libphoenix and userspace (as the stack usage and number of local variables). 

### PS-CODE-031
The variables should not be used for different purposes across the function. 

### PS-CODE-032
Static local variables could be used in libphoenix and userspace.

### Example
```c
void countSheeps(herd_t *herd)
{
    static int lastCount = 0;
    int count = 0;

    for (size_t i = 0; i < sizeof(herd->sheeps) / sizeof(herd->sheeps[0]); ++i) {
        if (herd->sheeps[i] != NULL) {
            ++count;
        }
    }

    printf("Counted %d sheeps (last time it was %d)\n", count, lastCount);
    lastCount = count;
}
```

## Global variables
### PS-CODE-033
In the kernel code global variables shall be always initialized in runtime.

### PS-CODE-034
Global variables should be used only if they're absolutely necessary.

### PS-CODE-035
The scope of global variables should be limited whenever possible by using `static`.

### PS-CODE-036
Global variables shall only be placed in common structures. 

### PS-CODE-037
The structure should be named after the system module that implements it, followed by `_common`. 

#### Example:
```c
static struct {
    spinlock_t spinlock;
} pmap_common;
```

### PS-CODE-038
The module name could be omitted in user space applications (i.e. not in the kernel) and name the structure `common`, only if static is used.

## Operators
### PS-CODE-039
One space character shall be used after and before the following binary and ternary operators:  
```c
=  +  -  <  >  *  /  %  |  &  ^  <=  >=  ==  !=  ?  :
```

### PS-CODE-040
No space shall be used after the following unary operators:  
```c
&  *  +  -  ~  !
```

### PS-CODE-041
The `sizeof` and `typeof` operators shall be treated as functions and are to be used in accordance to the following notation:  
```c
sizeof(x)
typeof(x)
```

### PS-CODE-042
If the increment `++` or decrement `--` operators are postfixed, no space shall be used before the operator. 

### PS-CODE-043
If the increment `++` or decrement `--` operators are prefixed, no space should be used after the operator.

## Conditional expressions
### PS-CODE-044
A space shall be used after a keyword of the conditional instruction. 

### PS-CODE-045
Opening and closing braces shall be always used.

### PS-CODE-046
The opening brace shall be put in the same line as the keyword of the conditional instruction. 

### PS-CODE-047
The closing brace shall be placed after the last line of the conditional instruction in a new line.

### Example:
```c
if (expr) {
    line 1
}

if (expr0) {
    line 1
    ...
}
else if (expr1) {
    line 1
    ...
}
else {
    line 1
    ...
}
```

## Type definition
### PS-CODE-048
New types should only be defined if it is absolutely necessary. 

### PS-CODE-049
if `typedef` is used for a structure/union, structure/union should be left anonymous if possible:

### Example
```c
typedef struct {
    int foo;
    int bar;
} foobar_t;
```

## Comments
### PS-CODE-050
When the C programming language is used only C language comments shall be used: `/* */`.

### PS-CODE-051
`//` comments shall not to be used.

### Example
Multi line comment:
```c
/*
 * line 1
 * line 2
 */
```

One line comment:

```c
/* comment */
```
### PS-CODE-052
Comments should be brief and placed only in essential parts of the code. 

### PS-CODE-053
Comments should not contain copied parts of specification.

### Note:
Comments are not the place to express programmer's novel writing skills.

### PS-CODE-054
Documentation generators (e.g. Doxygen) shall not be used.

## Code disabling
### PS-CODE-055
Disabled or dead code should not be placed in the code.
### Note:
Version control should be relied upon to hold obsolete code.

### PS-CODE-056
If disabled or dead code is present (it was necessary), preprocessor shall be used accordingly:  
```c
releveantCode();

#if 0
    obsoleteFunction();
#endif
```

## Preprocessor
### PS-CODE-057
The header with the `#include` preprocessing directive shall be placed after the label. 

### Example
```c
#include "pmap.h"
#include "spinlock.h"
#include "string.h"
#include "console.h"
#include "stm32.h"
```
### PS-CODE-058
MACROS should not be used in the code.

### PS-CODE-059
The preprocessor conditionals like `#if` or `if def` should not be used in the code.
#### Note: 
The use of preprocessing conditionals makes it harder to follow the code logic and can be used only if it is absolutely necessary.

### PS-CODE-060
Preprocessing conditionals shall be formatted as the following example:  
```c
#ifndef NOMMU
    process->mapp = &process->map;
    process->amap = NULL;

    vm_mapCreate(process->mapp, (void *)VADDR_MIN, process_common.kmap->start);

    /* Create pmap */
    p = vm_pageAlloc(SIZE_PAGE, PAGE_OWNER_KERNEL | PAGE_KERNEL_PTABLE);
    vaddr = vm_mmap(process_common.kmap, process_common.kmap->start, p, 1 << p->idx, NULL, 0, 0);

    pmap_create(&process->mapp->pmap, &process_common.kmap->pmap, p, vaddr);
#else
    process->mapp = process_common.kmap;
    process->amap = NULL;
    process->lazy = 1;
#endif
```

## Operating system messages
### PS-CODE-061
Operating system messages shall consist of, in that order:
- a subsystem name
- a colon
- a message body
- a newline character

### Example
```c
lib_printf("main: Starting syspage programs (%d) and init\n", syspage->progssz);
```
## Literals
### PS-CODE-063
The numeric literals suffixes shall be written with capital letters.

### Example
```c
#define SIZE_PAGE 0x200U
```

### PS-CODE-063
The numeric hexadecimal literals shall be written with small letters.

### Example
```c
#define SIZE_PAGE 0xffU
```

## Miscellaneous
### PS-CODE-062
The `goto` statement shall not be used. 

#### Note
The main goal of this prohibition is the minimization of the spaghetti code
generation and the prevention of the linear programming usage.

To better understand our position please read the famous Dijkstra article.

<https://homepages.cwi.nl/~storm/teaching/reader/Dijkstra68.pdf>

In our opinion, the usage of goto increases chaos in the source code and offers no value, such as minimizing the number of lines of code. It also encourages programmers to poor code structurization.
