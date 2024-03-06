# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = ''
copyright = '2024, Phoenix-RTOS'
author = 'Phoenix-RTOS'
release = '3.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx_copybutton'
]

suppress_warnings = ["myst.header"]
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
myst_heading_anchors = 3


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = ''
html_theme = 'sphinx_rtd_theme'
# html_css_files = ['css/furo-phoenix.css', 'css/furo-extensions-phoenix.css']
# html_static_path = ['_static']
# html_theme_options = {
#     "light_logo": "light_logo.png",
#     "light_css_variables": {
# 	"color-sidebar-background": "#F1F3F3",
# 	"color-toc-item-text--active": "#EA5B22",
# 	"color-foreground-primary": "#273149",
# 	"color-brand-primary": "#273149",
# 	"color-brand-content": "#1890d7",
# 	"font-stack": "sans-serif",
# 	"font-stack--headings": "inherit",
# 	"sidebar-caption-font-size": "100%",
# 	"sidebar-item-font-size": "82%",
# 	"toc-font-size": "50%"
#     },

#     "dark_logo": "dark_logo.png",
#     "dark_css_variables": {
# 	"color-sidebar-background": "#202020",
# 	"color-toc-item-text--active": "#EA5B22",
# 	"color-foreground-primary": "#cfd0d0",
# 	"color-brand-primary": "#81868d",
# 	"color-brand-content": "#1890d7",
# 	"font-stack": "sans-serif",
# 	"font-stack--headings": "inherit",
# 	"sidebar-caption-font-size": "100%",
#         "sidebar-item-font-size": "82%",
# 	"toc-font-size": "50%"
#     }
# }
