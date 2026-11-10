# order19: L0 (affine law, c=0 exact), C0, Map RG5. PREREG sha c4a157be...
import sys, json, math, numpy as np
sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order2/scripts')
from lib2 import XS, phase_ints, Fr
from symbols import FAM, sym_pair, S_rows, L
pairs=[sym_pair(f,i) for f in FAM for i in range(35)]
def B1b(u): u=Fr(u)%1; return 0.0 if u==0 else float(u)-0.5
def B2(u): u=float(Fr(u)%1); return u*u-u+1/6
def period(al,be,x,u):
    N=2*Fr(x).denominator
    for mult in (1,2,5,7,10,14,35,70):
        P=N*mult; j=np.arange(P); pts=j[:,None]*np.array(u)[None,:]
        k1,_=phase_ints(al,be,x,pts); k2,_=phase_ints(al,be,x,pts+P*np.array(u))
        if (k1==k2).all(): return P
    raise RuntimeError
def comps(al,be,x):
    N=math.lcm(period(al,be,x,(1,0)),period(al,be,x,(0,1)))
    i=np.arange(N); V=np.stack(np.meshgrid(i,i,indexing='ij'),-1).reshape(-1,2)
    k0,M=phase_ints(al,be,x,V); f=np.exp(2j*np.pi*k0/M).reshape(N,N)
    a1,a2=Fr(al[0]),Fr(al[1])
    b1=np.array([B1b((a1+n)/N) for n in i]); b2=np.array([B1b((a2+n)/N) for n in i])
    c1=np.array([B2((a1+n)/N) for n in i]); c2=np.array([B2((a2+n)/N) for n in i])
    return np.einsum('ij,i,j->',f,b1,b2), np.einsum('ij,i->',f,c1), np.einsum('ij,j->',f,c2)
M=np.zeros((105,105),complex)
for j,dct in enumerate(S_rows()):
    for k,es in dct.items():
        for e in es: M[j,k]+=np.exp(2j*np.pi*e/L)
k=1/math.sqrt(35); n=np.linalg.norm
D=np.load('/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order4b/data/A2.npz')
X=np.load('/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order18/data/a2_arrays.npz')
xs=np.array([float(x) for x in XS]); out={}
c0=n(D['S_A0']-(1/xs)[:,None]*k*(D['A0']@M.T)); out['C0']=dict(abs=float(c0),verdict='PASS' if c0<=1e-10 else 'VOID')
A=D['A2']-X['LN']; S=D['S_A2']-X['SLN']
R=S-xs[:,None]*k*(A@M.T); a=n(R)
out['L0']=dict(abs=float(a),rel=float(a/n(S)),normS=float(n(S)),verdict='PASS' if a<=1e-9 else ('FAIL' if a>=1e-4 else 'inconclusive'))
print(out,flush=True)
C=np.zeros((3,216,105),complex); SC=C.copy()
for ix,x in enumerate(XS):
    for j,(al,be) in enumerate(pairs):
        C[:,ix,j]=comps(al,be,x); SC[:,ix,j]=comps(al,be,-1/x)
np.savez('../data/rg5_arrays.npz',C=C,SC=SC)
chk=n(C[0]+0.5*C[1]+1.75*C[2]-X['CO']); out['corner_recon_abs']=float(chk)
rg=[]
for ci,name in enumerate(['C11','C2a','C2b']):
    for w in (-1,0,1):
        r=n(SC[ci]-(xs**w)[:,None]*k*(C[ci]@M.T)); out[f'RG5_{name}_w{w}']=dict(abs=float(r),rel=float(r/n(SC[ci]))); rg.append(r)
out['RG5']='FAIL (a component law passes)' if min(rg)<=1e-9 else ('PASS' if min(rg)>=1e-4 else 'inconclusive')
print(out,flush=True); json.dump(out,open('../data/l0.json','w'),indent=1)
