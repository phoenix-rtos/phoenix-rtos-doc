# Configuration file for the Sphinx documentation builder.

from version_management import get_version_context
from pathlib import Path
from datetime import datetime

project = ""
copyright = "2024-2025, Phoenix Systems"
author = "Phoenix Systems"

extensions = ["myst_parser", "sphinx_copybutton"]

templates_path = ["_templates"]
exclude_patterns = ["README", "_build", "Thumbs.db", ".DS_Store", "venv", "docsresources"]
myst_heading_anchors = 3
pygments_dark_style = "tango"

latexpdf_title = "Phoenix-RTOS Documentation"
latexpdf_author = ""
latexpdf_date = datetime.today().strftime('%d-%m-%Y')
latexpdf_version = "Ver. latest"

html_theme = "furo"
html_title = "Phoenix-RTOS Documentation"
html_favicon = "_static/images/favicon.png"
html_js_files = ["js/versions.js"]
html_style = ["css/furo-phoenix.css", "css/furo-extensions-phoenix.css"]
html_static_path = ["_static", "_static/images/light_logo.png"]
html_baseurl = "https://docs.phoenix-rtos.com/latest/"
html_context = {"versions": get_version_context()}

# TODO: add dark mode support
html_theme_options = {
    "light_logo": "light_logo.png",
    "light_css_variables": {
        "sidebar-caption-font-size": "100%",
        "sidebar-item-font-size": "90%",
        "sidebar-item-spacing-vertical": "0.4rem",
        "sidebar-item-line-height": "1.1rem",
        "color-sidebar-search-icon": "#EA5B22",
        "sidebar-search-space-above": "0.1rem",
        "sidebar-caption-space-above": "0.1rem",
        "sidebar-tree-space-above": "0.5rem",
        "sidebar-search-input-font-size": "95%",
        "font-stack": "'Open Sans', sans-serif",
        "color-sidebar-background": "#0F1724",
        "color-sidebar-link-text--top-level": "#273149",
        "color-sidebar-item-background--current": "F1F3F3",
        "color-foreground-primary": "#273149",
        "color-brand-content": "#1890d7",
        "color-header-background": "#0F1724",
        "color-header-text": "white",
    },
    "dark_logo": "light_logo.png",
    "dark_css_variables": {
        "sidebar-caption-font-size": "100%",
        "sidebar-item-font-size": "90%",
        "sidebar-item-spacing-vertical": "0.4rem",
        "sidebar-item-line-height": "1.1rem",
        "color-sidebar-search-icon": "#EA5B22",
        "sidebar-search-space-above": "0.1rem",
        "sidebar-caption-space-above": "0.1rem",
        "sidebar-tree-space-above": "0.5rem",
        "sidebar-search-input-font-size": "95%",
        "font-stack": "'Open Sans', sans-serif",
        "color-sidebar-background": "#0F1724",
        "color-sidebar-link-text--top-level": "#273149",
        "color-sidebar-item-background--current": "#0F1F3F3",
        "color-foreground-primary": "#273149",
        "color-brand-content": "#1890d7",
        "color-header-background": "#0F1724",
        "color-header-text": "white",
    },
}

latex_engine = "xelatex"
latex_table_style = ["colorrows"]
latex_documents = [
    ("index", "phoenix-rtos.tex", "Phoenix-RTOS Documentation", author, "howto", False),
]

latex_additional_files = [
    "_static/images/pdf/companylogo.png",
    "_static/images/pdf/last-page-image.png",
    "_static/images/pdf/first-page-image1.png",
    "_static/images/pdf/first-page-image2.png"
]

latex_elements = {
    'sphinxsetup': r'pre_padding-right=6pt, pre_padding-left=0pt',
    'makeindex': r'',
    'papersize': r'a4paper',
    'tableofcontents': r'''
        \makeatletter
        \begingroup
        \pagestyle{normal}
        \section*{Table of Contents}
        \@starttoc{toc}
        \clearpage
        \endgroup
        \makeatother
    ''',
    'fontpkg': r'''
        \setmainfont{Liberation Sans}
        \setsansfont{Liberation Sans}
        \setmonofont{DejaVu Sans Mono}
    ''',
    'extrapackages': r'''
        \usepackage{tocloft}
        \usepackage{graphicx}
        \usepackage{xcolor}
        \usepackage{etoolbox}
        \usepackage{lastpage}
        \usepackage{fontspec}
    ''',
    'preamble': Path("_static/latex/preamble.tex").read_text(),
    'atendofbody': Path("_static/latex/atendofbody.tex").read_text(),
    'maketitle': fr'''
        \newcommand{{\doctitle}}{{{latexpdf_title}}}
        \newcommand{{\docauthor}}{{{latexpdf_author}}}
        \newcommand{{\docversion}}{{{latexpdf_version}}}
        \newcommand{{\docdate}}{{{latexpdf_date}}}
    ''' + Path("_static/latex/maketitle.tex").read_text()
}
