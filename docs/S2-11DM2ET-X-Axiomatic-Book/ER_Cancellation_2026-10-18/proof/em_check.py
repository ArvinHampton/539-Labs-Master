# Check of the 1D Euler-Maclaurin formula used in rev2 Sec 6.2 (G3), u in [0,1], order p:
#  sum_{k>=0} f(k+u) = int_0^inf f - sum_{j=1}^p B_j(u)/j! f^{(j-1)}(0) + (-1)^{p+1}/p! int_0^inf Btilde_p(u-y) f^{(p)}(y) dy
# with complex t in a sector, f(y)=exp(-t*(y^2+y+1)) (positive-definite-type quadratic).
import mpmath as mp
mp.mp.dps=30
def Bt(p,x): return mp.bernpoly(p,x-mp.floor(x))
out=[]
for t in [mp.mpf('0.3'), mp.mpc('0.2','0.15'), mp.mpc('0.05','-0.04')]:
  f=lambda y: mp.exp(-t*(y*y+y+1))
  for u in [mp.mpf(0), mp.mpf('0.37'), mp.mpf(1)]:
    for p in [1,2,3]:
      lhs=mp.nsum(lambda k: f(k+u),[0,mp.inf])
      main=mp.quad(f,[0,mp.inf])
      corr=-mp.fsum(mp.bernpoly(j,u)/mp.factorial(j)*mp.diff(f,0,j-1) for j in range(1,p+1))
      pts=[0]+[k+u for k in range(0,200) if k+u>0]+[mp.inf]
      rem=(-1)**(p+1)/mp.factorial(p)*mp.quad(lambda y: Bt(p,u-y)*mp.diff(f,y,p),pts)
      out.append(f"t={mp.nstr(t,3)} u={mp.nstr(u,3)} p={p}: |LHS-RHS|={mp.nstr(abs(lhs-main-corr-rem),3)}")
print("\n".join(out)); open("em_check.txt","w").write("\n".join(out)+"\n")
