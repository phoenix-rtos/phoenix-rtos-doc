#
# Phoenix-RTOS
#
# Documentation resources
#
# LaTeX settings of the PDF documents
#
# Copyright 2025-2026 Phoenix Systems
# Author: Damian Loewnau
#
# SPDX-License-Identifier: BSD-3-Clause
#

from datetime import datetime
from pathlib import Path

RESOURCES_DIR = Path(__file__).parent

IMAGES = (
    "company_logo.png",
    "lastpage_image.png",
    "page_header.png",
    "titlepage_image.png",
)

DATE_FORMAT = "%d-%m-%Y"


def _read(filename):
    return (RESOURCES_DIR / filename).read_text(encoding="utf-8")


def _definitions(macros):
    r"""Render a {name: value} mapping as LaTeX \newcommand definitions."""
    return "".join(f"\\newcommand{{\\{name}}}{{{value}}}\n" for name, value in macros.items())


def latex_config(*, title="", author="", version="", date="", signatures="", history="", preamble=""):
    """Return the Sphinx LaTeX settings of the document.

    The `signatures` and the `history` are LaTeX of a page each, put after the
    title page, and the `preamble` is LaTeX added to the one of the package.
    """
    document_macros = {
        "doctitle": title,
        "docversion": version,
        "docdate": date or datetime.today().strftime(DATE_FORMAT),
    }
    # keep \docauthor undefined when unset - the templates then skip the author line
    if author:
        document_macros["docauthor"] = author

    # the same goes for the pages that follow the title one
    if signatures:
        document_macros["docsignatures"] = signatures
    if history:
        document_macros["dochistory"] = history

    return {
        "engine": "xelatex",
        "table_style": ["colorrows"],
        "additional_files": [str(RESOURCES_DIR / image) for image in IMAGES],
        "elements": {
            "sphinxsetup": r"pre_padding-right=6pt, pre_padding-left=0pt",
            "makeindex": r"",
            "papersize": r"a4paper",
            "tableofcontents": r"""
        \makeatletter
        \begingroup
        \pagestyle{normal}
        \section*{Table of Contents}
        \@starttoc{toc}
        \clearpage
        \endgroup
        \makeatother
    """,
            "fontpkg": r"""
        \setmainfont{Liberation Sans}
        \setsansfont{Liberation Sans}
        \setmonofont{DejaVu Sans Mono}
    """,
            "extrapackages": r"""
        \usepackage{tocloft}
        \usepackage{graphicx}
        \usepackage{xcolor}
        \usepackage{etoolbox}
        \usepackage{lastpage}
        \usepackage{fontspec}
    """,
            "preamble": _read("preamble.tex")
            + preamble,
            "atendofbody": _read("atendofbody.tex"),
            "maketitle": _definitions(document_macros) + _read("maketitle.tex"),
        },
    }
