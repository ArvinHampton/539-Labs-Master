# task (b): mp entries on XSb, one chunk per process
import sys; sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/A35_lawspace_exact')
from lib5mp import *
from symbols import FAM, sym_pair
from math import gcd
import pickle, time
XSb=sorted({Fr(h,m) for m in range(1,25) for h in range(1,25) if gcd(h,m)==1})
assert len(XSb)==359, len(XSb)
k,K=int(sys.argv[1]),int(sys.argv[2])
pairs=[sym_pair(f,i) for f in FAM for i in range(35)]
idx=[i for i in range(len(XSb)) if i%K==k]
out={}
t0=time.time()
for i in idx:
    x=XSb[i]; row=[]
    for al,be in pairs:
        a=A012mp(al,be,x); b=A012mp(al,be,-1/x); row.append((a,b))
    out[i]=[[(str(v.real),str(v.imag)) for v in a+b] for a,b in row]
    import lib5mp; lib5mp._ET.clear()
    print(i,str(x),round(time.time()-t0,1),flush=True)
    pickle.dump(out,open('../data/b_chunk_%d.pkl'%k,'wb'))
