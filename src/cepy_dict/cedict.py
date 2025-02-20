# Cedict - A chinese english dictionary library
#
# Copyright (C) 2025 Erik Swanson
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import contextlib
import pathlib

DEFAULT_PATH = pathlib.Path(__file__).parent / 'cc-cedict.txt'

@contextlib.contextmanager
def raw_file(path=None):
    """A context manager"""
    path = path if path is not None else DEFAULT_PATH
    with open(path) as f:
        yield f

def entries(path=None):
    """A generator over the entries"""
    path = path if path is not None else DEFAULT_PATH
    with raw_file(path) as f:
        for line in f.readlines():
            if line.strip().startswith("#") or line.strip() == "":
                continue
            (trad, _sep, rest) = line.partition(" ")
            (simp, _sep, rest) = rest.partition(" [")
            (pinyin, _sep, rest) = rest.partition("] ")
            defs = [d.strip() for d in rest.strip(" /\n\t").split("/")]
            yield (line, trad, simp, pinyin, defs)
