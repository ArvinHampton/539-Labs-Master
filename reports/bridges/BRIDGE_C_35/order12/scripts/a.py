# Route A
from common import *
import json
mp.mp.dps=25; M=Mmat(); A0=((2,7),(7,7))
sgn=lambda v:(v>0)-(v<0)
cE=lambda nu: Fr(1+sgn(nu[0])*sgn(nu[1]),2)
Ls=[(a,b,(35+b*b)//a) for b in range(-7,8) for a in range(1,43) if (35+b*b)%a==0 and (35+b*b)//a<=42]
assert len(Ls)==82
TT=T4+HO; c=lambda t:t/mp.sqrt(35)
def vecs(Amat,cone=None):
    tb=[tables(Amat,al,be,45,12,cone) for al,be in pairs]
    return {str(t):(mp.matrix([evalt(D,-1/t) for D in tb]),mp.matrix([evalt(D,t) for D in tb])) for t in TT}
VE=vecs(A0,cE); print('ThE done',flush=True)
VB=[]
for (a,b,cc) in Ls: VB.append(vecs(((a,b),(b,cc)))); print('A',a,b,cc,flush=True)
mx=lambda v:max(abs(x) for x in v)
chis={'i':1j,'-i':-1j,'1':1,'-1':-1}
R=lambda V,t,chi: V[str(t)][0]-chi*c(t)*(M*V[str(t)][1])
out={'A1':{},'A2':{}}
for (a,b,cc),V in zip(Ls,VB):
    out['A1'][str((a,b,cc))]={k:mp.nstr(max(mx(R(V,t,ch))/mx(V[str(t)][1]) for t in T4),3) for k,ch in chis.items()}
print(out['A1'],flush=True)
for k in ('i','-i'):
    ch=chis[k]; n=len(VB)
    # stack residual columns over T4
    cols=[[x for t in T4 for x in R(V,t,ch)] for V in VB]; rhs=[-x for t in T4 for x in R(VE,t,ch)]
    G=mp.matrix(n,n); bb=mp.matrix(n,1)
    for i in range(n):
        for j in range(i,n):
            G[i,j]=sum(mp.conj(p)*q for p,q in zip(cols[i],cols[j])); G[j,i]=mp.conj(G[i,j])
        bb[i]=sum(mp.conj(p)*q for p,q in zip(cols[i],rhs))
    x=mp.lu_solve(G,bb)
    def rr(ts): 
        return max(mx(R(VE,t,ch)+sum((x[i]*R(VB[i],t,ch) for i in range(n)),mp.matrix(105,1)))/mx(VE[str(t)][1]+sum((x[i]*VB[i][str(t)][1] for i in range(n)),mp.matrix(105,1))) for t in ts)
    r=rr(T4); rh=rr(HO)
    ver='pass' if (r<=1e-15 and rh<=1e-15) else ('FAIL' if r>=1e-4 else 'inconclusive')
    out['A2'][k]=dict(r=mp.nstr(r,4),r_holdout=mp.nstr(rh,4),xnorm=mp.nstr(max(abs(v) for v in x),4),verdict=ver); print(k,out['A2'][k],flush=True)
json.dump(out,open('../data/a.json','w'),indent=1)
