# Analytic-continuation test of the S-cocycle.
# (i) Fit a holomorphic polynomial in w=z-x0 to Psi(z) sampled ONLY in the upper half-plane,
#     evaluate the fit ON THE REAL AXIS at rationals (incl. large denominators) and compare with
#     the exact finite Bernoulli-sum psi(x) (fastkappa.psi).
import numpy as np, math
from fractions import Fraction as Fr
from lz_continuation import Psi
from fastkappa import psi
K=1/math.sqrt(35)
out=[]
for x0,rad in [(1.0,0.45),(0.5,0.3),(1.6,0.45)]:
    zs=[]
    for r in np.linspace(0.08,rad,9):
        for th in np.linspace(0.12,math.pi-0.12,15):
            zs.append(x0+r*np.exp(1j*th))
    zs=np.array(zs); vals=np.array([Psi(z,K) for z in zs])
    deg=14
    M=np.vander(zs-x0,deg+1,increasing=True)
    c,*_=np.linalg.lstsq(M,vals,rcond=None)
    res=np.max(np.abs(M@c-vals))
    out.append(f"x0={x0}: holomorphic fit deg {deg} on {len(zs)} upper-half-plane points (Im z >= {min(zs.imag):.3f}), max fit residual {res:.2e}")
    tests=sorted({Fr(x0).limit_denominator(1000)+Fr(k,d) for d in (7,13,29,31,47) for k in range(-int(0.35*d),int(0.35*d)+1) if abs(k/d)<=0.6*rad})
    worst=0
    for x in tests:
        if x<=0: continue
        ex=psi(x); fit=np.polyval(c[::-1],float(x)-x0)
        worst=max(worst,abs(ex-fit))
    out.append(f"   compared on real axis at {len(tests)} rationals (denominators up to 47): max |psi_exact - fit| = {worst:.2e}")
    # derivative check at x0
    out.append(f"   fit: psi(x0)={c[0]:.10f}  psi'(x0)={c[1]:.10f}; exact psi(x0)={psi(Fr(x0).limit_denominator(100)):.10f}")
print("\n".join(out)); open("lz_test.txt","w").write("\n".join(out)+"\n")
