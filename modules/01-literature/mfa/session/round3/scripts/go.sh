#!/bin/sh
# Third round: other databases into the session, then OpenAlex title/abstract
# into the session, then OpenAlex full text to CSV only (kept, not screened).
PY=/home/dbosk/.local/pipx/venvs/scholarcli/bin/python
cd "$(dirname "$0")"
$PY add.py && $PY oa_ta.py mfa-sufficient && $PY run.py openalex
echo finished > go.finished
