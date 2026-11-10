import json
from sympy import jacobi_symbol, kronecker_symbol
R={}
# C1: order of 6+sqrt35 mod 539
N=539
def mul(a,b): return ((a[0]*b[0]+35*a[1]*b[1])%N,(a[0]*b[1]+a[1]*b[0])%N)
x=(6,1);k=1
while x!=(1,0): x=mul(x,(6,1));k+=1
R['C1']={'order':k,'pass':k in (18,521,539)}
# C2
def dist(c):
    h=[0,0,0]
    for n in range(-10**4,10**4+1): h[(c*n*n)%3]+=1
    t=sum(h); return [v/t for v in h]
d=[dist(170),dist(2),dist(595)]
dom=[max(range(3),key=lambda r:x[r]) for x in d]
R['C2']={'dists':d,'dominant':dom,'pass':all(max(x)>=2/3 for x in d) and len(set(dom))==3}
# C4
sizes=[68]*3+[67]*5; S=[];n=1
for s in sizes:
    S.append(sum(int(kronecker_symbol(140,m)) for m in range(n,n+s))); n+=s
p1=all(abs(v)<=1 for v in S)
a,b=S[:3],S[3:]
p2=(all(v>=0 for v in a) and all(v<=0 for v in b)) or (all(v<=0 for v in a) and all(v>=0 for v in b))
R['C4']={'block_sums':S,'pass':p1 and p2}
# C5
def T3(n): return n//3 if n%3==0 else ((4*n+2)//3 if n%3==1 else (2*n+1)//3)
o=[4880]
while o[-1]!=1: o.append(T3(o[-1]))
R['C5']={'orbit':o,'steps':len(o)-1,'pass':595 in o}
json.dump(R,open('data/results.json','w'),indent=1); print(json.dumps(R))
