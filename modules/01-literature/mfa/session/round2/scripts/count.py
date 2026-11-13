import csv,io,glob,json,os,re,sys,unicodedata,collections
S=os.path.dirname(os.path.abspath(__file__))
def norm(t): return re.sub(r'[^a-z0-9]+',' ',unicodedata.normalize('NFKD',t or '').lower()).strip()[:90]
def key(r):
    d=(r.get('doi') or '').lower().strip()
    return 'doi:'+d if d else 'ti:'+norm(r.get('title'))
old={}
for s in ['effect','attribution','sufficient','necessary','method']:
    d=json.load(open(os.path.expanduser(f'~/.local/share/scholar/review_sessions/mfa-{s}.json')))
    ks=set()
    for dec in d['decisions']:
        p=dec.get('paper') or {}
        ks.add(key(p)); ks.add('ti:'+norm(p.get('title')))
    old[s]=ks
tot=collections.defaultdict(dict); new=collections.defaultdict(lambda: collections.defaultdict(set)); allrec=collections.defaultdict(set)
log={}
for l in open(S+'/log.tsv'):
    f=l.rstrip('\n').split('\t'); log[(f[0],f[1],f[2])]=f
for (sess,q,prov),f in sorted(log.items()):
    s=sess[4:]; path=f"{S}/{sess}-{q}-{prov}.csv"
    rows=[x for x in open(path,encoding='utf-8',errors='ignore') if x.strip() and not x.startswith('#')]
    rd=list(csv.DictReader(io.StringIO(''.join(rows)),delimiter='\t'))
    tot[s][(q,prov)]=len(rd)
    for r in rd:
        k=key(r); kt='ti:'+norm(r.get('title'))
        allrec[(s,prov=='openalex')].add(k)
        if k not in old[s] and kt not in old[s]: new[s][prov=='openalex'].add(k)
for s in ['effect','attribution','sufficient','necessary','method']:
    cells=tot[s]
    print(f"== {s}: cells done {len(cells)}")
    for (q,prov),n in sorted(cells.items()): print(f"     {q} {prov:9} {n}")
    nonoa=new[s][False]; oa=new[s][True]
    print(f"   new records not in yesterday's session: other databases {len(nonoa)}; OpenAlex {len(oa)} (of which also in other dbs {len(oa&nonoa)}); union {len(oa|nonoa)}")
