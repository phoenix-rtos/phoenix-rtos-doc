# Configuration file for the Sphinx documentation builder.

from version_management import get_version_context
from datetime import datetime
from phoenixsystems.docsresources import latex_default

project = ""
copyright = f"2024-{datetime.today().strftime('%Y')}, Phoenix Systems"
author = "Phoenix Systems"

extensions = ["myst_parser", "sphinx_copybutton"]

myst_enable_extensions = ["deflist", "fieldlist"]

templates_path = ["_templates"]
exclude_patterns = ["README", "_build", "Thumbs.db", ".DS_Store", "_venv", "docsresources", "pdf-template"]
exclude_patterns += ["utils", "kernel", "libc"]
myst_heading_anchors = 3
pygments_dark_style = "tango"

latexpdf_title = "Phoenix-RTOS Documentation"
latexpdf_author = ""
latexpdf_date = datetime.today().strftime('%d-%m-%Y')
latexpdf_version = "latest"
latexpdf_filename = "phoenix-rtos-documentation"

html_theme = "sphinx_book_theme"
html_title = "Phoenix-RTOS Documentation"
html_favicon = "_static/images/favicon.png"
html_static_path = ["_static"]
html_css_files = ["css/custom.css"]
html_baseurl = "https://docs.phoenix-rtos.com/latest/"
html_context = {"versions": get_version_context(), "current_version": "latest"}

html_sidebars = {"**": ["navbar-logo.html", "icon-links.html", "versions.html", "search-button-field.html", "sbt-sidebar-nav.html" ]}

# TODO: add sphinx-togglebutton?
# https://sphinx-book-theme.readthedocs.io/en/latest/reference/extensions.html

html_theme_options = {
    "path_to_docs": ".",
    "logo": {
        "image_light": "_static/images/phoenix-light.svg",
        "image_dark": "_static/images/phoenix-dark.svg",
    },
}

latex_documents = [
    ("index", f"{latexpdf_filename}.tex", latexpdf_title, author, "howto", False),
]

latex_engine = latex_default["engine"]
latex_table_style = latex_default["table_style"]

latex_additional_files = latex_default["additional_files"]

# overwrite the maketitle element to use the variables from the current file
modified_elements = latex_default["elements"].copy()
modified_elements["maketitle"] = fr'''
        \newcommand{{\doctitle}}{{{latexpdf_title}}}
        \newcommand{{\docauthor}}{{{latexpdf_author}}}
        \newcommand{{\docversion}}{{{latexpdf_version}}}
        \newcommand{{\docdate}}{{{latexpdf_date}}}
    ''' + modified_elements["maketitle"]

latex_elements = modified_elements
