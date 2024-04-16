# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = ''
copyright = '2024, Phoenix Systems'
author = 'Phoenix Systems'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx_copybutton'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
myst_heading_anchors = 3
pygments_dark_style = 'tango'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = 'Phoenix-RTOS Documentation'
html_favicon = '_images/RTOS_sign.png'
html_theme = 'furo'
html_style = ['css/furo-phoenix.css', 'css/furo-extensions-phoenix.css']
html_static_path = ['_static', '_images']
# TODO: add dark mode support
html_theme_options = {
	"light_css_variables": {
		"sidebar-caption-font-size": "100%",
		"sidebar-item-font-size": "90%",
		"sidebar-item-spacing-vertical": "0.4rem",
		"sidebar-item-line-height": "1.1rem",
		"sidebar-search-space-above": "0.1rem",
		"sidebar-caption-space-above": "0.1rem",
		"sidebar-tree-space-above": "0.5rem",
		"sidebar-search-input-font-size": "95%",
		"font-stack": "'Open Sans', sans-serif"
	},

	"dark_css_variables": {
		"sidebar-caption-font-size": "100%",
		"sidebar-item-font-size": "90%",
		"sidebar-item-spacing-vertical": "0.4rem",
		"sidebar-item-line-height": "1.1rem",
		"sidebar-search-space-above": "0.1rem",
		"sidebar-caption-space-above": "0.1rem",
		"sidebar-tree-space-above": "0.5rem",
		"sidebar-search-input-font-size": "95%",
		"font-stack": "'Open Sans', sans-serif"
	}
}
