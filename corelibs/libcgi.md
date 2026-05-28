# Common Gateway Interface library (libcgi)

`libcgi` provides helpers for Common Gateway Interface (CGI) programs that read request metadata, parse request
parameters, print HTTP headers, and provide an overridable authentication hook.

The public interface is declared in `<cgi.h>`.

## Request and authentication constants

| Constant | Meaning |
| --- | --- |
| `LIBCGI_METHOD_POST` | `REQUEST_METHOD` is `POST`, and `CONTENT_TYPE` is not `multipart/form-data`. |
| `LIBCGI_METHOD_POST_MULTIPART` | `REQUEST_METHOD` is `POST`, and `CONTENT_TYPE` starts with `multipart/form-data`. |
| `LIBCGI_METHOD_GET` | `REQUEST_METHOD` is `GET`. |
| `LIBCGI_METHOD_DELETE` | `REQUEST_METHOD` is `DELETE`. |
| `LIBCGI_METHOD_ERROR` | Request method cannot be read or matched. |
| `LIBCGI_AUTH_COOKIE_FILE` | Cookie-file authentication mode identifier. |

## Parameter structure

`libcgi_param_t` describes one URL or multipart parameter.

```c
typedef struct _libcgi_param {
    struct _libcgi_param *next;
    enum { LIBCGI_PARAM_DEFAULT, LIBCGI_PARAM_FILE } type;
    union {
        char *key;
        char *filename;
    };
    union {
        char *value;
        FILE *stream;
    };
} libcgi_param_t;
```

For URL parameters, `key` and `value` point into one internal allocation owned by the list.
For multipart form fields, `key` names a regular field and `stream` contains the field data.
For multipart file fields, `filename` stores the submitted file name and `stream` points to a temporary or stored file.

## Request helpers

````{function} libcgi_getRequestMethod()
Reads the `REQUEST_METHOD` environment variable and returns the current CGI request method.

For `POST`, the function also checks whether `CONTENT_TYPE` begins with `multipart/form-data`.

:returns: One of the `LIBCGI_METHOD_*` constants.
````

````{function} libcgi_getQueryString()
Returns the raw query string from the `QUERY_STRING` environment variable.

:returns: The pointer returned by `getenv("QUERY_STRING")`, or `NULL` when the variable is not set. The caller does not
  own the returned storage.
````

## Header printing

````{function} libcgi_printCode(code, status)
Prints the HTTP status header line to standard output.

The current implementation prints only `Status: <code>` and does not use `status`.

:param code: HTTP status code.
:param status: Status text argument retained by the API but ignored by the implementation.
:returns: Nothing.
````

````{function} libcgi_printHeaders(content_type, content_disposition, filename, raw_headers)
Prints CGI response headers to standard output and terminates the header block with an empty line.

When both `content_disposition` and `filename` are non-`NULL`, the function prints a `Content-Disposition` header.
It always prints `Content-Type` and then prints `raw_headers` when that argument is non-`NULL`.

:param content_type: Value printed after `Content-Type:`. The function expects a non-`NULL` pointer.
:param content_disposition: Optional disposition value.
:param filename: Optional filename used with `content_disposition`.
:param raw_headers: Optional raw header text printed before the final empty line.
:returns: Nothing.
````

## Parameter parsing

````{function} libcgi_getUrlParams()
Parses the raw query string into a linked list of key/value parameters.

The parser treats both `&` and `=` as separators. It does not decode percent escapes or `+` characters.

:returns: Head of a `libcgi_param_t` list, or `NULL` when `QUERY_STRING` is not set.
````

````{function} libcgi_freeUrlParams(params_head)
Releases a URL parameter list returned by `libcgi_getUrlParams()`.

:param params_head: List head returned by `libcgi_getUrlParams()`, or `NULL`.
:returns: Nothing.
````

````{function} libcgi_getMultipartParams(store_path)
Parses a `multipart/form-data` request from standard input.

The boundary is read from `CONTENT_TYPE`. Regular fields are stored in temporary streams. File fields are stored in
temporary streams when `store_path == NULL`, or in files named `<store_path>/<filename>` otherwise.

:param store_path: Directory for uploaded files, or `NULL` to use temporary streams for all parts.
:returns: Head of a `libcgi_param_t` list, or `NULL` on parse, allocation, stream, or boundary errors.
````

````{function} libcgi_freeMultipartParams(params_head)
Closes streams and releases a multipart parameter list returned by `libcgi_getMultipartParams()`.

:param params_head: List head returned by `libcgi_getMultipartParams()`, or `NULL`.
:returns: Nothing.
````

## Authentication hook

````{function} libcgi_isLogged(argc, ...)
Checks whether the current CGI caller is authenticated.

`libcgi` provides this function as a weak symbol that returns `0`. An application can provide its own definition with
the same name to implement local authentication.

:param argc: Number of authentication arguments supplied by the caller.
:param ...: Application-specific authentication arguments.
:returns: `0` in the default implementation. Application overrides define their own return contract.
````

## Build use

Add `cgi` to the application `LIBS` variable and include `<cgi.h>` from C sources that call the library.