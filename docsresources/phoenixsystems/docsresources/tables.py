#
# Phoenix-RTOS
#
# Documentation resources
#
# Column widths and page breaking of the tables
#
# Copyright 2026 Phoenix Systems
# Author: Damian Loewnau
#
# SPDX-License-Identifier: BSD-3-Clause
#

"""Layout of the tables which give no widths of their own.

Sphinx leaves the widths of such a table to tabulary and lets it break across
pages only above 30 rows. A table of fewer rows that does not fit a page is then
cut off at its end, and the taller ones are given columns that do not wrap at
all, so their text runs off the page.

The widths are therefore taken from the content of the table here, and a table
estimated not to fit a page is made breakable. Tables which state their widths,
by the :widths: option or by the tabularcolumns directive, are left alone.
"""

from docutils import nodes

# Characters of the text font that fit in one line of the full width of the text
LINE_CHARACTERS = 95

# Height of the text of a page and of one of its lines, in points. The page is
# taken a little shorter than it is, as the estimate below is a rough one, while
# a breakable table that does fit a page looks no different.
PAGE_HEIGHT = 640
LINE_HEIGHT = 12

# Space taken above and below the content of a cell, twice \psTableCellPadding
# of tables.tex
CELL_PADDING = 22

# Characters a column keeps beyond its longest word, for the padding of the cell
COLUMN_MARGIN = 4

# Characters of the text font one character of a bold header takes, and one of
# the monospace font of a literal, whose 6.02pt stand against the 4.77pt of the
# line of the text divided into LINE_CHARACTERS
HEADER_WIDTH = 1.15
LITERAL_WIDTH = 1.3


# Nodes typeset as a box, which is narrower than the page and holds no table
# that breaks across pages
BOXES = (nodes.entry, nodes.Admonition, nodes.sidebar, nodes.footnote, nodes.figure)


def is_boxed(node):
    """Tell whether the table stands inside a box of the document."""
    parent = node.parent
    while parent is not None:
        if isinstance(parent, BOXES):
            return True
        parent = parent.parent
    return False


def _column_count(node):
    for group in node.children:
        if isinstance(group, nodes.tgroup):
            return int(group.get("cols", 0))
    return 0


def _rows(node):
    """Yield the rows as (header, cells), skipping the cells of a nested table."""
    for group in node.children:
        if not isinstance(group, nodes.tgroup):
            continue
        for part in group.children:
            if not isinstance(part, (nodes.thead, nodes.tbody)):
                continue
            for row in part.children:
                cells, column = [], 0
                for entry in row.children:
                    span = entry.get("morecols", 0) + 1
                    cells.append((column, span, entry))
                    column += span
                yield isinstance(part, nodes.thead), cells


def _pieces(node, character):
    """Yield the text of the node as (characters, width of a character) pieces."""
    if isinstance(node, nodes.Text):
        yield str(node), character
        return
    if isinstance(node, nodes.literal):
        character = LITERAL_WIDTH
    for index, child in enumerate(node.children):
        if index:
            yield node.child_text_separator, character
        yield from _pieces(child, character)


def _measure(entry, character):
    """Characters of the text font the cell takes, and its longest word of them.

    A literal is set in the monospace font and a header in a bold one, both wider
    than the text the line of the page is measured in.
    """
    total, word, longest = 0, 0, 0
    for text, width in _pieces(entry, character):
        for letter in text:
            total += width
            word = 0 if letter.isspace() else word + width
            longest = max(longest, word)
    return total, longest


def _demands(node, columns):
    """Characters of the widest cell and of the longest word of every column.

    A cell spanning several columns tells nothing about a single one of them and
    is left out.
    """
    widest = [0] * columns
    longest_word = [0] * columns
    for header, cells in _rows(node):
        character = HEADER_WIDTH if header else 1
        for column, span, entry in cells:
            if span != 1 or column >= columns:
                continue
            cell, word = _measure(entry, character)
            widest[column] = max(widest[column], cell)
            longest_word[column] = max(longest_word[column], word)
    return widest, [round(word) for word in longest_word]


def _widths(widest, longest_word):
    """Share the line among the columns, in proportion but never below a word.

    A column too narrow for its longest word would have that word sticking out of
    the cell, so such a column is pinned to the width of the word and the rest of
    the line is shared again.
    """
    minimum = [word + COLUMN_MARGIN for word in longest_word]
    if sum(minimum) >= LINE_CHARACTERS:
        return minimum  # the words alone fill the line, there is nothing to share

    widths = list(minimum)
    free = LINE_CHARACTERS
    pending = set(range(len(widest)))
    while pending:
        weight = sum(max(widest[column], 1) for column in pending)
        share = {column: free * max(widest[column], 1) / weight for column in pending}
        pinned = {column for column in pending if share[column] < minimum[column]}
        if not pinned:
            for column in pending:
                widths[column] = max(1, round(share[column]))
            break
        for column in pinned:
            free -= minimum[column]
        pending -= pinned
    return widths


def _height(node, widths):
    """Points the table would take, to tell whether it fits a page."""
    height = 0
    for header, cells in _rows(node):
        character = HEADER_WIDTH if header else 1
        lines = 1
        for column, span, entry in cells:
            available = sum(widths[column : column + span]) or 1
            cell, _ = _measure(entry, character)
            lines = max(lines, -(-cell // available))
        height += lines * LINE_HEIGHT + CELL_PADDING
    return height


def colspec(node, colsep):
    """Return the LaTeX column specification of the table and its column widths."""
    widths = _widths(*_demands(node, _column_count(node)))
    total = sum(widths)
    columns = colsep.join(rf"\X{{{width}}}{{{total}}}" for width in widths)
    return f"{{{colsep}{columns}{colsep}}}\n", widths


def fits_page(node, widths):
    return _height(node, widths) <= PAGE_HEIGHT
