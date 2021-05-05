###Synopsis

`#include <dlfcn.h>`

`void *dlsym(void *restrict handle, const char *restrict name);`

###Description

The `dlopen()` function gets the address of a symbol from a symbol table handle.

Arguments:
<u>handle</u> - the pointer to the symbol table,
<u>name</u> - the symbol's name.

The `dlsym()` function returns the address of a symbol (a function identifier or a data object identifier) defined in the symbol table identified by the <u>handle</u> argument. The <u>handle</u> argument is a symbol table handle returned from a call to `dlopen()` (and which has not yet been released by a call to `dlclose()`), and <u>name</u> is the symbol's name as a character string. The return value from `dlsym()`, cast to a pointer to the type of the named symbol, can be used to call (in the case of a function) or access the contents of (in the case of a data object) the named symbol.
The `dlsym()` function searches for the named symbol in the symbol table referenced by <u>handle</u>. If the symbol table was created with lazy loading (see `RTLD_LAZY` in `dlopen()`), load ordering is used in `dlsym()` operations to relocate executable object files needed to resolve the symbol. The symbol resolution algorithm used is dependency order as described in `dlopen()`.

###Return value

On success, `dlsym()` returns:
    
 * if <u>name</u> names a function identifier - the address of the function converted from type pointer to function to type pointer to `void`;    a symbol table handle, otherwise it returns a null pointer.

 * if <u>name</u> names another symbol -  the address of the data object associated with the data object identifier named by <u>name</u> converted from a pointer to the type of the data object to a pointer to `void`.

Otherwise if <u>handle</u> does not refer to a valid symbol table handle or if the symbol named by <u>name</u> cannot be found in the symbol table associated with handle, `dlsym()` returns a null pointer.

###Errors

No errors are defined.

###Examples

The following example shows how `dlopen()` and `dlsym()` can be used to access either a function or a data object. For simplicity, error checking has been omitted.

    void *handle;
    int (*fptr)(int), *iptr, result;
    
    /* open the needed symbol table */
    handle = dlopen("/usr/`home/me/libfoo.so", RTLD_LOCAL | RTLD_LAZY);
    /* find the address of the function my_function */
    fptr = (int (*)(int))dlsym(handle, "my_function");
    /* find the address of the data object my_object */
    iptr = (int *)dlsym(handle, "my_OBJ");
    /* invoke my_function, passing the value of my_OBJ as the parameter */
    result = (*fptr)(*iptr);

###Implementation tasks

* Implement the `dlsym()` function.
