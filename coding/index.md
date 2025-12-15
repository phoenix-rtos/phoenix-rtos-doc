# Software Code Standards

## Introduction

This document defines the Software Code Standards to be followed when writing Phoenix-RTOS source code.
It is organized into sections that group coding rules, recommendations by topic.
Rules identify quality considerations that must always be followed unless an exception is approved by
the Technical Coordinator and Quality Assurance Engineer, this has to be noted in the  Source code peer-review.

Recommendations are practices which should be followed. Known exceptions have to be noted in the software coding
peer review record.

The identifiers referenced in this standard are:

- `PS-CODE-RULE-XXX` for rules, which are formulated using `shall` what indicates mandatory action;
- `PS-CODE-REC-XXX` for recommendations, which are formulated using `should`;

### Note

Rule numbering does not have to be sequential and should not be changed once assigned.
If a new rule is added in any section, it should be assigned the next available number after the highest existing rule
number.

## C language standard

### PS-CODE-RULE-001

The code shall be compliant with C99 (without GNU extensions) standard.

## MISRA C 2023 (2012)

### PS-CODE-RULE-002

The code shall be compliant with the set of MISRA C 2023 (2012) defined in
[Phoenix RTOS MISRA C Profile](./misracprofile.rst) with justified local rule exemptions.

### PS-CODE-RULE-003

Any local deviations from the [Phoenix RTOS MISRA C Profile](./misracprofile.rst) rules
shall be justified within the code.

## File label

### PS-CODE-REC-004

Each operating system source file should be marked with label with the following structure:

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

Main label blocks should be separated by an empty line.

The consecutive label blocks, in that order, should:

- inform that file is the part of Phoenix-RTOS operating system
- provide the information about the operating system
- describe the file functionality
- present copyright notices for the file, with the newest copyrights at the top and authors sorted
according to the importance of their contribution
- provide license information with %LICENSE% macro

#### Example

In this example, the file belongs to operating system kernel. The file implements `pmap` interface -
the hardware dependent part of memory management subsystem for managing the MMU or MPU (part of HAL).
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

## Allowed characters

### PS-CODE-REC-007

Only characters from the standard ASCII range (0x20–0x7E) should be used in source files.

## Indentation

### PS-CODE-REC-008

The `Tab` character should be used as code indentation.

#### Note

It is not allowed to make an indentation with space character. The source code
used for development tests (e.g. printf debug) should be entered without indentation. The following code presents
correctly formatted code with one line (`lib_printf`) entered for debug purposes. The inserted line should be removed
in the final code.

#### Example

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

### PS-CODE-REC-009

Separate source files should be created for each operating system module.

### PS-CODE-REC-010

Source files should be grouped in directories whose names correspond to the names of subsystems.

## Functions and modules

### PS-CODE-REC-011

Functions should be short and not too complex in terms of logic -
not shorter than 10 and not longer than 200 lines of code.

### PS-CODE-REC-012

The function should do one thing only.

### PS-CODE-REC-013

Functions should be separated with two `newline` characters.

### PS-CODE-REC-014

Function names should be created according to the following schema `[_]<subsystem>_<functionality>` where:

- `<subsystem>` is the name of subsystem or file in which function belongs
- `<functionality>` is a brief sentence explaining the implemented functionality.

#### Note

Functions used only inside the selected subsystem could be named with the name of the module
instead of the name of subsystem.

### PS-CODE-REC-016

The subsystem name should consist of one word.

### PS-CODE-REC-017

The subsystem name should not contain the `underscore` characters.

### PS-CODE-REC-018

The subsystem name should be written in the camelCase format if more than one word is used.

#### Example

The function for kernel space memory allocation could be named `vm_kmalloc()`.
The function for creating a new thread could be named `proc_threadCreate()`.

#### Note

An underscore character at the start of the function name indicates that the function is not synchronized, and its usage
by two parallel threads requires external synchronization. A good example of such function is the internal function
for adding a node to a red-black tree or the internal function for adding an item to a list.

### PS-CODE-REC-019

Functions used only internally in the file, where they are defined, should be declared as `static`.

### PS-CODE-REC-020

Functions exported outside the subsystem should be named with the subsystem name only.

### PS-CODE-REC-021

All external (i.e. non-static) symbols (including functions) of a library should be prefixed with the library name.

#### Example

We have library `libfoo` and it's function called `init`. This function must be prefixed with
either `foo` or `libfoo` - prefix has to be unique and be consistent within the library:

```c
int libfoo_init(void);

/* or */

int foo_init(void);
```

### PS-CODE-REC-022

If a library consists of submodules (i.e. well separated modules within one library) then second underscore can be used
to separate library from submodule and from functionality names.

#### Note

Please note that in general such functions shouldn't be a part of API, but need to adhere to namespace rules
as they can not also be `static`.  

#### Example

```c
int libfoo_bar_start();
```

### PS-CODE-REC-023

*Rule derived from MISRA C.*

When function handler is an argument of a function it should be specified with explicit arguments.

#### Example

Incorrect:

```c
int hal_cpuCreateContext(cpu_context_t **nctx, void *start, void *kstack, size_t kstacksz, void *ustack, void *arg, hal_tls_t *tls)
```

Correct:

```c
int hal_cpuCreateContext(cpu_context_t **nctx, void (*start)(void *harg), void *kstack, size_t kstacksz, void *ustack, void *arg, hal_tls_t *tls)
```

### PS-CODE-REC-025

*Recommendation derived from MISRA C.*

If the function output is not used it should be cast to `void`.

#### Example

```c
(void)lib_vprintf(fmt, ap);
```

### PS-CODE-REC-026

*Recommendation derived from MISRA C.*

Function types should be `typedef`-ed with `Fn_t` suffix to make them distinguishable from non-function types,
e.g. `startFn_t`, `sighandlerFn_t`

### PS-CODE-REC-027

*Recommendation derived from MISRA C.*

`extern` keyword should not be used in function prototypes as it’s the default.

## Variables

### PS-CODE-REC-028

Variables should be named with one short word without the underscore characters.

### PS-CODE-REC-029

For variable names longer than one word, the camelCase format should be used.

### PS-CODE-REC-030

When defining a variable, it should be assigned with a value (do not assume that its value is zero).

#### Note

**In the kernel code always initialize global/static variables at runtime.** There's not `.bss` and
`.data` initialization in the kernel.

### PS-CODE-REC-031

**In the kernel code always initialize global/static variables at runtime.** There's no `.bss` and
`const` should be used whenever it is not expected or prohibited for value to change.

## Local variables - kernel

### PS-CODE-REC-032

Local variables should be defined before the function code in the kernel.

### PS-CODE-REC-033

The stack usage and number of local variables should be minimized in the kernel.

### PS-CODE-REC-034

Static local variables should not be used in the kernel.

#### Example

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

### PS-CODE-REC-035

Scope of local variables should be minimized in libphoenix and userspace (as the stack usage and
number of local variables).

### PS-CODE-REC-036

The variables should not be used for different purposes across the function.

### PS-CODE-REC-037

Static local variables should be used in only libphoenix and userspace.

#### Example

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

### PS-CODE-REC-038

In the kernel code global variables should be always initialized at runtime.

### PS-CODE-REC-039

Global variables should be used only if they're absolutely necessary.

### PS-CODE-REC-040

The scope of global variables should be limited whenever possible by using `static`.

### PS-CODE-REC-041

Global variables should only be placed in common structures.

### PS-CODE-REC-042

The structure should be named after the system module that implements it, followed by `_common`.

#### Example

```c
static struct {
    spinlock_t spinlock;
} pmap_common;
```

#### Note

The module name could be omitted in user space applications (i.e. not in the kernel) and name the structure `common`,
only if static is used.

## Operators

### PS-CODE-REC-044

One space character should be used after and before the following binary and ternary operators:

```c
=  +  -  <  >  *  /  %  |  &  ^  <=  >=  ==  !=  ?  :
```

### PS-CODE-REC-045

No space should be used after the following unary operators:

```c
&  *  +  -  ~  !
```

### PS-CODE-REC-046

The `sizeof` and `typeof` operators should be treated as functions and are to be used in accordance
to the following notation:

```c
sizeof(x)
typeof(x)
```

### PS-CODE-REC-047

If the increment `++` or decrement `--` operators are postfixed, no space should be used before the operator.

### PS-CODE-REC-048

If the increment `++` or decrement `--` operators are prefixed, no space should be used after the operator.

## Conditional expressions

### PS-CODE-REC-049

A space should be used after a keyword of the conditional instruction.

### PS-CODE-REC-050

Opening and closing braces should always be used.

### PS-CODE-REC-051

The opening brace should be put in the same line as the keyword of the conditional instruction.

### PS-CODE-REC-052

The closing brace should be placed after the last line of the conditional instruction in a new line.

#### Example

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

### PS-CODE-REC-053

*Recommendation derived from MISRA C.*

Only values of `bool` type should be used as condition input.

#### Example

Incorrect:

```c
unsigned int len = 0;

if (!len)

```

Correct:

```c
unsigned int len = 0;  

if (len == 0U)
```

## Comparison output

### PS-CODE-REC-054

*Recommendation derived from MISRA C.*

An outcome of comparison operation should not be used as an integer value.

#### Example

```c
unsigned int a = 1U, b = 0U, c;
```

Incorrect:

```c
c = a == b;
```

Correct:

```c
c = (a == b) ? 1U : 0U;
```

## Type specifiers and definitions

### PS-CODE-REC-55

The type specifiers from the list bellow should be used:

- `char`
- `unsigned char`
- `int`
- `unsigned int`
- `long`
- `unsigned long`
- `long long`
- `unsigned long long`

### PS-CODE-REC-056

New types should only be defined if it is absolutely necessary.

### PS-CODE-REC-057

If `typedef` is used for a structure/union, structure/union should be left anonymous if possible:

#### Example

```c
typedef struct {
    int foo;
    int bar;
} foobar_t;
```

### PS-CODE-REC-058

*Recommendation derived from MISRA C.*

Types of defined length should be used over default C types.

#### Note

That is especially valid for static variables used to operate on processor registers.

#### Example

Not recommended:
`unsigned char`

Recommended:
`uint8_t, u8, __u8`

## Comments

### PS-CODE-REC-059

When the C programming language is used only C language comments should be used: `/* */`.

### PS-CODE-REC-060

`//` comments should not to be used.

#### Example

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

### PS-CODE-REC-061

Comments should be brief and placed only in essential parts of the code.

### PS-CODE-REC-062

Comments should not contain copied parts of specification.

#### Note

Comments are not the place to express programmer's novel writing skills.

### PS-CODE-REC-063

Documentation generators (e.g. Doxygen) should not be used.

## Code disabling

### PS-CODE-REC-064

Disabled or dead code should not be placed in the code.

#### Note

Version control should be relied upon to hold obsolete code.

### PS-CODE-REC-065

If disabled or dead code is present (it was necessary), preprocessor should be used accordingly:

```c
releveantCode();

#if 0
    obsoleteFunction();
#endif
```

## Preprocessor

### PS-CODE-REC-066

The header with the `#include` preprocessing directive should be placed after the label.

#### Example

```c
#include "pmap.h"
#include "spinlock.h"
#include "string.h"
#include "console.h"
#include "stm32.h"
```

### PS-CODE-REC-067

MACROS should not be used in the code.

### PS-CODE-REC-068

The preprocessor conditionals like: `#if`, `#ifdef` or `#ifndef` should not be used in the code.

#### Note

The use of preprocessing conditionals makes it harder to follow the code logic and can be used only
if it is absolutely necessary.

### PS-CODE-REC-069

Preprocessing conditionals should be formatted as the following example:

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

### PS-CODE-REC-070

Operating system messages should consist of, in that order:

- a subsystem name
- a colon
- a message body
- a newline character

#### Example

```c
lib_printf("main: Starting syspage programs (%d) and init\n", syspage->progssz);
```

## Literals

### PS-CODE-REC-071

The numeric literals suffixes should be written with capital letters.

#### Example

```c
#define SIZE_PAGE 0x200U
```

### PS-CODE-REC-072

*Recommendation derived from MISRA C.*

When shifting unsigned constants by more than 7 bits the `UL` suffix should be used.

#### Explanation

It’s not sufficient to mark them with `U` as MISRA classifies `U` constants, despite the C standard implications, as
8-bit essential type (see the “To assist in understanding” example in Rule 12.2 rationale, D.3 and D.7.4).

#### Exception

Per exception 1 to rule 10.3 it is allowed to assign simple constants to unsigned variables without the `U`/`UL` suffix,
like `size_t i = 0` provided that the constant fits into the variable type. Use of this exception is permitted as long
as it is stylistically consistent.

### PS-CODE-REC-073

The numeric hexadecimal literals should be written with small letters.

#### Example

```c
#define SIZE_PAGE 0xffU
```

### PS-CODE-REC-074

*Recommendation derived from MISRA C.*

`\0` literal should be used to define a variable of `char` type with a value of 0.

## Pointers

### PS-CODE-REC-075

`NULL` should be used as default value for empty pointers.

## Miscellaneous

### PS-CODE-REC-076

The `goto` statement should not be used.

#### Note

The main goal of this prohibition is the minimization of the spaghetti code
generation and the prevention of the linear programming usage.

To better understand our position please read the famous Dijkstra article.

<https://homepages.cwi.nl/~storm/teaching/reader/Dijkstra68.pdf>

In our opinion, the usage of goto increases chaos in the source code and
offers no value, such as minimizing the number of lines of code.
It also encourages programmers to poor code structurization.

### PS-CODE-REC-077

All user input should be sanitized - consider this especially in cases such as syscall implementations:
 e.g. check if flags are in the required range (example: `(var & FLAG_MASK_ALL) == 0`).

## Appendixes

```{toctree}
:maxdepth: 1
misracprofile.rst

```
