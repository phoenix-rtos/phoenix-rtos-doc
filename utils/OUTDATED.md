# Utilities Documentation — Outdated Points

## 1. nandtool — Mentioned But Not Documented

**Documentation:** Listed in `index.md` with a brief sentence. No dedicated documentation page exists.

**Current code:** Full implementation in `phoenix-rtos-utils/nandtool/`.

**Recommendation:** Create a documentation page for nandtool with usage, options, and examples.

---

## 2. cm4-tool — Mentioned But Not Documented

**Documentation:** Listed in `index.md` with a brief sentence. No dedicated documentation page.

**Current code:** Full implementation for imxrt117x-cm4 communication.

**Recommendation:** Create a documentation page for cm4-tool.

---

## 3. psd.md Is a Stub

**Documentation:** Contains only a placeholder `<!-- #TODO: add more information -->`.

**Current code:** Full Phoenix Serial Downloader implementation.

**Recommendation:** Expand psd.md with protocol description, usage guide, and supported platforms.

---

## 4. Missing PSH Applets from Documentation

**Documentation lists:** 48 applets.

**Current code (`psh/Makefile` `PSH_ALLCOMMANDS`):**
```makefile
PSH_ALLCOMMANDS := bind cat cd chmod cp date dd df dmesg echo edit exec hm hd \
  ifconfig kill ln ls mem mkdir mount nc nslookup ntpclient perf ping pm printenv \
  ps pwd reboot rm rmdir runfile route sync sysexec top touch tty umount uptime wget
```
Missing from docs: `chmod`, `hd`, `route`.

**Recommendation:** Add documentation pages for chmod, hd, and route applets.

---

## 5. PSH Applet List Inconsistency

**Documentation (`psh/index.md`):** Lists `clear`, `exit`, `reset`, `history`, `export`, `unset`, `pshlogin` as applets.

**Current code:** `clear`, `exit`, `reset`, `history` are internal shell commands in `pshapp/`, not separate applet directories and not in `PSH_ALLCOMMANDS`. `export` and `unset` are in `pshapp/env.c`. `pshlogin` is in `PSH_LINK_APPLETS` but not `PSH_ALLCOMMANDS`. These are built-in functions, not standalone applets.

**Recommendation:** Clarify which are standalone applets and which are built-in shell commands.
