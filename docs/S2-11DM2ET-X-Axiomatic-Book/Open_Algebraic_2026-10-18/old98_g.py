# (e) Does g = (gamma+I)/(2m) act on t-perp/<t> (the old space at s=98)?  Count <g,-1>-orbits vs <gamma,-1>-orbits there.
import sys, json
from fractions import Fraction as Fr
from item1_lead import data
s=int(sys.argv[1]); m=int(round((s/2)**.5)); p=int(sys.argv[2])
orb,counts,modes,mod,D,Mx,no=data(s,2)
els=list(orb)
Qi=lambda x: 2*x[0]*x[0]+2*s*x[0]*x[1]+s*x[1]*x[1]
cand=[x for x in els if x!=(0,0) and (p*x[0])%mod[0]==0 and (p*x[1])%mod[1]==0 and Qi(x)%(2*D*D)==0]
t=cand[0]
B=lambda x,y: Fr(Qi((x[0]+y[0],x[1]+y[1]))-Qi(x)-Qi(y),2*D*D)
perp=[x for x in els if B(x,t).denominator==1]
add=lambda x,y:((x[0]+y[0])%mod[0],(x[1]+y[1])%mod[1])
cls={}
for x in perp:
    if x in cls: continue
    c=[];y=x
    for j in range(p): c.append(y); y=add(y,t)
    k=min(c)
    for y in c: cls[y]=k
reps=sorted(set(cls.values()))
def gact(x):
    # x/D -> g(x/D) = ((-m x2)/D, (x1/m + 2m x2)/D) ; need integer coords mod D: x1/m requires m | x1 mod D up to adding D and t-multiples
    for j in range(p):
        y=add(x,(j*t[0]%mod[0],j*t[1]%mod[1]))
        for a in range(m):
            x1=y[0]+a*D
            if x1%m==0:
                z=((-m*y[1])%mod[0],(x1//m+2*m*y[1])%mod[1])
                if z in cls: return cls[z]
    return None
G=[[-1,-s],[2,2*s-1]]
gam=lambda x: cls.get(((G[0][0]*x[0]+G[0][1]*x[1])%mod[0],(G[1][0]*x[0]+G[1][1]*x[1])%mod[1]))
neg=lambda x: cls[((-x[0])%mod[0],(-x[1])%mod[1])]
gm={r:gact(r) for r in reps}
ok=all(v is not None for v in gm.values())
def count(ops):
    seen=set(); n=0
    for r in reps:
        if r in seen: continue
        n+=1; st=[r]; seen.add(r)
        while st:
            a=st.pop()
            for f in ops:
                b=f(a)
                if b not in seen: seen.add(b); st.append(b)
    return n
res=dict(s=s,p=p,t=t,n_classes=len(reps),g_well_defined=ok)
res["orbits_gamma_neg"]=count([gam,neg])
if ok:
    res["g_squared_is_gamma"]=all(gm[gm[r]]==gam(r) for r in reps)
    res["orbits_g_neg"]=count([lambda a:gm[a],neg])
print(json.dumps(res,default=int)); json.dump(res,open(f"old_g_{s}.json","w"),default=int)
