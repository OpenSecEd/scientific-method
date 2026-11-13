"""Make the exclusion labels consistent with the categories.

An exclusion label (x1-... to x6-...) belongs on a record excluded as
adjacent, one per record.  The classifier sometimes puts one on a record
it files as another topic or as bearing on the question, or puts two.
This removes the label from records that are not adjacent and keeps one
label where there are two (x6-not-english first, then the first given).
Usage: clean_x.py <session>"""
import re, sys
from scholar.review import load_session, save_session
sess = load_session(sys.argv[1], strict=True)
off = bear = multi = 0
for d in sess.decisions:
    xs = [t for t in d.tags if re.match(r"x\d-", t)]
    if not xs:
        continue
    if "adjacent-subtopic" not in d.tags:
        d.tags = [t for t in d.tags if t not in xs]
        if "off-topic-false-hit" in d.tags: off += 1
        else: bear += 1
    elif len(xs) > 1:
        keep = "x6-not-english" if "x6-not-english" in xs else xs[0]
        d.tags = [t for t in d.tags if t not in xs or t == keep]; multi += 1
save_session(sess)
print(f"{sys.argv[1]}: label removed from {off} off-topic and {bear} other non-adjacent record(s); {multi} record(s) reduced to one label")
