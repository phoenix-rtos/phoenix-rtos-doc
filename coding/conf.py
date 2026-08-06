# TemplateConfiguration file for the Sphinx documentation builder.

project = "Phoenix RTOS DO-178C"
copyright = "2025, Phoenix Systems"
author = "Phoenix Systems"

language = "en"

extensions = ["myst_parser", "sphinx_copybutton", "phoenixsystems.docsresources"]
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

exclude_patterns = ["README", "_build", "Thumbs.db", ".DS_Store", "_venv"]

latexpdf_title = "Software Code Standards"
latexpdf_version = "Rev. 1.0"
latexpdf_filename = "PHOENIX-RTOS-DO178-STD-0003-Software_Code_Standards"
latexpdf_signatures = r'''
        \section*{Approvals}
        \begin{table}[h!]
        \centering
        \color{ps-darkblue}
        \begin{tabular}{|p{3cm}|p{6cm}|p{5cm}|}
        \hline
         & \textbf{Name\newline Role} & \textbf{Signature \newline Date of signature} \\
        \hline
        \textbf{Elaborated by} & Bartłomiej Paczek, Kamil Ber \newline \small Technical Coordinators, Phoenix Systems Sp. z o.o. &  \\
        \hline
        \textbf{Reviewed by} & Karel Szurman \newline \small Technical Coordinator, LICRIT s.r.o. &  \\
        \hline
        \textbf{Approved by} & Lukáš Mačišák \newline \small Technical Coordinator, LICRIT s.r.o. & \\
        \hline
        \textbf{Approved by} & Bartłomiej Paczek \newline \small Technical Coordinator, Phoenix Systems Sp. z o.o. & \\
        \hline
        \end{tabular}
        \end{table}
        '''
latexpdf_history = r'''
        \section*{Document History}
        \begin{table}[h!]
        \centering
        \color{ps-darkblue}
        \begin{tabular}{|p{1cm}|p{8cm}|p{3cm}|p{2cm}|}
        \hline
        \textbf{Rev.} & \textbf{Description} & \textbf{Elaborated by} & \textbf{Date} \\
        \hline
        1.0 & Initial version & B. Paczek, K. Ber & 2026-01-12 \\
        \hline
        \end{tabular}
        \end{table}
        '''
latexpdf_preamble = r'''\setcounter{secnumdepth}{1}'''

latex_documents = [
    ("index", f"{latexpdf_filename}.tex", latexpdf_title, "", "howto", False),
]
