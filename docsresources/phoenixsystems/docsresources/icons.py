#
# Phoenix-RTOS
#
# Documentation resources
#
# Icons used in the PDF documents
#
# Copyright 2026 Phoenix Systems
# Author: Damian Loewnau
#
# SPDX-License-Identifier: BSD-3-Clause
#

"""Icons of the documentation sources, and the glyphs they are drawn with.

The text font holds none of these characters, while the fonts declared in
latex.py hold most of them. Every icon is drawn as a character of one of those
fonts, so that it stays a character of the PDF: it can be selected, copied, and
found by a search for it.

Where no monochrome font has the character of an icon, or where the glyph of it
reads worse than a plain shape - a hatched circle for a coloured one, an outlined
star for a filled one - the icon names the character to draw instead. Such an
icon is then found by a search for that character rather than for itself.

A document needing an icon that is not listed here can define its own mapping
with the latexpdf_icons option, which also overrides the entries below.
"""

from collections import namedtuple

# The fonts declared in latex.py, by the name of the family
SYMBOLS = "psSymbolFont"
FREE = "psFreeFont"

GREEN = "green!60!black"
RED = "red"
YELLOW = "yellow"
BLUE = "blue"
ORANGE = "orange"

# The character to draw, empty for the character of the icon itself; the font to
# take the glyph of it from; and the colour to typeset it in
Icon = namedtuple("Icon", "glyph font color", defaults=("", SYMBOLS, ""))

ICONS = {
    # marks
    "✅": Icon("✔", color=GREEN),  # U+2705, no monochrome font has it
    "✔": Icon(),  # U+2714 heavy check mark
    "❌": Icon(font=FREE, color=RED),  # U+274C cross mark
    "✖": Icon(),  # U+2716 heavy multiplication x
    "⚠": Icon(color=ORANGE),  # U+26A0 warning sign
    "❗": Icon(color=RED),  # U+2757 exclamation mark
    "❓": Icon(),  # U+2753 question mark
    # circles, the coloured ones drawn plain rather than hatched
    "🔴": Icon("⚫", color=RED),  # U+1F534 red circle
    "🟡": Icon("⚫", color=YELLOW),  # U+1F7E1 yellow circle
    "🟢": Icon("⚫", color=GREEN),  # U+1F7E2 green circle
    "🔵": Icon("⚫", color=BLUE),  # U+1F535 blue circle
    "⚫": Icon(),  # U+26AB medium black circle
    "⚪": Icon(),  # U+26AA medium white circle
    # squares and diamonds, the same way
    "🟥": Icon("⬛", color=RED),  # U+1F7E5 red square
    "🟨": Icon("⬛", color=YELLOW),  # U+1F7E8 yellow square
    "🟩": Icon("⬛", color=GREEN),  # U+1F7E9 green square
    "🟦": Icon("⬛", color=BLUE),  # U+1F7E6 blue square
    "⬛": Icon(),  # U+2B1B black large square
    "⬜": Icon(),  # U+2B1C white large square
    "🔶": Icon("◆", color=ORANGE),  # U+1F536 large orange diamond
    "🔷": Icon("◆", color=BLUE),  # U+1F537 large blue diamond
    # stars
    "⭐": Icon("★"),  # U+2B50, the glyph of it is an outlined star
    "★": Icon(),  # U+2605 black star
    "☆": Icon(),  # U+2606 white star
    # arrows
    "➡": Icon(),  # U+27A1 black rightwards arrow
    "⬅": Icon(),  # U+2B05 leftwards black arrow
    "⬆": Icon(),  # U+2B06 upwards black arrow
    "⬇": Icon(),  # U+2B07 downwards black arrow
    "▶": Icon(),  # U+25B6 black right pointing triangle
    "◀": Icon(),  # U+25C0 black left pointing triangle
    "⏭": Icon(),  # U+23ED next track
    "⏮": Icon(),  # U+23EE previous track
    # U+FE0F selects the emoji presentation of the preceding character and U+200D
    # joins the characters of a single emoji - neither of them is typeset, and
    # both are written as escapes, as they leave no trace of themselves in a file
    "\ufe0f": None,
    "\u200d": None,
}
