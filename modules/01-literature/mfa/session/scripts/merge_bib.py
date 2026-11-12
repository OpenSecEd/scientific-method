import re,sys
S=sys.argv[1]; OUT=sys.argv[2]
MAP={
 'effect':{'meyer2023':'Meyer2023MFAEffect','doerfler2019':'Doerfler2019LoginChallenges','kamar2026':'Kamar2026TwoFactorBanks','kawase2019':'Kawase2019AccountTakeover','egenti2026':'Egenti2026Nigeria','wang2024':'Wang2024SimpleNotSecure','campobasso2020':'Campobasso2020IMPaaS','mirian2019':'Mirian2019HackForHire','catalano2025':'Catalano2025BitM','google2022':'Google2022SaferInternet','maynes2019':'Maynes2019OneSimpleAction'},
 'attribution':{'nist2025sp80063b4':'NIST2025SP80063B','w3c2026webauthn3':'W3C2026WebAuthn3','ncsc2026fido2':'NCSC2026CredentialsPaper','cisa2022phishres':'CISA2022PhishingResistant','yadav2024local':'Yadav2024LocalAttacks','buttner2025devicebound':'Buttner2025DeviceBound','berladskyy2026attack':'Berladskyy2026AttackVectors','mitra2026trust':'Mitra2026TrustBoundary','jacomme2021formal':'Jacomme2021FormalMFA','guan2022formal':'Guan2022FormalFIDO2','buttner2025inconsistencies':'Buttner2025Inconsistencies','gautam2025secret':'Gautam2025Secret','barbosa2023rogue':'Barbosa2023RogueKey','lee2025windowshello':'Lee2025WindowsHello','mahdad2024fidola':'Mahdad2024FIDOLA','mahdad2023sok':'Mahdad2023SoK2FA','alqubaisi2020rush':'AlQubaisi2020Rush','wasser2026resilience':None,'wang2025illusion':'Wang2025TwoFAIllusion','jubur2021hiena':'Jubur2021PushBypass'},
 'sufficient':{'Wang2024Simple':'Wang2024SimpleNotSecure','Barbosa2021FIDO2':'Barbosa2021ProvableFIDO2','Bindel2023FIDO2':'Bindel2023ProvableFIDO2','Doerfler2019Challenges':'Doerfler2019LoginChallenges','Yadav2023Local':'Yadav2024LocalAttacks','Berladskyy2026Vectors':'Berladskyy2026AttackVectors','Mitra2026Trust':'Mitra2026TrustBoundary','Mitra2026Wooden':'Mitra2026WoodenHorse','Wasser2026Resilience':None},
 'necessary':{'Temoshok2025':'NIST2025SP80063B','Wiefling2022':'Wiefling2022PumpUp','Wiefling2019':'Wiefling2019ReallyYou','Makowski2023':'Makowski2023RBA','Campobasso2020':'Campobasso2020IMPaaS','Lin2022':'Lin2022PhishSheep','Spooren2015':'Spooren2015Fingerprinting','Buettner2024':'Buttner2024Recovery','Berladskyy2026':'Berladskyy2026AttackVectors','Buettner2025':'Buttner2025DeviceBound','Kunke2021':'Kunke2021Recovery','Catalano2025':'Catalano2025BitM','Mahdad2024':'Mahdad2024FIDOLA','Lee2025':'Lee2025WindowsHello','Jacomme2021':'Jacomme2021FormalMFA','Kamar2026':'Kamar2026TwoFactorBanks','Holthouse2025':'Holthouse2025TwentyThreeAndMe','NISTcswp4':'NIST2016PIVPrivileged','Cocheo2006':None,'CISA2022':'CISA2022PhishingResistant','OMB2022':'OMB2022ZeroTrust','NCSC2026paper':'NCSC2026CredentialsPaper','NCSC2026blog':'NCSC2026PasskeysBlog','NCSC2026page':'NCSC2026PasskeysPage','NCSC2026methods':'NCSC2026Methods'},
}
PREF={'NIST2025SP80063B':'attribution','Yadav2024LocalAttacks':'attribution','Doerfler2019LoginChallenges':'effect','NCSC2026CredentialsPaper':'attribution'}
ORDER=['effect','attribution','sufficient','necessary']
QNAME={'effect':'effect (RQ1)','attribution':'attribution (RQ2)','sufficient':'sufficiency (RQ3)','necessary':'necessity (RQ4)'}
def parse(path):
    lines=open(path,encoding='utf-8').read().split('\n'); out=[]; i=0; n=len(lines)
    while i<n:
        if re.match(r'^\s*@\w+\s*\{',lines[i]):
            j=i; depth=0
            while j<n:
                depth+=lines[j].count('{')-lines[j].count('}'); 
                if depth<=0 and j>=i: break
                j+=1
            entry=lines[i:j+1]
            k=i-1; blk=[]
            while k>=0 and lines[k].strip()=='' : k-=1
            while k>=0 and lines[k].lstrip().startswith('%'): blk.append(lines[k]); k-=1
            blk.reverse()
            key=re.match(r'^\s*@\w+\s*\{\s*([^,\s]+)',lines[i]).group(1)
            out.append((key,blk,entry)); i=j+1
        else: i+=1
    return out
merged={}; seq=[]; dropped=[]
for s in ORDER:
    for key,blk,entry in parse(f'{S}/mfa-{s}/mfa-{s}.bib'):
        new=MAP[s].get(key,key)
        if new is None: dropped.append((s,key)); continue
        if new not in merged: merged[new]={'uses':[]}; seq.append((s,new))
        merged[new]['uses'].append((s,blk,entry))
chunks=[]
cur=None
for s,new in seq:
    uses=merged[new]['uses']
    pref=PREF.get(new)
    uses.sort(key=lambda u:(0 if u[0]==pref else 1, ORDER.index(u[0])))
    if s!=cur:
        chunks.append('% '+'='*67+f"\n% Sources first cited for the question on {QNAME[s]}\n% "+'='*67+'\n'); cur=s
    lines=[f'% === provenance: {new} ===']
    for idx,(us,blk,entry) in enumerate(uses):
        body=[l for l in blk if not re.match(r'^\s*%\s*=+\s*provenance',l,re.I)]
        if len(uses)>1: lines.append(f'% --- use {idx+1} of {len(uses)}: question on {QNAME[us]} ---')
        lines+=body
    e=list(uses[0][2]); e[0]=re.sub(r'\{\s*[^,\s]+',('{'+new),e[0],count=1)
    chunks.append('\n'.join(lines+e)+'\n')
open(OUT,'w',encoding='utf-8').write('\n'.join(chunks))
print(len(seq),'entries; dropped:',dropped)
