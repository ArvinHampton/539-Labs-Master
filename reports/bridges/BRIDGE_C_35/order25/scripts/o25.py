import sys, math, json, numpy as np
from collections import Counter
sys.dont_write_bytecode=True
from cornerlib import *
from symbols import S_rows
Sr=S_rows(); N=105
pi=[None]*N; gex=[None]*N
for j,(al,be) in enumerate(pairs):
    ga=tuple(sum(Fr(int(g[r,c]))*al[c] for c in range(2)) for r in range(2)); gb=tuple(sum(Fr(int(g[r,c]))*be[c] for c in range(2)) for r in range(2))
    pi[j],gex[j]=reduce(ga,gb)
E1=all(pi[pi[j]]==j and (gex[j]+gex[pi[j]])%L==0 for j in range(N))
inv=[None]*N
for j in range(N): inv[pi[j]]=j
bad=0
for j in range(N):
    for k in range(N):
        a=Counter((gex[j]+e)%L for e in Sr[pi[j]].get(k,[]))
        b=Counter((e+gex[inv[k]])%L for e in Sr[j].get(inv[k],[]))
        if a!=b: bad+=1
out={'E1':E1,'E2_multiset_mismatches':bad,'E2':bad==0}
G=np.zeros((N,N),complex)
for j in range(N): G[j,pi[j]]=np.exp(2j*np.pi*gex[j]/L)
M=np.zeros((N,N),complex)
for j,d in enumerate(Sr):
    for kk,es in d.items():
        for e in es: M[j,kk]+=np.exp(2j*np.pi*e/L)
d=np.load('/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order18/data/a2_arrays.npz'); CO,SCO=d['CO'],d['SCO']
Z=np.load('/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order24/data/o24_arrays.npz'); Dx=Z['giK']-Z['K']; SDx=Z['SgiK']-Z['SK']
Pp=(np.eye(N)+G)/2; Pm=(np.eye(N)-G)/2
xs=np.array([float(x) for x in XS]); n=np.linalg.norm; k=1/math.sqrt(35)
def R(Y,SY): return SY-xs[:,None]*k*(Y@M.T)
Ym,SYm=CO@Pm.T,SCO@Pm.T; Yp,SYp=CO@Pp.T,SCO@Pp.T
out['rankPp']=int(np.linalg.matrix_rank(Pp,1e-9)); out['rankPm']=int(np.linalg.matrix_rank(Pm,1e-9))
out['id_Ym_eq_mhalfD']=float(max(np.abs(Ym+0.5*Dx).max(),np.abs(SYm+0.5*SDx).max()))
out['anti_invariance']=float(np.abs(Ym@G.T+Ym).max())
a=float(n(R(Ym,SYm))); s=float(n(SYm)); nv=float(n(Ym)/n(CO))
out['RG15']=dict(abs=a,predicted=52.03,norm=s,rel=a/s,nonvac=nv,verdict='vacuous' if nv<1e-3 else ('PASS' if a<=1e-8 else ('FAIL' if a>=1e-3*s else 'inconclusive')))
rt=float(n(R(CO,SCO))); rp=float(n(R(Yp,SYp)))
share=a*a/rt**2; pyth=abs(rt**2-a*a-rp*rp)/rt**2
out['RG16']=dict(R_total=rt,R_plus=rp,R_minus=a,share_minus=share,pythagoras_relerr=pyth,verdict='PASS' if (share>=0.5 and pyth<=1e-9) else ('FAIL' if share<0.5 else 'inconclusive'))
print(json.dumps(out,indent=1)); json.dump(out,open('../data/o25.json','w'),indent=1)
