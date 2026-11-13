"""Ask OpenAlex's search by meaning (search.semantic: embeddings of title
and abstract, at most 50 results) two questions in plain language, and
report (a) where one known paper ranks and (b) how our own screening had
classified each of the works returned.  The questions were fixed before
any result was seen.  Reads the sessions, changes nothing.
Usage: oa_semantic.py <outdir>"""
import sys, json, os, re, time, unicodedata, collections, requests, pyalex
from scholar.providers import get_provider
get_provider("openalex")
out = sys.argv[1]
Q = {
 "instruction": "whether multi-factor authentication (MFA) is necessary or sufficient for secure authentication of users",
 "threat-R8": "an attacker uses account recovery or a weaker fallback login to get around multi-factor authentication",
}
TARGET = "10.1145/3576915.3623180"
def norm(t): return re.sub(r"[^a-z0-9]+", " ", unicodedata.normalize("NFKD", t or "").lower()).strip()[:70]
cats = ["supports-claim", "qualifies-claim", "adjacent-subtopic", "off-topic-false-hit"]
idx = collections.defaultdict(set)
for s in ["effect", "attribution", "sufficient", "necessary"]:
    d = json.load(open(os.path.expanduser(f"~/.local/share/scholar/review_sessions/mfa-{s}.json")))
    for x in d["decisions"]:
        c = [t for t in x["tags"] if t in cats]
        v = c[0] if c else "?"
        if x["paper"].get("doi"): idx["doi:" + x["paper"]["doi"].lower()].add(v)
        idx["ti:" + norm(x["paper"].get("title"))].add(v)
for name, q in Q.items():
    p = {"search.semantic": q, "per_page": 50, "select": "id,doi,title,publication_year,relevance_score"}
    if pyalex.config.api_key: p["api_key"] = pyalex.config.api_key
    r = requests.get("https://api.openalex.org/works", params=p, timeout=60)
    if r.status_code != 200:
        print(name, "FAILED: HTTP", r.status_code, r.text[:200].replace(pyalex.config.api_key or "#", "KEY")); continue
    res = r.json()["results"]
    json.dump(res, open(f"{out}/{name}.json", "w"), indent=0)
    tally = collections.Counter(); rank = None
    rows = []
    for i, w in enumerate(res, 1):
        doi = (w.get("doi") or "").lower().replace("https://doi.org/", "")
        hit = idx.get("doi:" + doi, set()) | idx.get("ti:" + norm(w.get("title")), set())
        cl = ("bearing" if hit & {"supports-claim", "qualifies-claim"} else "adjacent" if "adjacent-subtopic" in hit
              else "another topic" if hit else "not in our records")
        tally[cl] += 1
        if doi == TARGET or "disabled mfa for you" in (w.get("title") or "").lower(): rank = rank or i
        rows.append(f"{i:2d} {cl:18s} {w.get('publication_year')} {(w.get('title') or '')[:95]}")
    print(f"== {name}: {len(res)} results; known paper at rank {rank}; our classification of the results: {dict(tally)}")
    open(f"{out}/{name}.txt", "w").write("\n".join(rows) + "\n")
    print("\n".join(rows[:12]))
    time.sleep(2)
