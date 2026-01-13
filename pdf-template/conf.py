# TemplateConfiguration file for the Sphinx documentation builder.

import sys
from datetime import datetime
from phoenixsystems.docsresources import latex_default

project = ""
copyright = "2025, Phoenix Systems"
author = "Phoenix Systems"

extensions = ["myst_parser", "sphinx_copybutton"]

exclude_patterns = ["README", "_build", "Thumbs.db", ".DS_Store", "_venv"]

latexpdf_title = "Your Title"
latexpdf_author = "Your Name"
latexpdf_date = datetime.today().strftime('%d-%m-%Y')
latexpdf_version = "Ver. X.X"
latexpdf_filename = "your_filename"

if ' ' in latexpdf_filename:
    print(
        "\n" + "=" * 70 + "\n"
        "ERROR: PDF filename cannot contain spaces!\n"
        f"Current name: '{latexpdf_filename}'\n"
        "Use underscores '_' or hyphens '-' instead of spaces.\n"
        "Examples: 'my_documentation' or 'my-documentation'\n"
        + "=" * 70 + "\n",
        file=sys.stderr
    )
    sys.exit(1)

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
