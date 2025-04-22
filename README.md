# phoenix-rtos-doc

The full documentation can be found on <https://docs.phoenix-rtos.com/>.

This repository contains all the necessary files needed to build
Phoenix-RTOS Documentation using [sphinx](https://github.com/sphinx-doc/sphinx).

It can be done using the following command:

```console
make clean html
```

The artifacts will be available in `_build` directory.

## Generate Documents Using the Phoenix-RTOS Template

Download the required requirements and the dependencies listed below:

```bash
latexmk texlive-full texlive-latex-extra
```

Example usage of the script:

```
python build_pdf.py [input_dirs/files]
```

Full help:
```bash
usage: build_pdf.py [-h] [-i INDEX] [-o OUTPUT] [-v] [-a AUTHORS] input_dirs [input_dirs ...]

Build Phoenix-RTOS PDF from Markdown sources.

positional arguments:
  input_dirs            Folders containing .md files

options:
  -h, --help            show this help message and exit
  -i INDEX, --index INDEX
                        Path to custom index.md (with toctree)
  -o OUTPUT, --output OUTPUT
                        Output PDF file name
  -v, --verbose         Show LaTeX output
  -a AUTHORS, --authors AUTHORS
                        Author(s) to appear on the title page
  -t TITLE, --title TITLE
                        Custom title to appear on the title page
```
