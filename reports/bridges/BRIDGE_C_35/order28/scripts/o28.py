# order28: RG19 (lines), RG20 (non-automorph cones). PREREG hashed first.
import sys, math, json, numpy as np
sys.dont_write_bytecode=True
from cornerlib import *
from symbols import S_rows
N=105; n=np.linalg.norm; k=1/math.sqrt(35); out={}
d=np.load('/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order18/data/a2_arrays.npz'); CO,SCO,LN,SLN=d['CO'],d['SCO'],d['LN'],d['SLN']
Z=np.load('/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order27/data/o27_arrays.npz'); GCO,SGCO=Z['g^1h^0'],Z['Sg^1h^0']
M=np.zeros((N,N),complex)
for j,dd in enumerate(S_rows()):
    for kk,es in dd.items():
        for ee in es: M[j,kk]+=np.exp(2j*np.pi*ee/L)
xs=np.array([float(x) for x in XS])
def R(Y,SY): return SY-xs[:,None]*k*(Y@M.T)
stk=lambda Y,SY: np.concatenate([Y.ravel(),SY.ravel()])
Qw,_=np.linalg.qr(np.stack([stk(CO,SCO),stk(GCO,SGCO)],1))
def dist(Y,SY): v=stk(Y,SY); return float(n(v-Qw@(Qw.conj().T@v))/n(v))
def law(Y,SY,nm):
    dv=dist(Y,SY); a=float(n(R(Y,SY))); rel=a/float(n(SY))
    out[nm]=dict(nonvac_d=dv,abs=a,rel=rel,verdict='VACUOUS' if dv<=1e-3 else ('PASS' if a<=1e-8 else ('FAIL' if rel>=1e-3 else 'inconclusive')))
vtx=np.array([1.0 if (Fr(al[0]).denominator==1 and Fr(al[1]).denominator==1) else 0.0 for al,be in pairs])
cones={'K':((1,0),(0,1)),'K1':((1,0),(1,1)),'K2':((1,1),(0,1)),'J1':((7,-1),(20,-3)),'J2':((20,-3),(13,-2))}
V={};SV={}
for c,(u1,u2) in cones.items():
    V[c]=np.array([[corner(al,be,x,u1,u2) for (al,be) in pairs] for x in XS]); SV[c]=np.array([[corner(al,be,-1/x,u1,u2) for (al,be) in pairs] for x in XS])
np.savez('../data/o28_arrays.npz',**V,**{'S'+c:v for c,v in SV.items()})
out['C1']=float(max(np.abs(V['K']-CO).max(),np.abs(SV['K']-SCO).max()))
o25=json.load(open('../../order25/data/o25.json')); RCO=R(CO,SCO); out['C2_relerr']=abs(float(n(RCO))-o25['RG16']['R_total'])/o25['RG16']['R_total']
out['subdiv_K']=float(max(np.abs(V['K1']+V['K2']-CO-0.25*vtx).max(),np.abs(SV['K1']+SV['K2']-SCO-0.25*vtx).max()))
out['subdiv_J']=float(max(np.abs(V['J1']+V['J2']-GCO-0.25*vtx).max(),np.abs(SV['J1']+SV['J2']-SGCO-0.25*vtx).max()))
law(LN,SLN,'RG19_LN')
out['RG19_explain']=dict(R_A2=float(n(R(LN+CO,SLN+SCO))),R_CO=float(n(RCO)),cos_RLN_minusRCO=float(np.real(np.vdot(R(LN,SLN).ravel(),-RCO.ravel()))/(n(R(LN,SLN))*n(RCO)+1e-300)))
AK,SAK=V['K1']-V['K2'],SV['K1']-SV['K2']; AJ,SAJ=V['J1']-V['J2'],SV['J1']-SV['J2']
law(AK,SAK,'RG20_AK'); law(AJ,SAJ,'RG20_AJ')
for c in ('K1','K2','J1','J2'): law(V[c],SV[c],'RG20_'+c)
B=np.stack([R(AK,SAK).ravel(),R(AJ,SAJ).ravel(),R(LN,SLN).ravel()],1); y=RCO.ravel()
cf,*_=np.linalg.lstsq(B,y,rcond=None); out['RG20_explain']=dict(captured_fraction=float(1-n(y-B@cf)**2/n(y)**2),coef=[str(c) for c in cf])
out['RG20']=out['RG20_AK']['verdict']
print(json.dumps(out,indent=1)); json.dump(out,open('../data/o28.json','w'),indent=1)
