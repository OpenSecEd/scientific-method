#!/bin/sh
# Classify the pending records of mfa-sufficient, a hundred at a time.
cd "$(dirname "$0")"
i=0
while [ $i -lt 8 ]; do
  i=$((i+1))
  scholar llm classify mfa-sufficient --no-examples -m anthropic/claude-sonnet-5-5 -n 100 \
    -t supports-claim -t qualifies-claim -t adjacent-subtopic -t off-topic-false-hit \
    -t x1-new-scheme -t x2-machine -t x3-usability-only -t x4-no-evidence \
    -t x5-other-question -t x6-not-english --no-enrich > classify-$i.log 2>&1
  left=$(/home/dbosk/.local/pipx/venvs/scholarcli/bin/python pending.py mfa-sufficient)
  echo "batch $i done, pending: $left" >> classify.progress
  [ "${left:-0}" = "0" ] && break
done
echo finished > classify.finished
