"""How complete are OpenAlex's abstracts?  For every record in the given
sessions whose abstract came from Web of Science (provider wos, abstract
present, DOI present), fetch the abstract OpenAlex holds for the same DOI
and compare lengths in words.  Reads the session files, changes nothing.
Usage: oa_abstracts.py <out.json> <session> [<session> ...]"""
import sys, json, os, time, collections, pyalex
from scholar.providers import get_provider
get_provider("openalex")
out = sys.argv[1]; rec = {}
for s in sys.argv[2:]:
    d = json.load(open(os.path.expanduser(f"~/.local/share/scholar/review_sessions/{s}.json")))
    for x in d["decisions"]:
        p = x["paper"]
        if x["provider"] == "wos" and (p.get("abstract") or "").strip() and p.get("doi"):
            rec[p["doi"].lower()] = len(p["abstract"].split())
dois = sorted(rec); oa = {}
for i in range(0, len(dois), 50):
    for w in pyalex.Works().filter(doi="|".join(dois[i:i + 50])).get(per_page=100):
        k = (w.get("doi") or "").lower().replace("https://doi.org/", "")
        a = w["abstract"]
        oa[k] = len(a.split()) if a else 0
    time.sleep(1)
rows = [{"doi": k, "wos": rec[k], "openalex": oa.get(k)} for k in dois]
json.dump(rows, open(out, "w"), indent=0)
def cls(r):
    if r["openalex"] is None: return "not in OpenAlex"
    if r["openalex"] == 0: return "no abstract"
    q = r["openalex"] / r["wos"]
    return "under half the length" if q < 0.5 else "half to nine tenths" if q < 0.9 else "complete"
tot = collections.Counter(cls(r) for r in rows)
print("records compared:", len(rows)); [print(f"  {k}: {v}") for k, v in tot.most_common()]
by = collections.defaultdict(collections.Counter)
for r in rows: by[r["doi"].split("/")[0]][cls(r)] += 1
for pre, c in sorted(by.items(), key=lambda kv: -sum(kv[1].values()))[:8]:
    print(pre, sum(c.values()), dict(c))
