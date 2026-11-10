import sys; sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order3c/scripts')
from lib3c import *
k,K=int(sys.argv[1]),int(sys.argv[2])
pairs=[sym_pair(f,i) for f in FAM for i in range(35)]
idx=[i for i in range(216) if i%K==k]
out={n:np.zeros((len(idx),105),complex) for n in ('A0','A1','A2','S_A0','S_A1','S_A2')}
for r,i in enumerate(idx):
    x=XS[i]
    for j,(al,be) in enumerate(pairs):
        out['A0'][r,j],out['A1'][r,j],out['A2'][r,j]=A012(al,be,x)
        out['S_A0'][r,j],out['S_A1'][r,j],out['S_A2'][r,j]=A012(al,be,-1/x)
np.savez('../data/chunk_%d.npz'%k,idx=np.array(idx),**out)
