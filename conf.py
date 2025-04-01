# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

from version_management import get_version_context


project = ""
copyright = "2024, Feniks Systems"
author = "Feniks Systems"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser", "sphinx_copybutton"]

templates_path = ["_templates"]
exclude_patterns = ["README.md", "_build", "Thumbs.db", ".DS_Store"]
myst_heading_anchors = 3
pygments_dark_style = "tango"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = "Feniks-RTOS Documentation"
html_favicon = "_images/RTOS_sign.png"
html_theme = "furo"
html_js_files = ["js/functions.js", "js/versions.js"]
html_style = ["css/furo-feniks.css", "css/furo-extensions-feniks.css"]
html_static_path = ["_static", "_images"]
html_baseurl = "https://docs.feniks-rtos.com/latest/"
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
