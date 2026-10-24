# Map A: is G = e(7x/20) K2_0 in V?  A1 exact rank mod 4 primes; A2 exact T-spectrum of the formal symbol space.
from common import *
import json, flint
from sympy import isprime, primitive_root
Lev=1
for m in range(1,16): Lev=Lev*9800*m//gcd(Lev,9800*m)
assert Lev==3531528000
P=[17657640001,21189168001,35315280001,42378336001]
out={'Lev':Lev}
# A2 first (cheap): T on formal 105-symbol span is monomial; exponents of eigenvalues mod 1
TR=T_rows(); perm={}; ph={}
for j,r in enumerate(TR):
    (k,es),=r.items(); perm[j]=k; ph[j]=Fr(es[0],L)
seen=set(); spec=[]
for j in range(105):
    if j in seen: continue
    cyc=[j]; 
    while perm[cyc[-1]]!=j: cyc.append(perm[cyc[-1]])
    seen|=set(cyc); c=len(cyc); tot=sum(ph[i] for i in cyc)%1
    spec+= [((tot+r)/c)%1 for r in range(c)]
out['A2_formal_T_exponents_distinct']=sorted({str(s) for s in spec})
out['A2_zero_in_formal_spec']= any(s==0 for s in spec)
out['A2_K2_0_cycle']={'len':1 if perm[I0]==I0 else 'n/a','exponent':str(ph[I0]) if perm[I0]==I0 else None}
print('A2 zero in spec:',out['A2_zero_in_formal_spec'],'K2_0',out['A2_K2_0_cycle'],flush=True)
for p in P:
    assert isprime(p) and (p-1)%Lev==0
    z=pow(primitive_root(p),(p-1)//Lev,p); assert pow(z,Lev//2,p)!=1
    rows=[]
    for x in XS:
        r=[Gp(*sym_pair(f,i),x,z,p,Lev) for f in FAM for i in range(35)]
        g=Grta_p(x,z,p,Lev)
        # sanity: G = e(7x/20) K2_0 exactly (e(7x/20) needs 20m | Lev)
        e=pow(z,(Lev//(20*x.denominator))*((7*x.numerator)%(20*x.denominator)),p)
        assert g==e*r[I0]%p, ('identity G=e(7x/20)K2_0 fails',x)
        rows.append(r+[g])
    M=flint.nmod_mat(216,105,[v for r in rows for v in r[:105]],p)
    M2=flint.nmod_mat(216,106,[v for r in rows for v in r],p)
    out[str(p)]={'rank_105':M.rank(),'rank_105_plus_G':M2.rank()}
    print(p,out[str(p)],flush=True)
json.dump(out,open('../data/testA.json','w'),indent=1)
