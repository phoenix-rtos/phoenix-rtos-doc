# Utilities — Design Observations

## Modular Applet System

Each PSH command lives in its own directory with a standard build convention. This enables per-target applet selection via the `PSH_COMMANDS` make variable.

## Auto-Registration Pattern

Constructor attributes register applets at load time:
```c
void __attribute__((constructor)) <cmd>_registerapp(void) {
    static psh_appentry_t app = { .name = "<cmd>", ... };
    psh_registerapp(&app);
}
```

No hardcoded command table — commands self-register.

## Unified Binary with Symlink Dispatch

Single `psh` binary contains all selected applets. When invoked via a symlink named after a command (e.g., `ls` → `psh`), it dispatches to the corresponding applet based on `argv[0]`.

## Convention: Applet Function Signatures

```c
void psh_<cmd>info(void);           // Brief description for help
int psh_<cmd>(int argc, char **argv); // Main entry point
void <cmd>_registerapp(void);        // Auto-registration (constructor)
```

## Resource Optimization

- Stack size: 4096 bytes (minimal for embedded)
- History buffer: 512 entries (fixed)
- No shell expansion (intentional for constrained systems)

## Build-Time Applet Selection

```makefile
PSH_COMMANDS = bind cat cd chmod cp ...  # Selected applets
PSH_PROJECT_DEPS = ...                    # Project-specific additions
```

Allows resource-constrained targets to include only needed commands.

## Five+ Undocumented Standalone Utilities

Beyond PSH, there are 6 undocumented utilities in `phoenix-rtos-utils/`: `benchmarks`, `gsm`, `spitool`, `metacheck`, `meterfs-migrate`, `nandpart`. Plus `cm4-tool` and `nandtool` are listed in docs but lack proper documentation pages. These serve specialized hardware management needs.
