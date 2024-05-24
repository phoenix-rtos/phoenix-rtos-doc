# Common Gateway Interface library (libcgi)

The `libcgi` library provides a set of functionalities for handling Common Gateway Interface (CGI) operations in C.

## Contents

- [General information](#general-information)
- [Request Method](#request-method)
- [Authentication Modes](#authentication-modes)
- [libcgi interface](#libcgi-interface)
  - [Data Structures](#data-structures)
  - [Parameters Management](#parameters-management)
- [Using libcgi](#using-libcgi)

## General information

The `libcgi` library is a helper library designed to facilitate CGI. It provides functions for retrieving request
methods, query strings, printing headers, managing URL and multipart parameters, and handling authentication.

## Request Method

The library defines an enumeration for various HTTP request methods:

- `LIBCGI_METHOD_POST`: Indicates a POST request method.
- `LIBCGI_METHOD_POST_MULTIPART`: Indicates a POST request with multipart data.
- `LIBCGI_METHOD_GET`: Indicates a GET request method.
- `LIBCGI_METHOD_DELETE`: Indicates a DELETE request method.
- `LIBCGI_METHOD_ERROR`: Used to indicate an error in determining the request method.

## Authentication Modes

The library also defines an enumeration for authentication modes, currently including:

- `LIBCGI_AUTH_COOKIE_FILE`: Indicates authentication via a cookie file.

## libcgi interface

- `libcgi_getRequestMethod` - Returns the request method used for the current CGI call.

```c
int libcgi_getRequestMethod(void)
```

- `libcgi_getQueryString` - Returns the query string from the current CGI call.

```c
char *libcgi_getQueryString(void)
```

- `libcgi_printCode` - Prints the HTTP status code and status message as part of the
response header.

```c
void libcgi_printCode(unsigned code, char *status)
```

- `libcgi_printHeaders` - Prints the HTTP response headers including content type, content disposition,
and any additional raw headers.

```c
void libcgi_printHeaders(char *content_type, char *content_disposition, char *filename, char *raw_headers)
```

- `libcgi_isLogged` - A customizable function to determine if a user is logged in.
It can take multiple arguments for validation.

```c
int libcgi_isLogged(int argc, ...)
```

### Data Structures

- `libcgi_param_t` - Represents a parameter, which could be a part of the URL query string or a part of multipart
form data.

```C
typedef struct _libcgi_param {
	struct _libcgi_param *next; //  Pointer to the next parameter in the list
	enum { LIBCGI_PARAM_DEFAULT, LIBCGI_PARAM_FILE } type; // The type of the parameter
	union { // Key of the parameter or filename if the parameter is a file.
		char *key;
		char *filename;
	};
	union { // Value of the parameter or file stream if the parameter is a file.
		char *value;
		FILE *stream;
	};
} libcgi_param_t;
```

### Parameters Management

- `libcgi_getUrlParams` - Retrieves a linked list of URL parameters.

```c
libcgi_param_t *libcgi_getUrlParams(void)
```

- `libcgi_freeUrlParams` - Frees the memory allocated for URL parameters.

```c
void libcgi_freeUrlParams(libcgi_param_t *params_head)
```

- `libcgi_getMultipartParams` - Retrieves a linked list of parameters from a multipart/form-data request.
The store_path parameter specifies where to store uploaded files

```c
libcgi_param_t *libcgi_getMultipartParams(char *store_path)
```

- `libcgi_freeMultipartParams` - Frees the memory allocated for multipart parameters.

```c
void libcgi_freeMultipartParams(libcgi_param_t *params_head)
```

## Using libcgi

To use functions provided by `libcgi` please add the library to the `LIBS` variable in `Makefile` and include the
required header file.

## See also

1. [Phoenix-RTOS core libraries](index.md)
2. [Phoenix-RTOS Graphics Library](libgraph.md)
3. [Table of Contents](../index.md)
