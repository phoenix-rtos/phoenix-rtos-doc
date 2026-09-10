#
# Phoenix-RTOS
#
# Documentation resources
#
# Corporate data presented in the PDF documents
#
# Copyright 2026 Phoenix Systems
# Author: Damian Loewnau
#
# SPDX-License-Identifier: BSD-3-Clause
#

"""Phoenix Systems corporate data used by the PDF templates.

This is the single source of truth shared by all language variants - only
language independent facts belong here, their wording lives in translations.py.
"""

COMPANY = {
    "name": "Phoenix Systems S.A.",
    "tax_id": "113-285-28-93",
    "registry_no": "145963772",
    "krs": "0001256594",
    "krs_division": "XIII",
    "share_capital": "241 650,00",
}

# Address lines are formatted with the translated city names from translations.py
OFFICES = (
    {
        "key": "hq",
        "country": "pl",
        "hq": True,
        "address": ("Mangalia 2a", "02-758 {warsaw}"),
    },
    {
        "key": "lomza",
        "country": "pl",
        "address": ("Sienkiewicza 10/17", "18-400 {lomza}"),
    },
    {
        "key": "uk",
        "country": "uk",
        "address": ("Engine Shed, Station Approach", "Temple Meads, Bristol, BS1 6QH"),
    },
)
