from mpmath import mp,mpf,sqrt,phi,log
mp.dps=30
o=[]
hbar=mpf('1.054571817e-34'); c=mpf(299792458); L=mpf('1.1056e-52')
o.append(f"17703994: sqrt(hbar*c/Lambda) [units J^1/2 m^2, not dimensionless] = {sqrt(hbar*c/L)}  (paper s0=1616033987)")
o.append(f"   cf. 1/sqrt(Lambda) [m] = {1/sqrt(L)}")
v=(61**2*55)**mpf(1.5)*mpf(3)**(mpf(1)/6); o.append(f"17703994: (61^2*55)^(3/2)*3^(1/6) = {v} (paper '58481 exact integer')")
o.append(f"   58481*539.9 s = {58481*mpf('539.9')} s; tropical year = 31556925.19 s; diff = {58481*mpf('539.9')-mpf('31556925.19')} s")
o.append(f"   kappa=(61^2*55)^(-1/3) = {(61**2*55)**(-mpf(1)/3)} (paper 0.181000...)")
o.append(f"   55+55*phi^7-12*55+484 = {55+55*phi**7-660+484} (paper '=539')")
o.append(f"   539*25 fs = {539*25e-15} s -> {1/(539*25e-15):.4g} Hz (paper: '40.00 Hz')")
o.append(f"   (61/55)^3*3^(1/6)*kappa = {(mpf(61)/55)**3*mpf(3)**(mpf(1)/6)*(61**2*55)**(-mpf(1)/3)} (paper prefactor 2.51e-9)")
def step(n):
  r=n%3
  if r==0: return n//3
  if r==1: return (n-1)//3
  k=0
  while (n+1+2*3**k)%3: k+=1
  return (n+1+2*3**k)//3
n=1616033987; seen={}; path=[n]
while n not in seen:
  seen[n]=len(path)-1; n=step(n); path.append(n)
o.append(f"17703994 map from s0: enters cycle after {seen[n]} steps; cycle length {len(path)-1-seen[n]}; path={path[:30]}")
o.append("   note: 'n≡2 (mod 3)' rule with minimal k: k=0 never works; k=1 always works → n→(n+7)/3")
import math
mx=max(range(1,200000),key=lambda s:(lambda s: (lambda f: f(f,s,0))(lambda f,x,i: i if x in (0,1,2,3) and i>0 or i>2000 else f(f,step(x),i+1)))(s))
o.append(f"18603243 'HQCC: every seed converges in 539±1 steps': max steps to reach {{0..3}} for seeds <2e5 under the 17703994 map ~ log3(n) (e.g. seed {mx})")
o.append(f"18603243: 1/137 = {mpf(1)/137}; CODATA alpha = 0.0072973525643; rel diff = {(mpf(1)/137-mpf('0.0072973525643'))/mpf('0.0072973525643')}")
open('verify_zenodo_numerics.out','w').write("\n".join(o)); print("\n".join(o))
