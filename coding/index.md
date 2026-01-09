# Software Code Standards for C and Assembly Code

## Introduction

This document defines the Software Code Standards to be followed when writing Phoenix-RTOS source code.
It is organized into sections that group coding rules and recommendations by topic.

The ruleset defined for C language is based on the MISRA-C 2023 coding guidelines. The MISRA-C (*de facto*)
standard has been tailored down to match the needs and objectives of operating system development.


Rules identify quality considerations that must always be followed unless an exception is approved by
the Technical Coordinator and Quality Assurance Engineer, this has to be noted in the Source code peer-review.

Recommendations are practices which should be followed. Known exceptions have to be noted in the software coding
peer review record.

The identifiers referenced in this standard are:

- `PS-GEN-RULE-XXX` generic rules for all supported languages (C and assembly), which are formulated using `shall` what indicates mandatory action;
- `PS-GEN-REC-XXX` generic recommendations  for all supported languages (C and assembly), which are formulated using `should`;
- `PS-C-RULE-XXX` rules for C language, which are formulated using `shall` what indicates mandatory action;
- `PS-C-REC-XXX` recommendations for C language, which are formulated using `should`;
- `PS-ASM-RULE-XXX` rules for assembly, which are formulated using `shall` what indicates mandatory action;
- `PS-ASM-REC-XXX` recommendations for assembly, which are formulated using `should`.

### Note
Rule numbering does not have to be sequential and must not be changed once assigned.
If a new rule is added in any section, it should be assigned the next available number after the highest existing rule
number.

## Objectives
This Software Code Standards is intended to help software developers, in particular developers of 
Phoenix-RTOS to:

- establish a consistent coding style;
- establish objectives for code peer-review;
- avoid undefined behavior constructs in C language;
- avoid common programming errors;
- limit program complexity.

## Generic rules and recommendations

### Names and identifiers

#### PS-GEN-REC-001

English should be the only language allowed in the code base.

##### Note

This means english words are recommended for file and object names. It also means comments in other language 
than english are not allowed in the code base. This recommendation does NOT prohibit usage of the so-called 
loanwords commonly used in english for technical nomenclature, for example: greek symbols for mathematical 
and scientific notation.

##### Example

```c
uint32_t result;    /* compliant, english */
uint32_t wynik;     /* non-compliant, polish */
float alpha;        /* compliant, scientific notation */
bool is_valid;      /* compliant, english */

/* This function computes ... */    /* compliant, english */
/* Funkcja liczy ... */             /* non-compliant, polish */
```

#### PS-GEN-REC-002

Only characters from the standard ASCII range (0x20–0x7E) should be used for names and identifiers.

#### PS-GEN-REC-003

All files should use LF (Unix-style) line endings.

##### Note
This means CRLF (Windows-style) is not permitted.

### Source Files

#### PS-GEN-REC-004

Separate source files should be created for each operating system module.

#### PS-GEN-REC-005

Source files should be grouped in directories whose names correspond to the names of subsystems.

#### PS-GEN-REC-006

Source files should have following file extensions:

- `.c` - C source files;
- `.h` - C header files;
- `.S` - Assembly source files;

#### PS-GEN-REC-007

Only lowercase alphanumeric characters (a-z, 0-9), underscores (_), and hyphens (-) should be used for 
source and header file names.


#### PS-GEN-REC-008

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
 * <License Identifier>
 */
```

Main label blocks should be separated by an empty line.

The consecutive label blocks, in that order, should:

- inform that file is the part of Phoenix-RTOS operating system
- provide the information about the operating system
- describe the file functionality
- present copyright notices for the file, with the newest copyrights at the top and authors sorted
according to the importance of their contribution
- provide license information with License Identifier macro

##### License Identifier
The License Identifier specifies the selected license and it can be assigned identifier of one 
of the standard open source license as defined at the [SPDX List](https://spdx.org/licenses/) 
for open source products or `Phoenix-Commercial` for commercial products. The statement 
`SPDX-License-Identifier: ` precedes the license identifier.

For open source products, the default license selected by Phoenix Systems is BSD-3-Clause
license for which the SPDX defines identifier: `BSD-3-Clause`.

This licensing scheme is compliant with [REUSE Specification](https://reuse.software/spec/).

##### Example

In this example, the file belongs to operating system kernel. The file implements `pmap` interface -
the hardware dependent part of memory management subsystem for managing the MMU or MPU (part of HAL).
The file was developed in years 2014-2015 and in the earlier period of 2005-2006. It has three
authors sorted according to the importance of their contribution. All names are presented.

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
 * SPDX-License-Identifier: BSD-3-Clause
 */
```

### Indentation

#### PS-GEN-REC-009

The `Tab` character should be used as code indentation.

##### Note

It is not allowed to make an indentation with space character. The following code presents
correctly formatted code with one line (`lib_printf`) entered for debug purposes. The debug line
is also indented with `Tab` character following this recommendation.

##### Example

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

```
irq_fpu_done:
	st  %sp, [%sp + 0x00] /* sp */
	rd  %y, %g2
	st  %g2, [%sp + 0x04] /* y */
```

## Coding standard for C

### C language standard

#### PS-C-RULE-001

The code shall be compliant with C99 (without GNU extensions) standard.

### MISRA C 2023 (2012)

#### PS-C-RULE-002

The code shall be compliant with the set of MISRA C 2023 (2012) defined in
[Phoenix RTOS MISRA C Profile](./misracprofile.rst) with justified local rule exemptions.

##### Note
MISRA C 2023 rule headlines can be accessed on [MISRA official git repository](https://gitlab.com/MISRA/MISRA-C/MISRA-C-2012/tools/-/blob/main/misra_c_2023__headlines_for_cppcheck.txt?ref_type=heads) 


#### PS-C-RULE-003

Any local deviations from the [Phoenix RTOS MISRA C Profile](./misracprofile.rst) rules
shall be justified within the code.


### Functions and modules

#### PS-C-REC-004

Functions should be short and not too complex in terms of logic -
not shorter than 10 and not longer than 200 lines of code.

#### PS-C-REC-005

Functions should be separated with two `newline` characters.

#### PS-C-REC-006

Function names should be created according to the following schema `[_]<subsystem>_<functionality>` where:

- `<subsystem>` is the name of subsystem or file in which function belongs
- `<functionality>` is a brief sentence explaining the implemented functionality.

##### Note

Functions used only inside the selected subsystem could be named with the name of the module
instead of the name of subsystem.

#### PS-C-REC-007

The subsystem name should consist of one word.

#### PS-C-REC-008

The subsystem name should be written in the camelCase format if more than one word is used.

##### Note
The `underscore` character is not allowed in the subsystem name.

##### Example

The function for kernel space memory allocation could be named `vm_kmalloc()`.
The function for creating a new thread could be named `proc_threadCreate()`.

##### Note

An underscore character at the start of the function name indicates that the function is not synchronized, 
and its usage requires external synchronization. A good example of such function is the internal function
for adding a node to a red-black tree or the internal function for adding an item to a list.

#### PS-C-REC-009

Functions used only internally in the file, where they are defined, should be declared as `static`.

#### PS-C-REC-010

All external (i.e. non-static) symbols (including functions) of a library should be prefixed with the library name.

##### Example

Library name is equivalent to submodule name in this case. We have library `libfoo` and it's function called `init`. 
This function must be prefixed with either `foo` or `libfoo` - prefix has to be unique and be consistent within 
the library:

```c
int libfoo_init(void);

/* or */

int foo_init(void);
```

#### PS-C-REC-011

If a library consists of submodules (i.e. well separated modules within one library) then second underscore can be used
to separate library from submodule and from functionality names.

##### Note

Please note that in general such functions shouldn't be a part of API, but need to adhere to namespace rules
as they can not also be `static`.  

##### Example

```c
int libfoo_bar_start();
```

#### PS-C-REC-012

Function declaration should include arguments' names.

##### Example

Incorrect:

```c
int sum(int, int);
```

Correct:

```c
int sum(int a, int b);
```

#### PS-C-REC-013

*Rule derived from MISRA C.*

When function handler is an argument of a function it should be specified with explicit arguments.

##### Example

Incorrect:

```c
int hal_cpuCreateContext(cpu_context_t **nctx, void *start, void *kstack, size_t kstacksz, void *ustack, void *arg, hal_tls_t *tls)
```

Correct:

```c
int hal_cpuCreateContext(cpu_context_t **nctx, void (*start)(void *harg), void *kstack, size_t kstacksz, void *ustack, void *arg, hal_tls_t *tls)
```

#### PS-C-REC-014

*Recommendation derived from MISRA C.*

If the function output is not used it should be cast to `void`.

##### Example

```c
(void)lib_vprintf(fmt, ap);
```

#### PS-C-REC-015

*Recommendation derived from MISRA C.*

Function types should be `typedef`-ed with `Fn_t` suffix to make them distinguishable from non-function types,
e.g. `startFn_t`, `sighandlerFn_t`

#### PS-C-REC-016

*Recommendation derived from MISRA C.*

`extern` keyword should not be used in function prototypes as it’s the default.

### Variables

#### PS-C-REC-017

Variables should be named with one short word without the underscore characters.

#### PS-C-REC-018

For variable names longer than one word, the camelCase format should be used.

#### PS-C-REC-019

When defining a variable, it should be assigned with a value (do not assume that its value is zero).

##### Note

**In the kernel code always initialize global/static variables at runtime.** There's not `.bss` and
`.data` initialization in the kernel.


### Local variables - kernel

#### PS-C-REC-020

Local variables should be defined before the function code in the kernel.

#### PS-C-REC-021

The stack usage and number of local variables should be minimized in the kernel.

#### PS-C-REC-022

Static local variables should not be used in the kernel.

##### Example

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

### Local variables - libphoenix, userspace

#### PS-C-REC-023

Scope of local variables should be minimized in `libphoenix` and user space (as the stack usage and
number of local variables).

#### PS-C-REC-024

The variables should not be used for different purposes across the function.

#### PS-C-REC-025

Static local variables should be used in only `libphoenix` and user space.

##### Example

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

### Global variables

#### PS-C-REC-026

In the kernel code global variables should be always initialized at runtime.

#### PS-C-REC-027

Global variables should be used only if they're absolutely necessary.

#### PS-C-REC-028

The scope of global variables should be limited whenever possible by using `static`.

#### PS-C-REC-029

Global variables should only be placed in common structures.

#### PS-C-REC-030

The structure should be named after the system module that implements it, followed by `_common`.

##### Example

```c
static struct {
    spinlock_t spinlock;
} pmap_common;
```

##### Note

The module name could be omitted in user space applications (i.e. not in the kernel) and name the structure `common`,
only if static is used.

### Operators

#### PS-C-REC-031

One space character should be used after and before the following binary and ternary operators:

```c
=  +  -  <  >  *  /  %  |  &  ^  <=  >=  ==  !=  ?  :
```

#### PS-C-REC-032

No space should be used after the following unary operators:

```c
&  *  +  -  ~  !
```

#### PS-C-REC-033

The `sizeof` and `typeof` operators should be treated as functions and are to be used in accordance
to the following notation:

```c
sizeof(x)
typeof(x)
```

#### PS-C-REC-034

If the increment `++` or decrement `--` operators are postfixed, no space should be used before the operator.

#### PS-C-REC-035

If the increment `++` or decrement `--` operators are prefixed, no space should be used after the operator.

### Conditional expressions

#### PS-C-REC-036

A space should be used after a keyword of the conditional instruction.

#### PS-C-REC-037

Opening and closing braces should always be used.

#### PS-C-REC-038

The opening brace should be put in the same line as the keyword of the conditional instruction.

#### PS-C-REC-039

The closing brace should be placed after the last line of the conditional instruction in a new line.

##### Example

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

#### PS-C-REC-040

*Recommendation derived from MISRA C.*

Only values of `bool` type should be used as condition input.

##### Example

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

### Comparison output

#### PS-C-REC-041

*Recommendation derived from MISRA C.*

An outcome of comparison operation should not be used as an integer value.

##### Example

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

### Type specifiers and definitions

#### PS-C-REC-042

New types should only be defined if it is absolutely necessary.

#### PS-C-REC-043

If `typedef` is used for a structure/union, structure/union should be left anonymous if possible:

##### Example

```c
typedef struct {
    int foo;
    int bar;
} foobar_t;
```

#### PS-C-REC-044

*Recommendation derived from MISRA C.*

Types of defined length should be used over default C types.

##### Note

That is especially valid for static variables used to operate on processor registers.

##### Example

Not recommended:
`unsigned char`

Recommended:
`uint8_t, u8, __u8`

### Comments

#### PS-C-REC-045

When the C programming language is used only C language comments should be used: `/* */`.

##### Note

`//` comments are not allowed in C source and header files.

##### Example

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

#### PS-C-REC-046

Comments should be brief and placed only in essential parts of the code.

#### PS-C-REC-047

Comments should not contain copied parts of specification.

#### PS-C-REC-048

Documentation generators (e.g. Doxygen) should not be used.

### Code disabling

#### PS-C-REC-049

Disabled or dead code should not be placed in the code.

##### Note

Version control should be relied upon to hold obsolete code.

### Preprocessor

#### PS-C-REC-050

Each header file (`.h`) should include header guard formatted as follows:

- based on `#ifndef`, `#define`, and `#endif` directives placed at the beginning and end of the file;
- starts and ends with `_`;
- upper case with `_` as words separator;
- name derived from module mnemonic and file name.

##### Note
Header guard protect from multiple inclusions.

##### Example
```c
/*
 * Phoenix-RTOS, file syscalls.h
 * ...
 * SPDX-License-Identifier: BSD-3-Clause
 */
#ifndef _PH_SYSCALLS_H_
#define _PH_SYSCALLS_H_

void _syscalls_init(void);

#endif
```

#### PS-C-REC-051

The header with the `#include` preprocessing directive should be placed after the label and header guard (for `.h` files).

##### Example

```c
#include "pmap.h"
#include "spinlock.h"
#include "string.h"
#include "console.h"
#include "stm32.h"
```

```c
#ifndef _PH_POSIX_POSIX_PRIVATE_H_
#define _PH_POSIX_POSIX_PRIVATE_H_

#include "hal/hal.h"
#include "proc/proc.h"
#include "posix.h"
```

#### PS-C-REC-052

The MACROS and DEFINE names should be written in upper case with `_` words separator.

##### Note
This allows to easily distinguish MACROS/DEFINES from objects.

#### PS-C-REC-053

The usage of MACROS should be minimized.

##### Note
Preprocessor text substitution for MACROS can lead to unexpected behavior. It is recommended to use 
`inline` functions instead.

#### PS-C-REC-054

The usage of preprocessing conditionals like: `#if`, `#ifdef` or `#ifndef` should be minimized
and limited to header guards.

##### Note

The use of preprocessing conditionals makes it harder to follow the code logic and can be used only
if it is absolutely necessary. The justification for each use case will be provided in code review.

#### PS-C-REC-055

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

### Operating system messages

#### PS-C-REC-056

Operating system messages should consist of, in that order:

- a subsystem name
- a colon
- a message body
- a newline character

##### Example

```c
lib_printf("main: Starting syspage programs (%d) and init\n", syspage->progssz);
```

### Literals

#### PS-C-REC-057

The numeric literals suffixes should be written with capital letters.

##### Example

```c
#define SIZE_PAGE 0x200U
```

#### PS-C-REC-058

*Recommendation derived from MISRA C.*

When shifting unsigned constants by more than 7 bits the `UL` suffix should be used.

##### Explanation

It’s not sufficient to mark them with `U` as MISRA classifies `U` constants, despite the C standard implications, as
8-bit essential type (see the “To assist in understanding” example in Rule 12.2 rationale, D.3 and D.7.4).

##### Exception

Per exception 1 to rule 10.3 it is allowed to assign simple constants to unsigned variables without the `U`/`UL` suffix,
like `size_t i = 0` provided that the constant fits into the variable type. Use of this exception is permitted as long
as it is stylistically consistent.

#### PS-C-REC-059

The numeric hexadecimal literals should be written with small letters.

##### Example

```c
#define SIZE_PAGE 0xffU
```

#### PS-C-REC-060

*Recommendation derived from MISRA C.*

`\0` literal should be used to define a variable of `char` type with a value of 0.

### Pointers

#### PS-C-REC-061

`NULL` should be used as default value for empty pointers.

### Miscellaneous

#### PS-C-REC-062

The `goto` statement should not be used.

##### Note

The main goal of this prohibition is the minimization of the spaghetti code
generation and the prevention of the linear programming usage.

To better understand our position please read the famous Dijkstra article.

<https://homepages.cwi.nl/~storm/teaching/reader/Dijkstra68.pdf>

In our opinion, the usage of goto increases chaos in the source code and
offers no value, such as minimizing the number of lines of code.
It also encourages programmers to poor code structurization.

#### PS-C-REC-063

*Recommendation derived from MISRA C.*

Usage of flexible array members should be minimized.

##### Explanation
While MISRA C prohibits the use of flexible array members, Phoenix-RTOS kernel employs this type of structure for kernel 
level management of dynamic data objects and memory. The recommendation to minimize usage of such constructs is dictated ]
due to potential implication of the presence of flexible array members (e.g. modification of behavior of `sizeof`).

##### Example
```c
typedef struct _vm_object_t {
	rbnode_t linkage;
	oid_t oid;
	int refs;
	size_t size;
	page_t *pages[];
} vm_object_t;
```

In the code above flexible structure `_vm_object_t` is used for memory management. Field `pages` can contain pointers to 
multiple pages in memory hence the allowed use of flexible array member.

#### PS-C-REC-064

*Recommendation derived from MISRA C.*

Recursive function calls, both direct and indirect, should be prohibited

##### Explanation
Recursive execution might make it impossible to determine the worst case stack usage.


#### PS-C-REC-065

All user input should be sanitized - consider this especially in cases such as syscall implementations:
 e.g. check if flags are in the required range (example: `(var & FLAG_MASK_ALL) == 0`).

### Appendixes

```{toctree}
:maxdepth: 1
misracprofile.rst

```

## Coding standard for Assembly
This coding standard is designed for GNU GCC and [GNU Assembler](https://www.gnu.org/software/binutils/) and
is targeting multiple architectures supported by Phoenix-RTOS. Presented rules and recommendations are introduced 
to maintain a consistent working experience across different Instruction Set Architectures.

### General rules and formatting

#### PS-ASM-REC-001

All assembly mnemonics (instructions) and register names should be written in lower case.

##### Example
```
movl %dr7, %eax   /* IA-32 ISA */
```

```
mov x1, sp        /* ARM64 ISA */
```

#### PS-ASM-REC-002

C language style comments should be used: `/* */` in assembly code.

##### Note

This allows to maintain a unified standard that works across all GCC-supported architectures. 
Architecture-specific comment characters (like `@` in ARM or `;` in IA-32/SPARC are not allowed. 

##### Example
```
irq_no_switch:
	/* restore current window */
	ld  [%sp + 0x04], %g1 /* y */
```

#### PS-ASM-REC-003

Assembly labels should be left aligned without any indentation.

### Defines and Preprocessing

#### PS-ASM-REC-004

C styles `#define` should be used for constants.

#### PS-ASM-REC-005

Magic numbers in code should be avoided.

##### Example
```
irq_no_switch:
#define X_ESR_EL1   x28

	mrs X_ESR_EL1, esr_el1      /* correct */
	mrs x28, esr_el1            /* incorrect, magic number in code! */
```

### Labels and naming

#### PS-ASM-REC-006

Local labels (no entry point to C code) should be written in lower case with `_` word separator.

##### Note

Labels for C code entry points match C declaration. Short labels e.g. `1:` are allowed e.g. for loops.

### Memory and Data

#### PS-ASM-REC-007

.align or .balign directive should be placed before data or functions declaration to ensure proper alignment.

##### Example

```
.align 4
.type .L_two_nans, %object
.L_two_nans:
.word 0
.word 0x7ff80000
.word 0
.word 0
.word 0
.word 0x7ff80000
.word 0
.word 0
```
