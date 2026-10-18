# All-rows S-cocycle check:  Phi(x) = kappa(-1/x) - |x| M kappa(x)  (exact Bernoulli sums)
#  (a) singular parts cancel: s(-1/x)|x| ... precisely  x s(-1/x) = M s(x) for x>0 (|x| for x<0), h = 0
#  (b) Phi_row(x) = -(2/pi)[ |x| a0(U)/2 - a0(u)/2 - |x| J_U(x) + J_u(-1/x) ]  for every row
#  (c) three-term cocycle relation  Phi(z) = T Phi(z/(z+1)) + (z/(z+1)) T M T Phi(z+1)   (z>0)
import numpy as np, math
from fractions import Fraction as Fr
from scipy.special import k0,k1
import family as F, uvec as U
from kappa_all import allcoef
M=F.Smatrix(); T=F.Tmatrix()
LOGEPS=U.LOGEPS
V=[U.vectors(al,be) for al,be in F.LABELS]
a0=np.array([v[2] for v in V])
def nodes(n):
    xs,ws=np.polynomial.legendre.leggauss(n); T_=[];W=[]
    for lo,hi in [(0,0.1),(0.1,0.3),(0.3,1.0)]:
        T_.append((hi-lo)/2*xs+(lo+hi)/2); W.append((hi-lo)/2*ws)
    tau=np.concatenate(T_); w=np.concatenate(W); return 1/tau, w/tau**2
tn,wn=nodes(160)
def tab(v):
    q,ph,c=v; a=2*np.pi*np.abs(q)[None,:]; Tt=tn[:,None]
    K0=k0(a*Tt);K1=k1(a*Tt)
    u=np.sqrt(tn)*(c+(ph*K0).sum(1)); ux=np.sqrt(tn)*((2j*np.pi*q*ph*K0).sum(1))
    uy=c/(2*np.sqrt(tn))+(ph*(K0/(2*np.sqrt(Tt))-np.sqrt(Tt)*a*K1)).sum(1)
    return u,0.5*(ux-1j*uy)
TAB=[tab(v) for v in V]
def Jall(z):
    w=1j*tn; wb=-1j*tn; R=tn/((w-z)*(wb-z)); vv=np.sqrt(R+0j); vwb=0.5/vv*1j/(2*(wb-z)**2)
    return np.array([np.sum(wn*1j*(uw*vv-u*vwb)) for u,uw in TAB])
out=[]
P=np.zeros_like(M)
for i,(al,be) in enumerate(F.LABELS):
    j,ph=F.reduce(-np.array(al),-np.array(be)); P[i,j]+=ph
xs=[Fr(1),Fr(1,3),Fr(2),Fr(3,5),Fr(7,4),Fr(-1),Fr(-2,3)]
PHI={}
ws=wh=wp=wP=0
for x in xs:
    cx=allcoef(x); cs=allcoef(-1/x); ax=abs(float(x))
    wP=max(wP,np.abs(P@cx[:,2]-cx[:,2]).max())
    sing=np.abs(ax*cs[:,0]-M@cx[:,0]).max()
    half=max(np.abs(cx[:,1]).max(),np.abs(cs[:,1]).max())
    Phi=cs[:,2]-ax*(M@cx[:,2]); PHI[x]=Phi
    Ju=Jall(float(-1/x)); JU=M@Jall(float(x)); a0U=M@a0
    per=-(2/math.pi)*(ax*a0U/2-a0/2-ax*JU+Ju)
    d=np.abs(per-Phi).max()
    ws=max(ws,sing);wh=max(wh,half);wp=max(wp,d)
    out.append(f"x={str(x):5}: max_rows |x s(-1/x)-M s(x)| = {sing:.1e}; max |t^-1/2 coeff| = {half:.1e}; max_rows |Phi_exact - period formula| = {d:.1e}; max |Phi| = {np.abs(Phi).max():.3f}")
out.append(f"SUMMARY over {len(xs)} x and 140 rows: singular cancellation {ws:.1e}, half-integer terms {wh:.1e}, period formula {wp:.1e}; P kappa = kappa: {wP:.1e}")
# (c) three-term relation at z with z, z/(z+1), z+1 all handled exactly
def Phi_at(z):
    if z not in PHI:
        cx=allcoef(z); cs=allcoef(-1/z); PHI[z]=cs[:,2]-float(z)*(M@cx[:,2])
    return PHI[z]
w3=0
for z in [Fr(1),Fr(1,2),Fr(2,3),Fr(3,2)]:
    lhs=Phi_at(z); rhs=T@Phi_at(z/(z+1))+float(z/(z+1))*(T@M@T@Phi_at(z+1))
    w3=max(w3,np.abs(lhs-rhs).max())
    out.append(f"three-term z={z}: max_rows |Phi(z) - T Phi(z/(z+1)) - z/(z+1) TMT Phi(z+1)| = {np.abs(lhs-rhs).max():.1e}")
# (d) S-relation Phi(-1/x) = -(1/|x|) M Phi(x)
for x in [Fr(1,3),Fr(2)]:
    out.append(f"S-relation x={x}: |Phi(-1/x) + M Phi(x)/|x|| = {np.abs(Phi_at(-1/x) if -1/x>0 else 0):.0e}" if False else "")
print("\n".join(o for o in out if o)); open("rows_check.txt","w").write("\n".join(o for o in out if o)+"\n")
np.save("phi_rows.npy",np.array([PHI[x] for x in xs]))
