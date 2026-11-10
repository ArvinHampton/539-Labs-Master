# Frozen (chmod a-w + sidecar) before the logged run. MR2 2026-11-09, OW d5eaeef3 stage 1 under OW 8b26c786 (Group A = Aut+(48) x wall Z2).
# S^4-dependent spin-2 modes on MN N=2 (V2 metric, Bachas-Estes operator). "Resonant algebra" naming: RA-1 (reduction identity), RA-2 (S^4 radial spectrum), RA-3 (Group A selection).
# Additive; no network.
import numpy as np, sympy as sp, hashlib, time, itertools
from numpy.polynomial import legendre as Lg
def P(*a): print(*a, flush=True)
T0=time.time(); R='/workspace/quantum-comp/reports/'
kk=R+'MR2_MN2_KK_TRUNCATION_BOLZA_AUT48_ISOM96_WALL_Z2_2026-11-09.py'
h=hashlib.sha256(open(kk,'rb').read()).hexdigest()
P(f"[0] KK .py sha256 {h} ({'MATCH 88949658' if h.startswith('88949658') else 'MISMATCH'}); exec'ing its verbatim V2 cand_metric block and its [T] mesh/assemble/solve helpers")
src=open(kk).read()
blk=src.split('# ---------------- S:')[1].split('src_v2=')[0].split('\n',1)[1]
tsec=src.split('# ---------------- T:')[1].split('SU=[')[0].split('\n',1)[1]
import scipy.sparse as sps, scipy.sparse.linalg as spla
exec(tsec.replace('P(f"[T]','(lambda *a:None)(f"[T]'))
exec(blk)
# ---- MN2 point (as in KK [S]) ----
X1v=2**sp.Rational(-3,5); X2v=X1v**sp.Rational(-2,3); X0v=1/(X1v*X2v)**2
F0v=X0v**-2; G0v=X1v*X2v/8*(2*X2v)
P(f"[P] MN2 point: X1 = 2^(-3/5) = {sp.N(X1v,12)}, X2 = X0 = {sp.N(X2v,12)} (X0 - X2 = {sp.nsimplify(sp.N(X0v-X2v,40))}), F0 = {sp.N(F0v,12)}, G0 = {sp.N(G0v,12)}, F0/G0 = {sp.nsimplify(F0v/G0v)}")
s_,t_=float(X2v),float(X1v); F0=float(F0v)
# ---- RA-1: reduction. S^4 in R^5 = R^3 (mu = (m0, m2 e^{i phi2}), X0=X2=s) + R^2 (nu = m1 e^{i phi1}, X1=t); |mu| = cos th, |nu| = sin th.
# Reduced Bachas-Estes operator on psi = f(Sigma) Theta(th) Y_j(mu-hat) e^{i q phi1} (q = 0 here; q != 0 is stage 2):
#   L = 2(-Delta_Sigma) + Lth,  Lth Theta = -(F0/rho) d/dth(4 D^(1/2) H^(-1/2) cos^2 sin Theta') + 4 F0 D [ j(j+1) s/cos^2 + q^2 t/sin^2 ] Theta
#   D = s cos^2 + t sin^2, H = sin^2/s + cos^2/t, rho = D^(-1/2) H^(1/2) cos^2 sin.
Gm,w7=cand_metric(); Gm=Gm.subs({a2s:0})
num={X1s:X1v,X2s:X2v,F0s:F0v,G0s:G0v,a1s:sp.Rational(7,10)}
Gn=Gm.subs(num)
crd=[t_,x1_,x2_,x3_,r_,u_,v_,al_,be_,p1_,p2_] if False else [sp.Symbol('t',real=True),x1_,x2_,x3_,r_,u_,v_,al_,be_,p1_,p2_]
crd=[sp.Symbol('t',real=True),x1_,x2_,x3_,r_,u_,v_,al_,be_,p1_,p2_]
Ginv=Gn.inv(); sqrtg=sp.sqrt(-Gn.det()); e2A=(w7*F0s).subs(num)
def full_op(psi):
    tot=0
    for a in range(5,11):
        for b in range(5,11):
            if Ginv[a,b]!=0: tot+=sp.diff(sqrtg*Ginv[a,b]*sp.diff(psi,crd[b]),crd[a])
    return -e2A*tot/sqrtg
th=sp.Symbol('th',positive=True)
sS,tS,F0S=sp.nsimplify(X2v),sp.nsimplify(X1v),F0v
Dth=sS*sp.cos(th)**2+tS*sp.sin(th)**2; Hth=sp.sin(th)**2/sS+sp.cos(th)**2/tS; rho=Dth**sp.Rational(-1,2)*sp.sqrt(Hth)*sp.cos(th)**2*sp.sin(th)
def red_op(Th,j,q=0):
    return -(F0S/rho)*sp.diff(4*sp.sqrt(Dth)/sp.sqrt(Hth)*sp.cos(th)**2*sp.sin(th)*sp.diff(Th,th),th)+4*F0S*Dth*(j*(j+1)*sS/sp.cos(th)**2+q**2*tS/sp.sin(th)**2)*Th
m0,m1,m2=sp.cos(al_),sp.sin(al_)*sp.cos(be_),sp.sin(al_)*sp.sin(be_)
tests=[('m1^2 (j=0)',m1**2,sp.sin(th)**2,0),('m0 (j=1)',m0,sp.cos(th),1),('m0*m1^2 (j=1)',m0*m1**2,sp.cos(th)*sp.sin(th)**2,1),
       ('m2 cos(phi2)*m1^4 (j=1)',m2*sp.cos(p2_)*m1**4,sp.cos(th)*sp.sin(th)**4,1),('(3m0^2-1+m1^2... ) j=2: 2m0^2-m2^2',2*m0**2-m2**2,sp.cos(th)**2,2)]
rng=np.random.default_rng(3); worst=0
for nm,psi,Th,j in tests:
    fo=full_op(psi); ro=red_op(Th,j)
    for _ in range(3):
        a=rng.uniform(0.2,2.9); b=rng.uniform(0.1,1.4); pt={al_:a,be_:b,u_:rng.uniform(-1,1),v_:rng.uniform(0.5,2),r_:1.3,p1_:0.4,p2_:0.9}
        thv=np.arcsin(np.sin(a)*np.cos(b))
        lhs=float(sp.N((fo/psi).subs(pt),20)); rhs=float(sp.N((ro/Th).subs(th,thv),20))
        worst=max(worst,abs(lhs-rhs)/max(1,abs(rhs)))
    P(f"[RA-1] full 11D Bachas-Estes operator (V2 metric, all cross terms, a1 = 7/10) vs reduced operator on {nm}: max rel diff over 3 random points {worst:.1e}")
P(f"[RA-1] Sigma-only control: on psi = f(u,v), full op = (F0/G0)(-Delta_H2) = 2(-Delta) [KK .py [S], exact]; uniform-point identity m^2 L5^2 = 2 lambda")

# ---- RA-1 exact: H = D/(s t), so D^(1/2) H^(-1/2) = sqrt(s t); with the MN2 constants the reduced operator is an exact shift of the round one
yy=sp.Symbol('q',integer=True); Thf=sp.Function('Theta')(th)
P(f"[RA-1x] exact: H*s*t - D = {sp.simplify(Hth*sS*tS-Dth)}; 4 F0 s t = {sp.nsimplify(sp.simplify(4*F0S*sS*tS))}, 4 F0 s^2 = {sp.nsimplify(sp.simplify(4*F0S*sS**2))}, 4 F0 t^2 = {sp.nsimplify(sp.simplify(4*F0S*tS**2))}")
jj=sp.Symbol('j',nonnegative=True)
round_rad=-1/(sp.cos(th)**2*sp.sin(th))*sp.diff(sp.cos(th)**2*sp.sin(th)*sp.diff(Thf,th),th)+(jj*(jj+1)/sp.cos(th)**2+yy**2/sp.sin(th)**2)*Thf
redg=-(F0S/rho)*sp.diff(4*sp.sqrt(Dth)/sp.sqrt(Hth)*sp.cos(th)**2*sp.sin(th)*sp.diff(Thf,th),th)+4*F0S*Dth*(jj*(jj+1)*sS/sp.cos(th)**2+yy**2*tS/sp.sin(th)**2)*Thf
dif=sp.simplify(sp.expand(sp.powsimp(sp.radsimp(redg-(2*round_rad+(2*jj*(jj+1)-yy**2)*Thf)))))
P(f"[RA-1x] exact (sympy, symbolic j, q, Theta): reduced MN2 operator - [2*(round unit-S^4 radial operator) + 2j(j+1) - q^2] = {dif}")
P("[RA-1x] => mu_{l,j,q} = 2 l(l+3) + 2 j(j+1) - q^2, l = j + |q| + 2n (round S^4 harmonics, l(l+3); control [RA-2] reproduces both the round values and the MN2 values below)")
# ---- RA-2: spectral Galerkin for Lth, basis cos^j sin^|q| P_k(cos 2th)
xg,wg=Lg.leggauss(400); thg=(xg+1)*np.pi/4; wg=wg*np.pi/4
def Lspec(s,t,F0,j,q=0,N=30):
    c,sn=np.cos(thg),np.sin(thg); D=s*c**2+t*sn**2; H=sn**2/s+c**2/t
    rh=D**-0.5*H**0.5*c**2*sn; pk=4*F0*D**0.5*H**-0.5*c**2*sn
    x=np.cos(2*thg); dx=-2*np.sin(2*thg)
    g=c**j*sn**abs(q); dg=(-j*c**(j-1)*sn**(abs(q)+1) if j>0 else 0)+(abs(q)*c**(j+1)*sn**(abs(q)-1) if q else 0)
    B=[];dB=[]
    for k in range(N):
        e=np.zeros(k+1); e[k]=1; pv=Lg.legval(x,e); dpv=Lg.legval(x,Lg.legder(e))*dx
        B.append(g*pv); dB.append(dg*pv+g*dpv)
    B=np.array(B); dB=np.array(dB)
    pot=4*F0*D*((j*(j+1)*s/c**2 if j else 0)+(q*q*t/sn**2 if q else 0))
    A=(dB*pk*wg)@dB.T+(B*rh*pot*wg)@B.T; M=(B*rh*wg)@B.T
    import scipy.linalg as sl
    return np.sort(sl.eigh(A,M,eigvals_only=True))
ctl=[Lspec(1,1,1,j,0,20)[:3] for j in range(3)]
P(f"[RA-2] control round S^4 (s=t=F0=1): Lth eigenvalues j=0,1,2 (first 3) = {[list(np.round(c,8)) for c in ctl]}; exact 4 l(l+3), l = j+2n: j=0 -> 0,40,112; j=1 -> 16,72,160; j=2 -> 40,112,216")
J=5; spec={}
for j in range(J+1):
    a=Lspec(s_,t_,F0,j,0,24); b=Lspec(s_,t_,F0,j,0,34); spec[j]=b[:4]
    ex=[2*(j+2*n)*(j+2*n+3)+2*j*(j+1) for n in range(4)]
    P(f"[RA-2] MN2 Lth, q=0, SO(3)_R spin j={j}: {'  '.join(f'{x:.10f}' for x in b[:4])}  (N=24 vs 34 max diff {np.abs(a[:4]-b[:4]).max():.1e}); closed form {ex}, max diff {np.abs(b[:4]-np.array(ex)).max():.1e}")
# ---- Sigma-only control: invariant levels (Aut+ trivial in I1 (NN) and I2 (DD)), scalar FEM of the KK [T] helpers
lam=[]
for bc in ('NN','DD'):
    w60,_=solve(60,bc,k=4); w120,_=solve(120,bc,k=4); ext=(4*w120-w60)/3; lam+= [x for x in ext if x>1e-6]
lam=sorted(lam)[:3]
P(f"[C] Sigma-only Group-A-invariant levels (FEM n=60/120 Richardson, reproduces KK log NN 23.078559, DD 222.371127): {[round(x,6) for x in lam]} -> m^2 L5^2 = 2 lambda = {[round(2*x,4) for x in lam]}")
# ---- RA-3: Group A selection and the assembled spectrum
P("[RA-3] selection: q = 0 (U(1)_twist-neutral) modes are functions on Sigma times S^4 harmonics; Aut+ acts on Sigma only (canonical lift is trivial on the q = 0 S^4 factor), so invariance <=> f in the Aut+-trivial part (I1 + I2): lambda in {0, 23.07856, 74.93, ..., 222.37 (I2), ...}.")
P("[RA-3] SO(3)_R = SU(2)_R/Z2 commutes with Aut+ and the wall Z2, so it is not projected: every spin j multiplet is kept whole (dim 2j+1); j = 0 = SU(2)_R singlets. Wall Z2 acts on 5D fields only; spin-2 (metric) is wall-even (Neumann at the wall, HW premise). No further removal.")
rows=[]
for lv in [0.0]+lam[:1]:
    for j in spec:
        for n,mu in enumerate(spec[j]):
            if lv==0 and j==0 and n==0: continue
            rows.append((2*lv+mu,lv,j,n,mu))
rows.sort()
P("[RA-3] lowest Group-A-invariant S^4-dependent spin-2 modes (q = 0): m^2 L5^2 = 2 lambda + mu_{j,n}; Delta = 2 + sqrt(4 + m^2 L5^2)")
for m2,lv,j,n,mu in rows[:10]:
    P(f"     m^2 L5^2 = {m2:12.6f}  Delta = {2+np.sqrt(4+m2):9.5f}  [lambda_Sigma = {lv:.5f}, SU(2)_R spin j = {j} (dim {2*j+1}), radial n = {n}, mu = {mu:.6f}]  {'below' if m2<2*lam[0] else 'above'} Sigma-only 46.157")
j0=[r for r in rows if r[2]==0]
P(f"[RA-3] lowest SU(2)_R-singlet S^4-dependent: m^2 L5^2 = {j0[0][0]:.6f} (Delta {2+np.sqrt(4+j0[0][0]):.5f}); lowest overall: {rows[0][0]:.6f} (j = {rows[0][2]}); Sigma-only lowest invariant 2*23.07856 = {2*lam[0]:.6f}")
P(f"[done] runtime {time.time()-T0:.1f} s")
