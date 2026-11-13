import json, os, sys
d = json.load(open(os.path.expanduser(f"~/.local/share/scholar/review_sessions/{sys.argv[1]}.json")))
print(sum(1 for x in d["decisions"] if x["status"] == "pending"))
