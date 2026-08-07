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

from .company import COMPANY, OFFICES
from .icons import ICONS
from .translations import translations

RESOURCES_DIR = Path(__file__).parent

IMAGES = (
    "company_logo.png",
    "lastpage_image.jpg",
    "page_header.png",
    "titlepage_image.jpg",
)

DATE_FORMAT = "%d-%m-%Y"
HQ_SUFFIX = " (HQ)"


def _read(filename):
    return (RESOURCES_DIR / filename).read_text(encoding="utf-8")


def _definitions(macros):
    r"""Render a {name: value} mapping as LaTeX \newcommand definitions."""
    return "".join(f"\\newcommand{{\\{name}}}{{{value}}}\n" for name, value in macros.items())


def _icon(char, icon):
    r"""Render an icon as a character of the font that has the glyph of it.

    The character is given by its code, as \newunicodechar has made the one of
    the icon active. Drawing a character, rather than a symbol of a font that
    knows no Unicode, is what keeps the icon selectable in the PDF and found by
    a search for it.
    """
    if icon is None:
        return ""

    glyph, font, color = icon
    drawn = rf'{{\{font}\symbol{{"{ord(glyph or char):04X}}}}}'
    return rf"\textcolor{{{color}}}{{{drawn}}}" if color else drawn


def _icon_definitions(icons):
    r"""Render a {character: icon} mapping as \newunicodechar definitions."""
    return "".join(
        f"\\newunicodechar{{{char}}}{{{_icon(char, icon)}}}\n" for char, icon in icons.items()
    )


def _company_macros(strings):
    """Build the macros used by the title page and the last page.

    The .tex templates hold the layout only - all the text they typeset is
    defined here, which keeps a single template for every language.
    """
    macros = {
        "psCompanyName": COMPANY["name"],
        "psRegistryInfo": "".join(f"{line.format(**COMPANY)}\\\\\n" for line in strings["registry_lines"]),
        "psContactLabel": strings["contact_label"],
        "psTocTitle": strings["toc_title"],
    }

    for office in OFFICES:
        country = strings["countries"][office["country"]] + (HQ_SUFFIX if office.get("hq") else "")
        lines = (rf"\textbf{{{country}}}", *(line.format(**strings["cities"]) for line in office["address"]))
        macros[f"psOffice{office['key'].capitalize()}"] = "\\\\\n".join(lines)

    return macros


def latex_config(
    language="en",
    *,
    title="",
    author="",
    subtitle="",
    version="",
    date="",
    signatures="",
    history="",
    preamble="",
    icons=None,
):
    """Return the Sphinx LaTeX settings for a document in the given language.

    The line below the title holds either the author, with a translated label,
    or a subtitle typeset as it is given. Only one of them can be used.

    The `signatures` and the `history` are LaTeX of a page each, put after the
    title page, and the `preamble` is LaTeX added to the one of the package.

    The `icons` mapping extends and overrides the icons supported by default.
    """
    if author and subtitle:
        raise ValueError("the author and the subtitle cannot share the line below the title")

    strings = translations(language)
    document_macros = {
        "doctitle": title,
        "docversion": version,
        "docdate": date or datetime.today().strftime(DATE_FORMAT),
    }
    # keep \docsubtitle undefined when unset - the templates then skip that line
    if subtitle:
        document_macros["docsubtitle"] = subtitle
    elif author:
        document_macros["docsubtitle"] = f"{strings['author_label']}: {author}"

    # the same goes for the pages that follow the title one
    if signatures:
        document_macros["docsignatures"] = signatures
    if history:
        document_macros["dochistory"] = history

    return {
        "engine": "xelatex",
        # the look of the tables comes from tables.tex, not from the sphinx styles
        "table_style": ["standard"],
        "additional_files": [str(RESOURCES_DIR / image) for image in IMAGES],
        "elements": {
            "sphinxsetup": r"pre_padding-right=6pt, pre_padding-left=0pt",
            "makeindex": r"",
            "papersize": r"a4paper",
            "tableofcontents": r"""
        \makeatletter
        \begingroup
        \pagestyle{normal}
        \section*{\psTocTitle}
        \@starttoc{toc}
        \clearpage
        \endgroup
        \makeatother
    """,
            "fontpkg": r"""
        \setmainfont{Liberation Sans}
        \setsansfont{Liberation Sans}
        \setmonofont{DejaVu Sans Mono}
        % the icons are drawn with the glyphs of these two, see icons.py
        \newfontfamily{\psSymbolFont}{Noto Sans Symbols2}
        \newfontfamily{\psFreeFont}{FreeSans}
    """,
            "extrapackages": r"""
        \usepackage{tocloft}
        \usepackage{graphicx}
        \usepackage{xcolor}
        \usepackage{etoolbox}
        \usepackage{lastpage}
        \usepackage{fontspec}
        \usepackage{newunicodechar}
    """,
            "preamble": _read("preamble.tex")
            + _read("tables.tex")
            + _definitions(_company_macros(strings))
            + _icon_definitions({**ICONS, **(icons or {})})
            + preamble,
            "atendofbody": _read("atendofbody.tex"),
            "maketitle": _definitions(document_macros) + _read("maketitle.tex"),
        },
    }
