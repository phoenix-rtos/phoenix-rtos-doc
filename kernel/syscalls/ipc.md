# Inter-process communication

## `syscalls_portCreate`

````C
GETFROMSTACK(ustack, u32 *, port, 0);
````

Creates new communication queue and returns its identifier in `port` variable.

## `syscalls_portDestroy`

````C
GETFROMSTACK(ustack, u32, port, 0);
````

Destroys communication queue identified by `port` variable.

## `syscalls_portRegister`

````C
GETFROMSTACK(ustack, unsigned int, port, 0);
GETFROMSTACK(ustack, char *, name, 1);
GETFROMSTACK(ustack, oid_t *, oid, 2);
````

Registers `port` in the namespace at `name` and returns object identifier `oid` identifying this association.

## `syscalls_msgSend`

````C
GETFROMSTACK(ustack, u32, port, 0);
GETFROMSTACK(ustack, msg_t *, msg, 1);
````

Sends message `msg` to queue identified by `port`. Execution of calling thread is suspended until receiving thread
responds to this message.

## `syscalls_msgRecv`

````C
GETFROMSTACK(ustack, u32, port, 0);
GETFROMSTACK(ustack, msg_t *, msg, 1);
GETFROMSTACK(ustack, msg_rid_t *, rid, 2);
````

Receives message `msg` from queue identified by `port`. The reception context is stored in variable `rid`.

## `syscalls_msgRespond`

````C
GETFROMSTACK(ustack, u32, port, 0);
GETFROMSTACK(ustack, msg_t *, msg, 1);
GETFROMSTACK(ustack, msg_rid_t, rid, 2);
````

Responds to message `msg` using reception context `rid`.

## `syscalls_lookup`

````C
GETFROMSTACK(ustack, char *, name, 0);
GETFROMSTACK(ustack, oid_t *, file, 1);
GETFROMSTACK(ustack, oid_t *, dev, 2);
````

Lookups for object identifier (`port` and resource `id`) associated with `name`. Object identifier representing file is
returned in `file` variable. If file is associated with other object the other object ID is returned in `dev`.

## `syscalls_signalHandle`

## `syscalls_signalPost`

## `syscalls_signalMask`

## `syscalls_signalSuspend`
