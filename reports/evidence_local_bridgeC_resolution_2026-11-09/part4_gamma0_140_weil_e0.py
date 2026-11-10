# Local-derived. Task 4: rho_{N2}(g) e0 = chi_140(d) e0 on a full (Schreier) generating set of Gamma0(140), all 48 Galois twists, float64.
import numpy as np, math, itertools
from fractions import Fraction as Fr
N=140; G=np.array([[2,14],[14,28]])
Ginv=[[Fr(28,-140),Fr(-14,-140)],[Fr(-14,-140),Fr(2,-140)]]
els=set()
for a in range(140):
    for b in range(140):
        x=(Ginv[0][0]*a+Ginv[0][1]*b, Ginv[1][0]*a+Ginv[1][1]*b)
        els.add((x[0]%1, x[1]%1))
els=sorted(els); assert len(els)==140
def bil(x,y): return (x[0]*(2*y[0]+14*y[1])+x[1]*(14*y[0]+28*y[1]))%1
def q(x): return Fr(1,2)*(x[0]*(2*x[0]+14*x[1])+x[1]*(14*x[0]+28*x[1]))%1
Bm=np.array([[int(bil(x,y)*140) for y in els] for x in els]); Qv=np.array([int(q(x)*140) for x in els])
assert all((bil(x,y)*140).denominator==1 for x in els for y in els) and all((q(x)*140).denominator==1 for x in els)
i0=els.index((0,0))
from sympy import jacobi_symbol
import functools
@functools.lru_cache(None)
def chi(n):
    n%=140
    if math.gcd(n,140)!=1: return 0
    # 140 = 4*35, chi_140 = chi_-4*chi_5*chi_-7 ; chi_-4(n)=(-1)^((n-1)/2)
    return int(((-1)**((n-1)//2))*int(jacobi_symbol(n,5))*int(jacobi_symbol(n,7)))
units=[a for a in range(1,140) if math.gcd(a,140)==1]; assert len(units)==48
def mats(a):
    z=lambda k: np.exp(2j*np.pi*a*k/140)
    S=chi(a)/math.sqrt(140)*z(-Bm)        # sigma_a(1/sqrt140)=chi140(a)/sqrt140 (sqrt140 = Gauss sum of chi140)
    T=np.diag(z(Qv)); return S,T
# group words
Sm=np.array([[0,-1],[1,0]]); Tm=np.array([[1,1],[0,1]])
L={'S':Sm,'s':np.array([[0,1],[-1,0]]),'T':Tm,'t':np.array([[1,-1],[0,1]])}
inv={'S':'s','s':'S','T':'t','t':'T'}
def wmat(w):
    M=np.eye(2,dtype=object)
    for c in w: M=M.dot(L[c].astype(object))
    return M
def key(c,d):
    return min((((u*c)%N,(u*d)%N)) for u in units)
# BFS cosets Gamma0(N) g, g ~ bottom row (c:d)
reps={key(0,1):''}; queue=['']
while queue:
    w=queue.pop(0); M=wmat(w)
    for x in 'ST':
        M2=M.dot(L[x].astype(object)); k=key(int(M2[1,0]),int(M2[1,1]))
        if k not in reps: reps[k]=w+x; queue.append(w+x)
print("cosets:",len(reps), "(index of Gamma0(140) = 140*3/2*6/5*8/7 = 288)")
gens=[]
for k,w in reps.items():
    for x in 'ST':
        M2=wmat(w+x); k2=key(int(M2[1,0]),int(M2[1,1])); w2=reps[k2]
        g=w+x+''.join(inv[c] for c in reversed(w2))
        Mg=wmat(g); assert int(Mg[1,0])%N==0
        if not (Mg==np.eye(2,dtype=object)).all(): gens.append((g,Mg))
print("Schreier generators (nontrivial):",len(gens), " max word length:",max(len(g) for g,_ in gens), " max #S letters:", max(sum(c in 'Ss' for c in g) for g,_ in gens))
maxres=0; worst=None
import time; t0=time.time()
for a in units:
    S,T=mats(a); R={'S':S,'s':S.conj().T,'T':T,'t':T.conj().T}
    # sanity: relations S^4=1, (ST)^3=S^2 for this twist
    if a in (1,3,139):
        print(f" a={a}: |S^4-I|={np.abs(np.linalg.matrix_power(S,4)-np.eye(140)).max():.2e}, |(ST)^3-S^2|={np.abs(np.linalg.matrix_power(S@T,3)-S@S).max():.2e}, |S S^*-I|={np.abs(S@S.conj().T-np.eye(140)).max():.2e}")
    for g,Mg in gens:
        v=np.zeros(140,complex); v[i0]=1
        for c in reversed(g): v=R[c]@v
        target=np.zeros(140,complex); target[i0]=chi(int(Mg[1,1]))
        r=np.abs(v-target).max()
        if r>maxres: maxres=r; worst=(a,g)
    print(' twist a=',a,'done; running max residual',maxres,'t=%.0fs'%(time.time()-t0),flush=True)
print("max over 48 Galois twists and all generators of |rho_a(g)e0 - chi140(d_g) e0|_inf =", maxres)
# control: element of Gamma0(70)\Gamma0(140)
S,T=mats(1); Mc=[[1,0],[70,1]]
# (1,0;70,1) = S^-1 T^-70 S ... check: s * T^-70 * S
w='s'+'t'*70+'S'; print("control word matrix:", wmat(w).tolist())
R={'S':S,'s':S.conj().T,'T':T,'t':T.conj().T}; v=np.zeros(140,complex); v[i0]=1
for c in reversed(w): v=R[c]@v
print("control (1,0;70,1): |component e0| =", abs(v[i0]), " mass off e0 =", np.linalg.norm(np.delete(v,i0)))
print("homomorphism check: d-entry multiplicative on 2000 random products in Gamma0(140):", end=' ')
import random; ok=True
for _ in range(2000):
    g1=random.choice(gens)[1]; g2=random.choice(gens)[1]; P_=g1.dot(g2)
    ok &= (chi(int(P_[1,1]))==chi(int(g1[1,1]))*chi(int(g2[1,1])))
print(ok)
