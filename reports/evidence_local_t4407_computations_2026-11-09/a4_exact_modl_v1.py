# Local-derived. t4407 item 4a hardening: rho_{N2}(g) e0 = chi_140(d) e0 for all 259 Schreier generators of Gamma0(140),
# EXACT arithmetic in Z[zeta_140] reduced modulo degree-1 primes l | ell, ell = 1 mod 140, + rigorous norm bound.
# Same lattice, same S/T matrices, same coset/Schreier construction as part4_gamma0_140_weil_e0.py (read-only, not modified).
import numpy as np, math, sys, time
from fractions import Fraction as Fr
from sympy import jacobi_symbol, isprime, primitive_root
N=140
Ginv=[[Fr(28,-140),Fr(-14,-140)],[Fr(-14,-140),Fr(2,-140)]]
els=set()
for a in range(140):
    for b in range(140):
        els.add(((Ginv[0][0]*a+Ginv[0][1]*b)%1, (Ginv[1][0]*a+Ginv[1][1]*b)%1))
els=sorted(els); assert len(els)==140
def bil(x,y): return (x[0]*(2*y[0]+14*y[1])+x[1]*(14*y[0]+28*y[1]))%1
def q(x): return Fr(1,2)*(x[0]*(2*x[0]+14*x[1])+x[1]*(14*x[0]+28*x[1]))%1
Bm=np.array([[int(bil(x,y)*140) for y in els] for x in els],dtype=np.int64); Qv=np.array([int(q(x)*140) for x in els],dtype=np.int64)
i0=els.index((0,0))
def chi(n):
    n%=140
    if math.gcd(n,140)!=1: return 0
    return int(((-1)**((n-1)//2))*int(jacobi_symbol(n,5))*int(jacobi_symbol(n,7)))
units=[a for a in range(1,140) if math.gcd(a,140)==1]
Sm=np.array([[0,-1],[1,0]],dtype=object); Tm=np.array([[1,1],[0,1]],dtype=object)
L={'S':Sm,'s':np.array([[0,1],[-1,0]],dtype=object),'T':Tm,'t':np.array([[1,-1],[0,1]],dtype=object)}
inv={'S':'s','s':'S','T':'t','t':'T'}
def wmat(w):
    M=np.eye(2,dtype=object)
    for c in w: M=M.dot(L[c])
    return M
def key(c,d): return min((((u*c)%N,(u*d)%N)) for u in units)
reps={key(0,1):''}; queue=['']
while queue:
    w=queue.pop(0); M=wmat(w)
    for x in 'ST':
        M2=M.dot(L[x]); k=key(int(M2[1,0]),int(M2[1,1]))
        if k not in reps: reps[k]=w+x; queue.append(w+x)
gens=[]
for k,w in reps.items():
    for x in 'ST':
        M2=wmat(w+x); k2=key(int(M2[1,0]),int(M2[1,1])); w2=reps[k2]
        g=w+x+''.join(inv[c] for c in reversed(w2)); Mg=wmat(g); assert int(Mg[1,0])%N==0
        if not (Mg==np.eye(2,dtype=object)).all(): gens.append((g,Mg))
smax=max(sum(c in 'Ss' for c in g) for g,_ in gens)
print("cosets",len(reps),"Schreier generators",len(gens),"max word length",max(len(g) for g,_ in gens),"max #S-letters s_max =",smax)
# rigorous bound: beta_i = g^s (rho(w)e0 - chi(d)e0)_i in Z[zeta_140], g = Gauss sum of chi_140 (g^2 = 140, g in Z[zeta]).
# every Galois conjugate rho_sigma is a product of unitary matrices => |sigma(beta_i)| <= 2*140^(s/2); |N(beta_i)| <= (2*140^(smax/2))^48.
log10_bound = 48*(math.log10(2)+ (smax/2)*math.log10(140))
print("log10 |N(beta_i)| bound =", round(log10_bound,3))
def run_prime(ell):
    r=primitive_root(ell); z=pow(r,(ell-1)//140,ell)          # a primitive 140th root of unity mod ell  <=> choice of degree-1 prime l | ell
    assert pow(z,70,ell)!=1 and pow(z,28,ell)!=1 and pow(z,20,ell)!=1 and pow(z,140,ell)==1
    zp=np.array([pow(z,k,ell) for k in range(140)],dtype=np.int64)
    gs=sum(chi(u)*int(zp[u]) for u in range(140))%ell        # Gauss sum image
    assert gs*gs%ell==140%ell, "Gauss sum^2 != 140 mod ell"
    gi=pow(gs,ell-2,ell)
    S=(gi*zp[(-Bm)%140])%ell; Si=(gi*zp[Bm%140])%ell; T=zp[Qv%140]; Ti=zp[(-Qv)%140]
    def mv(M,v): return np.array([int(x) for x in ((M*v[None,:])%ell).sum(axis=1)%ell],dtype=np.int64)
    I=np.eye(140,dtype=np.int64)
    def mm(A,B): return np.array([[sum(int(A[i,k])*int(B[k,j]) for k in range(140))%ell for j in range(140)] for i in range(140)],dtype=np.int64) if False else (np.array(np.matmul(A.astype(object),B.astype(object))%ell,dtype=np.int64))
    ok_rel = (mm(S,Si)==I).all()
    S2=mm(S,S); ST=mm(S,np.diag(T)); ST3=mm(mm(ST,ST),ST)
    ok_rel = ok_rel and (mm(S2,S2)==I).all() and (ST3==S2).all()
    R={'S':lambda v:mv(S,v),'s':lambda v:mv(Si,v),'T':lambda v:(T*v)%ell,'t':lambda v:(Ti*v)%ell}
    bad=0
    for g,Mg in gens:
        v=np.zeros(140,dtype=np.int64); v[i0]=1
        for c in reversed(g): v=R[c](v)
        tgt=np.zeros(140,dtype=np.int64); tgt[i0]=chi(int(Mg[1,1]))%ell
        if not (v%ell==tgt).all(): bad+=1
    # control: (1,0;70,1) must NOT fix the e0 line
    w='s'+'t'*70+'S'; v=np.zeros(140,dtype=np.int64); v[i0]=1
    for c in reversed(w): v=R[c](v)
    ctrl_off = int(np.count_nonzero(np.delete(v,i0)))
    return ok_rel,bad,ctrl_off
primes=[]; ell=2**31-1
while True:
    ell-=1
    if ell%140==1 and isprime(ell): primes.append(ell)
    if sum(math.log10(p) for p in primes) > log10_bound+20: break
print("using",len(primes),"primes ell = 1 mod 140 below 2^31; log10 prod =", round(sum(math.log10(p) for p in primes),3))
t0=time.time(); allok=True
for ell in primes:
    ok_rel,bad,ctrl=run_prime(ell)
    allok &= ok_rel and bad==0
    print(f" ell={ell}: S S^-1=I, S^4=I, (ST)^3=S^2 exact: {ok_rel}; generators failing: {bad}/{len(gens)}; control (1,0;70,1) nonzero off-e0 entries: {ctrl}; t={time.time()-t0:.0f}s",flush=True)
print("ALL PRIMES PASS:",allok, "| prod(ell) > bound on |N(beta_i)|:", sum(math.log10(p) for p in primes) > log10_bound)
print("CONCLUSION (if both True): every beta_i = 0 exactly, i.e. rho(g)e0 = chi_140(d)e0 exactly for all 259 generators, hence on Gamma0(140).")
