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

# Characters a word of a bold header takes over a word of the body
HEADER_WIDTH = 1.15


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
                    cells.append((column, span, entry.astext()))
                    column += span
                yield isinstance(part, nodes.thead), cells


def _demands(node, columns):
    """Characters of the widest cell and of the longest word of every column.

    A cell spanning several columns tells nothing about a single one of them and
    is left out.
    """
    widest = [0] * columns
    longest_word = [0] * columns
    for header, cells in _rows(node):
        bold = HEADER_WIDTH if header else 1
        for column, span, text in cells:
            if span != 1 or column >= columns:
                continue
            widest[column] = max(widest[column], len(text))
            words = (len(word) * bold for word in text.split())
            longest_word[column] = max(longest_word[column], max(words, default=0))
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
    for _, cells in _rows(node):
        lines = 1
        for column, span, text in cells:
            width = sum(widths[column : column + span]) or 1
            lines = max(lines, -(-len(text) // width))
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
