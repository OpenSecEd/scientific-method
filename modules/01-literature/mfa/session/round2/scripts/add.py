import json,subprocess,os,time,sys
S=os.path.dirname(os.path.abspath(__file__))
work=[w for w in json.load(open(S+'/worklist.json')) if w['provider']!='openalex']
for w in work:
    tag=f"{w['session']}-q{w['q']}-{w['provider']}"
    if os.path.exists(f"{S}/{tag}.added"): continue
    t=time.time()
    with open(f"{S}/{tag}.add.csv",'w') as o, open(f"{S}/{tag}.add.err",'w') as e:
        rc=subprocess.call(['scholar','search',w['query'],'-n',w['session'],'-p',w['provider'],'-l','0','-f','csv'],stdout=o,stderr=e)
    open(S+'/add.log','a').write(f"{tag}\trc={rc}\t{time.time()-t:.0f}s\n")
    if rc==0: open(f"{S}/{tag}.added",'w').write('ok')
