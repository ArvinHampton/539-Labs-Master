# Explicit intertwiner  X: rho_{L_ev} -> rho_rev=(S_lab^{-1},T),  L_ev = {x in Z^2 : x2 even} with B = x^T A y, A=[[2,7],[7,7]].
# Ansatz: X e_z = c0(z) u_{alpha(z),0} + c1(z) u_{alpha(z),-a}, alpha(z) = z mod Z^2.  Solve mod ell, recognise c's as roots of unity,
# then verify X S_W = S_lab^{-1} X and X T_W = T X EXACTLY in Z[zeta_280] (integer polynomials reduced mod Phi_280).
import pickle, json, sys
import numpy as np, sympy as sp
from fractions import Fraction as Fr
sys.path.insert(0,'.')
from intertwine import E, inv, p, N, S_lab_inv, T_rev, mm, nullspace_mod, rank_mod
R=pickle.load(open('rev_s7_exact.pkl','rb')); D=R['D']; LABELS=R['labels']; IDX={l:i for i,l in enumerate(LABELS)}
A=sp.Matrix([[2,7],[7,7]])
# L_ev' / L_ev in standard coordinates
Bm=sp.Matrix([[1,0],[0,2]]); G2=Bm.T*A*Bm; G2i=G2.inv()
els={}
for m1 in range(140):
    for m2 in range(140):
        z=Bm*G2i*sp.Matrix([m1,m2])
        y=G2i*sp.Matrix([m1,m2]); key=tuple(Fr(str(v))%1 for v in y)   # class mod L_ev (in N2 coords)
        els.setdefault(key,z)
Z=list(els.values()); assert len(Z)==140
q=[Fr(str((z.T*A*z)[0]/2))%1 for z in Z]
b=[[Fr(str((z.T*A*w)[0]))%1 for w in Z] for z in Z]
BES=sorted({l[1] for l in LABELS}); assert len(BES)==2
alpha=[tuple(int(Fr(str(v))*D)%D for v in z) for z in Z]
assert all((al,be) in IDX for al in alpha for be in BES), "alpha(z) not a rev label"
from collections import Counter
assert all(c==2 for c in Counter(alpha).values())
# Weil (Borcherds, sig 0) mod ell
TW=np.zeros((N,N),dtype=np.int64); SW=np.zeros((N,N),dtype=np.int64)
from intertwine import r35
ir140=inv(2*r35)
for k in range(N): TW[k,k]=E(q[k])
for k in range(N):
    for l in range(N): SW[l,k]=E(-b[k][l])*ir140%p
# sparse ansatz unknowns: (k, beta-index)
unk=[(k,t) for k in range(N) for t in range(2)]
rows=[]
def Xcol(v):
    X=np.zeros((N,N),dtype=np.int64)
    for n,(k,t) in enumerate(unk): X[IDX[(alpha[k],BES[t])],k]=v[n]
    return X
# build equations by linearity: columns of the system = vec(X_n SW - S X_n), vec(X_n TW - T X_n)
cols=[]
for n in range(len(unk)):
    v=np.zeros(len(unk),dtype=np.int64); v[n]=1; X=Xcol(v)
    cols.append(np.concatenate([((mm(X,SW)-mm(S_lab_inv,X))%p).ravel(),((mm(X,TW)-mm(T_rev,X))%p).ravel()]))
M=np.array(cols).T % p
rng=np.random.default_rng(3); C=(rng.integers(0,p,size=(len(unk)+40,M.shape[0]),dtype=np.int64)%p)
Cm=np.zeros((C.shape[0],M.shape[1]),dtype=np.int64)
for s0 in range(0,M.shape[0],2000): Cm=(Cm+(C[:,s0:s0+2000]@M[s0:s0+2000])%p)%p
ns=nullspace_mod(Cm,p)
print('sparse-ansatz solution space dim (compressed):',len(ns))
ok=[bool(not ((M@v)%p).any()) for v in ns]; print('each basis vector solves full system mod ell:',ok)
# normalise: choose solution with c0(z0)=1 for the 8 sector components -> take basis and look for root-of-unity solution
z280=E(Fr(1,280)); dlog={pow(z280,k,p):k for k in range(280)}
out={'sparse_dim':len(ns)}
# try: combination where all entries are roots of unity: solve for coefficients making each nonzero entry a 280th root of unity
# Basis vectors from nullspace are free-variable normalised; test each and simple sums
cands=[]
B=np.array(ns)
import itertools
for coeffs in itertools.product([0,1],repeat=len(ns)):
    if not any(coeffs): continue
    v=(np.array(coeffs)@B)%p
    if all(x==0 or (x in dlog) for x in v) and all(x!=0 for x in v):
        cands.append(v); break
if not cands:
    # rescale: fix v[0]=1 and solve generally (small dim): enumerate scalars in mu_280 for each basis element
    for scal in itertools.product(range(0,280,35),repeat=len(ns)):
        v=sum(pow(z280,s_,p)*B[i] for i,s_ in enumerate(scal))%p
        if all(x!=0 and x in dlog for x in v): cands.append(v); break
print('root-of-unity solution found:',bool(cands))
v=cands[0]; X=Xcol(v)
print('rank X mod ell:',rank_mod(X,p))
cexp={(k,t):Fr(dlog[int(v[n])],280) for n,(k,t) in enumerate(unk)}
# ---------- exact verification in Z[zeta_280] ----------
M_=280
Phi=sp.Poly(sp.cyclotomic_poly(M_,sp.Symbol('x')),sp.Symbol('x')).all_coeffs()[::-1]; Phi=np.array([int(c) for c in Phi],dtype=object)
def reduce_poly(vec):  # vec: integer coeffs of x^0..x^{279} (mod x^280-1); reduce mod Phi_280
    v=list(vec); dP=len(Phi)-1
    for i in range(len(v)-1,dP-1,-1):
        c=v[i]
        if c:
            for j in range(len(Phi)): v[i-dP+j]-=c*Phi[j]
    return v[:dP]
def is_zero(vec): return all(c==0 for c in reduce_poly(vec))
Sx={}   # S_lab^{-1}[j,i]... store sqrt35 * S_lab^{-1} entries as exponents: (S_lab^{-1})[i,j] = conj(S_lab[j,i]) = e(-r_ji)/sqrt35
for (j,i),r in R['S'].items(): Sx[(i,j)]=(-r)%1
Tx={k:v for k,v in R['T'].items()}
Xe={(IDX[(alpha[k],BES[t])],k):c for (k,t),c in cexp.items()}
Xrows={}; Xcolsd={}
for (i,k),c in Xe.items(): Xrows.setdefault(i,[]).append((k,c)); Xcolsd.setdefault(k,[]).append((i,c))
Srows={}
for (i,j),r in Sx.items(): Srows.setdefault(i,[]).append((j,r))
def addexp(vec,r,coef=1): vec[int((Fr(r)%1)*M_)%M_]+=coef
bad=0
# S: sum_y X[i,y] e(-b(y,k))  ==  2 * sum_j e(-r_ij) X[j,k]       (both sides times 2*sqrt35)
for i in range(N):
    for k in range(N):
        vec=[0]*M_
        for (y,c) in Xrows.get(i,[]): addexp(vec,c-b[y][k])
        for (j,r) in Srows[i]:
            for (kk,c) in Xrows.get(j,[]):
                if kk==k: addexp(vec,r+c,-2)
        if not is_zero(vec): bad+=1
# T: X T_W = T X :  X[i,k] e(q_k) == sum_j T[i,j] X[j,k]
badT=0
Trow={i:(j,r) for (i,j),r in Tx.items()}
for i in range(N):
    for k in range(N):
        vec=[0]*M_
        for (kk,c) in Xrows.get(i,[]):
            if kk==k: addexp(vec,c+q[k])
        j,r=Trow[i]
        for (kk,c) in Xrows.get(j,[]):
            if kk==k: addexp(vec,r+c,-1)
        if not is_zero(vec): badT+=1
print('EXACT check: S-equation failures',bad,' T-equation failures',badT)
# invertibility exactly: X is block-monomial: each alpha has a 2x2 block [c0(z),c0(z');c1(z),c1(z')]; det must be nonzero
dets_ok=True; blocks=[]
from collections import defaultdict
byal=defaultdict(list)
for k in range(N): byal[alpha[k]].append(k)
for al,ks in byal.items():
    z1,z2=ks; a11=cexp[(z1,0)];a21=cexp[(z1,1)];a12=cexp[(z2,0)];a22=cexp[(z2,1)]
    vec=[0]*M_; addexp(vec,a11+a22); addexp(vec,a12+a21,-1)
    if is_zero(vec): dets_ok=False
    blocks.append([str(al),[str(a11),str(a12)],[str(a21),str(a22)]])
print('X invertible (all 2x2 blocks nonsingular, exact):',dets_ok)
# describe c1/c0 relation
rel=Counter()
for k in range(N):
    z=Z[k]; d=(cexp[(k,1)]-cexp[(k,0)])%1
    rel[str(d)]+=1
out.update({'exact_S_failures':bad,'exact_T_failures':badT,'invertible':dets_ok,'c1_minus_c0_exponent_counts':dict(rel)})
pickle.dump({'Z':[tuple(str(v) for v in z) for z in Z],'q':[str(x) for x in q],'alpha':alpha,'BES':BES,'cexp':{f'{k},{t}':str(c) for (k,t),c in cexp.items()}},open('X_explicit.pkl','wb'))
json.dump(out,open('explicit.json','w'),indent=1); print(out)
