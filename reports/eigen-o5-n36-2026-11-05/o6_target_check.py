# O6: exact check of corpus §2.1 example over Z[Z/3], all targets; and grep source for a stated target.
import re,hashlib
P='/workspace/quantum-comp/reports/539labs/539_Labs_Technical_Corpus.md'
b=open(P,'rb').read(); print('corpus sha256',hashlib.sha256(b).hexdigest())
L=b.decode().splitlines(); sec=L[18:29]
hits=[(19+i,l) for i,l in enumerate(sec) if re.search(r'target|state \[|at \[',l,re.I)]
print('lines 19-29 mentioning a target state:',hits or 'NONE')
h1={0:1,1:1}; h2={0:-1,1:1,2:3}
for t in range(3):
    paths=[(a,c,h1[a]*h2[c]) for a in h1 for c in h2 if (a+c)%3==t]
    print('target',t,'W',sum(w for*_,w in paths),'N',sum(abs(w) for*_,w in paths),paths)
