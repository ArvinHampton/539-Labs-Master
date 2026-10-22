# A32: exact (mod-p certificate) intertwiner spaces between the 35-dim Weil rep of D(A_7) and rho_7 on W.
# Uses A/scripts/weil_family.py unchanged (read-only import). No certifier code touched.
import sys, json, math, numpy as np
sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/A/scripts')
from weil_family import WFam
from fractions import Fraction as Fr
from sympy import isprime, primitive_root
import flint
L=29400  # lcm(9800,140,12,8)
def find_p(k0):
    k=k0
    while True:
        p=k*L+1
        if p<2**31 and isprime(p): return p
        k+=1
OUT={}
def setup(p):
    g=primitive_root(p); z=pow(g,(p-1)//L,p); return z
def zpow(z,p,k): return pow(z,int(k)%L,p)
def sqrt35(p):
    from sympy.ntheory import sqrt_mod
    return sorted(sqrt_mod(35,p,all_roots=True))
def mm(A,B,p): return (A.astype(object).dot(B.astype(object))%p)
def rels(S,T,p):
    I=np.eye(len(S),dtype=object); R=mm(S,T,p); R3=mm(mm(R,R,p),R,p); S2=mm(S,S,p)
    return bool((R3==S2).all() and (mm(S2,S2,p)==I).all())
def rho7W(p,z):
    F=WFam(7); F.build_W(); w=F.w
    x=lambda i: zpow(z,p,3*F.ph[i])
    def restrict(rowfun):
        M=np.zeros((w,w),dtype=object)
        for o in np.nonzero(F.good)[0]:
            i0=F.rep[o]; J,PH=rowfun(i0)
            row=M[F.widx[o]]
            for j,ph in zip(J,PH):
                c=F.widx[F.orb[j]]
                if c>=0: row[c]=(row[c]+zpow(z,p,3*ph)*x(j))%p
            inv=pow(x(i0),-1,p); M[F.widx[o]]=(row*inv)%p
        return M
    G=restrict(F.S_row); J,PH=F.T_mono(); T=restrict(lambda i:(J[i:i+1],PH[i:i+1]))
    # numeric cross-check of the same formula vs WFam.SW up to diagonal conjugation
    return F,G,T
def weil35(A,p,z):
    A=np.array(A,dtype=object); det=int(A[0][0]*A[1][1]-A[0][1]**2); n=abs(det)
    adj=np.array([[A[1][1],-A[0][1]],[-A[0][1],A[0][0]]],dtype=object)
    reps=sorted({tuple((adj.dot(np.array([x,y],dtype=object)))%n) for x in range(n) for y in range(n)})
    reps=[np.array(r,dtype=object) for r in reps]
    b=lambda r1,r2: Fr(int(r1.dot(A.dot(r2))),det*det)%1
    inv2=pow(2,-1,n); q=[Fr((inv2*int(b(r,r)*n))%n,n) for r in reps]
    def ex(f): v=f*L; assert v.denominator==1; return int(v)
    T=np.diag([zpow(z,p,ex(x)) for x in q]).astype(object)
    G=np.array([[zpow(z,p,-ex(b(r1,r2))) for r2 in reps] for r1 in reps],dtype=object)
    return G,T,[str(x) for x in q]
def tspec(T,p,z):
    # exact eigenspace dims of finite-order T (p∤L => semisimple mod p, dims = char-0 dims)
    n=len(T); out={}
    for k in range(L):
        lam=zpow(z,p,k)
        M=flint.nmod_mat([[int((T[i][j]-(lam if i==j else 0))%p) for j in range(n)] for i in range(n)],p)
        d=n-M.rank()
        if d: out[k]=d
    return out
def hom_dim(S1,T1,S2,T2,p):
    n1,n2=len(S1),len(S2)
    I1=np.eye(n1,dtype=object); I2=np.eye(n2,dtype=object)
    # vec(X) column-major: vec(X A) = (A^T kron I2) vec X ; vec(B X) = (I1 kron B) vec X
    K=np.vstack([(np.kron(S1.T,I2)-np.kron(I1,S2))%p,(np.kron(T1.T,I2)-np.kron(I1,T2))%p])
    M=flint.nmod_mat(K.shape[0],K.shape[1],[int(v) for v in K.ravel()],p)
    return n1*n2-M.rank()
