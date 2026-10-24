# Map B-exact: check identity (B) with I*G at all 216 points, exactly mod two large primes:
#   G(-1/x) = e(-7/(20x)) * (1/(x sqrt35)) * sum_p e(-B(p,2a)) K3_p(x)      (x>0)
from common import *
import json
from sympy import isprime, primitive_root, nextprime
Lev=1
dens=[9800*m for m in range(1,16)]+[9800*x.numerator for x in XS]+[20*x.numerator for x in XS]+[35,4]
for d in dens: Lev=Lev*d//gcd(Lev,d)
def primes(n):
    out=[];k=1
    while len(out)<n:
        if isprime(k*Lev+1): out.append(k*Lev+1)
        k+=1
    return out
two_a=(2*a[0],2*a[1])
res={'Lev_digits':len(str(Lev))}
for p in primes(2):
    g=primitive_root(p) if p.bit_length()<64 else None
    # find generator of the Lev-th roots: z=h^((p-1)/Lev) with z of exact order Lev
    from sympy import factorint
    fac=factorint(Lev)
    h=2
    while True:
        z=pow(h,(p-1)//Lev,p)
        if all(pow(z,Lev//q,p)!=1 for q in fac): break
        h+=1
    z35=pow(z,Lev//35,p); i4=pow(z,Lev//4,p)
    from sympy import jacobi_symbol
    s35=(-i4*sum(jacobi_symbol(k,35)*pow(z35,k,p) for k in range(1,35)))%p
    assert s35*s35%p==35
    bad=[]
    for x in XS:
        y=-1/x
        lhs=Grta_p(y,z,p,Lev)
        acc=0
        for idx,mu in enumerate(MU):
            ph=(-B(mu,two_a))%1; e=pow(z,int(ph*Lev),p)
            acc+=e*Gp(mu,a,x,z,p,Lev)
        ph=Fr(-7,20)/x%1; e=pow(z,int(ph*Lev),p)
        rhs=e*acc%p*pow(x.numerator*pow(x.denominator,-1,p)%p*s35%p,-1,p)%p
        if lhs!=rhs: bad.append(str(x))
    res[str(p)]={'points':216,'mismatches':len(bad),'bad':bad[:20]}
    print(p,res[str(p)],flush=True)
json.dump(res,open('../data/testB_exact.json','w'),indent=1)
