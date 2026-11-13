"""Recompute the last column of ../../asta-sources.md after the second round:
for each of Asta's 41 sources, whether it is cited in this review or how the
search sessions classified it (matched by DOI, or else by title).
Usage: asta_overlap.py <asta-sources.md> <mfa.bib>   (rewrites the file)"""
import json, os, re, sys, unicodedata, collections
def norm(t): return re.sub(r"[^a-z0-9]+", " ", unicodedata.normalize("NFKD", t or "").lower()).strip()[:70]
md, bibf = sys.argv[1], sys.argv[2]
bib = open(bibf, encoding="utf-8").read()
cut = bib.index("% Sources cited only in the appendix that compares")
bdois = {d.lower() for d in re.findall(r"(?mi)^\s*doi\s*=\s*\{([^}]+)\}", bib[:cut])}
cat = ["supports-claim", "qualifies-claim", "adjacent-subtopic", "off-topic-false-hit"]
idx = collections.defaultdict(set)
for s in ["effect", "attribution", "sufficient", "necessary", "method"]:
    d = json.load(open(os.path.expanduser(f"~/.local/share/scholar/review_sessions/mfa-{s}.json")))
    for x in d["decisions"]:
        p = x["paper"]; c = [t for t in x["tags"] if t in cat]
        xl = [t for t in x["tags"] if re.match(r"x\d-", t)]
        v = f"{s}: {c[0] if c else '?'}" + (f" ({xl[0]})" if xl else "")
        if p.get("doi"): idx["doi:" + p["doi"].lower()].add(v)
        idx["ti:" + norm(p.get("title"))].add(v)
out = []; n = collections.Counter()
for line in open(md, encoding="utf-8"):
    if line.startswith("| ") and not line.startswith("| Asta") and not line.startswith("|---"):
        f = [x.strip() for x in line.strip().strip("|").split("|")]
        doi, title, was = f[5], f[2], f[7]
        hit = idx.get("doi:" + doi.lower(), set()) | idx.get("ti:" + norm(title), set())
        if "cited" in was.lower() and doi.lower() in bdois or was.lower().startswith("cited"):
            new = was; n["cited"] += 1
        elif hit:
            new = "; ".join(sorted(hit)); n["returned, not cited"] += 1
            n["  of which bearing"] += any("supports" in h or "qualifies" in h for h in hit)
        else:
            new = "not in our records"; n["not returned"] += 1
        f[7] = new; line = "| " + " | ".join(f) + " |\n"
    out.append(line)
open(md, "w", encoding="utf-8").write("".join(out))
print(dict(n))
