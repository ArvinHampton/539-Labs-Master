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
# ---- order39 RG36 (helpers above copied verbatim from order19/scripts/l0.py)
from scipy.stats import spearmanr
M=np.zeros((105,105),complex)
for j,dct in enumerate(S_rows()):
    for k_,es in dct.items():
        for e in es: M[j,k_]+=np.exp(2j*np.pi*e/L)
kap=complex(1.0000146975519928,-0.00033624064241876014); n=np.linalg.norm
NP=[Fr(41),Fr(43),Fr(47),Fr(53),Fr(59),Fr(41,2),Fr(43,2),Fr(47,2),Fr(41,3),Fr(43,3),Fr(47,3),Fr(53,3)]
for x in NP: assert x not in XS
ref=0.0013404387129956755; rows=[]
for x in NP:
    Y=np.array([comps(al,be,x)[2] for al,be in pairs]); S=np.array([comps(al,be,-1/x)[2] for al,be in pairs])
    r=float(n(S-kap*float(x)*(M@Y)/math.sqrt(35))/n(S)); rows.append(dict(x=str(x),num=x.numerator,r=r)); print(rows[-1],flush=True)
    np.save(f'../data/C2b_{str(x).replace("/","_")}.npy',np.stack([Y,S]))
o38=json.load(open('/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order38/data/o38.json'))
g={int(k):v['median_r'] for k,v in o38['RG35b']['groups'].items()}
for v in sorted(set(r_['num'] for r_ in rows)): g[v]=float(np.median([r_['r'] for r_ in rows if r_['num']==v]))
ks=sorted(g); rho=float(spearmanr(ks,[g[k] for k in ks])[0])
below=sum(r_['r']<ref for r_ in rows); med=float(np.median([r_['r'] for r_ in rows]))
v='PASS' if (below>=11 and med<ref and rho<=-0.9) else ('FAIL' if (med>=ref or below<=8) else 'inconclusive')
out=dict(points=rows,below=below,median_new=med,ref=ref,pooled_spearman=rho,new_groups={k:g[k] for k in ks if k>37},verdict=v)
json.dump(out,open('../data/o39.json','w'),indent=1); print(json.dumps({k:v_ for k,v_ in out.items() if k!='points'},indent=1))
