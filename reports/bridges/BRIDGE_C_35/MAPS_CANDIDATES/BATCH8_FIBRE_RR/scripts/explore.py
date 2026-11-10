# Explore candidate Resonant fibre weightings on Z/8 from written modular objects ONLY.
# Does NOT read or reference the residual law. Exact rationals.
import json
from fractions import Fraction as F
from sympy.ntheory import legendre_symbol
from sympy import jacobi_symbol
def kron140(n):
    # Kronecker symbol (140/n): 140 = 4*35, disc of Q(sqrt35)
    from sympy.ntheory.residue_ntheory import jacobi_symbol as J
    from math import gcd
    if gcd(n,140)!=1: return 0
    # (140/n) = (4/n)(35/n) ; (4/n)=1 for odd n; (35/n) Kronecker for odd n>0 via reciprocity
    n=abs(n); return J(35,n) if False else _k(35,n)
def _k(a,n):
    from sympy.ntheory import jacobi_symbol as J
    # Kronecker (a/n), n odd positive, a=35 ≡ 3 mod 4: (35/n) = (n/35)*(-1)^((n-1)/2)
    return J(n%35,35)*(-1)**((n-1)//2)
def mass(f, period):
    c=[F(0)]*8
    for x in range(period):
        c[f(x)%8]+=F(1,period)
    return c
cands={}
# unary thetas, x68 scaling (Map-C2 convention): 170n^2, 2R^2, 595m^2 ; index over Z (uniform density)
cands['A68_5n2/2']=mass(lambda n:170*n*n,8)
cands['B68_R2/34']=mass(lambda n:2*n*n,8)
cands['C68_35m2/4']=mass(lambda n:595*n*n,8)
cands['POOL68']=[(a+b+c)/3 for a,b,c in zip(cands['A68_5n2/2'],cands['B68_R2/34'],cands['C68_35m2/4'])]
# minimal integer scaling variants (x2, x34, x4)
cands['Amin_5n2']=mass(lambda n:5*n*n,8)
cands['Bmin_R2']=mass(lambda n:n*n,8)
cands['Cmin_35m2']=mass(lambda n:35*n*n,8)
# chi_140 on n mod 8 over one period lcm(140,8)=280
k=[kron140(n) for n in range(280)]
assert sum(k)==0
ab=[F(0)]*8; sg=[F(0)]*8
for n in range(280):
    ab[n%8]+=abs(k[n]); sg[n%8]+=k[n]
tot=sum(ab); cands['ABSCHI140']=[x/tot for x in ab]
cands['SIGNCHI140_raw']=sg
out={kk:[str(x) for x in v] for kk,v in cands.items()}
print(json.dumps(out,indent=1))
json.dump(out,open('data/explore.json','w'),indent=1)
