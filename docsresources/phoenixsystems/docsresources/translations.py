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
    "pl": {
        "toc_title": "Spis treści",
        "author_label": "Autor",
        "contact_label": "Kontakt",
        "registry_lines": (
            "NIP: {tax_id}, REGON: {registry_no}",
            "KRS: {krs} (Sąd Rejonowy dla m. st. Warszawy, {krs_division} Wydział Gospodarczy KRS)",
            "Kapitał zakładowy {share_capital} zł w całości opłacony",
        ),
        "countries": {"pl": "POLSKA", "uk": "WIELKA BRYTANIA"},
        "cities": {"warsaw": "Warszawa", "lomza": "Łomża"},
    },
}

DEFAULT_LANGUAGE = "en"

SUPPORTED_LANGUAGES = tuple(TRANSLATIONS)


def base_language(language):
    """Reduce a language tag such as 'pl_PL' or 'en-GB' to its base code."""
    return (language or DEFAULT_LANGUAGE).replace("-", "_").split("_")[0].lower()


def translations(language):
    """Return the strings for `language`, raise ValueError if it is not supported."""
    try:
        return TRANSLATIONS[base_language(language)]
    except KeyError:
        raise ValueError(
            f"no PDF templates for language {language!r}, supported: {', '.join(SUPPORTED_LANGUAGES)}"
        ) from None
