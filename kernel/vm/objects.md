# Memory objects

Memory objects back mapped data. They let multiple maps refer to the same loaded content and let private writable
mappings receive separate anonymous pages on write.

Phoenix-RTOS does not keep filesystem objects in the kernel. A mapped object is identified by `oid_t`, which names a
server port and server-local object identifier. The VM object layer asks that server for object data when a page is
needed.

## `vm_object_t`

`vm_object_t` is declared in `vm/object.h` and contains:

| Field | Meaning |
| --- | --- |
| `linkage` | Red-black tree node used by the object registry. |
| `oid` | Server-owned object identifier. |
| `refs` | Reference count. |
| `size` | Object size. |
| `pages` | Array of object page descriptors. |

`VM_OBJ_PHYSMEM` is a special object pointer used for physical-memory mappings.

## Object API

```{function} vm_object_t *vm_objectRef(vm_object_t *o)

Increments an object reference count.

:param o: Object to reference.
:returns: The same object pointer.
```

```{function} int vm_objectGet(vm_object_t **o, oid_t oid)

Finds or creates a VM object for `oid`.

:param o: Output object pointer.
:param oid: Server object identifier.
:returns: `EOK` on success or a negative error code.
```

```{function} int vm_objectPut(vm_object_t *o)

Drops an object reference and releases the object when the last reference is gone.

:param o: Object to release.
:returns: `EOK` on success or a negative error code.
```

```{function} page_t *vm_objectPage(vm_map_t *map, amap_t **amap, vm_object_t *o, void *vaddr, u64 offs)

Returns the page backing a mapping at the given object offset. The function also handles anonymous copy-on-write pages
for private writable mappings.

:param map: Map containing the faulting or requested address.
:param amap: Anonymous map associated with the map entry.
:param o: Backing memory object.
:param vaddr: Virtual address in the mapping.
:param offs: Offset in the object.
:returns: Page descriptor, or `NULL` on failure.
```

```{function} vm_object_t *vm_objectContiguous(size_t size)

Creates an object backed by a physically contiguous page range.

:param size: Object size in bytes.
:returns: New object, or `NULL` when allocation fails.
```

## Anonymous pages and private mappings

Private writable mappings use `amap_t` and anonymous pages instead of long shadow-object chains. A map entry points to
an anonymous map. When a write requires a private copy, the VM allocates a `PAGE_OWNER_APP` page, copies data from the
original object page when needed, and records the new page in the anonymous map.

Shared read-only mappings can reuse the same object pages in multiple maps. Private mappings allocate only the pages
that are modified.

## Server-backed data

Object data is loaded through message passing to the server identified by `oid_t`. This keeps file and device policy in
user-space servers while the kernel manages page ownership, mapping metadata, and copy-on-write state.

NOMMU targets keep simplified object metadata, but use the same object identifiers so loader and server code can use a
common interface.
