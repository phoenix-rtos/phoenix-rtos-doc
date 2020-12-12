###Synopsis

`#include <fnmatch.h>`

`int fnmatch(const char *pattern, const char *string, int flags);`

###Description

The `fnmatch` function  checks the string specified by the <u>string</u> argument to see if it matches the pattern specified by the <u>pattern</u> argument..

Arguments:

<u>pattern</u> - the pattern to be matched.
<u>string</u> - the string to check.
<u>flags</u> - the way to check compatibility of <u>string</u> and <u>pattern</u>.

The <u>flags</u> argument modifes the interpretation of <u>pattern</u> and <u>string</u>. It is the bitwise-inclusive `OR` of zero or more of the flags defined in <`fnmatch.h`>. These are:
 
 * `FNM_NOMATCH` the <u>string</u> does not match the <u>pattern</u>.
 
 * `FNM_PATHNAME` the interpretation of the <slash> character ( '/' ) in <u>string</u>. If it is set then it should be explicitly matched by a <slash> in <u>pattern</u>; it is not matched by either the <asterisk> or <question-mark> special characters, nor by a bracket expression. If the `FNM_PATHNAME` flag is not set, the <slash> character is treated as an ordinary character.

 * `FNM_NOESCAPE` if it is not set in <u>flags</u>, a <backslash> character in <u>pattern</u> followed by any other character matches that second character in <u>string</u>. In particular, "\\" matches a <backslash> in <u>string</u>. If <u>pattern</u> ends with an unescaped <backslash>, `fnmatch()` returns a non-zero value (indicating either no match or an error). If `FNM_NOESCAPE` is set, a <backslash> character is treated as an ordinary character.

 * `FNM_PERIOD` if it is <b>set</b> in <u>flags</u>, then a leading <period> ( '.' ) in <u>string</u> matches a <period> in <u>pattern</u>; by the value of `FNM_PATHNAME`:

     - If `FNM_PATHNAME` is set, a <period> is "leading" if it is the first character in <u>string</u> or if it immediately follows a <slash>.

     - If `FNM_PATHNAME` is not set, a <period> is "leading" only if it is the first character of <u>string</u>.

    If `FNM_PERIOD` is <b>not set</b>, then no special restrictions are placed on matching a period.

###Return value

 * `0` if string matches the pattern specified by <u>pattern</u>.

 * `FNM_NOMATCH` if there is no match. 

 * `-1` if an error occurs.
    
###Errors

No errors are defined.

###Implementation tasks

 * Implement `fnmatch.h` file containing constants mentioned above.
 * Implement the `fnmatch()` function.
 