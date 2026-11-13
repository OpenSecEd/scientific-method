"""Change the classification of records in a scholar session, replacing the
old category instead of appending to it (which `scholar sessions decide`
cannot do).  Usage:
  retag.py <session> <category> [<x-tag-or-theme> ...] -- <paper_id> [<paper_id> ...]
<category> is one of supports-claim, qualifies-claim, adjacent-subtopic,
off-topic-false-hit.  supports/qualifies set the record to kept, the other
two to discarded.  Extra tags (an exclusion label x1..x6 for a discard, a
theme for a cited record) are added; other existing tags are kept.  The
decision is marked as reviewed by a reader."""
import sys
from scholar.review import load_session, save_session, DecisionStatus, ReviewSource
CATS = ["supports-claim","qualifies-claim","adjacent-subtopic","off-topic-false-hit"]
XT = ["x1-new-scheme","x2-machine","x3-usability-only","x4-no-evidence","x5-other-question","x6-not-english"]
args = sys.argv[1:]; i = args.index("--")
name, cat, extra, ids = args[0], args[1], args[2:i], args[i+1:]
assert cat in CATS, cat
sess = load_session(name, strict=True)
decs = list(sess.decisions.values()) if isinstance(sess.decisions, dict) else list(sess.decisions)
byid = {d.paper.id: d for d in decs}
n = 0
for pid in ids:
    d = byid.get(pid)
    if d is None:
        print("not found:", pid); continue
    keep = [t for t in d.tags if t not in CATS and not (cat in ("supports-claim","qualifies-claim") and t in XT) and not (t in XT and any(e in XT for e in extra))]
    d.tags = [cat] + [t for t in extra if t not in keep] + keep
    d.status = DecisionStatus.KEPT if cat in ("supports-claim","qualifies-claim") else DecisionStatus.DISCARDED
    d.source = ReviewSource.LLM_REVIEWED if d.source != ReviewSource.HUMAN else ReviewSource.HUMAN
    n += 1
save_session(sess)
print(f"{name}: {n} record(s) set to {cat} {extra}")
