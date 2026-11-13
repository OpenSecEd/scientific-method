"""Add to each session the OpenAlex records that match its queries in title
or abstract.  scholar's OpenAlex provider searches the full text; here its
query builder is replaced by OpenAlex's title_and_abstract.search filter, and
everything else (paging, conversion, session merge, saving) is scholar's own
code.  The search is recorded in the session under the query string prefixed
with "title_and_abstract.search:"."""
import sys, json, os, datetime, time
import pyalex
from scholar.providers import get_provider
from scholar.scholar import SearchResult
from scholar.review import create_review_session, save_session
S = os.path.dirname(os.path.abspath(__file__))
only = sys.argv[1:]  # session names; empty = all
prov = get_provider("openalex")
prov._base_query = lambda q: pyalex.Works().filter(title_and_abstract={"search": q})
work = [w for w in json.load(open(S + "/worklist.json")) if w["provider"] == "openalex" and (not only or w["session"] in only)]
for w in work:
    tag = f"{w['session']}-q{w['q']}-openalex-ta"
    if os.path.exists(f"{S}/{tag}.added"):
        continue
    t = time.time()
    prov.last_error = None
    papers = prov._search_uncached(w["query"], 10**9, None)
    label = "title_and_abstract.search:" + w["query"]
    res = SearchResult(query=label, provider="openalex",
                       timestamp=datetime.datetime.now().isoformat(),
                       papers=papers, filters=None, limit=10**9,
                       error=prov.last_error)
    session = create_review_session([res], label, session_name=w["session"])
    save_session(session)
    line = f"{tag}\thits={len(papers)}\terror={prov.last_error}\tsession={len(session.decisions)}\tpending={len(session.pending_papers())}\t{time.time()-t:.0f}s"
    print(line, flush=True)
    open(S + "/oa_ta.log", "a").write(line + "\n")
    if not prov.last_error:
        open(f"{S}/{tag}.added", "w").write("ok")
