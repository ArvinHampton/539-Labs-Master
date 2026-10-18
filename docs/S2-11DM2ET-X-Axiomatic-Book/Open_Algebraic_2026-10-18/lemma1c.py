# (1) Exceptional s (extra reduced classes of norm -4d): does an extra class land in some Z_S O0?  (else cancellation-freeness survives)
import json, math, itertools, sympy
from sympy.ntheory.modular import crt
exc=json.load(open('lemma1.json'))["exceptions"] if False else [(27,4),(245,8),(363,4),(363,14),(847,12),(2025,16),(3971,20),(5043,4),(5043,14),(5043,52),(6877,24),(10935,28),(15125,8),(15125,62),(16337,32),(23275,36)]
out=[]
for s,c in exc:
    D=2*s*(s-2); d=s*(s-2); mod=(D,2*D); G=[[-1,-s],[2,2*s-1]]
    act=lambda x:((G[0][0]*x[0]+G[0][1]*x[1])%mod[0],(G[1][0]*x[0]+G[1][1]*x[1])%mod[1])
    def orbit(x0):
        o=set(); y=x0
        while True:
            o.add(y); o.add(((-y[0])%mod[0],(-y[1])%mod[1])); y=act(y)
            if y==x0: return o
    O0=orbit((s%D,(-2)%(2*D)))
    y=math.isqrt((c*c-4)*d); hits=[]
    for yy in (y,-y):
        x1=(yy-s*c)//2; X=(x1%D,c%(2*D))
        ps=[p for p in sympy.factorint(d) if p!=2]; M=2*D
        for S in itertools.product((0,1),repeat=len(ps)):
            u=1
            for b,p in zip(S,ps):
                if b: pe=p**sympy.multiplicity(p,M); u=u*int(crt([pe,M//pe],[pe-1,1])[0])%M
            if (u*s%D,(-2*u)%(2*D)) in orbit(X): hits.append((yy,[p for b,p in zip(S,ps) if b]))
    out.append(dict(s=s,c=c,extra_class_in_some_ZS_O0=hits))
    print(s,c,hits,flush=True)
json.dump(out,open("lemma1c.json","w"),indent=0)
