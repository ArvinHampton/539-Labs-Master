# Sample the S-cocycle psi(x) of the E-vector at order t^0 on a grid of rationals in (0,2], test smoothness.
exec(open('evector.py').read().split("a=(Fr(7,10)")[0])
import numpy as np
a=(Fr(7,10),Fr(-1,5)); zero=(Fr(0),Fr(0))
def psi(x):
    kL=Eexp(a,zero,-1/x)[1]
    sk=sum(Eexp(p,neg(a),x)[1] for p in reps)
    return kL-float(x)/math.sqrt(35)*sk
xs=sorted({Fr(h,m) for m in range(1,9) for h in range(1,2*m+1) if math.gcd(h,m)==1 and h<=10})
vals=[(float(x),psi(x),x) for x in xs]
X=np.array([v[0] for v in vals]); Y=np.array([v[1] for v in vals])
out=[f"{str(v[2]):5} x={v[0]:.5f}  psi={v[1].real:+.6e}{v[1].imag:+.6e}i" for v in vals]
for deg in (4,6,8):
    cr=np.polyfit(X,Y.real,deg); ci=np.polyfit(X,Y.imag,deg)
    res=np.max(np.abs(np.polyval(cr,X)-Y.real)+1j*0)+np.max(np.abs(np.polyval(ci,X)-Y.imag))
    out.append(f"polynomial fit degree {deg} on {len(X)} points: max residual {res:.2e}  (max |psi| = {np.max(np.abs(Y)):.2e})")
print("\n".join(out)); open("psi_grid.txt","w").write("\n".join(out)+"\n")
