# Frozen (chmod a-w + sidecar) before the logged run. MR2 2026-11-09, OW d5eaeef3 stage 2 under OW 8b26c786 (Group A = Aut+(48) x wall Z2).
# Charged S^4 towers (U(1)_twist charge q != 0, SU(2)_R spin j), spin-2 only. Resonant algebra naming: RA-4 (charged reduction), RA-5 (Landau/Maass ladder),
# RA-6 (Aut+ invariants in H^0(K^m)), RA-7 (assembled Group-A-invariant charged spin-2 masses). Additive; no network.
import numpy as np, sympy as sp, hashlib, time, io, contextlib
def P(*a): print(*a, flush=True)
T0=time.time(); R='/workspace/quantum-comp/reports/'
kk=R+'MR2_MN2_KK_TRUNCATION_BOLZA_AUT48_ISOM96_WALL_Z2_2026-11-09.py'; s1=R+'MR2_MN2_KK_A_S4_DEPENDENT_SPIN2_AUT48_2026-11-09.py'
for p_,e_ in ((kk,'88949658'),(s1,'17f821d2')):
    h=hashlib.sha256(open(p_,'rb').read()).hexdigest(); P(f"[0] {p_.split('/')[-1]} sha256 {h} ({'MATCH '+e_ if h.startswith(e_) else 'MISMATCH'})")
src=open(kk).read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(src.split('# ---------------- W:')[0])
    blk=src.split('# ---------------- S:')[1].split('src_v2=')[0].split('\n',1)[1]; exec(blk)
v2=R+'MR2_TWISTED_VACUA_ADOPTION_BLOCKERS_RIEMANN_SYSTOLE_FULL_EOM_2026-11-09_V2.py'
P(f"[0] V2 twist parameters: line 'a1=(1+zv)/2, a2=(1-zv)/2' present: {'a1=(1+zv)/sp.Integer(2), a2=(1-zv)/sp.Integer(2)' in open(v2).read()} -> MN2 (z=1): a1 = 1, a2 = 0")
# ---- RA-4: charged reduction check (full 11D Bachas-Estes op vs 2*H_q + mu) ----
X1v=2**sp.Rational(-3,5); X2v=X1v**sp.Rational(-2,3); F0v=(1/(X1v*X2v)**2)**-2; G0v=X1v*X2v/8*(2*X2v)
num={X1s:X1v,X2s:X2v,F0s:F0v,G0s:G0v,a1s:1,a2s:0}
Gn=cand_metric()[0].subs(num); w7=cand_metric()[1]
crd=[sp.Symbol('t',real=True),x1_,x2_,x3_,r_,u_,v_,al_,be_,p1_,p2_]
Ginv=Gn.inv(); sqrtg=sp.sqrt(-Gn.det()); e2A=(w7*F0s).subs(num)
def full_op(psi):
    tot=0
    for a in range(5,11):
        for b in range(5,11):
            if Ginv[a,b]!=0: tot+=sp.diff(sqrtg*Ginv[a,b]*sp.diff(psi,crd[b]),crd[a])
    return -e2A*tot/sqrtg
m0,m1,m2=sp.cos(al_),sp.sin(al_)*sp.cos(be_),sp.sin(al_)*sp.sin(be_)
def Hq(F,q,sgn): return -v_**2*(sp.diff(F,u_,2)-2*sp.I*sgn*q/v_*sp.diff(F,u_)-(q/v_)**2*F+sp.diff(F,v_,2))
rng=np.random.default_rng(5)
for q,S4,mu,lab in [(1,m1*sp.exp(sp.I*p1_),7,'nu (l=1,j=0,q=1)'),(2,m1**2*sp.exp(2*sp.I*p1_),16,'nu^2 (l=2,j=0,q=2)'),(1,m0*m1*sp.exp(sp.I*p1_),2*10+4-1,'m0 nu (l=2,j=1,q=1)'),(-3,m1**3*sp.exp(-3*sp.I*p1_),9+18,'nubar^3 (l=3,j=0,q=-3)')]:
    F=sp.exp(sp.Rational(3,2)*sp.I*u_)*v_**sp.Rational(5,2)
    fo=full_op(F*S4)
    for sgn in (1,-1):
        ex=2*Hq(F,q,sgn)*S4+mu*F*S4; worst=0
        for _ in range(3):
            pt={al_:rng.uniform(0.3,2.8),be_:rng.uniform(0.1,1.4),u_:rng.uniform(-1,1),v_:rng.uniform(0.5,2),r_:1.1,p1_:0.3,p2_:0.7}
            a_=complex(sp.N(fo.subs(pt),20)); b_=complex(sp.N(ex.subs(pt),20)); worst=max(worst,abs(a_-b_)/max(1,abs(b_)))
        if worst>=1e-10: P(f"[RA-4] {lab}: sign s = {sgn:+d} does not match (max rel diff {worst:.1e})")
        else: P(f"[RA-4] full 11D op on F(u,v)*{lab}: = 2 H_q F + mu F with mu = {mu} = 2l(l+3)+2j(j+1)-q^2 and H_q = -v^2[(d_u - i s q/v)^2 + d_v^2], s = {sgn:+d}: max rel diff {worst:.1e} (a1 = 1)")
# ---- RA-5: ladder (exact sympy): H_b = Delta_(2b) + b^2 with Maass Delta_k = -v^2(d_u^2+d_v^2) + i k v d_u; raising R_k = i v d_u + v d_v + k/2, lowering L_k = i v d_u - v d_v + k/2 ----
k=sp.Symbol('k'); Fg=sp.Function('F')(u_,v_); bb=sp.Symbol('b')
Dk=lambda G,kk_: -v_**2*(sp.diff(G,u_,2)+sp.diff(G,v_,2))+sp.I*kk_*v_*sp.diff(G,u_)
Rk=lambda G,kk_: sp.I*v_*sp.diff(G,u_)+v_*sp.diff(G,v_)+kk_*G/2
Lk=lambda G,kk_: sp.I*v_*sp.diff(G,u_)-v_*sp.diff(G,v_)+kk_*G/2
e1=sp.simplify(sp.expand(Hq(Fg,bb,1)-(Dk(Fg,2*bb)+bb**2*Fg)))
e2=sp.simplify(sp.expand(Dk(Rk(Fg,k),k+2)-Rk(Dk(Fg,k),k)))
e3=sp.simplify(sp.expand(Lk(Rk(Fg,k),k+2)-(Dk(Fg,k)+k/2*(1+k/2)*Fg)))
e4=sp.simplify(sp.expand(Dk(v_**(k/2)*sp.exp(sp.I*u_*0)*1,k)-(k/2)*(1-k/2)*v_**(k/2)))
P(f"[RA-5] exact: H_b - (Delta_2b + b^2) = {e1}; Delta_(k+2) R_k - R_k Delta_k = {e2}; L_(k+2) R_k - (Delta_k + (k/2)(1+k/2)) = {e3}; Delta_k on v^(k/2) (holomorphic weight-k type) - (k/2)(1-k/2) = {e4}")
P("[RA-5] => R_k commutes with the Laplacians and L R = Delta + (k/2)(1+k/2) > 0 on every eigenvalue that occurs (lambda > 0 at k = 0; m(1-m) + m(1+m) = 2m at k = 2m), so raising is injective and eigenvalue-preserving.")
P("[RA-5] => on K^n (weight 2n, b = n): spectrum of H_n = { n^2 + m(1-m) : m = 1..n, mult h0(K^m) } U { n^2 + lambda : lambda > 0 scalar Laplace eigenvalue }, with R equivariant for Aut+ (canonical lift);")
P("        n^2 + m(1-m) = n(2k+1) - k(k+1), k = n - m (hyperbolic Landau levels). Completeness of this list is the standard Maass raising/lowering theory (cited; identities above verified exactly).")
# ---- RA-6: Aut+ invariants in H^0(K^m) = Sym^m(rho) + det(rho) (x) Sym^(m-3)(rho), rho = H^0(K) ----
Cs=[cplx(D) for D,_ in G48]
for nm,Mm in [('x->ix',np.array([[1j,0],[0,1]])),('x->(x+1)/(1-x)',np.array([[1,1],[-1,1]],dtype=complex))]:
    Pm,kap=lift_pullback(Mm); dt=np.linalg.det(Mm)
    P(f"[RA-6] eta = dx^3/y^2 transforms by det^3/kappa = {dt**3/kap:.6f}; det of the H^0(K) matrix Pm = {np.linalg.det(Pm):.6f} (equal => eta carries det rho) [{nm}]")
def symtr(C,m):
    if m<0: return 0
    w=np.linalg.eigvals(C); return sum(w[0]**a*w[1]**(m-a) for a in range(m+1))
inv={}
for m in range(1,9):
    ch=np.array([symtr(C,m)+(np.linalg.det(C)*symtr(C,m-3) if m>=3 else 0) for C in Cs]); dim=ch[[i for i,(D,_) in enumerate(G48) if np.allclose(D,np.eye(4))][0]].real
    inv[m]=int(round(np.mean(ch).real))
    orb=(1 if m==1 else 0)+(-(2*m-1)+m//2+(2*m)//3+(7*m)//8 if m>=2 else 0)
    P(f"[RA-6] H^0(K^{m}): dim {int(round(dim))} (RR: {2 if m==1 else 2*m-1}); Aut+-invariant dimension = {np.mean(ch).real:.6f}; control: (2,3,8) orbifold formula dim S_2m = -(2m-1) + [m/2] + [2m/3] + [7m/8] (m>=2; m=1: g(orbifold)=0 -> 0) = {orb if m>=2 else 0}")
# ---- Sigma scalar invariant levels (KK FEM helpers) ----
tsec=src.split('# ---------------- T:')[1].split('SU=[')[0].split('\n',1)[1]
with contextlib.redirect_stdout(io.StringIO()): exec(tsec)
lam=[]
for bc in ('NN','DD'):
    w60,_=solve(60,bc,k=4); w120,_=solve(120,bc,k=4); lam+=[x for x in (4*w120-w60)/3 if x>1e-6]
lam=sorted(lam)[:2]
P(f"[C] Aut+-invariant scalar levels lambda > 0 (FEM n=60/120 Richardson): {[round(x,6) for x in lam]}; uniform-point control m^2 L5^2 = 2 lambda = {[round(2*x,4) for x in lam]}")
# ---- RA-7 assemble: m^2 L5^2 = 2 H + mu, mu = 2l(l+3)+2j(j+1)-q^2, l = j+|q|+2n ----
rows=[]
for q in range(1,9):
    Hs=[(q*q+m*(1-m),f'Landau m={m} (H^0(K^{m}) inv {inv[m]})',inv[m]) for m in range(1,q+1) if inv.get(m,0)>0]+[(q*q+x,f'raised scalar lambda={x:.5f}',1) for x in lam]
    for H,lab,mult in Hs:
        for j in range(0,4):
            for n in range(0,3):
                l=j+q+2*n; mu=2*l*(l+3)+2*j*(j+1)-q*q
                rows.append((2*H+mu,q,j,l,H,lab,mult))
rows.sort()
P("[RA-7] lowest Group-A-invariant charged spin-2 modes (each q also at -q; SU(2)_R multiplet dim 2j+1; x Sigma invariant multiplicity):")
for m2_,q,j,l,H,lab,mult in rows[:14]:
    P(f"     m^2 L5^2 = {m2_:10.5f}  Delta = {2+np.sqrt(4+m2_):9.5f}  |q| = {q}, j = {j}, l = {l}, H_Sigma = {H:.5f} [{lab}], Sigma-invariant mult {mult}")
P("[RA-7] completeness of the list below 120: for |q| >= 7 every Sigma level has H >= |q| and l >= |q|, so m^2 L5^2 >= 2|q| + q^2 + 6|q| >= 105 with Landau invariants only at m = 6, 8 (m <= 8 checked): q=7, m=6 gives 2*19 + 91 = 129; raised-scalar levels for |q| >= 5 give >= 151.")
P(f"[RA-7] q = 1, 2: no Landau-level invariants (H^0(K), H^0(K^2) have none) -> lowest via raised lambda = 23.07856: q=1: {min(r[0] for r in rows if r[1]==1):.5f}, q=2: {min(r[0] for r in rows if r[1]==2):.5f}")
P(f"[done] runtime {time.time()-T0:.1f} s")
