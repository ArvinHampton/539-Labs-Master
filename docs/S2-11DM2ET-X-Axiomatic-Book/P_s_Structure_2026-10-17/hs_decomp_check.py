# Exact check (to q^N) of the cone decomposition of H_s used for its EM expansion:
# H_s = [S(K+) - W1+/2 - W2+/2] - [S(K-) - W1-/2 - W2-/2],  K+ = closed cone((0,1),(21,-1)) = sqcup_s (s,0)+N v1+N v2.
import numpy as np, math
N=2000
from fractions import Fraction as Fr
def Qs(n,k): return n*n+7*n*k+Fr(7,2)*k*(k+1)
H=np.zeros(N+1,dtype=object); H[:]=Fr(0)
B=200
for n in range(-30*B//10*3, 30*B//10*3+1):
    pass
# direct H_s
nn=np.arange(-1500,1501)[:,None]; kk=np.arange(-120,121)[None,:]
w2=np.sign(5*nn)-np.sign(-nn-21*kk)               # = 2w
e2=2*nn*nn+14*nn*kk+7*kk*(kk+1)                   # = 2 Q_s
m=(w2!=0)&(e2<=2*N)
assert not (m[0,:].any() or m[-1,:].any() or m[:,0].any() or m[:,-1].any())
H2=np.bincount((e2[m]//2).astype(np.int64),weights=w2[m].astype(np.float64),minlength=N+1)[:N+1]   # = 2 H_s
# decomposition
def coneS(sign):
    s=np.zeros(N+1)
    i=np.arange(0,80)[:,None]; j=np.arange(0,80)[None,:]
    for r in range(21):
        n_=sign*(r + 21*j); k_=sign*(i - j)
        e2=2*n_*n_+14*n_*k_+7*k_*(k_+1); mm=e2<=2*N
        assert not (mm[-1,:].any() or mm[:,-1].any())
        s+=np.bincount((e2[mm]//2).astype(np.int64),minlength=N+1)[:N+1]
    return s
def wall(v,sign):
    s=np.zeros(N+1)
    for j in range(0,400):
        n_,k_=sign*j*v[0],sign*j*v[1]; e=int(Qs(n_,k_))
        if e<=N: s[e]+=1
    return s
D2 = 2*(coneS(1)-0.5*wall((0,1),1)-0.5*wall((21,-1),1)) - 2*(coneS(-1)-0.5*wall((0,1),-1)-0.5*wall((21,-1),-1))
ok = np.array_equal(D2, H2)
msg=f"{'PASS' if ok else 'FAIL'} H_s = [K+ - walls/2] - [K- - walls/2] (21 residues (s,0)) exact to q^{N}"
print(msg); open('hs_decomp_check.txt','w').write(msg+"\n")
