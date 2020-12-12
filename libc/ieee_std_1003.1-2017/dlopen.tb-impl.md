###Synopsis

`#include <dlfcn.h>`

`void *dlopen(const char *file, int mode);`

###Description

The `dlopen()` function opens a symbol table handle.

Arguments:
<u>file</u> - the executable object file,
<u>mode</u> - the way `dlopen()` operates upon <u>file</u> with respect to the processing of relocations and the scope of visibility of the symbols provided within <u>file</u>.
 
The `dlopen()` function makes the symbols (function identifiers and data object identifiers) in the executable object file specified by <u>file</u> available to the calling program.

Executable object files eligible for this operation are shared libraries or programs.

The <u>file</u> argument is used to construct a pathname to the executable object file. 

If <u>file</u> is a null pointer, `dlopen()` returns a global symbol table handle for the currently running process image. This symbol table handle provides access to the symbols from an ordered set of executable object files consisting of the original program image file, any executable object files loaded at program start-up as specified by that process file (for example, shared libraries), and the set of executable object files loaded using `dlopen()` operations with the `RTLD_GLOBAL` flag. As the latter set of executable object files can change during execution, the set of symbols made available by this symbol table handle can also change dynamically.

Only a single copy of an executable object file is brought into the address space, even if `dlopen()` is invoked multiple times in reference to the executable object file, and even if different pathnames are used to reference the executable object file.

The <u>mode</u> parameter describes how `dlopen()` operates upon file with respect to the processing of relocations and the scope of visibility of the symbols provided within file. When an executable object file is brought into the address space of a process, it may contain references to symbols whose addresses are not known until the executable object file is loaded.

These references are relocated before the symbols can be accessed. The <u>mode</u> parameter governs when these relocations take place and may have the following values:

* `RTLD_LAZY` - Relocations are performed at the time of the `dlopen()` call. Specifying `RTLD_LAZY` improves performance on implementations supporting dynamic symbol binding since a process might not reference all of the symbols in an executable object file.
        
* `RTLD_NOW` - All necessary relocations are performed when the executable object file is first loaded. This may waste some processing if relocations are performed for symbols that are never referenced. This behaviour may be useful for applications that need to know that all symbols referenced during execution will be available before `dlopen()` returns.
 
Any executable object file loaded by `dlopen()` that requires relocations against global symbols can reference the symbols in the original process image file, any executable object files loaded at program start-up, from the initial process image itself, from any other executable object file included in the same `dlopen()` invocation, and any executable object files that were loaded in any `dlopen()` invocation and which specified the RTLD_GLOBAL flag. To determine the scope of visibility for the symbols loaded with a `dlopen()` invocation, the mode parameter should be a bitwise-inclusive OR with one of the following values:

*  `RTLD_GLOBAL` - The executable object file's symbols is made available for relocation processing of any other executable object file. In addition, symbol lookup using `dlopen(NULL,<u>mode</u>)` and an associated `dlsym()` allows executable object files loaded with this mode to be searched.
    
*  `RTLD_LOCAL` - The executable object file's symbols are not available for relocation processing of any other executable object file.

If neither `RTLD_GLOBAL` nor `RTLD_LOCAL` is specified, the default behaviour is unspecified.

If an executable object file is specified in multiple `dlopen()` invocations, <u>mode</u> is interpreted at each invocation.

If `RTLD_NOW` has been specified, all relocations are completed rendering further `RTLD_NOW` operations redundant and any further `RTLD_LAZY` operations irrelevant.

If `RTLD_GLOBAL` has been specified, the executable object file maintains the `RTLD_GLOBAL` status regardless of any previous or future specification of `RTLD_LOCAL`, as long as the executable object file remains in the address space.

Symbols introduced into the process image through calls to `dlopen()` are used in relocation activities. Such symbols duplicate symbols already defined by the program or previous `dlopen()` operations. To resolve the ambiguities such a situation might present, the resolution of a symbol reference to symbol definition is based on a symbol resolution order. Two such resolution orders are defined:

* load order - Load order establishes an ordering among symbol definitions, such that the first definition loaded (including definitions from the process image file and any dependent executable object files loaded with it) has priority over executable object files added later (by `dlopen()`). Load ordering is used in relocation processing. 

* dependency order - Dependency ordering uses a breadth-first order starting with a given executable object file, then all of its dependencies, then any dependents of those, iterating until all dependencies are satisfied. With the exception of the global symbol table handle obtained via a `dlopen()` operation with a null pointer as the file argument, dependency ordering is used by the `dlsym()` function. Load ordering is used in `dlsym()` operations upon the global symbol table handle.
    
When an executable object file is first made accessible via `dlopen()`, it and its dependent executable object files are added in dependency order. Once all the executable object files are added, relocations are performed using load order. If an executable object file or its dependencies had been previously loaded, the load and dependency orders may yield different resolutions.

The symbols introduced by `dlopen()` operations and available through `dlsym()` are at a minimum those which are exported as identifiers of global scope by the executable object file. Typically, such identifiers are those that were specified in C source code as having `extern` linkage.

###Return value

On success, `dlopen()` returns a symbol table handle, otherwise it returns a null pointer.

Possible reasons of fail:

* <u>file</u> cannot be found,

* <u>file</u> cannot be opened for reading,

* <u>file</u> is not of an appropriate executable object file format for processing by `dlopen()`,

* an error occurs during the process of loading <u>file</u> or relocating its symbolic references.

###Errors

No errors are defined.

###Implementation tasks

* Implement the `dlfcn.h` file defining at least the following constants: `RTLD_LAZY`, `RTLD_NOW`, `RTLD_GLOBAL`, `RTLD_LOCAL`.
* Implement the `dlopen()` function.