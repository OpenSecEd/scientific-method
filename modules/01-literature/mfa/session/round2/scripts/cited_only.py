"""Keep theme tags only on records that the report cites.

A record is cited if it is kept and its DOI, or else its title, is that of
an entry in the bibliography.  Theme tags on any other record are removed
(the classifier copies them from the session's vocabulary, and a run may
have tagged a record it then did not cite).  Extra tags named after
`--drop` are removed from every record.
Usage: cited_only.py <session> <bibfile> <theme> [<theme> ...] [--drop <tag> ...]"""
import re, sys, unicodedata
from scholar.review import load_session, save_session

def norm(t):
    t = unicodedata.normalize("NFKD", re.sub(r"[{}\\]", "", t or "")).lower()
    return re.sub(r"[^a-z0-9]+", " ", t).strip()

def fields(bib, name):
    out = []
    for m in re.finditer(r"(?mi)^\s*%s\s*=\s*\{" % name, bib):
        i = m.end(); depth = 1; j = i
        while depth and j < len(bib):
            depth += {"{": 1, "}": -1}.get(bib[j], 0); j += 1
        out.append(" ".join(bib[i:j - 1].split()))
    return out

a = sys.argv[1:]
drop = set()
if "--drop" in a:
    k = a.index("--drop"); drop = set(a[k + 1:]); a = a[:k]
name, bibfile, themes = a[0], a[1], set(a[2:])
bib = open(bibfile, encoding="utf-8").read()
dois = {d.lower() for d in fields(bib, "doi")}
titles = {norm(t)[:60] for t in fields(bib, "title")}
sess = load_session(name, strict=True)
decs = list(sess.decisions.values()) if isinstance(sess.decisions, dict) else list(sess.decisions)
stripped = kept = 0
for d in decs:
    if drop & set(d.tags):
        d.tags = [t for t in d.tags if t not in drop]
    if not themes & set(d.tags):
        continue
    cited = getattr(d.status, "value", d.status) == "kept" and (
        (d.paper.doi or "").lower() in dois or norm(d.paper.title)[:60] in titles)
    if cited:
        kept += 1
        print("  cited:", [t for t in d.tags if t in themes], (d.paper.title or "")[:70])
    else:
        d.tags = [t for t in d.tags if t not in themes]; stripped += 1
save_session(sess)
print(f"{name}: {kept} cited record(s) keep a theme; theme tags removed from {stripped} other(s)")
