# Filesystems Documentation — Outdated Points

## 1. Documentation Is Essentially Empty

**Documentation (`filesystems/index.md`):** Contains only 3 sentences — filesystem servers implement protocols, register ports, and refers users to the source repository.

**Current code:** 7 disk-based filesystems at `phoenix-rtos-filesystems/`: dummyfs, ext2, fat, jffs2, littlefs, meterfs, rofs. Each with full implementations, distinct feature sets, and different use cases.

**Recommendation:** The entire filesystems chapter needs to be written from scratch. At minimum, it should list all filesystems, their use cases, and their feature sets.

---

## 2. FAT Filesystem Is Read-Only

**Code evidence:** `phoenix-rtos-filesystems/fat/libfat.c` lines 95–115: `libfat_write()` returns `-EROFS` for all write operations (write, truncate, link, unlink).

**Recommendation:** When documenting FAT, this limitation must be prominently stated.

---

## 3. EXT2 Feature Flags Misleading

**Current code:** `phoenix-rtos-filesystems/ext2/sb.h` defines fields for:
- Journal: lines 103–104, 214–220 (journal UUID, inode, device, backup)
- Compression: line 130 (`INCOMPAT_COMPRESSION = 0x0001`)
- Encryption: line 262 (`encryptAlgos[4]`)

None of these features are implemented — only the header fields are defined for format compatibility.

**Recommendation:** When documenting ext2, clearly state which features are supported vs. which are defined but unimplemented.

---

## 4. JFFS2 Incomplete Features

**Code's own TODO file (`phoenix-rtos-filesystems/jffs2/TODO`) lists:**
- Asynchronous operations not fully implemented
- Compression tuning incomplete (`disable compression in commit_write()?`, `fine-tune the allocation / GC thresholds`)
- Checkpointing not done (`do we need this? scan is quite fast`)
- Per-inode compression tuning via `chattr` not implemented
- NAND bad block check incomplete

**Recommendation:** Document known limitations alongside the JFFS2 feature description.
