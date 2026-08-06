#
# Phoenix-RTOS
#
# Documentation resources
#
# LaTeX resources for the Sphinx documentation builder
#
# Copyright 2025-2026 Phoenix Systems
# Author: Damian Loewnau
#
# SPDX-License-Identifier: BSD-3-Clause
#

"""Phoenix Systems LaTeX resources for Sphinx.

Add "phoenixsystems.docsresources" to `extensions` in conf.py, the document
properties are taken from the `latexpdf_*` options. The language of the
generated PDF follows Sphinx's own `language` option, so it can be also
switched from the command line with `-D language=pl`.
"""

from sphinx.errors import ConfigError
from sphinx.writers.latex import LaTeXTranslator, Table

from . import tables
from .latex import latex_config

__all__ = ["latex_config", "setup"]


def _configure_latex(app, config):
    try:
        defaults = latex_config(
            config.language,
            title=config.latexpdf_title,
            author=config.latexpdf_author,
            subtitle=config.latexpdf_subtitle,
            version=config.latexpdf_version,
            date=config.latexpdf_date,
            signatures=config.latexpdf_signatures,
            history=config.latexpdf_history,
            preamble=config.latexpdf_preamble,
            icons=config.latexpdf_icons,
        )
    except ValueError as exc:
        # a document silently typeset in the wrong language must not be released
        raise ConfigError(f"docsresources: {exc}") from exc

    config.latex_engine = defaults["engine"]
    config.latex_table_style = defaults["table_style"]
    # values set in conf.py take precedence over the defaults of this package
    config.latex_additional_files = [*defaults["additional_files"], *config.latex_additional_files]
    config.latex_elements = {**defaults["elements"], **config.latex_elements}


def _lay_out_table(translator, node):
    """Lay out a table that gives no widths of its own.

    A table of a cell of another table is left to sphinx, as the breaking across
    pages a table may end up needing cannot happen inside a cell.
    """
    if len(translator.tables) > 1:
        return

    table = translator.tables[-1]
    if table.colspec or "colwidths-given" in table.classes:
        return

    spec, widths = tables.colspec(node, table.colsep)
    table.colspec = spec
    # both are read back by the patched methods of Table
    table.fixed_width = True
    # a box holds the table of it whole, so that one has to fit as it is
    table.breakable = not (tables.is_boxed(node) or tables.fits_page(node, widths))


def _patch_table_layout():
    """Extend the table handling of the latex writer of sphinx.

    Sphinx sizes the columns of a table with tabulary, which shrinks them all in
    the same proportion when the content does not fit, and lets a table break
    across pages only above 30 rows, which cuts off the ones that are shorter but
    still taller than a page. There is no option for either, hence the writer is
    extended here, and a document needs to state no widths of its own.
    """
    if getattr(LaTeXTranslator, "_ps_table_layout", False):
        return

    visit_table = LaTeXTranslator.visit_table
    is_longtable = Table.is_longtable
    get_table_type = Table.get_table_type

    def patched_visit_table(self, node):
        visit_table(self, node)
        _lay_out_table(self, node)

    def patched_is_longtable(self):
        return getattr(self, "breakable", False) or is_longtable(self)

    def patched_get_table_type(self):
        # with the widths given there is nothing for tabulary to measure, and a
        # cell holding a list or a code block is not for it to typeset twice
        if getattr(self, "fixed_width", False) and not self.is_longtable():
            return "tabular"
        return get_table_type(self)

    LaTeXTranslator.visit_table = patched_visit_table
    LaTeXTranslator._ps_table_layout = True
    Table.is_longtable = patched_is_longtable
    Table.get_table_type = patched_get_table_type



def setup(app):
    _patch_table_layout()
    app.add_config_value("latexpdf_title", "", "env", str)
    app.add_config_value("latexpdf_author", "", "env", str)
    app.add_config_value("latexpdf_subtitle", "", "env", str)
    app.add_config_value("latexpdf_version", "", "env", str)
    app.add_config_value("latexpdf_date", "", "env", str)
    app.add_config_value("latexpdf_signatures", "", "env", str)
    app.add_config_value("latexpdf_history", "", "env", str)
    app.add_config_value("latexpdf_preamble", "", "env", str)
    app.add_config_value("latexpdf_icons", {}, "env", dict)
    app.connect("config-inited", _configure_latex)

    return {"parallel_read_safe": True, "parallel_write_safe": True}
