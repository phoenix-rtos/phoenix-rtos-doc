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
        )
    except ValueError as exc:
        # a document silently typeset in the wrong language must not be released
        raise ConfigError(f"docsresources: {exc}") from exc

    config.latex_engine = defaults["engine"]
    config.latex_table_style = defaults["table_style"]
    # values set in conf.py take precedence over the defaults of this package
    config.latex_additional_files = [*defaults["additional_files"], *config.latex_additional_files]
    config.latex_elements = {**defaults["elements"], **config.latex_elements}


def setup(app):
    app.add_config_value("latexpdf_title", "", "env", str)
    app.add_config_value("latexpdf_author", "", "env", str)
    app.add_config_value("latexpdf_subtitle", "", "env", str)
    app.add_config_value("latexpdf_version", "", "env", str)
    app.add_config_value("latexpdf_date", "", "env", str)
    app.add_config_value("latexpdf_signatures", "", "env", str)
    app.add_config_value("latexpdf_history", "", "env", str)
    app.add_config_value("latexpdf_preamble", "", "env", str)
    app.connect("config-inited", _configure_latex)

    return {"parallel_read_safe": True, "parallel_write_safe": True}
