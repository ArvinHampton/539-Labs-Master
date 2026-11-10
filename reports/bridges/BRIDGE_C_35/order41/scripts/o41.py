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
# ---- order41 RG38 (helpers above verbatim from order19/scripts/l0.py)
M=np.zeros((105,105),complex)
for j,dct in enumerate(S_rows()):
    for k_,es in dct.items():
        for e in es: M[j,k_]+=np.exp(2j*np.pi*e/L)
kap=complex(1.0000146975519928,-0.00033624064241876014); n=np.linalg.norm
NUM=[61,67,71]; DEN=[1,2,4,5]; r={}
for a in NUM:
    for d in DEN:
        x=Fr(a,d); assert x not in XS
        Y=np.array([comps(al,be,x)[2] for al,be in pairs]); S=np.array([comps(al,be,-1/x)[2] for al,be in pairs])
        r[(a,d)]=float(n(S-kap*float(x)*(M@Y)/math.sqrt(35))/n(S)); print(a,d,r[(a,d)],flush=True)
viol=[]
for a in NUM:
    for d1,d2 in zip(DEN,DEN[1:]):
        if not r[(a,d2)]<r[(a,d1)]: viol.append(f"num{a}:den{d1}->{d2}")
for d in DEN:
    for a1,a2 in zip(NUM,NUM[1:]):
        if not r[(a2,d)]<r[(a1,d)]: viol.append(f"den{d}:num{a1}->{a2}")
v='PASS' if not viol else ('FAIL' if len(viol)>=3 else 'inconclusive')
out=dict(r={f"{a}/{d}":r[(a,d)] for a,d in r},violations=viol,n_claims=17,verdict=v)
json.dump(out,open('../data/o41.json','w'),indent=1); print(json.dumps(out,indent=1))
