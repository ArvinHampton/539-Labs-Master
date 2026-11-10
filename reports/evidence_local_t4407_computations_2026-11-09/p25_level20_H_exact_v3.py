# Local-derived. t4407 P10 closure: hypothesis H for D2 (+) D5, i.e. rho_{D2} is trivial on Gamma(4) and rho_{D5} is trivial on Gamma(5)
# (hence rho_{D2} (x) rho_{D5} is trivial on Gamma(20) and factors through SL2(Z/20)). EXACT arithmetic in Q(zeta_20) (Fraction coefficients
# mod Phi_20). Same discriminant-form construction and Bruinier normalisation as p25_local_parts_v1 (read only).
import math
from fractions import Fraction as Fr
from sympy import cyclotomic_poly, symbols, Poly
X=symbols('X'); M=20; PHI=Poly(cyclotomic_poly(M,X),X); DEG=PHI.degree()
red=[]
for k in range(2*M):
    r=Poly(X**k,X).rem(PHI).all_coeffs()[::-1]; r=[Fr(int(c)) for c in r]+[Fr(0)]*(DEG-len(r)); red.append(r)
class C:
    __slots__=('v',)
    def __init__(s,v=None): s.v=v if v is not None else [Fr(0)]*DEG
    @staticmethod
    def z(k): return C(list(red[k%M]))
    @staticmethod
    def n(q): c=C(); c.v[0]=Fr(q); return c
    def __add__(s,o): return C([a+b for a,b in zip(s.v,o.v)])
    def __sub__(s,o): return C([a-b for a,b in zip(s.v,o.v)])
    def __mul__(s,o):
        prod=[Fr(0)]*(2*DEG)
        for i,a in enumerate(s.v):
            if a:
                for j,b in enumerate(o.v):
                    if b: prod[i+j]+=a*b
        out=[Fr(0)]*DEG
        for k,c in enumerate(prod):
            if c:
                for t,rc in enumerate(red[k]): out[t]+=c*rc
        return C(out)
    def iszero(s): return all(a==0 for a in s.v)
    def conj(s):
        out=C()
        for i,a in enumerate(s.v):
            if a: out=out+C.z(-i)*C.n(a)
        return out
Ginv=[[Fr(28,-140),Fr(-14,-140)],[Fr(-14,-140),Fr(2,-140)]]
els=sorted({((Ginv[0][0]*a+Ginv[0][1]*b)%1,(Ginv[1][0]*a+Ginv[1][1]*b)%1) for a in range(140) for b in range(140)})
def bil(x,y): return (x[0]*(2*y[0]+14*y[1])+x[1]*(14*y[0]+28*y[1]))%1
def q(x): return (Fr(1,2)*(x[0]*(2*x[0]+14*x[1])+x[1]*(14*x[0]+28*x[1])))%1
def order(x): return math.lcm(x[0].denominator,x[1].denominator)
Dp={2:[x for x in els if order(x) in (1,2,4)], 5:[x for x in els if order(x) in (1,5)]}
def ez(fr): return C.z(int((fr%1)*M))   # e(fr) for fr in (1/20)Z
Lm={'S':((0,-1),(1,0)),'s':((0,1),(-1,0)),'T':((1,1),(0,1)),'t':((1,-1),(0,1))}
inv={'S':'s','s':'S','T':'t','t':'T'}
def mmul(A,B): return ((A[0][0]*B[0][0]+A[0][1]*B[1][0],A[0][0]*B[0][1]+A[0][1]*B[1][1]),(A[1][0]*B[0][0]+A[1][1]*B[1][0],A[1][0]*B[0][1]+A[1][1]*B[1][1]))
def wmat(w):
    Mx=((1,0),(0,1))
    for c in w: Mx=mmul(Mx,Lm[c])
    return Mx
def gamma_schreier(N):  # Schreier generators of Gamma(N) = ker(SL2(Z) -> SL2(Z/N))
    key=lambda Mx: tuple(Mx[i][j]%N for i in range(2) for j in range(2))
    reps={key(((1,0),(0,1))):''}; Q=['']
    while Q:
        w=Q.pop(0); Mx=wmat(w)
        for x in 'ST':
            k=key(mmul(Mx,Lm[x]))
            if k not in reps: reps[k]=w+x; Q.append(w+x)
    gens=[]
    for k,w in reps.items():
        for x in 'ST':
            w2=reps[key(wmat(w+x))]; g=w+x+''.join(inv[c] for c in reversed(w2)); Mg=wmat(g)
            assert key(Mg)==(1,0,0,1)%N if False else all((Mg[i][j]-(1 if i==j else 0))%N==0 for i in range(2) for j in range(2))
            if Mg!=((1,0),(0,1)): gens.append(g)
    return len(reps),gens
for p,N in [(2,4),(5,5)]:
    S_=Dp[p]; n=len(S_)
    G=C()
    for x in S_: G=G+ez(q(x))
    c=G.conj()*C.n(Fr(1,n))                       # e(-sig/8)/sqrt|D| = conj(G)/|D|
    Sm=[[ez(-bil(x,y))*c for y in S_] for x in S_]; Si=[[Sm[j][i].conj() for j in range(n)] for i in range(n)]
    Tm=[ez(q(x)) for x in S_]; Ti=[t.conj() for t in Tm]
    def mv(A,v): return [sum((A[i][j]*v[j] for j in range(n) if not v[j].iszero()),C()) for i in range(n)]
    def apply(w,v):
        for ch in reversed(w):
            v = mv(Sm,v) if ch=='S' else mv(Si,v) if ch=='s' else [a*b for a,b in zip(Tm,v)] if ch=='T' else [a*b for a,b in zip(Ti,v)]
        return v
    idx,gens=gamma_schreier(N)
    bad=0
    for g in gens:
        for b in range(n):
            e=[C.n(1 if i==b else 0) for i in range(n)]
            if not all((a-bb).iszero() for a,bb in zip(apply(g,e),e)): bad+=1; break
    print(f"rho_D{p}: [SL2(Z):Gamma({N})] = {idx} (expected |SL2(Z/{N})| = {N**3*math.prod(1-1/r**2 for r in (2,3,5,7) if N%r==0):.0f}); "
          f"Schreier generators of Gamma({N}): {len(gens)}, max length {max(map(len,gens))}; generators with rho(g) != I (exact): {bad}")
print("=> if both 0: rho_D2 trivial on Gamma(4), rho_D5 trivial on Gamma(5); rho_D2 (x) rho_D5 trivial on Gamma(20) ⊂ Gamma(4)∩Gamma(5): H holds (exact).")
