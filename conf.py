# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

from version_management import get_version_context

project = ""
copyright = "2024, Phoenix Systems"
author = "Phoenix Systems"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser", "sphinx_copybutton"]

templates_path = ["_templates"]
exclude_patterns = ["README.md", "_build", "Thumbs.db", ".DS_Store"]
# exclude_patterns = ["*.md", "_build", "Thumbs.db", ".DS_Store", "**/*.md"]
myst_heading_anchors = 3
pygments_dark_style = "tango"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = "Phoenix-RTOS Documentation"
html_favicon = "_images/RTOS_sign.png"
html_theme = "furo"
html_js_files = ["js/functions.js", "js/versions.js"]
html_style = ["css/furo-phoenix.css", "css/furo-extensions-phoenix.css"]
html_static_path = ["_static", "_static/images", "_static/gifs"]
html_baseurl = "https://docs.phoenix-rtos.com/latest/"
html_context = {"versions": get_version_context()}

linkcheck_timeout = 30

latex_engine = 'xelatex'
latex_documents = [
    ("index", "phoenix.tex", "Phoenix-RTOS Documentation", author, "howto", True),
]
latex_additional_files = ["_static/images/pdf-titlepage.png", "_static/images/small_logo.png", "_static/images/companylogo.png", "_static/images/endpage.png"]
latex_elements = {
    'makeindex': r'',
    'papersize': r'a4paper',
    'babel': '\\usepackage[english]{babel}',
    'extrapackages': r'''
        \usepackage{graphicx}
        \usepackage{tocloft}
        \usepackage{xcolor}
        \usepackage[absolute]{textpos}
        \usepackage{fontspec}
        \usepackage[english]{babel}
        \usepackage{fancyhdr}
        \usepackage{tikz}    % Add this for drawing the circle
        \usepackage{fancyvrb}
        \usepackage{framed}
    ''',
    'preamble': r'''
        \setmainfont{Liberation Sans}
        \addtolength{\cftsubsecnumwidth}{4pt}
        \setcounter{secnumdepth}{3}
        \definecolor{ps-orange}{HTML}{ea5b22}
        \definecolor{lightgray}{RGB}{245, 245, 245}
        \addto\captionsenglish{\renewcommand{\contentsname}{\textcolor{ps-orange}{Table of contents}}}

        % Define the fancy page style
        \fancypagestyle{normal}{
            \fancyhf{}    % Clear all header/footer fields
            \fancyhead[R]{\includegraphics[width=2.5cm]{small_logo.png}}    % Logo in right header
            \fancyfoot[R]{%
                \begin{tikzpicture}
                    \node[circle, fill=ps-orange, text=white, minimum size=20pt, inner sep=0pt, font=\bfseries] {\thepage};
                \end{tikzpicture}%
            }
            \renewcommand{\headrulewidth}{0pt}    % Remove header line
        }

        % Code block styling
        \usepackage{listings}
        \definecolor{lightgray}{RGB}{248,248,248}

        % Override Sphinx verbatim settings
        \fvset{
            frame=none,
            numbers=none,
            fontfamily=ttfamily,
            baselinestretch=1.2
        }
        % Sphinx-specific settings
        \sphinxsetup{
            VerbatimColor={rgb}{0.97,0.97,0.97},  % Background color for code blocks
            VerbatimBorderColor={rgb}{0.97,0.97,0.97},  % Make border same as background
            verbatimwithframe=false,
            verbatimsep=8pt,
            verbatimborder=0pt    % Set border width to 0
        }

        % Additional frame removal
        \renewenvironment{Verbatim}{%
            \setlength{\fboxsep}{0pt}%
            \setlength{\fboxrule}{0pt}%
            \begin{flushleft}%
        }{%
            \end{flushleft}%
        }

        % Apply the style to all pages
        \pagestyle{normal}
    ''',
    'maketitle': r'''
        \newgeometry{margin=0pt}
        \thispagestyle{empty}
        \begin{figure}
            \includegraphics[width=\paperwidth,height=\paperheight]{pdf-titlepage.png}
        \end{figure}
        \clearpage
        \restoregeometry
    ''',
    'atendofbody': r'''
        \clearpage
        \thispagestyle{empty}
        
        % Company logo in upper left corner
        \begin{textblock*}{10cm}(2cm,2cm)    % Adjust position as needed
            \includegraphics[width=8cm]{companylogo.png}
        \end{textblock*}
        
        % Right side main image
        \vspace*{1.5cm}    % Adjust space from top
        \begin{flushright}
            \makebox[0pt][r]{    % Creates box that won't affect other elements
                \rlap{\hspace{-12.5cm}\includegraphics[width=1\textwidth]{endpage.png}}
            }
        \end{flushright}
        
        % Three text blocks stacked vertically
        \vspace{2cm}    % Adjust space before text blocks
        \begin{flushright}
            \hspace{0.5cm}    % Left margin
            {\fontsize{24}{28} \selectfont \textbf{Phoenix Systems Sp. z o. o.}}

            \vspace{1cm}
            {\fontsize{11}{15} TAX ID: PL113-285-28-93, National Official Business Registry Number: 145963772\\  
KRS: 0000417999 (XIV Commercial Division of the National Court Register)\\
Share capital 241 650,00 PLN (fully paid)}

            \vspace{1cm}
            {\fontsize{14}{18} \textcolor{orange}{phoenix-rtos.com}  |  github.com/phoenix-rtos}
            
            \vspace{0cm}
            {\fontsize{14}{18} Contact: contact@phoenix-rtos.com}
        \end{flushright}
        
        % Three bottom blocks horizontally aligned
        \vspace{1.6cm}    % Space before bottom blocks
        \begin{center}
            \begin{minipage}{0.4\textwidth}
                {\fontsize{11}{15} \textbf{POLAND (HQ)} \\ Ostrobramska 86 \\
04-163 Warsaw, Poland}
            \end{minipage}%
            \hspace{-2cm}%    % Negative space between first and second block
            \begin{minipage}{0.4\textwidth}
                {\fontsize{11}{15} \textbf{POLAND} \\ Sienkiewicza 10/17 \\
18-400 Łomża, Poland}
            \end{minipage}%
            \hspace{-2cm}%    % Negative space between first and second block
            \begin{minipage}{0.4\textwidth}
                {\fontsize{11}{15} \textbf{UNITED KINGDOM} \\ Engine Shed, Station Approach \\
Temple Meads, Bristol, BS1 6QH, UK}
            \end{minipage}
        \end{center}
        
        % Orange line below bottom blocks
        \vspace{1cm}
        \begin{center}
            \color{orange}\rule{\textwidth}{2pt}
        \end{center}
''',
}

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
