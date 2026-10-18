# Leading radial profile G(x) := lim_{t->0} t*C(e(x)e^{-t}) / I  (= Gauss mean of e(x Q_s) over residues).
# Test: does any scalar Fricke-type slash  h(x) - lam*(N x)^{-k} h(-1/(N x))  cancel the t^{-1} singularity
# at all rationals?  Necessary condition: |G(x)| = |lam| |N x|^{2-k} |G(-1/(N x))| for all x.
import cmath, math
from fractions import Fraction as Fr
def G(x):
    x = Fr(x) % 1; m = x.denominator; h = x.numerator; L = 2*m
    s = 0
    for n in range(L):
        for k in range(L):
            Q = n*n + 7*n*k + 7*k*(k+1)//2
            s += cmath.exp(2j*math.pi*((h*Q) % m)/m)
    return s/L**2
xs = sorted({Fr(h,m) for m in range(1,30) for h in range(1,m+1) if math.gcd(h,m)==1})
Gc = {}
def g(x):
    x = Fr(x) % 1
    if x not in Gc: Gc[x] = G(x)
    return Gc[x]
out=[]
for N in (7, 35, 70, 140):
    pairs=[]; zero_mismatch=0
    for x in xs:
        gx=abs(g(x)); gy=abs(g(-1/(N*x)))
        if (gx<1e-9) != (gy<1e-9): zero_mismatch+=1
        if gx>1e-9 and gy>1e-9: pairs.append((math.log(abs(N*x)), math.log(gx/gy), x))
    # least squares  log(gx/gy) = log|lam| + (2-k) log|Nx|
    if len(pairs)<3:
        out.append(f"W_{N}: {len(xs)} rationals; zero-pattern mismatches {zero_mismatch} (G(x)!=0 but G(-1/(Nx))=0 or vice versa); only {len(pairs)} pairs with both nonzero -> no fit"); continue
    n=len(pairs); sx=sum(p[0] for p in pairs); sy=sum(p[1] for p in pairs)
    sxx=sum(p[0]**2 for p in pairs); sxy=sum(p[0]*p[1] for p in pairs)
    slope=(n*sxy-sx*sy)/(n*sxx-sx*sx); icpt=(sy-slope*sx)/n
    res=max(abs(p[1]-icpt-slope*p[0]) for p in pairs)
    out.append(f"W_{N}: {len(xs)} rationals (denominators < 30); zero-pattern mismatches {zero_mismatch}; "
               f"pairs both nonzero {len(pairs)}; best fit k = {2-slope:.4f}, |lam| = {math.exp(icpt):.4f}; max residual in log = {res:.4f}")
for N in (7,):
    out.append("  first zero-pattern mismatches for W_7: " + ", ".join(str(x) for x in xs if (abs(g(x))<1e-9)!=(abs(g(-1/(7*x)))<1e-9))[:200])
    out.append("  sample of W_7 data (x, |G(x)|, |G(-1/(7x))|, |7x|):")
    for x in [Fr(1,7),Fr(3,7),Fr(5,7),Fr(1),Fr(2,3),Fr(1,3),Fr(1,11),Fr(4,9),Fr(1,9)]:
        out.append(f"   {str(x):5} {abs(g(x)):.6f} {abs(g(-1/(7*x))):.6f} {abs(7*x):.4f}")
# exact values of |G| on denominators
out.append("|G(h/m)| by denominator m (all h coprime give same |G|? ):")
for m in range(1,30):
    vals=sorted({round(abs(g(Fr(h,m))),9) for h in range(1,m+1) if math.gcd(h,m)==1})
    out.append(f"  m={m:2}: {vals}")
print("\n".join(out)); open("fricke_profile.txt","w").write("\n".join(out)+"\n")
