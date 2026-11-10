import sys, math, json, numpy as np
sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order2/scripts')
from lib2 import XS
from symbols import S_rows, L
Z=np.load('../data/o24_arrays.npz'); G=Z['Gg']; d=np.load('/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order18/data/a2_arrays.npz'); CO,SCO=d['CO'],d['SCO']
P=np.eye(105,dtype=complex); m=None
for i in range(1,10001):
    P=P@G
    if np.abs(P-np.eye(105)).max()<1e-9: m=i; break
out={'order':m}
if m:
    Pi=sum(np.linalg.matrix_power(G,i) for i in range(m))/m
    M=np.zeros((105,105),complex)
    for j,dd in enumerate(S_rows()):
        for kk,es in dd.items():
            for ee in es: M[j,kk]+=np.exp(2j*np.pi*ee/L)
    xs=np.array([float(x) for x in XS]); n=np.linalg.norm
    Y=CO@Pi.T; SY=SCO@Pi.T; Pr=xs[:,None]*(Y@M.T)/math.sqrt(35); a=float(n(SY-Pr)); s=float(n(SY)); nv=float(n(Y)/n(CO))
    out['RG14']=dict(abs=a,norm=s,rel=a/max(s,1e-300),nonvac=nv,rankPi=int(np.linalg.matrix_rank(Pi,1e-9)),
       verdict='vacuous' if nv<1e-3 else ('PASS' if a<=1e-8 else ('FAIL' if a>=1e-3*s else 'inconclusive')))
else: out['RG14']='not applicable'
print(out); json.dump(out,open('../data/rg14.json','w'),indent=1)
