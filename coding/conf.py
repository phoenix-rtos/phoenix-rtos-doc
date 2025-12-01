# TemplateConfiguration file for the Sphinx documentation builder.

from datetime import datetime
from phoenixsystems.docsresources import latex_default

project = "Phoenix RTOS DO-178C"
copyright = "2025, Phoenix Systems"
author = "Phoenix Systems"

extensions = ["myst_parser", "sphinx_copybutton"]
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

exclude_patterns = ["README", "_build", "Thumbs.db", ".DS_Store", "_venv"]

latexpdf_title = "Software Code Standards"
latexpdf_author = "Bartłomiej Paczek"
latexpdf_reviewer = 'Kamil Ber'
latexpdf_date = datetime.today().strftime('%d-%m-%Y')
latexpdf_version = "Rev. 1.0"
latexpdf_filename = "PHOENIX-RTOS-DO178-STD-0003-Software_Code_Standards"
latexpdf_dochistory = r'''
        \begin{table}[h!]
        \centering
        \color{ps-darkblue}
        \begin{tabular}{p{1cm}|p{8cm}|p{3cm}|p{2cm}}
        \hline
        \textbf{Rev.} & \textbf{Description} & \textbf{Elaborated by} & \textbf{Date} \\
        \hline
        0.1 & Initial draft & B. Paczek & 2025-12-01 \\
        \hline
        \end{tabular}
        \end{table}
        '''

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
        \newcommand{{\docreviewer}}{{{latexpdf_reviewer}}}
        \newcommand{{\docversion}}{{{latexpdf_version}}}
        \newcommand{{\docdate}}{{{latexpdf_date}}}
        \newcommand{{\dochistory}}{{{latexpdf_dochistory}}}

    ''' + modified_elements["maketitle"]

modified_elements["preamble"] = modified_elements["preamble"] + r'''\setcounter{secnumdepth}{1}'''
latex_elements = modified_elements
