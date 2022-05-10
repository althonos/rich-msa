import argparse
import os

import Bio.AlignIO
import rich

from . import RichAlignment


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=True)
    parser.add_argument("-f", "--format")
    parser.add_argument("-n", "--max-name-width", type=int, default=10)

    args = parser.parse_args()

    msa = Bio.AlignIO.read(args.input, args.format or "fasta")
    viewer = RichAlignment(
        names=[record.id for record in msa],
        sequences=[str(record.seq) for record in msa],
        max_name_width=args.max_name_width,
    )

    panel = rich.panel.Panel(viewer, title=os.path.basename(args.input))
    rich.print(panel)
