# order24: RG12, RG13. PREREG sha above.
import sys, math, json, numpy as np
sys.dont_write_bytecode=True
from cornerlib import *
from symbols import S_rows
d=np.load('/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order18/data/a2_arrays.npz'); CO,SCO=d['CO'],d['SCO']
def Gam(gm):
    G=np.zeros((105,105),complex)
    for j,(al,be) in enumerate(pairs):
        ga=tuple(sum(Fr(int(gm[r,c]))*al[c] for c in range(2)) for r in range(2)); gb=tuple(sum(Fr(int(gm[r,c]))*be[c] for c in range(2)) for r in range(2))
        k,e=reduce(ga,gb); G[j,k]=np.exp(2j*np.pi*e/L)
    return G
Gg=Gam(g); Ggi=Gam(gi)
M=np.zeros((105,105),complex)
for j,dd in enumerate(S_rows()):
    for kk,es in dd.items():
        for ee in es: M[j,kk]+=np.exp(2j*np.pi*ee/L)
cones={'K':((1,0),(0,1)),'gK':((-1,2),(-7,13)),'giK':((13,-2),(7,-1))}
V={c:np.zeros_like(CO) for c in cones}; SV={c:np.zeros_like(CO) for c in cones}
for ix,x in enumerate(XS):
    for j,(al,be) in enumerate(pairs):
        for c,(u1,u2) in cones.items():
            V[c][ix,j]=corner(al,be,x,u1,u2); SV[c][ix,j]=corner(al,be,-1/x,u1,u2)
    if ix%40==0: print('pt',ix,flush=True)
n=np.linalg.norm; out={}
out['C1']=float(max(np.abs(V['K']-CO).max(),np.abs(SV['K']-SCO).max()))
out['C2']=float(max(np.abs(CO@Gg.T-V['giK']).max(),np.abs(CO@Ggi.T-V['gK']).max(),np.abs(SCO@Gg.T-SV['giK']).max(),np.abs(SCO@Ggi.T-SV['gK']).max()))
out['C3_commutator']=float(np.abs(Gg@M-M@Gg).max())
xs=np.array([float(x) for x in XS]); k=1/math.sqrt(35)
def law(Y,SY,nonvac):
    P=xs[:,None]*k*(Y@M.T); a=float(n(SY-P)); s=float(n(SY)); kap=np.vdot(P,SY)/np.vdot(P,P)
    v='vacuous' if nonvac<1e-3 else ('PASS' if a<=1e-8 else ('FAIL' if a>=1e-3*s else 'inconclusive'))
    return dict(abs=a,norm=s,rel=a/s,fitted_rel=float(n(SY-kap*P)/s),kappa=[kap.real,kap.imag],nonvac=nonvac,verdict=v)
Avg=(V['gK']+V['K']+V['giK'])/3; SAvg=(SV['gK']+SV['K']+SV['giK'])/3
out['RG12']=law(Avg,SAvg,float(n(Avg-CO)/n(CO)))
D=V['giK']-V['K']; SD=SV['giK']-SV['K']
out['RG13']=law(D,SD,float(n(D)/n(CO)))
out['ref_CO']=law(CO,SCO,1.0)
np.savez('../data/o24_arrays.npz',**V,**{'S'+c:SV[c] for c in SV},Gg=Gg)
print(json.dumps(out,indent=1)); json.dump(out,open('../data/o24.json','w'),indent=1)
