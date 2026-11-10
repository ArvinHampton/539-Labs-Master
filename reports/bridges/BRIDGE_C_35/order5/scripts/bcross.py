# task (b) cross-check: mp entries vs float lib3c (read-only) at all rows
import sys, pickle, glob, json; sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order3c/scripts')
sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/A35_lawspace_exact')
import lib3c, numpy as np
from fractions import Fraction as Fr
from math import gcd
from symbols import FAM, sym_pair
XSb=sorted({Fr(h,m) for m in range(1,25) for h in range(1,25) if gcd(h,m)==1})
k,K=int(sys.argv[1]),int(sys.argv[2])
D={}
for f in glob.glob('../data/b_chunk_*.pkl'): D.update(pickle.load(open(f,'rb')))
pairs=[sym_pair(f,i) for f in FAM for i in range(35)]
mx=0.0
for i in range(359):
    if i%K!=k: continue
    for j,(al,be) in enumerate(pairs):
        v=list(lib3c.A012(al,be,XSb[i]))+list(lib3c.A012(al,be,-1/XSb[i]))
        for o in range(6):
            mpv=complex(float(D[i][j][o][0]),float(D[i][j][o][1])); mx=max(mx,abs(mpv-v[o])/max(1,abs(mpv)))
json.dump(dict(max_rel=mx),open('../data/bcross_%d.json'%k,'w')); print(mx)
