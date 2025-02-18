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

import pathlib

import cepy_dict

TEST_DICT = pathlib.Path(__file__).parent / "test_dict.txt"

def test_cepy_dict_raw_file_loads_full_dict():
    with cepy_dict.raw_file() as f:
        line_count = len(f.readlines())
    assert line_count > 100_000

def test_cepy_dict_raw_file_test_file():
    with cepy_dict.raw_file(TEST_DICT) as f:
        line_count = len(f.readlines())
    assert line_count == 6

def test_cepy_dict_entries_test_file():
    entries = list(cepy_dict.entries(TEST_DICT))
    assert len(entries) == 3

    # First entry
    line, trad, simp, pinyin, defs = entries[0]
    assert trad == "巨蟒"
    assert pinyin == "ju4 mang3"
    assert defs == ["python"]

    # Second Entry
    line, trad, simp, pinyin, defs = entries[1]
    assert trad != simp
    assert simp == "程序设计"
    assert pinyin == "cheng2 xu4 she4 ji4"
    assert defs == ["computer programming"]

    # Third Entry
    line, trad, simp, pinyin, defs = entries[2]
    assert len(defs) == 9
