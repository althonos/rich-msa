import argparse
import json
import os
import typing

import Bio.AlignIO
import rich
from rich.color import Color
from rich.style import Style
from rich.console import Console

from . import RichAlignment

_FORMATS = {
    "clustal",
    "emboss",
    "fasta",
    "fasta-m10",
    "ig",
    "msg",
    "nexus",
    "phylip",
    "phylip-sequential",
    "phylip-relaxed",
    "stockholm",
    "mauve"
}

def main(argv: typing.Optional[typing.List[str]] = None, console: rich.console.Console = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--input",
        required=True,
        help="The path to the alignment file to render",
    )
    parser.add_argument(
        "-f",
        "--format",
        default="fasta",
        choices=_FORMATS,
        help="The format of the alignment file"
    )
    parser.add_argument(
        "-n",
        "--max-name-width",
        type=int,
        default=10,
        help="The maximum width of the name column"
    )
    parser.add_argument(
        "-c",
        "--colors",
        help="The path to a JSON file in Gecos format with the color scheme to use"
    )
    args = parser.parse_args(argv)

    console = console if console is not None else Console()
    try:
        # load style if any
        if args.colors:
            with open(args.colors, "rb") as colors_file:
                data = json.load(colors_file)
                styles = {
                    letter:rich.style.Style(bold=True, color=Color.parse(color))
                    for letter, color in data["colors"].items()
                }
        else:
            styles = None
        # load MSA using Biopython
        msa = Bio.AlignIO.read(args.input, args.format)
        viewer = RichAlignment(
            names=[record.id for record in msa],
            sequences=[str(record.seq) for record in msa],
            max_name_width=args.max_name_width,
            styles=styles,
        )
        # render the MSA
        panel = rich.panel.Panel(viewer, title=os.path.basename(args.input))
        console.print(panel)
    except Exception as err:
        console.print_exception()
        return getattr(err, "errno", 1)
    else:
        return 0
