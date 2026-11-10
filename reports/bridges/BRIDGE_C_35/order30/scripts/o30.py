# order30: RG23 (arc-length weights), RG24 (uniform SB average). PREREG hashed first.
import sys, math, json, numpy as np
sys.dont_write_bytecode=True
from cornerlib import *
from symbols import S_rows
N=105; n=np.linalg.norm; k=1/math.sqrt(35); out={}
d=np.load('/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order18/data/a2_arrays.npz'); CO,SCO=d['CO'],d['SCO']
Z=np.load('/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order27/data/o27_arrays.npz'); GCO,SGCO=Z['g^1h^0'],Z['Sg^1h^0']
M=np.zeros((N,N),complex)
for j,dd in enumerate(S_rows()):
    for kk,es in dd.items():
        for ee in es: M[j,kk]+=np.exp(2j*np.pi*ee/L)
xs=np.array([float(x) for x in XS])
def R(Y,SY): return SY-xs[:,None]*k*(Y@M.T)
stk=lambda Y,SY: np.concatenate([Y.ravel(),SY.ravel()])
Qw,_=np.linalg.qr(np.stack([stk(CO,SCO),stk(GCO,SGCO)],1))
def dist(Y,SY): v=stk(Y,SY); return float(n(v-Qw@(Qw.conj().T@v))/max(n(v),1e-300))
def nearlaw(Y,S):
    X=xs[:,None]*k*(Y@M.T); kap=np.vdot(X,S)/np.vdot(X,X); return float(n(S-kap*X)/n(S)),[kap.real,kap.imag]
Am=np.array([[2,7],[7,7]]); Qf=lambda u: 0.5*np.array(u)@Am@np.array(u)
ell=lambda u,v: math.acosh((np.array(u)@Am@np.array(v))/(2*math.sqrt(Qf(u)*Qf(v))))
Larc=0.5*math.log(6+math.sqrt(35))
vtx=np.array([1.0 if (Fr(al[0]).denominator==1 and Fr(al[1]).denominator==1) else 0.0 for al,be in pairs])
cache={}
def cor(u1,u2):
    if (u1,u2) not in cache:
        cache[(u1,u2)]=(np.array([[corner(al,be,x,u1,u2) for (al,be) in pairs] for x in XS]),np.array([[corner(al,be,-1/x,u1,u2) for (al,be) in pairs] for x in XS]))
    return cache[(u1,u2)]
C=cor((1,0),(0,1)); out['C1']=float(max(np.abs(C[0]-CO).max(),np.abs(C[1]-SCO).max()))
RCO=R(CO,SCO); nR=float(n(RCO)); out['C2_relerr']=abs(nR-54.4056376674763)/54.4056376674763
out['L_check']=abs(ell((1,0),(0,1))-Larc)
rays=[(1,0),(0,1)]; rg23={}; rg24={}
for depth in (1,2,3,4):
    nr=[rays[0]]
    for a,b in zip(rays,rays[1:]): nr+=[(a[0]+b[0],a[1]+b[1]),b]
    rays=nr; cones=list(zip(rays,rays[1:]))
    ls=[ell(u,v) for u,v in cones]
    Sm=np.zeros_like(CO); SSm=Sm.copy(); Wn=Sm.copy(); SWn=Sm.copy()
    for (u1,u2),l in zip(cones,ls):
        V,SV=cor(u1,u2); Sm+=V; SSm+=SV; Wn+=l/Larc*V; SWn+=l/Larc*SV
    C3=float(max(np.abs(Sm-CO-0.25*(len(cones)-1)*vtx).max(),np.abs(SSm-SCO-0.25*(len(cones)-1)*vtx).max())); C4=abs(sum(ls)-Larc)
    RW=R(Wn,SWn); e=float(n(RCO+RW))/nR; c=float(abs(np.vdot(RW.ravel(),-RCO.ravel()))/(n(RW)*nR))
    lam=-np.vdot(RW.ravel(),RCO.ravel())/np.vdot(RW.ravel(),RW.ravel()); s=float(n(RCO+lam*RW))/nR
    rg23[depth]=dict(ncones=len(cones),C3=C3,C4=C4,weights_minmax=[min(ls)/Larc,max(ls)/Larc],nonvac_d=dist(Wn,SWn),R_W=float(n(RW)),e=e,cos=c,s=s,lam=[lam.real,lam.imag],nearlaw_W=nearlaw(Wn,SWn))
    U,SU=Sm/len(cones),SSm/len(cones); D,SD=CO-U,SCO-SU
    rg24[depth]=dict(t=float(n(R(D,SD)))/nR,nonvac_d=dist(D,SD),nearlaw_U=nearlaw(U,SU))
    print(depth,rg23[depth],rg24[depth],flush=True)
e=[rg23[i]['e'] for i in (1,2,3,4)]
v23='VACUOUS' if min(r['nonvac_d'] for r in rg23.values())<=1e-3 else ('PASS' if (e[3]<=1e-6 or rg23[4]['cos']>=1-1e-6) else ('FAIL' if (e[3]>=0.1 and rg23[4]['cos']<=0.99) else 'inconclusive'))
out['RG23']=dict(per_depth=rg23,divergence_flag=bool(e[1]<e[2]<e[3]),verdict=v23)
t4=rg24[4]['t']; out['RG24']=dict(per_depth=rg24,verdict='VACUOUS' if rg24[4]['nonvac_d']<=1e-3 else ('PASS' if t4<=1e-6 else ('FAIL' if t4>=0.1 else 'inconclusive')))
out['CO_nearlaw']=nearlaw(CO,SCO)
np.savez('../data/o30_cones.npz',**{f"{a}_{b}":v[0] for (a,b),v in cache.items()},**{f"S{a}_{b}":v[1] for (a,b),v in cache.items()})
print(json.dumps(out,indent=1)); json.dump(out,open('../data/o30.json','w'),indent=1)
