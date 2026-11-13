"""Copy a session export (CSV) without the abstract column.
The abstracts belong to the databases; every record keeps its DOI or URL.
Usage: strip_abstracts.py <export.csv> <copy.csv>"""
import csv, sys
src, dst = sys.argv[1], sys.argv[2]
with open(src, newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
cols = [c for c in rows[0].keys() if c != "abstract"]
with open(dst, "w", newline="", encoding="utf-8") as f:
    f.write("# Abstracts removed from this copy (they belong to the databases); "
            "every record keeps its DOI or URL.\n")
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
    w.writeheader(); w.writerows(rows)
print(dst, len(rows), "records")
