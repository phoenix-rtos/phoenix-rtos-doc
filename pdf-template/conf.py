# TemplateConfiguration file for the Sphinx documentation builder.

import sys

project = ""
copyright = "2025, Phoenix Systems"
author = "Phoenix Systems"

# language of the generated document, "en" or "pl"
# it can be also overridden per build: make latexpdf O="-D language=pl"
language = "en"

extensions = ["myst_parser", "sphinx_copybutton", "phoenixsystems.docsresources"]

exclude_patterns = ["README", "_build", "Thumbs.db", ".DS_Store", "_venv"]

latexpdf_title = "Your Title"
latexpdf_author = "Your Name"
latexpdf_version = "Ver. X.X"
latexpdf_filename = "your_filename"
# latexpdf_date = "01-01-2026"  # defaults to the build date

# The line below the title holds either the author, prefixed with a label
# translated to the language of the document, or a subtitle typeset as it is
# given. Setting both is an error, leaving both empty omits that line.
# latexpdf_subtitle = "Prepared for ..."

if " " in latexpdf_filename:
    print(
        "\n" + "=" * 70 + "\n"
        "ERROR: PDF filename cannot contain spaces!\n"
        f"Current name: '{latexpdf_filename}'\n"
        "Use underscores '_' or hyphens '-' instead of spaces.\n"
        "Examples: 'my_documentation' or 'my-documentation'\n" + "=" * 70 + "\n",
        file=sys.stderr,
    )
    sys.exit(1)

latex_documents = [
    ("index", f"{latexpdf_filename}.tex", latexpdf_title, author, "howto", False),
]
