# `rich-msa` [![Stars](https://img.shields.io/github/stars/althonos/rich-msa.svg?style=social&maxAge=3600&label=Star)](https://github.com/althonos/rich-msa/stargazers)

*A simple module to render colorful Multiple Sequence Alignment with `rich` in the terminal.*

[![Actions](https://img.shields.io/github/workflow/status/althonos/rich-msa/Test/main?logo=github&style=flat-square&maxAge=300)](https://github.com/althonos/rich-msa/actions)
[![Coverage](https://img.shields.io/codecov/c/gh/althonos/rich-msa?style=flat-square&maxAge=3600)](https://codecov.io/gh/althonos/rich-msa/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square&maxAge=2678400)](https://choosealicense.com/licenses/mit/)
[![PyPI](https://img.shields.io/pypi/v/rich-msa.svg?style=flat-square&maxAge=3600)](https://pypi.org/project/rich-msa)
[![Wheel](https://img.shields.io/pypi/wheel/rich-msa.svg?style=flat-square&maxAge=3600)](https://pypi.org/project/rich-msa/#files)
[![Python Versions](https://img.shields.io/pypi/pyversions/rich-msa.svg?style=flat-square&maxAge=3600)](https://pypi.org/project/rich-msa/#files)
[![Python Implementations](https://img.shields.io/badge/impl-universal-success.svg?style=flat-square&maxAge=3600&label=impl)](https://pypi.org/project/rich-msa/#files)
[![Source](https://img.shields.io/badge/source-GitHub-303030.svg?maxAge=2678400&style=flat-square)](https://github.com/althonos/rich-msa/)
[![Mirror](https://img.shields.io/badge/mirror-EMBL-009f4d?style=flat-square&maxAge=2678400)](https://git.embl.de/larralde/rich-msa/)
[![GitHub issues](https://img.shields.io/github/issues/althonos/rich-msa.svg?style=flat-square&maxAge=600)](https://github.com/althonos/rich-msa/issues)
[![Changelog](https://img.shields.io/badge/keep%20a-changelog-8A0707.svg?maxAge=2678400&style=flat-square)](https://github.com/althonos/rich-msa/blob/master/CHANGELOG.md)
[![Downloads](https://img.shields.io/badge/dynamic/json?style=flat-square&color=303f9f&maxAge=86400&label=downloads&query=%24.total_downloads&url=https%3A%2F%2Fapi.pepy.tech%2Fapi%2Fprojects%2Frich-msa)](https://pepy.tech/project/rich-msa)


## 🔧 Installing

Install the `rich-msa` package directly from [PyPi](https://pypi.org/project/rich-msa)
which hosts universal wheels that can be installed with `pip`:
```console
$ pip install rich-msa
```

## 💡 Example

Use Biopython to load a MSA from an aligned FASTA file, and render it to the
terminal:

```python
import Bio.AlignIO
import rich
from rich_msa import RichAlignment

msa = Bio.AlignIO.read("tests/data/swissprot-halorhodopsin.muscle.afa", "fasta")
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


## 🪛 Command-Line

If you have the `rich-msa` library installed from PyPI, you can use it directly
to view any alignment file, provided you have [Biopython](https://biopython.org) installed:

```console
$ python -m rich_msa -i tests/data/swissprot-halorhodopsin.muscle.afa
```

*Use the `-f` flag to change the file format from aligned FASTA (default) to
any alignment format supported by Biopython.*

## 💭 Feedback

### ⚠️ Issue Tracker

Found a bug ? Have an enhancement request ? Head over to the [GitHub issue
tracker](https://github.com/althonos/rich-msa/issues) if you need to report
or ask something. If you are filing in on a bug, please include as much
information as you can about the issue, and try to recreate the same bug
in a simple, easily reproducible situation.

### 🏗️ Contributing

Contributions are more than welcome! See
[`CONTRIBUTING.md`](https://github.com/althonos/rich-msa/blob/main/CONTRIBUTING.md)
for more details.

## ⚖️ License

This library is provided under the [MIT License](https://choosealicense.com/licenses/mit/).

*This project is in no way not affiliated, sponsored, or otherwise endorsed
by the [original Rich authors](https://github.com/textualize). It was developed
by [Martin Larralde](https://github.com/althonos/) during his PhD project
at the [European Molecular Biology Laboratory](https://www.embl.de/) in
the [Zeller team](https://github.com/zellerlab).*
