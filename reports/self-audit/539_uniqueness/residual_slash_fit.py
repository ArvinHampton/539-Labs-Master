# RTA Def 8.1/Prop 8.2 (22143607_Final_draft*: ~lines 236-246): residual_factor(x)=a+bt+ct^2+d/(1+t^2), t=7x-3, fitted to 4 sample magnitudes at x=1/7,3/7,5/7,1.
# 4 free coefficients, 4 data points -> exact interpolation for ANY targets (if the 4x4 system is nonsingular). Demonstrate with paper values and random targets.
import numpy as np
xs=np.array([1/7,3/7,5/7,1.0]); t=7*xs-3
A=np.stack([np.ones(4),t,t**2,1/(1+t**2)],1)
print("cond(A) =",np.linalg.cond(A))
for name,y in [("paper magnitudes",np.array([19.8012,1.8248,9.2417,20.9022])),("random",np.random.default_rng(7).uniform(0,50,4)),("s=11-like arbitrary",np.array([3.,1.,4.,1.5]))]:
  target=y*np.sqrt(np.abs(7*xs))  # undo |7x|^{-1/2}
  c=np.linalg.solve(A,target); fit=np.abs(7*xs)**-0.5*(A@c)
  print(f"{name}: coeffs={np.round(c,4)} max rel err={np.max(np.abs(fit-y)/y):.1e}")
