"""Remove theme tags from records that are not cited.  The classifier may
reuse a theme tag it finds in the session's vocabulary; only cited records
should carry one.  Usage:
  strip_themes.py <session> <theme> [<theme> ...] -- <cited doi> [<cited doi> ...]"""
import sys
from scholar.review import load_session, save_session
a = sys.argv[1:]; i = a.index("--")
name, themes, cited = a[0], set(a[1:i]), {d.lower() for d in a[i+1:]}
sess = load_session(name, strict=True)
decs = list(sess.decisions.values()) if isinstance(sess.decisions, dict) else list(sess.decisions)
n = 0
for d in decs:
    doi = (d.paper.doi or "").lower()
    if doi in cited: continue
    if any(t in themes for t in d.tags):
        d.tags = [t for t in d.tags if t not in themes]; n += 1
save_session(sess)
print(f"{name}: theme tags removed from {n} uncited record(s)")
