#!/usr/bin/bash
set -euo pipefail
IFS=$'\n\t'

PROJECT_ROOT="$(dirname "$0")"

curl https://www.mdbg.net/chinese/export/cedict/cedict_1_0_ts_utf-8_mdbg.zip -o cedict.zip
unzip cedict.zip
mv cedict_ts.u8 "$PROJECT_ROOT/src/cepy_dict/cc-cedict.txt"
rm cedict.zip
