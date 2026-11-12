"""Check every double-quoted passage in the QUOTE fields of a provenance .bib
against a corpus of extracted full texts (whitespace- and hyphenation-normalised).
usage: verify_quotes.py file.bib textdir [textdir...]"""
import sys,re,glob,os,unicodedata
def norm(s):
    s=unicodedata.normalize('NFKC',s)
    s=s.replace('­','')
    s=re.sub(r'-\s*\n\s*','',s)           # hyphenation at line end
    s=re.sub(r'[‘’‚`\']',"'",s); s=re.sub(r'[“”„"]','"',s)
    s=re.sub(r'[‐-―−]','-',s)
    s=re.sub(r'\s+',' ',s)
    return s.lower()
corpus={}
for d in sys.argv[2:]:
    for f in glob.glob(os.path.join(d,'*.txt'))+glob.glob(os.path.join(d,'*.html'))+glob.glob(os.path.join(d,'*.xml')):
        try: corpus[f]=norm(open(f,encoding='utf-8',errors='ignore').read())
        except Exception as e: pass
nohyph={f:t.replace('-','') for f,t in corpus.items()}
bib=open(sys.argv[1],encoding='utf-8').read()
blocks=re.split(r'(?m)^% === provenance: ',bib)[1:]
tot=ok=0
for b in blocks:
    key=b.split(' ',1)[0].strip()
    com='\n'.join(l[1:] for l in b.split('\n') if l.startswith('%'))
    m=re.search(r'QUOTE.*?(?=\n\s*(VERIFIED|COUNTER|DATE|PICKED|FOUND-VIA|CLAIM)\b)',com,re.S)
    abstract_only='ABSTRACT ONLY' in com.upper() or 'abstract only' in com.lower()
    if not m: print(f'{key}: NO QUOTE FIELD'); continue
    qs=re.findall(r'"((?:[^"\\]|\\.){25,})"',re.sub(r'\s+',' ',m.group(0)))
    for q in qs:
        tot+=1
        parts=[p for p in re.split(r'\s*\[?\.\.\.\]?\s*|\s*\[…\]\s*',q) if len(p)>20]
        hit=None
        for f,t in corpus.items():
            if all(norm(p) in t or norm(p).replace('-','') in nohyph[f] for p in parts): hit=f; break
        if hit: ok+=1
        print(f"{'OK  ' if hit else 'MISS'} {key}{' [abstract-only]' if abstract_only else ''}: {q[:90]}{'  <- '+os.path.basename(hit) if hit else ''}")
print(f'{ok}/{tot} quotes found')
