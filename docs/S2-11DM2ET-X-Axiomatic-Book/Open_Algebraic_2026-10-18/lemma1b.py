# (1) Part B: which products Z_S of local involutions map the orbit O0 = <gamma,-1> nu0 (nu0=(s,-2), Delta coords mod (D,2D), D=2s(s-2)) to itself.
import sys, json, itertools, sympy
from sympy.ntheory.modular import crt
res=[]
for s in range(5,int(sys.argv[1])+1,2):
    D=2*s*(s-2); mod=(D,2*D); G=[[-1,-s],[2,2*s-1]]
    act=lambda x:((G[0][0]*x[0]+G[0][1]*x[1])%mod[0],(G[1][0]*x[0]+G[1][1]*x[1])%mod[1])
    x0=(s%D,(-2)%(2*D)); orb=set(); y=x0
    while True:
        orb.add(y); orb.add(((-y[0])%mod[0],(-y[1])%mod[1])); y=act(y)
        if y==x0: break
    ps=[p for p in sympy.factorint(s*(s-2)) if p!=2]; M=2*D
    fix=[]
    for S in itertools.product((0,1),repeat=len(ps)):
        u=1
        for b,p in zip(S,ps):
            if b: pe=p**sympy.multiplicity(p,M); u=u*int(crt([pe,M//pe],[pe-1,1])[0])%M
        if (u*x0[0]%mod[0],u*x0[1]%mod[1]) in orb: fix.append(tuple(p for b,p in zip(S,ps) if b))
    res.append(dict(s=s,primes=ps,stabilizer=fix,orbit_size=len(orb)))
bad=[r for r in res if r["stabilizer"]!=[()]]
print("odd s in [5,%s]: cases where some nonempty S fixes O0:"%sys.argv[1],len(bad),bad[:10])
json.dump(res,open("lemma1b.json","w"),indent=0)
