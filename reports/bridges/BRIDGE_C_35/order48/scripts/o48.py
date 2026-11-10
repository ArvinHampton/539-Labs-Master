import sys, math, json, numpy as np
sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order2/scripts')
from lib2 import XS, Fr
from symbols import FAM, sym_pair, S_rows, reduce, L
pairs=[sym_pair(f,i) for f in FAM for i in range(35)]
M=np.zeros((105,105),complex)
for j,d in enumerate(S_rows()):
    for kk,es in d.items():
        for ee in es: M[j,kk]+=np.exp(2j*np.pi*ee/L)
Pi=np.zeros((105,105),complex)
for j,(al,be) in enumerate(pairs):
    kk,ee=reduce(al,(-be[0],-be[1])); Pi[j,kk]=np.exp(2j*np.pi*ee/L)
kM=M/math.sqrt(35); kMi=np.linalg.inv(kM); n=np.linalg.norm
B='/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/'
Z=np.load(B+'order19/data/rg5_arrays.npz'); A=np.load(B+'order18/data/a2_arrays.npz')
objs={'C11':(Z['C'][0],Z['SC'][0]),'C2a':(Z['C'][1],Z['SC'][1]),'C2b':(Z['C'][2],Z['SC'][2]),'CO':(A['CO'],A['SCO']),'LN_contrast':(A['LN'],A['SLN'])}
pr=[(XS.index(x),XS.index(1/x),float(x)) for x in XS if x>1 and (1/x) in XS]
out={'n_pairs':len(pr)}
for nm,(Y,S) in objs.items():
    w=0.0
    for i,ii,x in pr:
        Rx=S[i]-x*(kM@Y[i]); Ry=S[ii]-(1/x)*(kM@Y[ii])
        pred=-(1/x)*np.conj(Pi@(kMi@Rx)); w=max(w,float(n(Ry-pred)/n(Ry)))
    out[nm]=dict(max_rel=w,verdict='PASS' if w<=1e-10 else ('FAIL' if w>=1e-6 else 'inconclusive'))
print(out); json.dump(out,open('../data/o48.json','w'),indent=1)
