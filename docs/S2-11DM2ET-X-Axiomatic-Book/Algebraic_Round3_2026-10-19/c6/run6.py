# x=0 radial coefficients of H_s with walls c1=(-1,1), c2=(-a,b); PSLQ in basis {1, sqrt(sqf(Delta))} (Cat B recognition).
import sys, json, math, mpmath as mp, sympy as sp
from asym_general import expansion
mp.mp.dps=70
def edge(s,a,b):
    m,bb=s*(a-b), s*b-2*a; g=math.gcd(m,abs(bb)); return (m//g, bb//g)
s,a,b=map(int,sys.argv[1:4]); K=int(sys.argv[4]) if len(sys.argv)>4 else 9
u2=edge(s,a,b); c=expansion(s,0,1,K,u2=u2)
D=(s-2)*((2*a-b)*s*b-2*a*a)//(b*b) if b==1 else sp.Rational((s-2)*(2*a*a-2*s*a*b+s*b*b)*-1, 1)
D=sp.Rational(-(s-2)*(2*a*a-2*s*a*b+s*b*b))   # 4Q(c1)Q(c2) = (s-2)*(-2Q(c2))
core=sp.sqrt(D).as_coeff_Mul()[1]**2 if not sp.sqrt(D).is_rational else 1
out=dict(s=s,a=a,b=b,u2=u2,Delta=str(D),sqf=str(core),coeffs={})
for e,v in c.items():
    rec=dict(val=mp.nstr(v.real,65))
    if e%2:
        r=v.real/mp.sqrt(2*mp.pi*s)
        basis=[r,1]+([mp.sqrt(int(core))] if core!=1 else [])
        rec['pslq']=mp.pslq(basis,maxcoeff=10**28,maxsteps=10**7,tol=mp.mpf(10)**-55)
    out['coeffs'][e]=rec
print(json.dumps(out,default=str)); json.dump(out,open(f"run6_s{s}_a{a}_b{b}.json","w"),indent=1,default=str)
