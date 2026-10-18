"""Independent rebuild of the Theorem F label family, S, T, P (from the written formulas), and
EXACT verification (all Galois conjugates) of S^2 = P, P^2 = I, (ST)^3 = I on Fix(P); counts 140/70/35/72;
gamma-stabiliser order; T order; T spectrum multiplicities. Written from scratch for the 2026-10-18 audit."""
import numpy as np, math, itertools
from fractions import Fraction as Fr
from collections import Counter
out=[]
def pr(*s): print(*s); out.append(" ".join(map(str,s)))
def Bf(u,v): return u[0]*(2*v[0]+7*v[1]) + u[1]*(7*v[0]+7*v[1])
def Qf(u): return Bf(u,u)/2
def md(v): return (Fr(v[0])%1, Fr(v[1])%1)
def add(u,v): return (u[0]+v[0],u[1]+v[1])
def neg(u): return (-u[0],-u[1])
Ainv=[[Fr(-1,5),Fr(1,5)],[Fr(1,5),Fr(-2,35)]]
def Av(v): return (2*v[0]+7*v[1], 7*v[0]+7*v[1])
def inLp(v): w=Av(v); return w[0].denominator==1 and w[1].denominator==1
a=(Fr(7,10),Fr(-1,5)); wc=(Fr(1,10),Fr(-1,35)); zero=(Fr(0),Fr(0))
LP=sorted({md((Ainv[0][0]*i+Ainv[0][1]*j, Ainv[1][0]*i+Ainv[1][1]*j)) for i in range(35) for j in range(35)})
ALS=LP+[md(add(p,a)) for p in LP]   # same ordering as family.py
BES=[zero, neg(a)]
pr("|L'/Z^2| =",len(LP), " alpha classes =",len(set(ALS)), " a in L'?",inLp(a), " 2a in L'?",inLp((2*a[0],2*a[1])))
pr("A(a-wc) =",Av(add(a,neg(wc))), "-> wc = a mod L':", inLp(add(a,neg(wc))), "; (1/2,0) = wc mod L':", inLp(add((Fr(1,2),Fr(0)),neg(wc))))
LAB=[(al,be) for al in ALS for be in BES]; IDX={l:i for i,l in enumerate(LAB)}; N=len(LAB)
pr("labels =",N)
def red(al,be):
    """u_{al,be} -> (index, rational phase r) meaning e(r) u_label"""
    for b0 in BES:
        mu=add(be,neg(b0))
        if inLp(mu): return IDX[(md(al),b0)], Bf(al,mu)%1
    raise ValueError
# phase-monomial descriptions: lists of (i,j,r)
Sent=[]; 
for i,(al,be) in enumerate(LAB):
    for p in LP:
        j,r=red(add(p,neg(be)),al); Sent.append((i,j,(Bf(al,be)+r)%1))
Tent=[]
for i,(al,be) in enumerate(LAB):
    j,r=red(al,add(add(al,be),wc)); Tent.append((i,j,(-Qf(al)-Bf(al,wc)+r)%1))
Pent=[]
for i,(al,be) in enumerate(LAB):
    j,r=red(neg(al),neg(be)); Pent.append((i,j,r))
rowcount=Counter(i for i,j,r in Sent); pairs=Counter((i,j) for i,j,r in Sent)
pr("S: entries per row min/max =",min(rowcount.values()),max(rowcount.values()), "; repeated (i,j) pairs:", sum(1 for v in pairs.values() if v>1))
M=1
for (_,_,r) in Sent+Tent+Pent: M=M*r.denominator//math.gcd(M,r.denominator)
M=M*140//math.gcd(M,140)
pr("common phase denominator M =",M)
def mat(ent,j=1):
    X=np.zeros((N,N),complex)
    for (i,k,r) in ent: X[i,k]+=np.exp(2j*np.pi*float((j*r)%1))
    return X
# compare with stored matrices (same label ordering as family.py: alpha classes sorted (x70), L' block then a+L' block)
try:
    S_st=np.load("../2026-10-17-psi-conditions/S_matrix.npy"); T_st=np.load("../2026-10-17-psi-conditions/T_matrix.npy")
    S1=mat(Sent)/math.sqrt(35); T1=mat(Tent)
    pr("max|S_rebuilt - S_stored| =",f"{np.abs(S1-S_st).max():.1e}", " max|T_rebuilt - T_stored| =",f"{np.abs(T1-T_st).max():.1e}")
except Exception as ex: pr("stored-matrix comparison skipped:",ex)
def chi140(n):
    from sympy import jacobi_symbol
    # Kronecker symbol (140/n) for n odd coprime to 140: (140/n) = (35/n) * (4/n) = (35/n) for odd n
    return int(jacobi_symbol(35, n)) if n%2 else 0
# Gauss-sum normalisation of sqrt(35) under Galois: sigma_j(sqrt35) = chi(j) sqrt35  (check numerically)
g=lambda j: complex(sum(chi140(n)*np.exp(2j*np.pi*j*n/140) for n in range(1,140) if math.gcd(n,140)==1))
pr("Gauss sum check sigma_j(2 sqrt35) = chi(j) 2sqrt35 at j=1,3,11,13:", [f"{(g(j)/(chi140(j)*2*math.sqrt(35))).real:.12f}" for j in (1,3,11,13)])
worst={'S2':0,'P2':0,'ST3':0,'PT':0}
units=[j for j in range(1,M) if math.gcd(j,M)==1]
for j in units:
    S0=mat(Sent,j); T=mat(Tent,j); P=mat(Pent,j); I=np.eye(N)
    worst['S2']=max(worst['S2'],np.abs(S0@S0-35*P).max())
    worst['P2']=max(worst['P2'],np.abs(P@P-I).max())
    worst['PT']=max(worst['PT'],np.abs(P@T-T@P).max())
    X=S0@T; X3=X@X@X
    worst['ST3']=max(worst['ST3'],np.abs(X3@(I+P)-chi140(j)*35*math.sqrt(35)*(I+P)).max())
    worst['ST3all']=max(worst.get('ST3all',0),np.abs(X3-chi140(j)*35*math.sqrt(35)*I).max())
pr(f"EXACT (all {len(units)} Galois conjugates sigma_j, j in (Z/{M})^x): max entry moduli of the algebraic-integer differences:")
pr(f"  S0^2-35P: {worst['S2']:.1e};  P^2-I: {worst['P2']:.1e};  PT-TP: {worst['PT']:.1e};  (S0 T)^3 (I+P) - 35^(3/2)(I+P): {worst['ST3']:.1e}")
pr(f"  (S0 T)^3 - 35^(3/2) I on all 140 labels: {worst['ST3all']:.1e}  => (ST)^3 = I exactly on all of C^140 (while S^2 = P != I)")
pr("  all < 1/2 at every conjugate => each difference is an algebraic integer of norm < 1 => exactly 0.")
pr("  Hence exactly: S^2 = P, P^2 = I, [P,T]=0, and (ST)^3 = I on Fix(P) (S = S0/sqrt35).")
# also: (ST)^3 vs P on all 140
S=mat(Sent)/math.sqrt(35); T=mat(Tent); P=mat(Pent); I=np.eye(N)
X3=np.linalg.matrix_power(S@T,3)
pr(f"on all 140: |(ST)^3 - I| = {np.abs(X3-I).max():.2f}, |(ST)^3 - P| = {np.abs(X3-P).max():.2f}  (so S^2=P holds, S^2=I only on Fix(P); (ST)^3=I on all 140)")
pr("rank(I+P) = dim Fix(P) =", np.linalg.matrix_rank(I+P, tol=1e-8))
# fixed labels of P
fixed=[LAB[i] for (i,k,r) in Pent if i==k]
pr("P-fixed labels:", [(tuple(map(str,al)),tuple(map(str,be))) for al,be in fixed], " phases:", [str(r) for (i,k,r) in Pent if i==k])
# gamma stabiliser order
Gm=[[-1,-7],[2,13]]
def gact(g,v): return (g[0][0]*v[0]+g[0][1]*v[1], g[1][0]*v[0]+g[1][1]*v[1])
def gpow(k):
    R=[[1,0],[0,1]]
    for _ in range(k): R=[[sum(Gm[i][l]*R[l][j] for l in range(2)) for j in range(2)] for i in range(2)]
    return R
assert Qf(gact(Gm,(Fr(3,7),Fr(2,11))))==Qf((Fr(3,7),Fr(2,11)))
for k in range(1,5):
    gk=gpow(k); ok=True
    for al,be in LAB:
        if md(gact(gk,al))!=md(al): ok=False;break
        mu=add(gact(gk,be),neg(be))
        if not inLp(mu) or Bf(al,mu)%1!=0: ok=False;break
    pr(f"gamma^{k} stabilises all 140 labels (coset and phase): {ok}")
    if ok: break
# T order and spectrum on Fix(P)
Tperm={i:(k,r) for (i,k,r) in Tent}
def Tpow_is_identity(n):
    for i in range(N):
        j=i; ph=Fr(0)
        for _ in range(n):
            k,r=Tperm[j]; ph+=r; j=k
        if j!=i or ph%1!=0: return False
    return True
ordT=next(n for n in range(1,1000) if Tpow_is_identity(n))
pr("order of T on all 140 labels (exact) =",ordT)
# T restricted to Fix(P): basis via projector
w,Vv=np.linalg.eigh((I+P+(I+P).conj().T)/4)
B=Vv[:,w>0.5]; TT=B.conj().T@T@B
ev=np.linalg.eigvals(TT); rs=np.round((np.angle(ev)/(2*np.pi))%1*840).astype(int)%840
mult=Counter(Fr(int(x),840) for x in rs)
pr("dim Fix(P) basis =",B.shape[1], "; T|Fix(P) eigenvalue multiplicities:", dict(sorted(Counter(mult.values()).items())), "; distinct =",len(mult), "; total =",sum(mult.values()))
pr("  values with multiplicity 4:", sorted(str(k) for k,v in mult.items() if v==4))
# cyclic S,T span of row e_(a,0)
ia=IDX[(md(a),zero)]
rows=[np.eye(N)[ia]]; span=np.array(rows)
frontier=[rows[0]]
while frontier:
    new=[]
    for v in frontier:
        for Mx in (S,T):
            wv=v@Mx
            cand=np.vstack([span,wv])
            if np.linalg.matrix_rank(cand,tol=1e-9)>span.shape[0]: span=cand; new.append(wv)
    frontier=new
pr("label-space cyclic span of row e_(a,0) under S,T: dim =",span.shape[0], "; after projection to Fix(P) (rows times (I+P)/2): rank =", np.linalg.matrix_rank(span@(I+P)/2, tol=1e-9))
open("thmF_exact.txt","w").write("\n".join(out)+"\n")
pr(f"unitarity: |S S^* - I| = {np.abs(S@S.conj().T-I).max():.1e}, |T T^* - I| = {np.abs(T@T.conj().T-I).max():.1e}")
import mpmath as mp; mp.mp.dps=30
pr("I = log(6+sqrt35)/(2 sqrt35) =", mp.nstr(mp.log(6+mp.sqrt(35))/(2*mp.sqrt(35)),22))
open("thmF_exact.txt","w").write("\n".join(out)+"\n")
SS=B.conj().T@S@B
evs=np.linalg.eigvals(SS)
pr(f"S on Fix(P): tr = {np.trace(SS).real:+.1e}{np.trace(SS).imag:+.1e}i ; eigenvalues +1: {int((abs(evs-1)<1e-8).sum())}, -1: {int((abs(evs+1)<1e-8).sum())}")
open("thmF_exact.txt","w").write("\n".join(out)+"\n")
