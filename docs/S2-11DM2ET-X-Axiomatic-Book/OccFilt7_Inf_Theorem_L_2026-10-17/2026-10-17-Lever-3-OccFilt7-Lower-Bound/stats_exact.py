import gzip,math,sys,numpy as np
D=int(sys.argv[1])
ex=[int(l.split()[1]) for l in gzip.open(f'data/exact_{D}.txt.gz','rt')]
def lg(x): 
    x=abs(x); s=str(x); return math.log(int(s[:17]))+ (len(s)-min(17,len(s)))*math.log(10) if x else float('-inf')
L=np.array([lg(x) for x in ex]); S=np.array([(x>0)-(x<0) for x in ex])
d=np.arange(D+1)
print('== per residue mod 14: fit log|g| = c sqrt d + b log d + e on d>2000; sign changes counted for d>300')
for r in range(14):
    if r%7 not in (0,1,2,4): continue
    idx=d[(d%14==r)&(d>2000)]
    X=np.vstack([np.sqrt(idx),np.log(idx),np.ones(len(idx))]).T
    co,*_=np.linalg.lstsq(X,L[idx],rcond=None); res=L[idx]-X@co
    i2=d[(d%14==r)&(d>300)]; sc=np.sum(S[i2][1:]!=S[i2][:-1])
    print(f'r={r:2d}: c={co[0]:.5f} b={co[1]:.3f} e={co[2]:.3f} max|res|={np.abs(res).max():.3f} signchanges(d>300)={sc} sign@end={S[idx][-1]}')
# windowed statistics per decade
print('== growth table: window, max log10|g|, min nonzero log10|g| per class')
for lo,hi in [(248,1000),(1000,10**4),(10**4,10**5)]+([(10**5,10**6)] if D>=10**6 else []):
    row=[]
    for c in (0,1,2,4):
        idx=d[(d%7==c)&(d>=lo)&(d<hi)]
        row.append((round(L[idx].max()/math.log(10),2), round(L[idx].min()/math.log(10),2), int(idx[np.argmin(L[idx])])))
    print(lo,hi,row)
# min |g| / envelope : normalized by exp(fit) of class max
print('== smallest |g(d)| relative to local neighbours (dips), d>1000')
for c in (0,1,2,4):
    idx=d[(d%7==c)&(d>1000)]
    loc=L[idx]-np.maximum.accumulate(L[idx])
    j=np.argsort(loc)[:5]
    print(c,[(int(idx[k]),round(float(loc[k]),2)) for k in j])
