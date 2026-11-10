# order26: controls, I1, RG17, RG17'. PREREG hashed first.
import sys, math, json, numpy as np
sys.dont_write_bytecode=True
from cornerlib import *
from symbols import S_rows
N=105; n=np.linalg.norm; k=1/math.sqrt(35)
d=np.load('/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order18/data/a2_arrays.npz'); CO,SCO=d['CO'],d['SCO']
G=np.zeros((N,N),complex)
for j,(al,be) in enumerate(pairs):
    ga=tuple(sum(Fr(int(g[r,c]))*al[c] for c in range(2)) for r in range(2)); gb=tuple(sum(Fr(int(g[r,c]))*be[c] for c in range(2)) for r in range(2))
    kk,e=reduce(ga,gb); G[j,kk]=np.exp(2j*np.pi*e/L)
M=np.zeros((N,N),complex)
for j,dd in enumerate(S_rows()):
    for kk,es in dd.items():
        for ee in es: M[j,kk]+=np.exp(2j*np.pi*ee/L)
vtx=np.array([1.0 if (Fr(al[0]).denominator==1 and Fr(al[1]).denominator==1) else 0.0 for al,be in pairs])
cones={'K':((1,0),(0,1)),'giK':((13,-2),(7,-1)),'B':((7,-1),(1,0))}
V={c:np.zeros_like(CO) for c in cones}; SV={c:np.zeros_like(CO) for c in cones}
for ix,x in enumerate(XS):
    for j,(al,be) in enumerate(pairs):
        for c,(u1,u2) in cones.items():
            V[c][ix,j]=corner(al,be,x,u1,u2); SV[c][ix,j]=corner(al,be,-1/x,u1,u2)
np.savez('../data/o26_arrays.npz',**{c:V[c] for c in V},**{'S'+c:SV[c] for c in SV})
xs=np.array([float(x) for x in XS])
def R(Y,SY): return SY-xs[:,None]*k*(Y@M.T)
Pm=(np.eye(N)-G)/2; out={}
out['C1']=float(max(np.abs(V['K']-CO).max(),np.abs(SV['K']-SCO).max()))
out['C2']=float(max(np.abs(CO@G.T-V['giK']).max(),np.abs(SCO@G.T-SV['giK']).max()))
D=V['giK']-V['K']; SD=SV['giK']-SV['K']; Ym,SYm=CO@Pm.T,SCO@Pm.T
out['C3']=float(max(np.abs(Ym+0.5*D).max(),np.abs(SYm+0.5*SD).max()))
RY=R(Ym,SYm); out['C4']=abs(float(n(RY))-52.0306)
es={}
for s in (1,-1):
    for t in (0,.25,-.25):
        es[f"s={s},t={t}"]=float(max(np.abs(D-s*V['B']-t*vtx).max(),np.abs(SD-s*SV['B']-t*vtx).max()))
mn=min(es.values()); nv=float(n(V['B'])/n(D))
X=np.stack([np.concatenate([V['B'].ravel(),SV['B'].ravel()]),np.tile(vtx,2*len(XS)).astype(complex)],1); y=np.concatenate([D.ravel(),SD.ravel()])
co,*_=np.linalg.lstsq(X,y,rcond=None); lsrel=float(n(y-X@co)/n(y))
out['I1']=dict(errors=es,min=mn,nonvac=nv,ls_coef=[str(c) for c in co],ls_relres=lsrel,verdict='vacuous' if nv<1e-3 else ('PASS' if mn<=1e-10 else ('FAIL' if mn>=1e-6 else 'inconclusive')))
RB=R(V['B'],SV['B']); PRB=RB@Pm.T; a=RY.ravel(); b=PRB.ravel()
beta=np.vdot(b,a)/np.vdot(b,b); res=float(n(a-beta*b)); r=res/float(n(a)); nv2=float(n(b)/n(a))
out['RG17']=dict(beta=str(beta),abs=res,r=r,nonvac=nv2,verdict='vacuous' if nv2<1e-3 else ('PASS' if r<=1e-6 else ('FAIL' if r>=0.1 else 'inconclusive')))
ab=float(n(RB)); rel=ab/float(n(SV['B'])); nv3=float(n(V['B'])/n(CO))
out['RG17p']=dict(abs=ab,rel=rel,nonvac=nv3,verdict='vacuous' if nv3<1e-3 else ('PASS' if ab<=1e-8 else ('FAIL' if rel>=1e-3 else 'inconclusive')))
print(json.dumps(out,indent=1)); json.dump(out,open('../data/o26.json','w'),indent=1)
