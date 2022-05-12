import sys
import os
from typing import Dict, List, Optional

import rich
from rich.padding import Padding, PaddingDimensions
from rich.table import Table
from rich.style import Style
from rich.styled import Styled
from rich.text import Text
from rich.console import Console, ConsoleOptions, RenderResult


__version__ = "0.1.0"
__author__ = "Martin Larralde <martin.larralde@embl.de>"
__license__ = "MIT"


@rich.repr.auto
class RichAlignment:
    """A `rich` renderable object to display a multiple sequence alignment."""

    _DEFAULT = Style(color="gray30", bold=True)
    _STYLES = {
        l: Style(color=c, bold=True)
        for ls, c in [
            ("AVFPMILW", "red"),
            ("DE", "blue"),
            ("RK", "purple"),
            ("STYHCNGQ", "green"),
        ]
        for l in ls
    }

    def __init__(
        self,
        names: List[str],
        sequences: List[str],
        *,
        gap_character: str = "-",
        max_name_width: int = 10,
        padding: PaddingDimensions = (1, 2, 1, 2),
        styles: Optional[Dict[str, Style]] = None,
        default_style: Optional[Style] = None,
    ) -> None:
        """Create a new `RichAlignment` object.

        Arguments:
            names (`list` of `str`): A list of sequence names to show.
            sequences (`list` of `str`): A list of aligned sequences to show.

        Keyword Arguments:
            gap_character (`str`): The character to treat as a gap in the
                alignment, used for counting the offset in the coordinates
                column.
            max_name_width (`int`): The maximum number of characters to
                display in the sequence name column.
            padding (`rich.padding.PaddingDimensions`): The padding for the
                sequence blocks. Vertical padding will be used between
                blocks, and horizontal padding will be used between columns.
            styles (`dict` of `rich.style.Style`): A dictionary mapping
                individual sequence characters to the style they should be
                rendered with.
            default_style (`rich.style.Style`): The default style to use
                for unknown characters.

        """
        if len(names) != len(sequences):
            raise ValueError("`names` and `sequences` must have the same length")
        if max_name_width <= 0:
            raise ValueError("`max_name_width` must be strictly positive")
        if sequences and not all(len(seq) == len(sequences[0]) for seq in sequences):
            raise ValueError("All strings in `sequences` must have the same length")
        self.names = names
        self.sequences = sequences
        self.sequence_length = len(self.sequences[0]) if sequences else 0
        self.gap_character = gap_character
        self.max_name_width = max_name_width
        self.padding = Padding.unpack(padding)
        self.styles = self._STYLES.copy() if styles is None else styles
        self.default_style = self._DEFAULT if default_style is None else default_style

    def __rich_console__(
        self,
        console: Console,
        options: ConsoleOptions,
    ) -> RenderResult:
        # compute width of the columns so that we know how to wrap the sequences
        length_width = len(str(self.sequence_length))
        name_width = min(self.max_name_width, max(map(len, self.names)))
        if options.no_wrap:
            block_length = self.sequence_length
        else:
            block_length = (
                options.max_width - name_width - length_width - self.padding[1] * 3
            )
        # create a grid to store the different blocks of wrapped sequences
        grid = Table.grid(padding=(self.padding[0], 0, self.padding[2], 0), pad_edge=False)
        grid.add_column(width=options.max_width, no_wrap=True)
        for block_pos in range(0, self.sequence_length, block_length):
            # create the grid with the current sequence block
            table = Table.grid(
                padding=(0, self.padding[1], 0, self.padding[3]),
                pad_edge=False,
            )
            table.add_column(width=name_width, no_wrap=True, overflow="ellipsis")
            table.add_column(width=length_width, no_wrap=True, justify="right")
            table.add_column(width=block_length, no_wrap=True)
            # add each sequence to the block
            for name, characters in zip(self.names, self.sequences):
                offset = (
                    block_pos - characters[:block_pos].count(self.gap_character) + 1
                )
                letters = [
                    (letter, self.styles.get(letter, self.default_style))
                    for letter in characters[block_pos : block_pos + block_length]
                ]
                cell_name = name[:name_width-1] + "…" if len(name) > self.max_name_width else name
                table.add_row(
                    cell_name,
                    Styled(str(offset), rich.style.Style(bold=True, color="cyan")),
                    Text.assemble(*letters, no_wrap=True),
                )
            # add the block to the grid
            grid.add_row(table)
        # render the grid
        yield grid
