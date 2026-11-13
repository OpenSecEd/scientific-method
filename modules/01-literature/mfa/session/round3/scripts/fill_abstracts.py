"""Add abstracts from OpenAlex to the PENDING records of a session that
have none (Scopus and IEEE give none here).  `scholar enrich` would go
through every record of the session, some 800 old ones included, and ran
out of time in the second round; this asks only for the pending ones, by
DOI, fifty to a request.  Usage: fill_abstracts.py <session>"""
import sys, time, pyalex
from scholar.providers import get_provider
from scholar.review import load_session, save_session
get_provider("openalex")            # sets up pyalex as scholar does
sess = load_session(sys.argv[1])
todo = [d for d in sess.decisions
        if getattr(d.status, "value", d.status) == "pending"
        and not (d.paper.abstract or "").strip() and d.paper.doi]
print("pending without abstract, with DOI:", len(todo))
by = {d.paper.doi.lower(): d for d in todo}
dois = list(by); got = 0
for i in range(0, len(dois), 50):
    chunk = dois[i:i + 50]
    for w in pyalex.Works().filter(doi="|".join(chunk)).get(per_page=100):
        a = w["abstract"]
        k = (w.get("doi") or "").lower().replace("https://doi.org/", "")
        if a and k in by:
            by[k].paper.abstract = a; got += 1
    time.sleep(1)
save_session(sess)
left = sum(1 for d in sess.decisions if getattr(d.status, "value", d.status) == "pending" and not (d.paper.abstract or "").strip())
print("abstracts added:", got, "| pending still without abstract:", left)
