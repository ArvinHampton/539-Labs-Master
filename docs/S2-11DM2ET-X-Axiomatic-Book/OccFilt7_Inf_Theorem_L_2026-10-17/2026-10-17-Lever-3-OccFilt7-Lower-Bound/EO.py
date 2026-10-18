# Verify (Cat A identity check): (-1)^m phi_n(m) = [x^m] prod_{odd j<=n}(1+x^j) / prod_{k=floor(n/2)+1}^{n}(1-x^{2k})  (>=0)
# and split (-1)^d g_7(d) = E_d - O_d with E (even n), O (odd n) nonnegative.
import math,sys,gzip
D=int(sys.argv[1]);M=D//7+1;nmax=math.isqrt(D)
# check identity for n<=60, m<=3000
MM=3000
p=[1]+[0]*MM
ok=True
for n in range(1,61):
    for m in range(n,MM+1): p[m]-=p[m-n]
    q=[1]+[0]*MM
    for j in range(1,n+1,2):
        for m in range(MM,j-1,-1): q[m]+=q[m-j]
    for k in range(n//2+1,n+1):
        for m in range(2*k,MM+1): q[m]+=q[m-2*k]
    if any(((-1)**m)*p[m]!=q[m] for m in range(MM+1)) or min(q)<0: ok=False
print('identity+positivity check n<=60, m<=3000:',ok)
p=[1]+[0]*M;E=[0]*(D+1);O=[0]*(D+1)
for n in range(nmax+1):
    if n:
        for m in range(n,M+1): p[m]-=p[m-n]
    T=E if n%2==0 else O
    for m in range(0,(D-n*n)//7+1):
        T[n*n+7*m]+= p[m] if m%2==0 else -p[m]
assert min(E)>=0 and min(O)>=0
ex=None if D>100000 else [int(l.split()[1]) for l in gzip.open(f'data/exact_{D}.txt.gz','rt')]
if ex: print('E-O == (-1)^d g:', all(E[d]-O[d]==(-1)**d*ex[d] for d in range(D+1)))
for c in (0,1,2,4):
    ge=[d for d in range(D+1) if d%7==c and E[d]>=O[d]]
    print(f'class {c}: last d with E_d>=O_d: {ge[-1] if ge else None}; count {len(ge)}; tail list {ge[-12:]}')
import mpmath as mp
y=mp.findroot(lambda y:1-y**7-y**2,0.84); R=(1-mp.sqrt(1-y*y))/y; print("predicted lim E/O =",R)
for D2 in [10**3,10**4,3*10**4,10**5,3*10**5,10**6]:
    if D2<=D:
        for dd in range(D2-13,D2+1):
            if dd%7 in (0,1,2,4): print(dd,"E/O=%.8f"%(E[dd]/O[dd]))
for d in [248,1000,10000,D-13]:
    for dd in range(d,d+7):
        if dd%7 in (0,1,2,4): print(dd,'E',E[dd],'O',O[dd],'(O-E)/O=%.4f'%((O[dd]-E[dd])/O[dd]))
    print()
