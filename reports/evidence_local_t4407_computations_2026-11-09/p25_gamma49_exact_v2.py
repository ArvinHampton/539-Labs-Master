# Local-derived. t4407 2/5-parts, exact version of the Gamma0(49)-visibility step of p25_local_parts_v1 (v1's SVD step was float; v1 kept).
# Claim: rho_{D2} (x) rho_{D5} (dim 20, level 20) has NO 1-dim subrepresentation, i.e. no vector v with T v = w v, S v = w' v for a
# character of SL2(Z) (w = i^k, w' = w^-3 = i^k, k=0..3). Method: for each k, the T-eigenspace is spanned by e_x with e(q(x)) = w; the
# restricted map (S - w') : C^{X_w} -> C^20 has full column rank over F_ell (ell = 1 mod 140, so it has a primitive 140th root) =>
# full column rank over Q(zeta_140) (rank cannot increase under reduction mod a prime of Z[zeta][1/(2*5*7)]) => kernel 0 over C. Exact.
import math
from fractions import Fraction as Fr
from sympy import isprime, primitive_root, Matrix, GF
Ginv=[[Fr(28,-140),Fr(-14,-140)],[Fr(-14,-140),Fr(2,-140)]]
els=sorted({((Ginv[0][0]*a+Ginv[0][1]*b)%1,(Ginv[1][0]*a+Ginv[1][1]*b)%1) for a in range(140) for b in range(140)})
def bil(x,y): return (x[0]*(2*y[0]+14*y[1])+x[1]*(14*y[0]+28*y[1]))%1
def q(x): return (Fr(1,2)*(x[0]*(2*x[0]+14*x[1])+x[1]*(14*x[0]+28*x[1])))%1
def order(x): return math.lcm(x[0].denominator,x[1].denominator)
D2=[x for x in els if order(x) in (1,2,4)]; D5=[x for x in els if order(x) in (1,5)]
def add(x,y): return ((x[0]+y[0])%1,(x[1]+y[1])%1)
D25=[add(a,b) for a in D2 for b in D5]; assert len(set(D25))==20
for ell in [2147482681, 2147482121, 2147480161]:
    assert ell%140==1 and isprime(ell)
    z=pow(primitive_root(ell),(ell-1)//140,ell); e=lambda fr: pow(z,int((fr%1)*140)%140,ell)
    G25=sum(e(q(x)) for x in D25)%ell; G25c=sum(e(-q(x)) for x in D25)%ell      # Gauss sum of D2+D5 and its complex conjugate
    assert G25*G25c%ell==20, "G*conj(G) != |D|"
    c=G25c*pow(20,ell-2,ell)%ell                                               # e(-sig/8)/sqrt(20) = conj(G)/20
    S=[[c*e(-bil(x,y))%ell for y in D25] for x in D25]   # S e_y = c sum_x e(-(x,y)) e_x (symmetric)
    i4=pow(z,35,ell)
    res=[]
    for k in range(4):
        w=pow(i4,k,ell); X=[j for j,x in enumerate(D25) if e(q(x))==w]
        if not X: res.append((k,0,'empty')); continue
        Mx=Matrix([[ (S[r][j]-(w if r==j else 0))%ell for j in X] for r in range(20)])
        rk=Mx.rank(iszerofunc=lambda a: a%ell==0) if False else Matrix(Mx).applyfunc(lambda a:a%ell)
        from sympy.polys.matrices import DomainMatrix
        dm=DomainMatrix.from_Matrix(Mx).convert_to(GF(ell)); r=dm.rank()
        res.append((k,len(X),r))
    print(f"ell={ell}: [k, dim T-eigenspace for i^k, F_ell-rank of (S - i^k) on it] =",res, "=> no 1-dim subrep" if all(t[2]==t[1] for t in res if t[2]!='empty') else "=> CHECK")
