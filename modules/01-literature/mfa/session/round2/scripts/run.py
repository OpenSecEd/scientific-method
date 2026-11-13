import json,subprocess,sys,os,time
S=os.path.dirname(os.path.abspath(__file__)); prov=sys.argv[1]
work=[w for w in json.load(open(S+'/worklist.json')) if w['provider']==prov]
# the four searches that failed yesterday go first
work.sort(key=lambda w:(0 if w['status']!='capped' else 1))
for w in work:
    base=f"{S}/{w['session']}-q{w['q']}-{prov}"
    if os.path.exists(base+'.done'): continue
    t=time.time()
    with open(base+'.csv','w') as o, open(base+'.err','w') as e:
        rc=subprocess.call(['scholar','search',w['query'],'-p',prov,'-l','0','-f','csv'],stdout=o,stderr=e)
    n=sum(1 for l in open(base+'.csv',errors='ignore') if l.strip() and not l.startswith('#'))-1
    res=[l.strip() for l in open(base+'.csv',errors='ignore') if l.startswith('# Results')]
    open(S+'/log.tsv','a').write(f"{w['session']}\tq{w['q']}\t{prov}\t{w['status']}\trc={rc}\trows={n}\t{res[0] if res else ''}\t{time.time()-t:.0f}s\n")
    if rc==0: open(base+'.done','w').write('ok')
