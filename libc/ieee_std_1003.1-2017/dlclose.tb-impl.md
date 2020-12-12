###Synopsis

`#include <dlfcn.h>`

`int dlclose(void *handle);`

###Description

The `dlclose()` function informs the system that the symbol table handle specified by <u>handle</u> is no longer needed by the application.

Arguments:
<u>handle</u> - the symbol table handle.
 
The `dlclose()` makes a statement of intent on the part of the process, it is not any requirement upon the implementation. 
Afterwords the executable object files that were loaded by `dlopen()` are unloaded. 

Once a symbol table handle has been closed, an application assumes that any symbols (function identifiers and data object identifiers) made visible using <u>handle</u>, are no longer available to the process.

Although a `dlclose()` operation is not required to remove any functions or data objects from the address space, neither is an implementation prohibited from doing so. The only restriction on such a removal is that no function nor data object is removed to which references have been relocated, until or unless all such references are removed. For instance, an executable object file that had been loaded with a `dlopen()` operation specifying the `RTLD_GLOBAL` flag might provide a target for dynamic relocations performed in the processing of other relocatable objects - in such environments, an application may assume that no relocation, once made, shall be undone or remade unless the executable object file containing the relocated object has itself been removed.
 
###Return value

`0` on success, `-1` if <u>handle</u> does not refer to an open symbol table handle or if the symbol table handle could not be closed.

###Errors

No errors are defined.

###Implementation tasks

* Implement the `dlclose()` function.