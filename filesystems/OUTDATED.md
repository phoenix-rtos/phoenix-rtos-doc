# Filesystems Documentation — Outdated Points

## 1. Documentation Is Essentially Empty

**Documentation (`index.md`):** Contains only 3 sentences — filesystem servers implement protocols, register ports, and refers users to the source repository.

**Current code:** 7 disk-based filesystems + 6 pseudo-filesystems with full implementations, distinct feature sets, and different use cases.

**Recommendation:** The entire filesystems chapter needs to be written from scratch. At minimum, it should list all filesystems, their use cases, and their feature sets.

---

## 2. FAT Filesystem Is Read-Only

**Documentation:** Not mentioned (because filesystems aren't documented at all).

**Code reality:** `libfat_write()` always returns `-EROFS`. FAT support is read-only.

**Recommendation:** When documenting FAT, this limitation must be prominently stated.

---

## 3. EXT2 Feature Flags Misleading

**Current code:** Defines compression, encryption, and journal fields in superblock headers, but none are implemented.

**Recommendation:** When documenting ext2, clearly state which features are supported vs. which are defined but unimplemented.

---

## 4. JFFS2 Incomplete Features

**Code's own TODO file lists:**
- Asynchronous operations not fully implemented
- Compression tuning incomplete
- Checkpointing not done

**Recommendation:** Document known limitations alongside the JFFS2 feature description.
