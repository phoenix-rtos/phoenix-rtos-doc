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

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
myst_heading_anchors = 3

# pygments_style = 'css/pygments-phoenix.css'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = ''
html_theme = 'furo'
html_css_files = ['css/furo.css', 'css/furo-extensions.css']
html_static_path = ['_static']
html_theme_options = {
    "light_logo": "light_logo.png",
    "light_css_variables": {
	"color-sidebar-background": "#0F1724",
	"color-toc-background": "#F1F3F3",
	"color-sidebar-search-icon": "#EA5B22",
	"color-toc-item-text--active": "#F1F3F3",
	"color-foreground-primary": "#273149",
	"color-brand-primary": "#273149",
	"color-brand-content": "#1890d7",
	"font-stack": "sans-serif",
	"font-stack--headings": "inherit",
	"sidebar-caption-font-size": "100%",
	"sidebar-item-font-size": "90%",
	"sidebar-item-spacing-vertical": "0.4rem",
	"sidebar-item-line-height": "1.1rem",
	"sidebar-search-space-above": "0.1rem",
	"sidebar-caption-space-above": "0.1rem",
	"sidebar-tree-space-above": "0.5rem",
	"sidebar-search-input-font-size": "95%"
    },

    "dark_logo": "light_logo.png",
    "dark_css_variables": {
	"color-sidebar-background": "#0F1724",
        "color-toc-background": "#F1F3F3",
        "color-sidebar-search-icon": "#EA5B22",
        "color-toc-item-text--active": "#F1F3F3",
        "color-foreground-primary": "#273149",
        "color-brand-primary": "#273149",
        "color-brand-content": "#1890d7",
        "font-stack": "sans-serif",
        "font-stack--headings": "inherit",
        "sidebar-caption-font-size": "100%",
        "sidebar-item-font-size": "90%",
        "sidebar-item-spacing-vertical": "0.4rem",
        "sidebar-item-line-height": "1.1rem",
        "sidebar-search-space-above": "0.1rem",
        "sidebar-caption-space-above": "0.1rem",
        "sidebar-tree-space-above": "0.5rem",
	"sidebar-search-input-font-size": "95%"
    },
}