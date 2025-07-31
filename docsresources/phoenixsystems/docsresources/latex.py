from pathlib import Path

RESOURCES_DIR = Path(__file__).parent

latex_default = {
    "engine": "xelatex",
    "table_style": ["colorrows"],
    "additional_files": [
        str(RESOURCES_DIR / "company_logo.png"),
        str(RESOURCES_DIR / "lastpage_image.png"),
        str(RESOURCES_DIR / "page_header.png"),
        str(RESOURCES_DIR / "titlepage_image.png"),
    ],
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
        "preamble": (RESOURCES_DIR / "preamble.tex").read_text(),
        "atendofbody": (RESOURCES_DIR / "atendofbody.tex").read_text(),
        "maketitle": (RESOURCES_DIR / "maketitle.tex").read_text(),
    },
}
