# t722u R-E2 slash regen + R-D3 Im-shifted contour diagnostics. DIAGNOSTICS-ONLY, NOT Cat A.
import sys, json, hashlib, math, cmath
from fractions import Fraction as Fr
import mpmath as mp
mp.mp.dps=30
XI="/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/deduce_t713u_ga3_fill/data/Xi_regen_N106.tsv"
assert hashlib.sha256(open(XI,'rb').read()).hexdigest()=="35b186f9df70c2bf247432edcef946e5f66f0ddf1bbca2f4454a30b210707197","BLOCKED: Xi sha"
c={}
for L in open(XI):
    if L.startswith('#') or not L.strip(): continue
    a,b=L.split(); c[Fr(a)]=Fr(b)
sys.path.insert(0,"/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/deduce_t713u_ga3_fill/scripts")
import ga3_fill as G   # psi_any only (t713s4484); chdirs to psi dir
# R-E2
T=[-2,0,2,4]; Y=[Fr("19.801180"),Fr("3.160700"),Fr("20.665180"),Fr("55.302065")]
M=[[Fr(1),Fr(t),Fr(t*t),Fr(1,1+t*t)] for t in T]
def solve(M,y):
    n=len(y); A=[r[:]+[y[i]] for i,r in enumerate(M)]
    for i in range(n):
        p=next(k for k in range(i,n) if A[k][i]!=0); A[i],A[p]=A[p],A[i]
        for k in range(n):
            if k!=i and A[k][i]!=0:
                f=A[k][i]/A[i][i]; A[k]=[u-f*v for u,v in zip(A[k],A[i])]
    return [A[i][n]/A[i][i] for i in range(n)]
abcd=solve(M,Y)
def F(x): t=7*Fr(x)-3; return abcd[0]+abcd[1]*t+abcd[2]*t*t+abcd[3]/(1+t*t)
def slash(x): return mp.mpf(F(x).numerator)/F(x).denominator/mp.sqrt(abs(7*mp.mpf(Fr(x).numerator)/Fr(x).denominator))
X=[Fr(1,7),Fr(3,7),Fr(5,7),Fr(1)]
sl={str(x):slash(x) for x in X}
old={str(x):G.slash(float(x))[0] for x in X}
slash_out=dict(method="exact Fraction 4x4 solve, Written family, Object A residual_factor (dfd2b4b0 L31) as exact rationals",
  abcd_exact=[str(v) for v in abcd], abcd_30=[mp.nstr(mp.mpf(v.numerator)/v.denominator,30) for v in abcd],
  slash_30={k:mp.nstr(v,30) for k,v in sl.items()}, slash_t713u_4dec=old,
  diff={k:float(sl[k]-old[k]) for k in sl}, interp_resid=[str(F(Fr(t+3,7))-y) for t,y in zip(T,Y)])
# R-D3
def I(z):
    s=mp.mpc(0)
    for nu,v in c.items():
        nu_=mp.mpf(nu.numerator)/nu.denominator
        s+= -mp.expjpi(mp.mpf(1)/4)*(mp.mpf(v.numerator)/v.denominator)/mp.sqrt(2*nu_)*mp.exp(2j*mp.pi*nu_*z)
    return s
def tail(eps):
    s=mp.mpf(0); k=4*106+1
    while True:
        nu=mp.mpf(k)/4; t=mp.sqrt(nu)*(2*mp.floor(mp.sqrt(nu/35))+2)/mp.sqrt(2*nu)*mp.exp(-2*mp.pi*nu*eps)
        s+=t; k+=1
        if eps>0 and t<mp.mpf(10)**-25: break
        if eps==0 and k>4*5000: return mp.inf
    return s
def shift(eps): return sum(abs(float(v))/math.sqrt(2*float(nu))*(1-math.exp(-2*math.pi*float(nu)*eps)) for nu,v in c.items())
psi={}
for x in X:
    for y in (x,-1/(7*x)): psi[str(y)]=complex(G.psi_any(y))
rows=[]
for eps in (0.1,0.05,0.02,0.01,0.005,0.0):
    e=mp.mpf(eps); Tb=tail(e)
    for x in X:
        wx=-1/(7*x); hx=mp.mpc(psi[str(x)])*mp.expjpi(-0.25)-I(mp.mpf(float(x))+1j*e)
        hw=mp.mpc(psi[str(wx)])*mp.expjpi(-0.25)-I(mp.mpf(float(wx))+1j*e)
        z=mp.mpf(float(x))+1j*e; wz=-1/(7*z)
        hw2=mp.mpc(psi[str(wx)])*mp.expjpi(-0.25)-I(wz)
        s=sl[str(x)]; d=hx-s*hw; d2=hx-s*hw2
        sig=abs(7*float(x))**-0.5*5e-5*(1+abs(7*float(x)-3)+(7*float(x)-3)**2+1/(1+(7*float(x)-3)**2))
        tol=10*(1e-12+sig*float(abs(hw)))
        Ed=float(Tb*(1+s))+2e-9 if Tb!=mp.inf else float('inf')
        rows.append(dict(eps=eps,x=str(x),Wx=str(wx),h=[float(hx.real),float(hx.imag)],hW=[float(hw.real),float(hw.imag)],
          slash=float(s),delta=[float(d.real),float(d.imag)],absdelta=float(abs(d)),absdelta_W7z_variant=float(abs(d2)),
          tol=tol,tail_T=float(Tb) if Tb!=mp.inf else "inf(divergent majorant)",E_delta=Ed,shift_S=shift(eps)))
json.dump(dict(slash=slash_out,psi={k:[v.real,v.imag] for k,v in psi.items()},rows=rows),sys.stdout,indent=1)
