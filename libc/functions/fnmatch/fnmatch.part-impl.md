# fnmatch

## Synopsis

`#include <fnmatch.h>`

`int fnmatch(const char *pattern, const char *string, int flags);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `fnmatch()` function shall match patterns as described below. It checks the string specified by the _string_
argument to see if it matches the pattern specified by the _pattern_ argument.

The following patterns matching a single character shall match a single character: ordinary characters, special pattern
characters, and pattern bracket expressions. The pattern bracket expression also shall match a single collating element.
A `\` character shall escape the following character. The escaping `\` shall be discarded. If a
pattern ends with an unescaped `\`, it is unspecified whether the pattern does not match anything or the
pattern is treated as invalid.

An ordinary character is a pattern that shall match itself. It can be any character in the supported character set
except for `NUL`, those special shell characters in Quoting that require quoting, and the following three special
pattern characters. Matching shall be based on the bit pattern used for encoding the character, not on the graphic
representation of the character. If any character (ordinary, shell special, or pattern special) is quoted, that pattern
shall match the character itself. The shell special characters always require quoting.

When unquoted and outside a bracket expression, the following three characters shall have special meaning in the
specification of patterns:

* `?` - A `?` is a pattern that shall match any character.
* `*` - An `*` is a pattern that shall match multiple characters, as described below.
* `[` - If an open bracket introduces a bracket expression, except that the `<exclamation-mark>` character `'!'`
 shall replace the `^` character `'^'` in its role in a non-matching list in the regular expression
 notation, it shall introduce a pattern bracket expression.

 A bracket expression starting with an unquoted `^` character produces unspecified results. Otherwise, `'['`
 shall match the character itself. When pattern matching is used where shell quote removal is not performed (such as in
 the argument to the find - name primary when find is being called using one of the exec functions, or in the pattern
 argument to the `fnmatch()` function), special characters can be escaped to remove their special meaning by preceding
 them with a `\` character. This escaping `\` is discarded. The sequence `"\\"` represents one literal `\`. All the
 requirements and effects of quoting on ordinary, shell special, and special pattern characters shall apply to escaping
 in this context.

The following rules are used to construct patterns matching multiple characters from patterns matching a single
character:

* The `*` is a pattern that shall match any string, including the null string.

* The concatenation of patterns matching a single character is a valid pattern that shall match the concatenation of the
single characters or collating elements matched by each of the concatenated patterns.

* The concatenation of one or more patterns matching a single character with one or more `*` characters is a valid
pattern. In such patterns, each `*` shall match a string of zero or more characters, matching the greatest possible
number of characters that still allows the remainder of the pattern to match the string.

The _flags_ argument shall modify the interpretation of _pattern_ and _string_. It is the bitwise-inclusive OR of zero
or more of the _flags_ defined in `<fnmatch.h>`. If the `FNM_PATHNAME` flag is set in _flags_, then a `/` character
`( '/' )` in _string_ shall be explicitly matched by a `/` in _pattern_; it shall not be matched by either the `*` or
`?` special characters, nor by a bracket expression. If the `FNM_PATHNAME` flag is not set, the `/` character shall be
treated as an ordinary character.

* If `FNM_NOESCAPE` is not set in _flags_, a `\` character in _pattern_ followed by any other character shall match that
second character in _string_. In particular, `"\\"` shall match a `\` in _string_.

* If _pattern_ ends with an unescaped `\`, `fnmatch()` shall return a non-zero value (indicating either no match or an
error). If `FNM_NOESCAPE` is set, a `\` character shall be treated as an ordinary character.

* If `FNM_PERIOD` is set in _flags_, then a leading `<period>` `'.'` in _string_ shall match a `<period>` in
_pattern_, where the location of `"leading"` is indicated by the value of `FNM_PATHNAME`:

* If `FNM_PATHNAME` is set, a `<period>` is `"leading"` if it is the first character in _string_ or if it immediately
follows a `/`.

* If `FNM_PATHNAME` is not set, a `<period>` is `"leading"` only if it is the first character of _string_.

* If `FNM_PERIOD` is not set, then no special restrictions are placed on matching a period.

## Return value

If _string_ matches the pattern specified by _pattern_, then `fnmatch()` shall return `0`. If there is no match,
`fnmatch()` shall return `FNM_NOMATCH`, which is defined in `<fnmatch.h>`. If an error occurs, `fnmatch()` shall
return another non-zero value.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../index.md)
2. [Table of Contents](../../../index.md)
