# order23: RG9b corrected, RG11, RG10. PREREG sha e390d61b...
import sys, math, json, numpy as np
sys.dont_write_bytecode=True
from cornerlib import *
from symbols import S_rows
s=np.array([[-1,-7],[0,1]]); assert (s.T@A@s==A).all()
d=np.load('/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order18/data/a2_arrays.npz'); CO,SCO=d['CO'],d['SCO']
Gs=np.zeros((105,105),complex)
for j,(al,be) in enumerate(pairs):
    sa=tuple(sum(Fr(int(s[r,c]))*al[c] for c in range(2)) for r in range(2)); sb=tuple(sum(Fr(int(s[r,c]))*be[c] for c in range(2)) for r in range(2))
    k,e=reduce(sa,sb); Gs[j,k]=np.exp(2j*np.pi*e/L)
A0=np.load('/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order4b/data/A2.npz')['A0']
out={'C2':float(np.abs(A0@Gs.T-A0).max())}
Q0=np.zeros_like(CO); Cs=Q0.copy(); K1=Q0.copy(); K2=Q0.copy(); SQ0=Q0.copy(); SCs=Q0.copy(); vtx=np.zeros(105)
for j,(al,be) in enumerate(pairs): vtx[j]=1.0 if (Fr(al[0]).denominator==1 and Fr(al[1]).denominator==1) else 0.0
for ix,x in enumerate(XS):
    for j,(al,be) in enumerate(pairs):
        Q0[ix,j]=corner(al,be,x,(1,0),(0,1)); Cs[ix,j]=corner(al,be,x,(-1,0),(-7,1))
        K1[ix,j]=corner(al,be,x,(1,0),(1,1)); K2[ix,j]=corner(al,be,x,(1,1),(0,1))
        SQ0[ix,j]=corner(al,be,-1/x,(1,0),(0,1)); SCs[ix,j]=corner(al,be,-1/x,(-1,0),(-7,1))
    if ix%40==0: print('pt',ix,flush=True)
n=np.linalg.norm
out['C1']=float(max(np.abs(Q0-CO).max(),np.abs(SQ0-SCO).max()))
e=float(np.abs(K1+K2-0.25*vtx[None,:]-CO).max()); out['RG9b_corr']=dict(e=e,n_vertex_companions=int(vtx.sum()),verdict='PASS' if e<=1e-12 else ('FAIL' if e>=1e-9 else 'inconclusive'))
e11=float(np.abs(CO@Gs.T-Cs).max()); nu=float(n(CO@Gs.T-CO)/n(CO))
out['RG11']=dict(e=e11,nonvac=nu,verdict=('PASS' if nu>=1e-3 else 'vacuous') if e11<=1e-9 else ('FAIL' if e11>=1e-6 else 'inconclusive'))
M=np.zeros((105,105),complex)
for j,dd in enumerate(S_rows()):
    for kk,es in dd.items():
        for ee in es: M[j,kk]+=np.exp(2j*np.pi*ee/L)
xs=np.array([float(x) for x in XS]); U=Q0+Cs; SU=SQ0+SCs
Y=xs[:,None]*(U@M.T)/math.sqrt(35); a10=float(n(SU-Y)); nv=float(n(U)/n(CO))
kap=np.vdot(Y,SU)/np.vdot(Y,Y)
out['RG10']=dict(abs=a10,normSU=float(n(SU)),rel=a10/float(n(SU)),nonvac=nv,fitted_kappa=[kap.real,kap.imag],fitted_rel=float(n(SU-kap*Y)/n(SU)),
  verdict='vacuous' if nv<1e-3 else ('PASS' if a10<=1e-8 else ('FAIL' if a10>=1e-3*float(n(SU)) else 'inconclusive')))
np.savez('../data/o23_arrays.npz',U=U,SU=SU,Cs=Cs,K1=K1,K2=K2,Gs=Gs)
print(json.dumps(out,indent=1)); json.dump(out,open('../data/o23.json','w'),indent=1)
