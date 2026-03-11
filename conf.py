# Configuration file for the Sphinx documentation builder.

from datetime import datetime
from phoenixsystems.docsresources import latex_default
from doc_utilities import get_git_rev, get_version_context

# should be either "lastest" or release branch tag (e.g. "v3.3.2")
doc_title = "Phoenix-RTOS Documentation"
doc_version = "latest"
doc_today = datetime.today()

project = ""
copyright = f"2024-{doc_today.year}, Phoenix Systems"
author = "Phoenix Systems"

html_last_updated_fmt = ""

extensions = ["myst_parser", "sphinx_copybutton"]

myst_enable_extensions = ["deflist", "fieldlist"]

templates_path = ["_templates"]
exclude_patterns = ["README", "_build", "Thumbs.db", ".DS_Store", "_venv", "docsresources", "pdf-template"]
exclude_patterns += ["libc"]
myst_heading_anchors = 3
pygments_dark_style = "tango"

latexpdf_title = doc_title
latexpdf_author = author
latexpdf_date = doc_today.strftime('%d-%m-%Y')
latexpdf_version = doc_version
latexpdf_filename = "phoenix-rtos-documentation"

html_theme = "sphinx_book_theme"
html_title = doc_title
html_favicon = "_static/images/favicon.png"
html_static_path = ["_static"]
html_css_files = ["css/custom.css"]
html_baseurl = "https://docs.phoenix-rtos.com/latest/"
html_context = {"versions": get_version_context(), "current_version": doc_version}

html_sidebars = {"**": ["navbar-logo.html", "icon-links.html", "versions.html", "search-button-field.html", "sbt-sidebar-nav.html" ]}

# TODO: add sphinx-togglebutton?
# https://sphinx-book-theme.readthedocs.io/en/latest/reference/extensions.html

repo_url = "https://github.com/phoenix-rtos/phoenix-rtos-doc"

git_rev, git_hash = get_git_rev()
repo_rev_url = f"{repo_url}/commit/{git_hash}"

html_theme_options = {
    "repository_url": "https://github.com/phoenix-rtos/phoenix-rtos-doc",
    "repository_branch": "master" if doc_version == "latest" else doc_version,
    "use_edit_page_button": True,
    "use_source_button": True,
    "use_issues_button": True,
    "path_to_docs": ".",
    "logo": {
        "image_light": "_static/images/phoenix-light.svg",
        "image_dark": "_static/images/phoenix-dark.svg",
    },
    "extra_footer": f"<div>Revision: <a href=\"{repo_rev_url}\">{git_rev}</a></div>",
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
