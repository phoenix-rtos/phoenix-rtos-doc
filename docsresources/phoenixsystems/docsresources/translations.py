#
# Phoenix-RTOS
#
# Documentation resources
#
# Wording of the PDF documents for each supported language
#
# Copyright 2026 Phoenix Systems
# Author: Damian Loewnau
#
# SPDX-License-Identifier: BSD-3-Clause
#

"""Wording of the PDF templates for each supported language.

Facts (registry numbers, street addresses) are never repeated here - they come
from company.py and are substituted into the templates below, so that all
language variants stay in sync when the corporate data changes.
"""

TRANSLATIONS = {
    "en": {
        "toc_title": "Table of Contents",
        "author_label": "Author",
        "contact_label": "Contact",
        "registry_lines": (
            "TAX ID: PL{tax_id}, National Official Business Registry Number: {registry_no}",
            "KRS: {krs} ({krs_division} Commercial Division of the National Court Register)",
            "Share capital {share_capital} PLN (fully paid)",
        ),
        "countries": {"pl": "POLAND", "uk": "UNITED KINGDOM"},
        "cities": {"warsaw": "Warsaw", "lomza": "Lomza"},
    },
}

DEFAULT_LANGUAGE = "en"

SUPPORTED_LANGUAGES = tuple(TRANSLATIONS)


def base_language(language):
    """Reduce a language tag such as 'pl_PL' or 'en-GB' to its base code."""
    return (language or DEFAULT_LANGUAGE).replace("-", "_").split("_")[0].lower()


def translations(language):
    """Return the strings for `language`, falling back to English."""
    return TRANSLATIONS.get(base_language(language), TRANSLATIONS[DEFAULT_LANGUAGE])
