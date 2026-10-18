# Generic Appell-Lerch m(x,Q,z) as Laurent series in q; x=sx q^xa, Q=sQ q^Qb, z=sz q^zc (signs +-1)
from collections import defaultdict
M=201; OFF=60
def mono_mul(d1,d2):
    out=defaultdict(int)
    for a,x in d1.items():
        for b,y in d2.items():
            if a+b<M: out[a+b]+=x*y
    return out
def m(sx,xa,sQ,Qb,sz,zc,R=40):
    num=defaultdict(int)
    for r in range(-R,R+1):
        c2=r*(r-1)//2
        sg=(-1)**r*sQ**(c2%2)*sz**(r%2); ex=Qb*c2+zc*r
        us=-(sQ**((r-1)%2))*sx*sz; ue=Qb*(r-1)+xa+zc   # 1/(1 + w), w = -Q^{r-1}xz = us*q^ue... careful: 1-Q^{r-1}xz
        # 1-Q^{r-1}xz = 1 - (sQ^{r-1} sx sz) q^{ue}; let v = sQ^{r-1}sx sz
        v=sQ**((r-1)%2)*sx*sz
        if ue>0:
            for k in range(M):
                if ex+k*ue>=M: break
                num[ex+k*ue]+=sg*v**k
        elif ue<0:  # 1/(1-v q^ue) = -sum_{k>=1} v^{-k} q^{-k ue}
            for k in range(1,M+OFF):
                e2=ex-k*ue
                if e2>=M: break
                num[e2]-=sg*v**k
        else: raise Exception("pole")
    jz=defaultdict(int)
    for n in range(-R,R+1):
        c2=n*(n-1)//2; e=Qb*c2+zc*n
        if e<M: jz[e]+=(-1)**n*sQ**(c2%2)*sz**(n%2)
    lo=min(jz); 
    # invert jz (Laurent, leading lo)
    a=[jz.get(lo+i,0) for i in range(M+OFF)]
    b=[0]*(M+OFF); b[0]=1/a[0] if abs(a[0])!=1 else a[0]
    for k in range(1,M+OFF): b[k]=-sum(a[i]*b[k-i] for i in range(1,k+1))*b[0]
    inv={i-lo:b[i] for i in range(M+OFF)}
    return mono_mul(num,inv)
def g2():
    exec(open('verify.py').read().split("# --- Calibration s=1")[0],globals())
    return g(2,M)
t1=m(1,5,1,12,1,4); t2=m(1,5,1,12,1,8); t3=m(1,1,1,12,1,4); t4=m(1,1,1,12,1,8)
tot=defaultdict(int)
for d,c in ((t1,1),(t2,1)):
    for k,v in d.items(): tot[k]+=c*v
for d in (t3,t4):
    for k,v in d.items(): tot[k-1]+=v
G=g2()
ok=all(tot.get(i,0)==G[i] for i in range(-5,M-2)) 
print("s=2 HM(4.5) line 3 [m(q^5,q^12,q^4)+m(q^5,q^12,q^8)+q^-1 m(q,q^12,q^4)+q^-1 m(q,q^12,q^8)] match to q^198:",ok)
print([tot.get(i,0) for i in range(-2,15)]); print(G[:15])
# last line: 2m(q,-q^3,-1)+2qJ12^3/(J4J_{3,12})
t=m(1,1,-1,3,-1,0)
print("2m(q,-q^3,-1) first:",[2*t.get(i,0) for i in range(0,15)])
bad=[i for i in range(0,M-20) if abs(tot.get(i,0)-G[i])>1e-9]
print("line3 mismatches in [0,180]:",bad[:10])
