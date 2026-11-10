import json
from itertools import combinations
from fractions import Fraction
from sympy import Matrix, kronecker_symbol
sg=lambda v:(v>0)-(v<0)
w2=lambda a,b,c: sg(a-b)+sg(b-c)+sg(c-a)
O=[21+9*j for j in range(539)]
tau=lambda x: x//21 if x<420 else 20+(x-420)//20
f=[tau(x) for x in O]; df=[f[i+1]-f[i] for i in range(538)]
TR=list(combinations(range(9),3)); SQ=list(combinations(range(9),2))
def gram_rank(vs):
    G=Matrix([[sum(x*y for x,y in zip(u,v)) for v in vs] for u in vs]); return G.rank()
def survive(I):
    tw=[];sad=[];twf=[]
    for i in I:
        for a,b,c in TR: w=w2(a,b,c); tw.append(w); sad.append(0); twf.append(w*f[i])
    for i in I:
        if i<538:
            for a,b in SQ: tw.append(0); sad.append(sg(a-b)*df[i]); twf.append(0)
    eta=[s-t for s,t in zip(sad,twf)]
    r2=gram_rank([tw,eta]); r3=gram_rank([tw,eta,sad])
    return dict(rank_tw_eta=r2,rank_with_sad=r3,survives=(r2==2 and r3==3))
R={'control_full':survive(range(539))}
R['fibres']={r:survive([i for i in range(539) if i%8==r]) for r in range(8)}
S={r for r in range(8) if R['fibres'][r]['survives']}
pred20={r for r in range(8) if int(kronecker_symbol(140,2*r+1))==1}
void=not R['control_full']['survives']
R['survival_set']=sorted(S); R['C20_predicted_set']=sorted(pred20)
R['C19']='VOID' if void else ('PASS' if S==set(range(8)) else 'FAIL')
R['C20']='VOID' if void else ('PASS' if S==pred20 else 'FAIL')
json.dump(R,open('data/b5.json','w'),indent=1); print(json.dumps(R))
