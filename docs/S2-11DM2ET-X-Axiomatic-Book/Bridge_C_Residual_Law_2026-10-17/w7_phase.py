# Phase of the W_7 relation on the support: R(x) := G(x) / ( 7^{-1/2} (7x) G(-1/(7x)) ),
# where (7x) is the weight-1 factor (c tau + d) at tau -> x.  If |R| = 1 identically and R is a fixed
# root of unity / character, the leading singular parts admit a weight-1 scalar cancellation on the support.
exec(open('fricke_profile.py').read().split("xs = sorted")[0])
import math
rows=[]
for m in range(1,20):
    for h in range(1,m+1):
        if math.gcd(h,m)!=1: continue
        x=Fr(h,m); gx=G(x); gy=G(-1/(7*x))
        if abs(gx)>1e-9 and abs(gy)>1e-9:
            R=gx/(7**-0.5*float(7*x)*gy)
            rows.append(f"x={str(x):6} |R|={abs(R):.6f} arg(R)/pi={cmath.phase(R)/math.pi:+.6f}")
        elif abs(gx)>1e-9:
            rows.append(f"x={str(x):6} G(x)={gx:.4f} but G(W7 x)=0  -> singular part of C at x cannot be cancelled by any scalar W_7 slash")
print("\n".join(rows)); open('w7_phase.txt','w').write("\n".join(rows)+"\n")
