# `cepy-dict` -- A sleepy Chinese-English dictionary in python

## Install

The package is [available on
PyPI](https://pypi.org/project/cepy-dict/) and can be installed with
`pip`:

```
pip install cepy-dict
```

## Usage

This package provides a Chinese-English dictionary which can be loaded
in a textual format with a context manager or as an iterator of entries:

**Raw Text -- `cepy_dict.raw_file`**:

A context manager which provides a file handle just like `with open()`
would:

```python
import cepy_dict

with cepy_dict.raw_file() as f:
    f.readlines()
```

**Iterator of entries -- `cepy_dict.entries`**:

```python
import cepy_dict

for entry in cepy_dict.entries():
    entry_text, traditional, simplified, pinyin, definitions = entry
```

By default both of these functions use the built in dictionary, but
both can optionally take an argument `path` which can be a path to any
dictionary in the [cc-cedict
format](https://cc-cedict.org/wiki/format:syntax).

## Advanced Tooling

This package only provides very basic tooling. It's main purpose is to
be a pip-installable Chinese-English dictionary. For more advanced
tools, see the higher level package
[cepy-tools](https://github.com/swans-one/cepy-tools).

# CC-CEDICT

This package includes
[CC-CEDICT](https://www.mdbg.net/chinese/dictionary?page=cc-cedict).

CC-CEDICT is a Chinese-English dictionary licensed under the [CC BY-SA
4.0](https://creativecommons.org/licenses/by-sa/4.0/) license. It is
redistributed in this library under the GPLv3, a compatible license.
