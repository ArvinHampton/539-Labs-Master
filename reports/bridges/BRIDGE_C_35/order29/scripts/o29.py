# order29: RG21 (lines vs order17 law form), RG22 (Stern-Brocot alternating rule). PREREG hashed first.
import sys, math, json, numpy as np
sys.dont_write_bytecode=True
from cornerlib import *
from symbols import S_rows
N=105; n=np.linalg.norm; k=1/math.sqrt(35); out={}
d=np.load('/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order18/data/a2_arrays.npz'); CO,SCO,LN,SLN=d['CO'],d['SCO'],d['LN'],d['SLN']
Z=np.load('/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order27/data/o27_arrays.npz'); GCO,SGCO=Z['g^1h^0'],Z['Sg^1h^0']
P=np.zeros((N,N),complex)
for j,(al,be) in enumerate(pairs):
    kk,e=reduce((-al[0],-al[1]),(-be[0],-be[1])); P[j,kk]=np.exp(2j*np.pi*e/L)
M=np.zeros((N,N),complex)
for j,dd in enumerate(S_rows()):
    for kk,es in dd.items():
        for ee in es: M[j,kk]+=np.exp(2j*np.pi*ee/L)
xs=np.array([float(x) for x in XS])
def R(Y,SY): return SY-xs[:,None]*k*(Y@M.T)
stk=lambda Y,SY: np.concatenate([Y.ravel(),SY.ravel()])
Qw,_=np.linalg.qr(np.stack([stk(CO,SCO),stk(GCO,SGCO)],1))
def dist(Y,SY): v=stk(Y,SY); return float(n(v-Qw@(Qw.conj().T@v))/max(n(v),1e-300))
def law17(Y,S):
    res={}
    for w in (-1,-0.5,0,0.5,1):
        X=(xs**-w)[:,None]*k*(Y@M.T); den=np.vdot(X,X); kap=np.vdot(X,S)/den; a=float(n(S-kap*X)); res[str(w)]=dict(r=a/float(n(S)),abs=a,kappa=[kap.real,kap.imag])
    rmin=min(v['r'] for v in res.values()); return res,rmin
out['C1']=None
Pp=lambda Y:0.5*(Y+Y@P.T); Pm=lambda Y:0.5*(Y-Y@P.T)
for nm,(Y,S) in {'LN':(LN,SLN),'LN_plus':(Pp(LN),Pp(SLN)),'LN_minus':(Pm(LN),Pm(SLN)),'CO':(CO,SCO)}.items():
    res,rmin=law17(Y,S); dv=dist(Y,S); small=float(n(Y))<1e-6*float(n(LN))
    v='VACUOUS' if (nm!='CO' and (dv<=1e-3 or small)) else ('PASS' if rmin<=1e-8 else ('FAIL' if rmin>=1e-3 else 'inconclusive'))
    out['RG21_'+nm]=dict(weights=res,r_min=rmin,nonvac_d=dv,norm=float(n(Y)),verdict=v)
out['corner_only_isolated']=out['RG21_LN']['verdict']=='PASS' and out['RG21_CO']['verdict']=='FAIL'
# RG22
vtx=np.array([1.0 if (Fr(al[0]).denominator==1 and Fr(al[1]).denominator==1) else 0.0 for al,be in pairs])
rays=[(1,0),(0,1)]; cache={}
def cor(u1,u2):
    if (u1,u2) not in cache:
        cache[(u1,u2)]=(np.array([[corner(al,be,x,u1,u2) for (al,be) in pairs] for x in XS]),np.array([[corner(al,be,-1/x,u1,u2) for (al,be) in pairs] for x in XS]))
    return cache[(u1,u2)]
C=cor((1,0),(0,1)); out['C1']=float(max(np.abs(C[0]-CO).max(),np.abs(C[1]-SCO).max()))
RCO=R(CO,SCO); out['C2_relerr']=abs(float(n(RCO))-54.4056376674763)/54.4056376674763
for depth in (1,2,3):
    nr=[rays[0]]
    for a,b in zip(rays,rays[1:]): nr+=[(a[0]+b[0],a[1]+b[1]),b]
    rays=nr; cones=list(zip(rays,rays[1:]))
    Sm=np.zeros_like(CO); SSm=np.zeros_like(CO); Al=np.zeros_like(CO); SAl=np.zeros_like(CO)
    for i,(u1,u2) in enumerate(cones):
        V,SV=cor(u1,u2); Sm+=V; SSm+=SV; s=1 if i%2==0 else -1; Al+=s*V; SAl+=s*SV
    ctrl=float(max(np.abs(Sm-CO-0.25*(len(cones)-1)*vtx).max(),np.abs(SSm-SCO-0.25*(len(cones)-1)*vtx).max()))
    RA=R(Al,SAl); T=float(n(RCO+RA)); cs=float(abs(np.vdot(RA.ravel(),-RCO.ravel()))/(n(RA)*n(RCO)))
    dv=dist(Al,SAl)
    vT='VACUOUS' if dv<=1e-3 else ('PASS' if T<=1e-8 else ('FAIL' if T>=1e-3*float(n(RCO)) else 'inconclusive'))
    vC='VACUOUS' if dv<=1e-3 else ('PASS' if cs>=1-1e-6 else ('FAIL' if cs<=0.99 else 'inconclusive'))
    out[f'RG22_n{depth}']=dict(ncones=len(cones),subdiv_ctrl=ctrl,nonvac_d=dv,R_Alt=float(n(RA)),T_abs=T,T_rel=T/float(n(RCO)),cos=cs,verdict_T=vT,verdict_cos=vC)
    print(depth,out[f'RG22_n{depth}'],flush=True)
np.savez('../data/o29_cones.npz',**{f"{a}_{b}":v[0] for (a,b),v in cache.items()},**{f"S{a}_{b}":v[1] for (a,b),v in cache.items()})
print(json.dumps(out,indent=1)); json.dump(out,open('../data/o29.json','w'),indent=1)
