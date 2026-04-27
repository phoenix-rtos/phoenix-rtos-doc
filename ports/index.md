# Ports

## Synopsis

After reading this chapter, you will know:

- How third-party software is packaged as ports using `port.def.sh` definitions
- How to select ports for a target using `ports.yaml` configuration
- How port dependencies, conflicts, and version requirements work
- Which of the available ports are supported on your target

Phoenix-RTOS supports a collection of third-party open-source tools that
have been adapted (ported) to it.

The collection lies in the
[phoenix-rtos-ports](https://github.com/phoenix-rtos/phoenix-rtos-ports)
repository. For information on structure of `phoenix-rtos` repositories, see
[Project repository](../project/index.md) chapter.

For a list of ports available on Phoenix-RTOS, see {doc}`port_list`.

## Brief conceptual description

Ports are defined using a `port.def.sh` file and can be enabled on a
target using `ports.yaml` files defined per target/project.

For an in-depth port structure specification, see {doc}`port_def`.

For instructions on how to pick ports to install when building Phoenix-RTOS, see
{doc}`ports_yaml`.

## Table of contents

```{toctree}
:maxdepth: 1

port_def.md
ports_yaml.md
port_list.md
port_docs_index.md
```
