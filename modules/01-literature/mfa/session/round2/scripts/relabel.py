"""Give every discarded 'adjacent-subtopic' record in a session the label of
the exclusion criterion that applies (x1..x6), using the same language model
that classified the records.  Only a tag is added: status, source and
confidence of the decision are left as they are."""
import sys, json, re, time
import llm
from scholar.review import load_session, save_session
CRIT = """Exclusion criteria (give exactly one tag per record):
x1-new-scheme: proposes a new authentication scheme, protocol or system and offers only its own security argument or evaluation for it.
x2-machine: concerns authentication between machines or devices with no human user (IoT devices, sensors, vehicles, networks).
x3-usability-only: studies only the usability, adoption, perception or deployment of authentication and reports nothing about security outcomes.
x4-no-evidence: an opinion, overview, tutorial, recommendation or review without evidence of its own or a stated method.
x5-other-question: concerns the authentication of human users, with evidence, but does not bear on the question below (another aspect or another question).
x6-not-english: not written in English."""
XT = ["x1-new-scheme","x2-machine","x3-usability-only","x4-no-evidence","x5-other-question","x6-not-english"]
name, question = sys.argv[1], sys.argv[2]
model = llm.get_model("anthropic/claude-sonnet-5-5")
sess = load_session(name, strict=True)
todo = [d for d in sess.decisions.values() if d.status.value == "discarded" and "adjacent-subtopic" in d.tags and not any(t in XT for t in d.tags)] if isinstance(sess.decisions, dict) else [d for d in sess.decisions if d.status.value == "discarded" and "adjacent-subtopic" in d.tags and not any(t in XT for t in d.tags)]
print(name, "to label:", len(todo), flush=True)
B = 25; done = 0; counts = {}
for i in range(0, len(todo), B):
    batch = todo[i:i+B]
    items = "\n".join(f"[{j}] {d.paper.title}\n    {(d.paper.abstract or '(no abstract)')[:500]}" for j, d in enumerate(batch))
    prompt = (f"A literature review asks: {question}\nThe records below were screened and found NOT to bear on that question as evidence. "
              f"For each, say which exclusion criterion applies.\n\n{CRIT}\n\nRecords:\n{items}\n\n"
              "Answer with a JSON list only, one object per record in order: [{\"i\": 0, \"tag\": \"x1-new-scheme\"}, ...]")
    for attempt in range(3):
        try:
            txt = model.prompt(prompt).text()
            arr = json.loads(re.search(r"\[.*\]", txt, re.S).group(0))
            got = {int(o["i"]): o["tag"] for o in arr if o.get("tag") in XT}
            if len(got) >= len(batch) - 1: break
        except Exception as e:
            got = {}; time.sleep(3)
    for j, d in enumerate(batch):
        t = got.get(j)
        if t:
            d.add_tag(t); counts[t] = counts.get(t, 0) + 1; done += 1
    if (i // B) % 8 == 7:
        save_session(sess); print("  ...", done, flush=True)
save_session(sess)
print(name, "labelled", done, "of", len(todo), counts, flush=True)
