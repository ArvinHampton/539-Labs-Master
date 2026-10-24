# BRIDGE_C_35 shared code. Read-only import of A35 symbols.py (CORE_FREEZE: nothing there is modified).
import sys, numpy as np
sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/A35_lawspace_exact')
from symbols import *          # A, MU, a, FAM, sym_pair, B, Q, T_rows, L
from fractions import Fraction as Fr
from math import gcd
XS=sorted({Fr(h,m) for m in range(1,16) for h in range(1,3*m+1) if gcd(h,m)==1}); assert len(XS)==216
I0=0  # index of mu=0 in MU
assert MU[[i for i in range(35) if MU[i]==(0,0)][0]]==(0,0)
I0=[i for i in range(35) if MU[i]==(0,0)][0]
def Gp(al,be,x,z,p,Lev):
    """Exact finite Gauss mean G_{al,be}(x) reduced mod p, z = primitive Lev-th root of 1 mod p.
    Same formula as A51 rank216.py (box 4m, coordinates scaled by 70); x>0 or x<0 rational."""
    x=Fr(x); m=x.denominator; Lb=4*m; N=9800*m; assert Lev%N==0; zN=pow(z,Lev//N,p)
    i,j=np.meshgrid(np.arange(Lb),np.arange(Lb),indexing='ij')
    assert Fr(int(al[0]*70),70)==al[0] and Fr(int(al[1]*70),70)==al[1]
    v0=int(al[0]*70)+70*i; v1=int(al[1]*70)+70*j; b0,b1=int(be[0]*70),int(be[1]*70)
    Q2=2*v0*v0+14*v0*v1+7*v1*v1; Bn=v0*(2*b0+7*b1)+v1*(7*b0+7*b1)
    ph=np.array((x.numerator*Q2+2*m*Bn)%N,dtype=np.int64); cnt=np.bincount(ph.ravel(),minlength=N)
    return sum(int(cnt[k])*pow(zN,int(k),p) for k in np.nonzero(cnt)[0])*pow(Lb*Lb,-1,p)%p
def Q7(n,k): return n*n+7*n*k+(7*k*(k+1))//2
def Grta_p(x,z,p,Lev):
    """RTA leading-profile mean G(x)=(2m)^-2 sum_{(n,k) mod 2m} e(x Q_7(n,k)) mod p."""
    x=Fr(x); m=x.denominator; assert Lev%m==0; zm=pow(z,Lev//m,p)
    n,k=np.meshgrid(np.arange(2*m),np.arange(2*m),indexing='ij')
    q=(n*n+7*n*k+(7*k*(k+1))//2)%m; ph=(x.numerator*q)%m
    cnt=np.bincount(ph.ravel(),minlength=m)
    return sum(int(cnt[r])*pow(zm,r,p) for r in range(m) if cnt[r])*pow(4*m*m,-1,p)%p
def Grta_c(x):
    x=Fr(x); m=x.denominator
    n,k=np.meshgrid(np.arange(2*m),np.arange(2*m),indexing='ij')
    q=(n*n+7*n*k+(7*k*(k+1))//2)%m
    return np.exp(2j*np.pi*(x.numerator*q%m)/m).mean()
