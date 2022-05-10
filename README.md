# `rich-msa` [![Stars](https://img.shields.io/github/stars/althonos/rich-msa.svg?style=social&maxAge=3600&label=Star)](https://github.com/althonos/rich-msa/stargazers)

*A simple module to render colorful Multiple Sequence Alignment with `rich` in the terminal.*

## 💡 Example

Use Biopython to load a MSA from an aligned FASTA file, and render it to the
terminal:

```python
import Bio.AlignIO
from rich_msa import RichAlignment

msa = Bio.AlignIO.read("tests/data/swissprot-halorhodopsin.muscle.afa" "fasta")
viewer = RichAlignment(
    names=[record.id for record in msa],
    sequences=[str(record.seq) for record in msa],
)

panel = rich.panel.Panel(viewer, title="swissprot-halorhodopsin.muscle.afa")
rich.print(panel)
```

You should get an output similar to the following picture, scaled to your
terminal width:
![screenshot](https://github.com/althonos/rich-msa/raw/main/static/example1.png)

## ⚖️ License

This library is provided under the [MIT License](https://choosealicense.com/licenses/mit/).

*This project is in no way not affiliated, sponsored, or otherwise endorsed
by the [original Rich authors](https://github.com/textualize). It was developed
by [Martin Larralde](https://github.com/althonos/) during his PhD project
at the [European Molecular Biology Laboratory](https://www.embl.de/) in
the [Zeller team](https://github.com/zellerlab).*
