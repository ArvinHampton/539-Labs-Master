#!/usr/bin/env python3
# MR2 2026-11-09: independent cross-check of NL BPS calibrated-wall files (704df3ee, 89ec258a, f8801bff, ERRATUM18 92dded27), OW d5eaeef3.
# Own code. Not using NL's scripts. CGR inputs transcribed by MR2 from the local text /workspace/pp-audit-kk/cgr.txt ((3.8), (5.15), (5.16)).
# Convention: L = R - (1/2) G_ij dX^i dX^j - V (5D Einstein frame, mostly plus). Level-0: G = 60*delta (i.e. -30(dphi)^2 - 30(dlam)^2).
import sympy as sp, itertools, time, random
T0 = time.time()
def P(s): print(s, flush=True)
ph, la, w, g, l = sp.symbols('phi lambda w g l', real=True)
P("== MR2 cross-check of NL BPS calibrated-wall files ==")
# ---------- 1. B1 / C1-C2 ----------
P("\n== 1. Superpotential (B1, C1, C2) ==")
V38 = g**2*(sp.Rational(1,2)*l**2*sp.exp(12*la-16*ph) - 2*l*sp.exp(-10*ph) - sp.Rational(1,2)*sp.exp(-4*ph)*(3*sp.exp(8*la) + 12*sp.exp(-2*la)))
P("V(3.8), psi=0, T_ab=delta (MR2 transcription: Lpot = g^2{-1/2 e^{12la-16ph} l^2 + 2l e^{-10ph} + 1/2 e^{-4ph}[e^{8la}(TrT)^2 - 2e^{8la}Tr T^2 + 4e^{-2la}TrT]}, TrT=3):")
P(f"  V = {V38}")
W = g/2*(sp.exp(-2*ph)*(2*sp.exp(-6*la) + 3*sp.exp(4*la)) + l*sp.exp(-8*ph+6*la))
X = [ph, la]; Gm = sp.diag(60, 60)
res1 = sp.simplify(sp.expand(2*sum(Gm.inv()[i,j]*sp.diff(W,X[i])*sp.diff(W,X[j]) for i in range(2) for j in range(2)) - sp.Rational(4,3)*W**2 - V38))
P(f"  [M1] V - (2 G^ij W_i W_j - (4/3) W^2) with G = 60 delta  [= (1/30)|dW|^2 - (4/3)W^2]: {res1}")
# flow equations from 1D action, own derivation: L1 = e^{4A}(12A'^2 - 30 ph'^2 - 30 la'^2 - V)
r = sp.symbols('r'); A = sp.Function('A')(r); f = sp.Function('f')(r); h = sp.Function('h')(r)
Vf = V38.subs({ph: f, la: h}); L1 = sp.exp(4*A)*(12*A.diff(r)**2 - 30*f.diff(r)**2 - 30*h.diff(r)**2 - Vf)
EL = [sp.diff(sp.diff(L1, q.diff(r)), r) - sp.diff(L1, q) for q in (A, f, h)]
Ham = 12*A.diff(r)**2 - 30*f.diff(r)**2 - 30*h.diff(r)**2 + Vf
Wf = W.subs({ph: f, la: h})
flow = {A.diff(r): -Wf/3, f.diff(r): sp.diff(W, ph).subs({ph: f, la: h})/30, h.diff(r): sp.diff(W, la).subs({ph: f, la: h})/30}
def apply_flow(e):
    e = e.subs({A.diff(r,2): sp.diff(-Wf/3, r), f.diff(r,2): sp.diff(flow[f.diff(r)], r), h.diff(r,2): sp.diff(flow[h.diff(r)], r)})
    e = e.subs(flow); e = e.subs(flow)
    return sp.simplify(sp.expand(e*sp.exp(-4*A)))
P(f"  [M1] first-order flow A'=-W/3, X'=2G^-1 dW = W_X/30 solves: Hamiltonian {apply_flow(Ham)}; EL_A {apply_flow(EL[0])}; EL_phi {apply_flow(EL[1])}; EL_lam {apply_flow(EL[2])}")
# MN2 point
sub = {ph: sp.log(2)/30, la: sp.log(2)/10, l: -1}
dW = [sp.simplify(sp.diff(W, z).subs(sub)) for z in X]; dV = [sp.simplify(sp.diff(V38, z).subs(sub)) for z in X]
Ws = sp.nsimplify(sp.simplify(W.subs(sub)/g)); Lsq = sp.simplify((3/(Ws*g))**2)
P(f"  [M2] MN2 (l=-1, e^30ph = e^10la = 2): dW = {dW}, dV = {dV}; W*/g = {Ws} (=3*2^(1/3)/2: {sp.simplify(Ws - 3*2**sp.Rational(1,3)/2) == 0}); g^2 L^2 = {sp.simplify(g**2*Lsq)} (= 2^(4/3): {sp.simplify(g**2*Lsq - 2**sp.Rational(4,3)) == 0})")
P(f"       V* = {sp.simplify(V38.subs(sub))}; -12/L^2 = {sp.simplify(-12/Lsq)}; equal: {sp.simplify(V38.subs(sub) + 12/Lsq) == 0}")
P(f"       T entries at MN2: e^(-6la) = {sp.simplify(sp.exp(-6*la).subs(sub))} (MR2 X1 = 2^(-3/5)); e^(4la) = {sp.simplify(sp.exp(4*la).subs(sub))} (MR2 X2 = X0 = 2^(2/5))")
H = sp.Matrix([[sp.diff(V38, a, b).subs(sub) for b in X] for a in X])
M = (Gm.inv()*H*Lsq).applyfunc(sp.simplify)
P(f"  [M2] m^2 L^2 = eig(G^-1 Hess V) L^2 = {[sp.nsimplify(sp.simplify(e)) for e in M.eigenvals()]}  (MR2/NL K1, ecee2668 s7: -4, +12)")
HW = sp.Matrix([[sp.diff(W, a, b).subs(sub) for b in X] for a in X])
Ex = (Gm.inv()*2*HW*sp.sqrt(Lsq)).applyfunc(sp.simplify)
P(f"  [M3] B3: linearised W-flow exponents x L = {[sp.nsimplify(sp.simplify(e)) for e in Ex.eigenvals()]}; eigvecs {[[sp.nsimplify(sp.simplify(x/v[0][1])) for x in v[0]] for _,_,v in Ex.eigenvects()]}")
P(f"  [M3] (D) point not in CGR level-0 sector: dV/dlam at lam=0 = {sp.simplify(sp.diff(V38, la).subs(la, 0))} != 0 for l != 0; (D) has a=0 (no twist) while CGR has the twist with l = -1. (D) check V0=-12/L5^2 done in 5D singlet frame (MR2 crosscheck b44cd004 M5).")
# (5.15)/(5.16) and NL C2
S_, O_, vp = sp.symbols('Sigma Omega varphi', positive=True)
V516 = -g**2*O_**-2*S_**-2*(2*l*sp.exp(2*vp)*O_*S_**3 - sp.Rational(1,2)*sp.exp(4*vp)*l**2 - sp.Rational(1,2)*sp.exp(4*vp)*O_**4 + 4*O_*S_**3 + 2*sp.exp(2*vp)*O_**2 + 2*sp.exp(2*vp)*O_**3*S_**3)
m515 = {S_: sp.exp(-(ph+3*la)), O_: sp.exp(3*ph-la-w), vp: la-3*ph-w/2}
P(f"  [M4] (5.16) potential at z=0 (MR2 transcription) on w=0 via (5.15) minus V(3.8): {sp.simplify(sp.expand(V516.subs(m515).subs(w,0) - V38))}")
kin = sp.expand(6*(sp.diff(m515[S_],ph)*sp.Symbol('dph') + sp.diff(m515[S_],la)*sp.Symbol('dla') + sp.diff(m515[S_],w)*sp.Symbol('dw'))**2/m515[S_]**2
     + 2*(sp.diff(m515[O_],ph)*sp.Symbol('dph') + sp.diff(m515[O_],la)*sp.Symbol('dla') + sp.diff(m515[O_],w)*sp.Symbol('dw'))**2/m515[O_]**2
     + 4*(sp.diff(m515[vp],ph)*sp.Symbol('dph') + sp.diff(m515[vp],la)*sp.Symbol('dla') + sp.diff(m515[vp],w)*sp.Symbol('dw'))**2)
P(f"  [M4] (5.16) kinetic G = diag(6/Sigma^2, 2/Omega^2, 4) pulled back to (phi, lam, w): {sp.simplify(kin)}  (level-0 part must be 60 dph^2 + 60 dla^2)")
W3 = g/(2*O_*S_)*(O_**2*sp.exp(2*vp) + 2*O_*S_**3 + l*sp.exp(2*vp) + 2)   # = -2 sqrt3 g P with NL C2's P
G3 = sp.diag(6/S_**2, 2/O_**2, 4); Y = [S_, O_, vp]
res3 = sp.simplify(sp.expand(2*sum(G3.inv()[i,i]*sp.diff(W3,Y[i])**2 for i in range(3)) - sp.Rational(4,3)*W3**2 - V516))
P(f"  [M4] NL C2: W3 = -2 sqrt3 g P = g/(2 Omega Sigma)(Omega^2 e^2vp + 2 Omega Sigma^3 + l e^2vp + 2): V516 - (2G^ij W_i W_j - 4/3 W^2) on full (Sigma,Omega,varphi) = {res3}")
P(f"  [M4] W3 on w=0 slice minus NL B1 W: {sp.simplify(sp.expand(W3.subs(m515).subs(w,0) - W))}; dW3/dw at w=0: {sp.simplify(sp.diff(W3.subs(m515), w).subs(w,0))} (0 => w=0 slice invariant under the 3D W-flow)")
# ---------- 4. no-wall obstruction ----------
P("\n== 4. Level-0 obstruction (B6, B7, D3) ==")
idt = sp.simplify(sp.expand(sp.diff(W, ph) + 2*W + 3*g*l*sp.exp(6*la-8*ph)))
P(f"  [M7] W_phi + 2W + 3 g l e^(6la-8ph) = {idt}  => 4(W_phi+2W) = +12 g e^(6la-8ph) > 0 at l=-1, g>0")
W3w = W3.subs(m515)
P(f"  [M8] extension to w != 0 (SO(3)-breaking, PP F10 'not covered'): W3_phi + 2 W3 at fixed (lam, w) = {sp.factor(sp.simplify(sp.diff(W3w, ph) + 2*W3w))}")
# D3: trace identity on level-0 faces. Own derivation of fibre volume: det of T^{-1}_ij dmu dmu on S^4, T=diag(t1,t1,t2,t2,t2), t1^2 t2^3 = 1
import mpmath as mp; mp.mp.dps = 30
def fib_ratio(t1, ang):
    t2 = t1**(-mp.mpf(2)/3)
    a1, a2, a3, a4 = ang
    def mu(q):
        b1, b2, b3, b4 = q
        return [mp.cos(b1), mp.sin(b1)*mp.cos(b2), mp.sin(b1)*mp.sin(b2)*mp.cos(b3), mp.sin(b1)*mp.sin(b2)*mp.sin(b3)*mp.cos(b4), mp.sin(b1)*mp.sin(b2)*mp.sin(b3)*mp.sin(b4)]
    Tinv = [1/t1, 1/t1, 1/t2, 1/t2, 1/t2]; Tv = [t1, t1, t2, t2, t2]
    J = [[mp.diff(lambda z: mu([z if k == j else ang[k] for k in range(4)])[i], ang[j]) for j in range(4)] for i in range(5)]
    gT = mp.matrix(4, 4); g1 = mp.matrix(4, 4)
    for p in range(4):
        for q in range(4):
            gT[p,q] = sum(Tinv[i]*J[i][p]*J[i][q] for i in range(5)); g1[p,q] = sum(J[i][p]*J[i][q] for i in range(5))
    m = mu(ang); Dl = sum(Tv[i]*m[i]**2 for i in range(5))
    return mp.det(gT)/mp.det(g1), Dl
for t1 in [mp.mpf('0.6'), mp.mpf('1.7')]:
    ang = [mp.mpf('0.7'), mp.mpf('1.1'), mp.mpf('0.4'), mp.mpf('2.0')]
    rat, Dl = fib_ratio(t1, ang)
    P(f"  [M9] fibre: det(T^-1 dmu dmu)/det(round) = {mp.nstr(rat,20)} ; Delta = mu.T.mu = {mp.nstr(Dl,20)} (float, dps 30)")
Dd, Ap, fp_, hp, eps = sp.symbols('Delta Aprime phiprime lamprime epsilon', positive=True)
dlnD = sp.Symbol('dlnD')  # d_lam ln Delta
# ln det g_int = 2 ln(Delta^(1/3) e^(6ph)) + 4 ln(Delta^(-2/3)) + ln(Delta) ; ln g_xx = 2A + (1/3)ln Delta - 4 ph
Kint = eps*sp.Rational(1,2)*(12*fp_ + (sp.Rational(2,3) - sp.Rational(8,3) + 1)*hp*dlnD)
kx = eps*(Ap - 2*fp_ + sp.Rational(1,6)*hp*dlnD)
P(f"  [M9] (K_int + 6 k_x)/eps = {sp.expand((Kint + 6*kx)/eps)}   (NL D3: 6A' - 6ph' + 1/2 lam' d_lam ln Delta)")
v_, X_ = sp.symbols('v Xv', positive=True)
Wl = sp.diff(W, la); Wp10 = sp.diff(W, ph) + 10*W
s1 = sp.simplify(sp.expand(Wl.subs(l,-1)*2/g*sp.exp(2*ph+6*la)))   # in terms of X = e^{-6ph+12la}, v = e^{10la}
s2 = sp.simplify(sp.expand(Wp10.subs(l,-1)*2/g*sp.exp(2*ph+6*la)))
P(f"  [M9] D3 conditions on W-flows (l=-1), times 2e^(2ph+6la)/g: W_lam -> {s1}; W_phi+10W -> {s2}")
Xe, ve = sp.symbols('Xe ve')
eqs = [s1.subs(sp.exp(-6*ph+12*la), Xe), s2.subs(sp.exp(-6*ph+12*la), Xe)]
eqs = [sp.expand(e.subs(sp.exp(10*la), ve).subs(sp.exp(-6*ph+12*la), Xe)) for e in eqs]
P(f"     rewritten: {eqs}; solve: {sp.solve(eqs, [Xe, ve], dict=True)}  (need Xe>0, ve>0)")
# ---------- 2. D1/D2 Clifford ----------
P("\n== 2. D1/D2: own 32x32 Clifford algebra (exact sympy) ==")
s0 = sp.Matrix([[1,0],[0,1]]); sx = sp.Matrix([[0,1],[1,0]]); sy = sp.Matrix([[0,-sp.I],[sp.I,0]]); sz = sp.Matrix([[1,0],[0,-1]])
def kron(*ms):
    out = ms[0]
    for m_ in ms[1:]: out = sp.kronecker_product(out, m_)
    return out
E = []
for k in range(5):
    E.append(kron(*([sz]*k + [sx] + [s0]*(4-k)))); E.append(kron(*([sz]*k + [sy] + [s0]*(4-k))))
E.append(kron(*[sz]*5))   # 11 Euclidean generators of Cl(11) in 32 dims
Gam = [sp.I*E[0]] + E[1:]   # Gamma_0^2 = -1; eta = diag(-1, 1, ..., 1); lower-index gammas
eta = [-1] + [1]*10
for a in range(11):
    for b in range(11):
        assert Gam[a]*Gam[b] + Gam[b]*Gam[a] == (2*eta[a] if a == b else 0)*sp.eye(32)
P("  Clifford relations {Gamma_a, Gamma_b} = 2 eta_ab verified exactly")
up = lambda a: eta[a]*Gam[a]
def prod(idx):
    out = sp.eye(32)
    for i in idx: out = out*up(i)
    return out
def Gslash(Gc):  # Gc: dict sorted 4-tuple -> value (all spatial indices: up = down)
    out = sp.zeros(32)
    for idx, val in Gc.items(): out += 24*val*prod(idx)
    return out
def Gthree(Gc, a):  # Gamma^{cde} G_{acde}, summed over all c,d,e
    out = sp.zeros(32)
    for idx, val in Gc.items():
        if a in idx:
            pos = idx.index(a); rest = idx[:pos] + idx[pos+1:]
            out += 6*((-1)**pos)*val*prod(rest)
    return out
TAN = list(range(10)); NRM = 10
def nullity(kdiag, Gc, sig, s):
    Gs = Gslash(Gc); rows = []
    for a in TAN:
        rows.append(kdiag[a]*Gam[a] + sp.Rational(sig,144)*(Gam[a]*Gs - 12*Gthree(Gc, a)))
    rows.append(Gam[NRM] - s*sp.eye(32))
    return 32 - sp.Matrix.vstack(*rows).rank()
# C6/M5 face: tangential 0..3 = x (k_x), 4,5 = Sigma (k_Sigma = k_x), 6..9 = transverse y (k_T = -2k_x); G_{6789}
for q in (1, -1):
    for sig in (1, -1):
        for s in (1, -1):
            kd = [1]*4 + [1]*2 + [-2]*4
            n1 = nullity(kd, {(6,7,8,9): -6*q*sig}, sig, s)
            P(f"  [M5] C6 face (k_S=k_x=1, k_T=-2, G_6789=-6 q sigma) q={q} sigma={sig} Gamma_n={s}: solution dim = {n1}")
kd = [1]*4 + [1]*2 + [sp.Rational(-3,2)]*4
P(f"  [M5] control k_T=-1.5: dims over (q,sigma,s), G=-6q sigma: {[nullity(kd, {(6,7,8,9): -6*q*sg}, sg, s) for q in (1,-1) for sg in (1,-1) for s in (1,-1)]}")
P(f"  [M5] control MN2-type face k_x=-1, internal 0, G=0: {[nullity([-1]*4+[0]*6, {}, sg, s) for sg in (1,-1) for s in (1,-1)]}")
random.seed(7)
subs4 = list(itertools.combinations(range(4, 10), 4))
cnt = []
for trial in range(6):
    Gc = {c: random.randint(-9, 9) for c in subs4}
    cnt.append(nullity([-1]*4 + [0]*6, Gc, 1, 1))
P(f"  [M6] MN2-type face (k_x=-1, internal K=0) with 6 random integer internal G (all 15 components): solution dims {cnt}")
# D2 algebra: sum over internal a of Gamma^a (Gamma_a Gslash - 12 Gamma^{cde} G_acde) = -6 Gslash
Gc = {c: random.randint(-5, 5) for c in subs4}
Gs = Gslash(Gc)
lhs = sp.zeros(32)
for a in range(4, 10): lhs += up(a)*(Gam[a]*Gs - 12*Gthree(Gc, a))
P(f"  [M6] identity sum_int Gamma^a(Gamma_a Gslash - 12 Gamma^cde G_acde) + 6 Gslash == 0 for random internal G: {(lhs + 6*Gs).is_zero_matrix}")
P("       => from the x-row (Gslash eps = -144 sigma k_x eps) and the internal rows: K_int eps = (6 sigma/144) Gslash eps = -6 k_x eps  (D2)")
# ---------- 3. D4 constant ----------
P("\n== 3. D4 constant (ERRATUM18) ==")
dl, e_L = sp.symbols('delta eL', positive=True)
P("  MN2 face: k_x = -eL, internal K = 0 (internal metric r-independent at MN2) => K_int + 6k_x = -6 eL.")
P("  |d(K_int)| <= 6 delta (6 diagonal entries, |dK|_op <= delta), |6 d k_x| <= 6 delta => need 12 delta >= 6 eL, i.e. delta >= eL/2.")
P(f"  sharpness witness at delta = eL/2: k_x = -eL/2, each internal k = +eL/2: K_int + 6k_x = {sp.simplify(6*e_L/2 + 6*(-e_L/2))}")
P(f"  NL D4 (10 delta, 3/5) vs ERRATUM18 (12 delta, 1/2): 10 delta -> threshold {sp.Rational(6,10)} eL (not a valid bound: witness above meets the trace at delta=eL/2 < 3eL/5); 12 delta -> 1/2 eL (correct, sharp for the trace)")
# ---------- 5. MR2 wall consistency ----------
P("\n== 5. MR2 wall data from the same face formulas ==")
kxs = -e_L; Kt = 4*kxs
rho = sp.simplify(2*(kxs - Kt)); p_int = sp.simplify(-2*(0 - Kt))   # S^a_b = -(2/kappa^2)(K^a_b - delta K), units 1/kappa^2
P(f"  exact MN2 face (IR kept): rho = {rho}, internal pressure = {p_int} (x kappa^-2) -> stress ratio rho:|p| = {sp.simplify(rho/(-p_int))} (MR2 6:8), null energy rho+p = {sp.simplify(rho+p_int)} (MR2 -2k), deficit/rho = {sp.simplify(-(rho+p_int)/rho)} (L3 1/3)")
P(f"  D2 would require K_int = -6k_x = {6*e_L}; MR2 face has 0 => non-BPS (consistent with D4)")
P(f"\nDONE {time.time()-T0:.0f}s")
