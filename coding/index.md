# Coding convention

The chapter presents coding convention used in the implementation files of Feniks-RTOS.

## C language standard

In general code should be compliant with C99 (without GNU extensions) standard.

## File label

Each operating system source file is marked with label with the following structure:

```c
    /*
     * <Project name>
	 *
	 * <Name of the software module, optional>
     *
     * <Brief file description>
     *
     * Copyright <Years of active development> Feniks Systems
     * Author: <List of authors>
     *
     * %LICENSE%
     */
```

Example of a file that is a part of the Feniks-RTOS kernel:

```c
    /*
     * Feniks-RTOS
     *
     * Operating system kernel
     *
     * pmap - machine dependent part of VM subsystem (ARM)
     *
     * Copyright 2014-2015 Feniks Systems
     * Copyright 2005-2006 Pawel Pisarczyk
     * Author: Pawel Pisarczyk, Radoslaw F. Wawrzusiak, Jacek Popko
     *
     * %LICENSE%
     */
```

Main label blocks are separated with empty line. The first label block informs that file is the part of Feniks-RTOS
operating system. In next block the information about the operating system module is provided. In this example, the file
belongs to operating system kernel. Third label block describes the file functionality. In presented example label, the
file implements `pmap` interface - the hardware dependent part of memory management subsystem for managing the MMU or
MPU (part of HAL). Fourth label block presents copyright notices and authors of the file. Newest copyrights are located
on the top. Copyrights are associated with dates informing about the development periods separated with commas. In the
example label the file was developed in years 2014-2015 and in the earlier period of 2005-2006. Presented file has three
authors sorted according to the importance of their contribution. All names are presented. Next block contains the
information that file belongs to the operating system project. The %LICENSE% macro is used to inject the license
conditions.

Labels in each file should be constructed according to presented rules. Modification of these rules is not allowed.

## Indentation

Code indentation is based on tabulator. It is not allowed to make an indentation with space character. The source code
used for development tests (e.g. printf debug) should be entered without indentation. The following code presents
correctly formatted code with one line (`lib_printf`) entered for debug purposes. The inserted line should be removed
in the final code.

```c
    int main(void)
    {
        _hal_init();
        hal_consolePrint(ATTR_BOLD, "Feniks-RTOS microkernel v. " VERSION "\n");

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

Separate source files should be created for each operating system module. Source files are grouped in directories which
names correspond to the names of subsystems.

## Functions

Functions should be short and not too complex in terms of logic. The function should do one thing only. Functions should
be separated with two newline characters.

## Function names

Function names should be created according to the following schema `[_]<subsystem>_<functionality>` where `<subsystem>`
is the name of subsystem or file to which function belongs and `<functionality>` is the brief sentence explaining the
implemented functionality. The subsystem name should be a one word without the underline characters. The functionality
could be expressed using many words but without the underlines. In such case camelCase should be used.

For example function for kernel space memory allocation could be named `vm_kmalloc()`. Function for creating a new
thread could be named `proc_threadCreate()`.

The underline character at the start of the function name means that function is not synchronized and its usage by two
parallel threads demands the external synchronization. Good example of such function is the internal function for adding
the node to the red-black tree or the internal function for adding the item to the list.

Functions used internally in C file should be declared as static. Functions used only inside the selected subsystem
could be named with the name of the module instead of the name of subsystem. Functions exported outside the subsystem
must be named with subsystem name only.

All external (i.e. non-static) symbols (including functions) of a library must be prefixed with a library name.
For example, lets say we have library `libfoo` and it's function called `init`. This function must be prefixed with
either `foo` or `libfoo` - prefix has to be unique and be consistent within the library:

```c
    int libfoo_init(void);

    /* or */

    int foo_init(void);
```

If a library consists of submodules (i.e. well separated modules within one library) then second underscore can be used
to separate library from submodule and from functionality names. Please note that in general such functions shouldn't be
a part of API, but need to adhere to namespace rules as can not be `static` also. Example of this naming scheme:

```c
    int libfoo_bar_start();
```

## Function length

Function should be not longer than 200 lines of code and not shorter than 10 lines of code.

## Variables

Variables should be named with one short words without the underline characters. If one word is not enough for variable
name then use camelCase. When defining a variable, assign it a value, do not assume that its value is zero. **In the
kernel code always initialize global/static variables in runtime.** There's not `.bss` and `.data` initialization in
the kernel.

`const` should be used whenever it is not expected or prohibited for value to change.

## Local variables - kernel

Local variables should be defined before the function code. The stack usage and number of local variables should be
minimized. Static local variables are not allowed.

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

## Local variables - libfeniks, userspace

Scope of local variables should be minimalized, as the stack usage and number of local variables. It is advised to
avoid reusing variables for different purposes across the function. Static local variables are allowed.

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

In the kernel code global variables should be always initialized in runtime. Global variables should be used only if
they're absolutely necessary. Scope should be limited whenever possible by using `static`. If they are used, global
variables can only be placed in common structures. The structure should be named after the system module that implements
it, followed by `_common`. Example notation is shown below.

```c
    static struct {
        spinlock_t spinlock;
    } pmap_common;
```

It is acceptable to omit module name in user space applications (i.e. not in the kernel) and name the structure
`common`, only if static is used.

## Operators

One space character should be used after and before the following binary and ternary operators:

```c
    =  +  -  <  >  *  /  %  |  &  ^  <=  >=  ==  !=  ?  :
```

No space should be used after the following unary operators:

```c
    &  *  +  -  ~  !
```

The `sizeof` and `typeof`are treated as functions and are to be used in accordance to the following notation:

```c
    sizeof(x)
    typeof(x)
```

In case of increment `++` and decrement `--` operators following rules should be applied. If they are postfixed, no
space should be used before the operator. If they are prefixed, no space should be used after the operator.

## Conditional expressions

Notation of conditional expression is presented below.

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

A space should be used after a keyword of the conditional instruction. Opening and closing braces should be always used.
The opening brace should be put in the same line as the keyword of the conditional instruction. The closing brace should
be placed after the last line of the conditional instruction in a new line.

## Type definition

New types can only be defined if it is absolutely necessary. if `typedef` is used for a structure/union, structure/union
should be left anonymous if possible:

```c
    typedef struct {
       int foo;
       int bar;
    } foobar_t;
```

## Comments

When the C programming language is used only C language comments should be used. It means that only `/* */` are allowed
and `//` are not to be used at all. A two line comment is presented below.

```c
    /*
     * line 1
     * line 2
     */
```

One line comment should look like the following example.

```c
    /* comment */
```

All comments should be brief and placed only in essential parts of the code. Comments are not the place to copy parts of
the specifications. Nor are they the place to express programmer's novel writing skills.

The use of any kind of documentation generator (e.g. Doxygen) is strictly forbidden.

## Code disabling

Leaving disabled, dead code should be avoided, version control should be relied upon to hold obsolete code. However,
should it be necessary, preprocessor should be used:

```c
        releveantCode();

    #if 0
        obsoleteFunction();
    #endif
```

## Preprocessor

The header with the `#include` preprocessing directive should be placed after the label. The example header notation is
shown below.

```c
    #include "pmap.h"
    #include "spinlock.h"
    #include "string.h"
    #include "console.h"
    #include "stm32.h
```

It is advised not to use MACROS in the code.

It is not advised to use preprocessor conditionals like `#if` or `if def'. The use of preprocessing conditionals makes
it harder to follow the code logic. If it is absolutely necessary to use preprocessing conditionals, they ought to be
formatted as the following example.

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

Following notation for operating system messages should be applied. Message should start from a subsystem name, which
should be followed by colon and a message body. An example is shown below.

```c
    lib_printf("main: Starting syspage programs (%d) and init\n", syspage->progssz);
```

## Coding guidelines

MISRA C:2012 coding guideline standard should be adhered to in all matters not addressed in this guideline (advisory
rules are optional).

## Miscellaneous

The `goto` statement shall not be used. The main goal of this prohibition is the minimalization of the spaghetti code
generation and the prevention of the linear programming usage.

To better understand our position please read the famous Dijkstra article.

<https://homepages.cwi.nl/~storm/teaching/reader/Dijkstra68.pdf>

In our opinion usage of `goto` increases the chaos in the source code and absolutely brings no value like
minimalization of the number of lines of code. It also encourages programmers to poor code structurization.

## See also

1. [Table of Contents](../index.md)
