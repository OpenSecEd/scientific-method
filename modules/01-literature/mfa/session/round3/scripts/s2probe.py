"""Probe Semantic Scholar's two public search endpoints (no key) with
natural-language questions and report where one known paper ranks.
Usage: s2probe.py <outdir>.  Queries are fixed below, written before
any result was seen."""
import json, sys, time, urllib.parse, urllib.request, urllib.error
out = sys.argv[1]
Q = {
 "instruction": "whether multi-factor authentication (MFA) is necessary or sufficient for secure authentication of users",
 "threat-R8": "an attacker uses account recovery or a weaker fallback login to get around multi-factor authentication",
}
TARGET_DOI = "10.1145/3576915.3623180"; TARGET_ARXIV = "2306.09708"; TARGET_TITLE = "disabled mfa for you"
def get(url):
    for wait in (0, 20, 40, 80, 160, 240):
        time.sleep(wait)
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "literature-review-script"})
            return json.load(urllib.request.urlopen(req, timeout=60))
        except urllib.error.HTTPError as e:
            if e.code != 429: return {"error": f"HTTP {e.code}"}
        except Exception as e:
            return {"error": repr(e)}
    return {"error": "HTTP 429 after retries"}
for name, q in Q.items():
    qs = urllib.parse.quote(q)
    snip = get(f"https://api.semanticscholar.org/graph/v1/snippet/search?query={qs}&limit=1000")
    json.dump(snip, open(f"{out}/{name}-snippet.json", "w"))
    time.sleep(5)
    kw = get(f"https://api.semanticscholar.org/graph/v1/paper/search?query={qs}&limit=100&fields=title,year,externalIds")
    json.dump(kw, open(f"{out}/{name}-keyword.json", "w"))
    # paper-level ranking of the snippet results: first appearance of each paper
    papers = []
    for d in snip.get("data", []):
        p = d.get("paper", {})
        key = p.get("corpusId")
        if key not in [x[0] for x in papers]:
            papers.append((key, p.get("title"), d.get("score"), (d.get("snippet") or {}).get("snippetKind"), (d.get("snippet") or {}).get("text", "")[:300]))
    hit = [(i + 1, x) for i, x in enumerate(papers) if TARGET_TITLE in (x[1] or "").lower()]
    print(f"== {name}: snippet search: {len(snip.get('data', []))} snippets, {len(papers)} papers, error={snip.get('error')}")
    for i, x in hit: print(f"   TARGET at paper rank {i}: kind={x[3]} score={x[2]}\n   snippet: {x[4]}")
    for i, x in enumerate(papers[:10]): print(f"   {i+1:3d}. {x[1]}")
    kd = kw.get("data", [])
    kh = [i + 1 for i, p in enumerate(kd) if TARGET_TITLE in (p.get("title") or "").lower()]
    print(f"   keyword search: total={kw.get('total')} returned={len(kd)} error={kw.get('error')} TARGET rank={kh}")
    for i, p in enumerate(kd[:5]): print(f"   k{i+1}. {p.get('title')}")
    time.sleep(5)
