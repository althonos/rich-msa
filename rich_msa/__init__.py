import sys
import os
import typing

import rich
from rich.padding import Padding, PaddingDimensions
from rich.table import Table
from rich.style import Style
from rich.styled import Styled
from rich.text import Text
from rich.console import Console, ConsoleOptions, RenderResult


class RichAlignment:
    """A `rich` renderable object to display a multiple sequence alignment."""

    _STYLES = {
        l: Style(color=c, bold=True)
        for ls, c in [
            ("AVFPMILW", "red"),
            ("DE", "blue"),
            ("RK", "purple"),
            ("STYHCNGQ", "green"),
            ("-*", "gray30"),
        ]
        for l in ls
    }

    def __init__(
        self,
        names: typing.List[str],
        sequences: typing.List[str],
        *,
        gap_character: str = "-",
        max_name_width: int = 10,
        padding: PaddingDimensions = (1, 2)
    ):
        self.names = names
        self.sequences = sequences
        self.sequence_length = len(self.sequences[0]) if self.sequences else 0
        self.gap_character = gap_character
        self.max_name_width = max_name_width
        self.padding = Padding.unpack(padding)

    def __rich_console__(
        self,
        console: Console,
        options: ConsoleOptions,
    ) -> RenderResult:

        sequence_length = self.sequence_length
        length_width = len(str(sequence_length))
        name_width = min(self.max_name_width, max(map(len, self.names)))
        block_length = (
            options.max_width - name_width - length_width - self.padding[1] * 3
        )
        grid = Table.grid(padding=(self.padding[0], 0, self.padding[2], 0))
        grid.add_column(width=options.max_width, no_wrap=True)

        for block_pos in range(0, self.sequence_length, block_length):

            table = Table.grid(
                padding=(0, self.padding[1], 0, self.padding[3]), pad_edge=False
            )
            table.add_column(max_width=name_width, no_wrap=True, overflow="ellipsis")
            table.add_column(width=length_width, justify="right")
            table.add_column(no_wrap=True)

            for name, characters in zip(self.names, self.sequences):
                offset = (
                    block_pos - characters[:block_pos].count(self.gap_character) + 1
                )
                letters = [
                    (letter, self._STYLES[letter])
                    for letter in characters[block_pos : block_pos + block_length]
                ]
                table.add_row(
                    name,
                    Styled(str(offset), rich.style.Style(bold=True, color="cyan")),
                    Text.assemble(*letters),
                )

            grid.add_row(table)

        yield grid
