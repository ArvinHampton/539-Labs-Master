#!/usr/bin/env python3
# MR2 2026-11-09 cross-check of NL JS-C breathing-mode files (OW d5eaeef3, 90cec14c). Independent of NL/PP code.
# Geometry engine (NumGeom, invariants, cand_metric conventions) exec'd from the frozen V2 .py (sha ad134752...), banner suppressed.
# (a1) NL E1 singlet ODEs vs the full 11D Einstein equations (own metric, own flux RHS);
# (a2) NL E4 identity R_{r a} = (3/2) beta' d_a ln D on the MN2 V2 metric with uniform breathing (own construction);
# (b)  5D Einstein-frame kinetic metric and potential of the singlet truncation; sign of the breathing kinetic term; masses at the (D)-type point;
# (d)  curvature-vs-l_p numbers.
import hashlib, io, contextlib, time
T00 = time.time()
V2 = '/workspace/quantum-comp/reports/MR2_TWISTED_VACUA_ADOPTION_BLOCKERS_RIEMANN_SYSTOLE_FULL_EOM_2026-11-09_V2.py'
raw = open(V2,'rb').read(); h = hashlib.sha256(raw).hexdigest()
assert h == 'ad134752da79e3064e209cd840b0aec53e004e3fa0fec8bbc9299eb12940eb85', h
with contextlib.redirect_stdout(io.StringIO()):
    exec(raw.decode().split('# ======================= MAIN =======================')[0])
mp.mp.dps = 40
def P(s): print(s, flush=True)
P("== MR2 cross-check of NL breathing-mode work (dps 40) ==")
P(f"V2 routines sha256 verified: {h}")
# ---------------- (a1) singlet truncation ----------------
P("\n== (a1) NL E1: ds^2 = e^{2A}dx_{1,3}^2 + dy^2 + e^{2B}(du^2+dv^2)/v^2 + e^{2C} dOmega_4^2, G4 = Q dOmega_4 (unit form), q = Q e^{-4C} ==")
P("   11D sugra (own RHS): R_MN = (1/12)(G_M...G_N... - g_MN G^2/12) => S4 block R = +q^2/3 g ; all other blocks R = -q^2/6 g")
y = sp.symbols('y', real=True); th = sp.symbols('th1:5', real=True)
A1, A2, B0, B1, B2, C0, C1, C2 = sp.symbols('A1 A2 B0 B1 B2 C0 C1 C2', real=True)
Af = A1*y + A2*y**2/2; Bf = B0 + B1*y + B2*y**2/2; Cf = C0 + C1*y + C2*y**2/2
GS = sp.zeros(11)
for i, s_ in enumerate([-1,1,1,1]): GS[i,i] = s_*sp.exp(2*Af)
GS[4,4] = 1; GS[5,5] = sp.exp(2*Bf)/v**2; GS[6,6] = sp.exp(2*Bf)/v**2
om = [1, sp.sin(th[0])**2, (sp.sin(th[0])*sp.sin(th[1]))**2, (sp.sin(th[0])*sp.sin(th[1])*sp.sin(th[2]))**2]
for i in range(4): GS[7+i,7+i] = sp.exp(2*Cf)*om[i]
NS = NumGeom(GS, [t,x1,x2,x3,y,u,v]+list(th), [y,v,th[0],th[1],th[2]], [A1,A2,B0,B1,B2,C0,C1,C2])
def singlet_check(a1, b0, b1, c0, c1, q2, use_constraint_q=True):
    S = 4*a1 + 2*b1 + 4*c1
    if use_constraint_q:
        kin = (S**2 - 4*a1**2 - 2*b1**2 - 4*c1**2)/2
        q2 = 4*(-kin + (-2*mp.exp(-2*b0) + 12*mp.exp(-2*c0))/2)
    a2 = q2/6 - a1*S; b2 = q2/6 - mp.exp(-2*b0) - b1*S; c2 = -q2/3 + 3*mp.exp(-2*c0) - c1*S
    g_, gi_, Rm = NS.at([a1, a2, b0, b1, b2, c0, c1, c2], [mp.mpf(0), mp.mpf('1.3'), mp.mpf('0.9'), mp.mpf('1.2'), mp.mpf('0.7')])
    Ric = invariants(g_, gi_, Rm, 11)[4]
    res = 0
    for i in range(11):
        for j in range(11):
            rhs = (q2/3 if i >= 7 else -q2/6)*g_[i,j]
            res = max(res, abs(Ric[i,j] - rhs))
    return q2, res
for (a1, b0, b1, c0, c1) in [(mp.mpf('-0.7'), mp.mpf('-0.4'), mp.mpf('0.3'), mp.mpf('-0.6'), mp.mpf('-0.2')),
                             (mp.mpf('-1.1'), mp.mpf('-0.8'), mp.mpf('-0.5'), mp.mpf('-0.3'), mp.mpf('0.4'))]:
    q2, res = singlet_check(a1, b0, b1, c0, c1, None)
    P(f"  generic data A'={a1}, B={b0}, B'={b1}, C={c0}, C'={c1}; q^2 from NL constraint = {mp.nstr(q2,12)}: max |R_MN - RHS| with NL's A'',B'',C'' = {mp.nstr(res,3)}")
    q2b, resb = singlet_check(a1, b0, b1, c0, c1, q2*mp.mpf('1.1'), use_constraint_q=False)
    P(f"     control: same data, q^2 x 1.1 (constraint violated, second-order eqs kept): max residual = {mp.nstr(resb,6)} (must be nonzero, in yy only)")
fpB = -mp.log(4)/2; fpC = -mp.log(mp.mpf(8)/3)/2
q2f, resf = singlet_check(mp.mpf(-1), fpB, mp.mpf(0), fpC, mp.mpf(0), mp.mpf(24), use_constraint_q=False)
P(f"  NL fixed point A'=-1, e^-2B=4, e^-2C=8/3, q^2=24: max residual {mp.nstr(resf,3)}")
P(f"  (D)-type ratios: R_H2^2/L^2 = e^(2B) = {mp.nstr(mp.exp(2*fpB),10)} (V2 (D): G0/F0 = (1/6)/(2/3) = 0.25); R_S4^2/L^2 = e^(2C) = {mp.nstr(mp.exp(2*fpC),10)} (V2 (D): (1/4)/(2/3) = 0.375)")
# ---------------- (b) 5D reduction: kinetic sign/normalisation, potential, masses ----------------
P("\n== (b) 5D Einstein frame: a = A + w, w = (2B+4C)/3, dy5 = e^w dy. Constraint 6a'^2 - K_c/2 + U = 0 <-> 6 a5dot^2 - K/4 + V/2 = 0 (L = R - K/2 (dphi)^2 - V): K = 2K_c, V = 2U e^{-2w} ==")
ap, bp, cp, Bs, Cs, Qs = sp.symbols('ap bp cp B C Q', real=True)
Ap = ap - (2*bp + 4*cp)/3; Sx = 4*Ap + 2*bp + 4*cp
kin = sp.expand((Sx**2 - 4*Ap**2 - 2*bp**2 - 4*cp**2)/2)
P(f"  kinetic part of NL constraint with A' = a' - (2B'+4C')/3: {kin}")
Kc = sp.expand(-2*(kin - 6*ap**2)); Km = sp.Matrix([[sp.diff(Kc, bp, 2)/2, sp.diff(Kc, bp, cp)/2], [sp.diff(Kc, bp, cp)/2, sp.diff(Kc, cp, 2)/2]])*2
P(f"  cross terms a'B', a'C' present: {any(sp.diff(kin, ap, z) != 0 for z in (bp, cp))}; K_c = {Kc}; K (= 2K_c) matrix = {Km.tolist()}; eigenvalues {[sp.nsimplify(e) for e in Km.eigenvals()]} -> positive definite: {all(e > 0 for e in Km.eigenvals())}")
P(f"  pure S4 breathing (B fixed): K_CC = {Km[1,1]} > 0, canonical phi = sqrt({Km[1,1]}) C; healthy sign")
w = (2*Bs + 4*Cs)/3
U = sp.exp(-2*Bs) - 6*sp.exp(-2*Cs) + Qs**2*sp.exp(-8*Cs)/4
V = 2*U*sp.exp(-2*w)
B0n = sp.log(sp.Rational(1,4))/2; C0n = sp.log(sp.Rational(3,8))/2; Q0n = sp.sqrt(24)*sp.exp(4*C0n)
sub = {Bs: B0n, Cs: C0n, Qs: Q0n}
grad = [sp.nsimplify(sp.simplify(sp.diff(V, z).subs(sub))) for z in (Bs, Cs)]
H = sp.Matrix([[sp.diff(V, z1, z2).subs(sub) for z2 in (Bs, Cs)] for z1 in (Bs, Cs)]).applyfunc(sp.simplify)
L5sq = sp.simplify(sp.exp(2*w).subs(sub))
V0 = sp.simplify(V.subs(sub))
P(f"  at (D)-type point: dV = {grad}; V0 = {V0}; -12/L5^2 = {sp.simplify(-12/L5sq)} (L5 = e^w)")
M = (Km.inv()*H*L5sq).applyfunc(sp.simplify)
ev = M.eigenvects()
for e, mult, vecs in ev:
    vv = [sp.nsimplify(sp.simplify(x/vecs[0][1])) if vecs[0][1] != 0 else x for x in vecs[0]]
    P(f"  m^2 L5^2 = {sp.nsimplify(e)} (Delta = {sp.nsimplify(2+sp.sqrt(4+e))} = {sp.N(2+sp.sqrt(4+e),10)}), eigvec (dB : dC) = {vv}")
# ---------------- (a2) E4 identity on MN2 with uniform breathing ----------------
P("\n== (a2) NL E4 on the V2 MN2 metric: 7D block x e^{2 gamma beta(r)}, S4 block (all c-terms incl. twist) x e^{2 beta(r)}, beta = b1 (r-1) + b2 (r-1)^2/2 ==")
GAM, BB1, BB2 = sp.symbols('gamma_b b1 b2', real=True)
bet = BB1*(r-1) + BB2*(r-1)**2/2
def breath_metric():
    X1, X2 = X1s, X2s; X0 = 1/(X1*X2)**2
    D = X0*m0**2+X1*m1**2+X2*m2**2
    G = sp.zeros(11); w7 = D**sp.Rational(1,3)*sp.exp(2*GAM*bet); eS = sp.exp(2*bet)
    for i, s_ in enumerate([-1,1,1,1,1]): G[i,i] = w7*F0s*s_/r**2
    G[5,5] = w7*G0s/v**2; G[6,6] = w7*G0s/v**2
    c = eS*D**sp.Rational(-2,3)/4
    dm = [[sp.diff(m, al), sp.diff(m, be)] for m in (m0, m1, m2)]; Xs = [X0, X1, X2]
    for i in range(2):
        for j in range(2):
            G[7+i,7+j] += c*sum(dm[k][i]*dm[k][j]/Xs[k] for k in range(3))
    for k,(ph,ai,mu) in enumerate([(9,a1s,m1),(10,a2s,m2)]):
        fac = c*mu**2/Xs[k+1]
        G[ph,ph] += fac; G[ph,5] += fac*ai/v; G[5,ph] += fac*ai/v; G[5,5] += fac*ai**2/v**2
    return G
NB = NumGeom(breath_metric(), coords, dep, PARAMS+[GAM, BB1, BB2])
fp = FP["MN2(z=1)"]; X1, X2 = fp['X1'], fp['X2']; X0 = (X1*X2)**-2
PAR = [mp.mpf(sp.N(x_, 60)) for x_ in [X1, X2, X0**-2, X1*X2/8*((1-fp['z'])*X1+(1+fp['z'])*X2), 1, 0]]
X1n, X2n = PAR[0], PAR[1]; X0n = 1/(X1n*X2n)**2
def dlnD(a_, b_):
    D = X0n*mp.cos(a_)**2 + X1n*(mp.sin(a_)*mp.cos(b_))**2 + X2n*(mp.sin(a_)*mp.sin(b_))**2
    dDa = 2*mp.sin(a_)*mp.cos(a_)*(-X0n + X1n*mp.cos(b_)**2 + X2n*mp.sin(b_)**2)
    dDb = 2*mp.sin(a_)**2*mp.sin(b_)*mp.cos(b_)*(X2n - X1n)
    return dDa/D, dDb/D
for (a_, b_) in [(mp.mpf('0.7'), mp.mpf('0.4')), (mp.mpf('2.01'), mp.mpf('1.1'))]:
    for gm in [mp.mpf(-1), mp.mpf('-0.5'), mp.mpf(0), mp.mpf('0.5')]:
        for (b1, b2) in [(mp.mpf('0.5'), mp.mpf('0.1')), (mp.mpf('-0.3'), mp.mpf('0.7'))]:
            g_, gi_, Rm = NB.at(PAR+[gm, b1, b2], [mp.mpf(1), mp.mpf(1), a_, b_])
            Ric = invariants(g_, gi_, Rm, 11)[4]
            la, lb = dlnD(a_, b_)
            P(f"  (al,be)=({mp.nstr(a_,3)},{mp.nstr(b_,3)}) gamma={mp.nstr(gm,2)} beta'={mp.nstr(b1,2)} beta''={mp.nstr(b2,2)}: R_r,al/(1.5 beta' dal lnD) = {mp.nstr(Ric[4,7]/(mp.mpf(3)/2*b1*la),16)} ; R_r,be/(1.5 beta' dbe lnD) = {mp.nstr(Ric[4,8]/(mp.mpf(3)/2*b1*lb),16)}")
    g_, gi_, Rm = NB.at(PAR+[mp.mpf('0.5'), mp.mpf(0), mp.mpf(0)], [mp.mpf(1), mp.mpf(1), a_, b_])
    Ric = invariants(g_, gi_, Rm, 11)[4]
    P(f"  control beta = 0 at ({mp.nstr(a_,3)},{mp.nstr(b_,3)}): R_r,al = {mp.nstr(Ric[4,7],3)}, R_r,be = {mp.nstr(Ric[4,8],3)}")
# ---------------- (d) numbers ----------------
P("\n== (d) EFT numbers at N=4880 (l_p = 1) ==")
ell = 2*(mp.pi*N)**(mp.mpf(1)/3); F0 = PAR[2]
P(f"  l = {mp.nstr(ell,10)}; L5 = l sqrt(F0) = {mp.nstr(ell*mp.sqrt(F0),10)}; l_p^2 R_max = 12/l^2 = {mp.nstr(12/ell**2,6)}; l_p^2 sqrt(Riem^2)_sup = sqrt(3408)/l^2 = {mp.nstr(mp.sqrt(3408)/ell**2,6)}; l_p^2 max|K_sec| = (40/3)/l^2 = {mp.nstr(mp.mpf(40)/3/ell**2,6)}")
P(f"  R^4 / R suppression ~ (l_p^2 sqrt Riem^2)^3 = {mp.nstr((mp.sqrt(3408)/ell**2)**3,4)}")
P(f"\nDONE {time.time()-T00:.0f}s")
