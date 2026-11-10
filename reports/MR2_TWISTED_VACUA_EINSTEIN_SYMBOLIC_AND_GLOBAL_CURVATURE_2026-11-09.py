#!/usr/bin/env python3
# MR2 2026-11-09 (OW ff8a1670, item A): EXACT 11D Einstein check for MN1, MN2, BBBW z=2, z=3 at the V2 fixed points, LAMBDA = 1/16.
# Imports the frozen blocker V2 code (sha ad134752...) verbatim up to its MAIN section (cand ansatz, Omega_sym, FP, wedge, perm_sign).
# Method (no tuning, no tolerances):
#  * g = Delta^{-2/3} ghat with ghat RATIONAL; coordinates s_a = tan(alpha/2), s_b = tan(beta/2) make every entry rational.
#  * R_MN(g) from R_MN(ghat) via the exact conformal formula (n = 11, omega = -(1/3) ln Delta, d omega rational).
#  * G4 = *_g Omega = Delta^{1} sqrt|ghat| *'_{ghat} Omega ; flux terms are quadratic in G4, so only |det ghat| (rational) enters:
#    E_MN = R_MN - Delta^4 |det ghat| ( X_MN - ghat_MN Y/12 )/12 ,  X_MN = G'_MPQR G'_N^PQR (ghat), Y = G'^2 (ghat).
#    (e^{-12 omega} = Delta^4.)
#  * Arithmetic in the exact rational-function field Q(X1, X2[, s_a, s_b]); the fixed point is then imposed EXACTLY:
#    X2 = X1 (2z+w)/(1+z), w = sqrt(1+3z^2) = (P - 4z(1-z)^2 X1^5)/Q, numerator reduced modulo the minimal polynomial of X1 over Q.
#    Zero remainder <=> exact zero at the true (algebraic) fixed point. Denominators checked nonzero numerically (60 digits).
#  * r, v: the metric and Omega are invariant under (t,x,r)->lambda(t,x,r) and the H2 isometries (u,v)->(lambda u + c, lambda v)
#    (du/v and du^dv/v^2 invariant), which act transitively on (r) x H2; E_MN is covariant, so E = 0 at r = v = 1 for all (s_a, s_b)
#    implies E = 0 everywhere. Mode 'symbolic' uses r = v = 1 with s_a, s_b symbolic; mode 'points' uses random rational r, v, s_a, s_b.
import sys, time, random, itertools
import sympy as sp, mpmath as mp
from sympy import QQ, field
SRC = '/workspace/quantum-comp/reports/MR2_TWISTED_VACUA_ADOPTION_BLOCKERS_RIEMANN_SYSTOLE_FULL_EOM_2026-11-09_V2.py'
src = open(SRC).read(); exec(src[:src.index('# ======================= MAIN')])
MODE = sys.argv[1] if len(sys.argv) > 1 else 'points'
WHICH = sys.argv[2].split(',') if len(sys.argv) > 2 else list(FP.keys())
def P(s): print(s, flush=True)
sa, sb = sp.symbols('s_a s_b', real=True)
n = 11; DEP = [4, 6, 7, 8]
trig = {sp.cos(al): (1-sa**2)/(1+sa**2), sp.sin(al): 2*sa/(1+sa**2), sp.cos(be): (1-sb**2)/(1+sb**2), sp.sin(be): 2*sb/(1+sb**2)}
J = {7: 2/(1+sa**2), 8: 2/(1+sb**2)}
X0e = 1/(X1s*X2s)**2
def hatmetric():
    X1, X2 = X1s, X2s; X0 = X0e
    D = X0*m0**2+X1*m1**2+X2*m2**2
    G = sp.zeros(11)
    for i, s_ in enumerate([-1,1,1,1,1]): G[i,i] = D*F0s*s_/r**2
    G[5,5] = D*G0s/v**2; G[6,6] = D*G0s/v**2
    c = sp.Rational(1,4)
    dm = [[sp.diff(m, al), sp.diff(m, be)] for m in (m0, m1, m2)]; Xs = [X0, X1, X2]
    for i in range(2):
        for j in range(2):
            G[7+i,7+j] += c*sum(dm[k][i]*dm[k][j]/Xs[k] for k in range(3))
    for k,(ph,ai,mu) in enumerate([(9,a1s,m1),(10,a2s,m2)]):
        fac = c*mu**2/Xs[k+1]
        G[ph,ph] += fac; G[ph,5] += fac*ai/v; G[5,ph] += fac*ai/v; G[5,5] += fac*ai**2/v**2
    return G, D
GH, DEL = hatmetric()
# consistency with the V2 ansatz: GH * Delta^{-2/3} == cand_metric()
chk = sp.simplify((GH*DEL**sp.Rational(-2,3) - cand_metric()).applyfunc(lambda e: sp.simplify(e)))
P(f"check ghat*Delta^(-2/3) == V2 cand_metric(): {chk == sp.zeros(11)}")
Om_s, U_s = Omega_sym()
def to_s(e, legs=()):
    e = e.subs(trig) if False else e.xreplace(trig)
    for L in legs:
        if L in J: e = e*J[L]
    return e
def cand_subs(fp, lam, kap, x1rat=None):
    z = fp['z']
    sub = {F0s: (X1s*X2s)**4, G0s: X1s*X2s/8*((1-z)*X1s+(1+z)*X2s), a1s: fp['a1'], a2s: fp['a2'], LAM: lam, KAP: kap}
    return sub
def minpoly_data(fp):
    z = sp.Integer(fp['z']); w = sp.sqrt(1+3*z**2)
    X1ex = fp['X1']; mpoly = sp.minimal_polynomial(X1ex, X1s)
    if z in (0, 1):
        x2map = sp.nsimplify(fp['X2']/fp['X1'])*X1s
    else:
        Pp = 1+7*z+7*z**2+33*z**3; Qq = 1+4*z+19*z**2
        wexpr = (Pp - 4*z*(1-z)**2*X1s**5)/Qq          # from X1^5 = (P - Q w)/(4 z (1-z)^2)
        x2map = sp.expand(X1s*(2*z+wexpr)/(1+z))
    return mpoly, x2map
def exact_zero_test(num_poly_expr, fp, mpoly, x2map):
    e = sp.expand(num_poly_expr.subs(X2s, x2map))
    rem = sp.rem(sp.Poly(e, X1s), sp.Poly(mpoly, X1s)) if e.has(X1s) else sp.Poly(e, X1s)
    return rem.is_zero, rem
def sdet_f(M, K):
    A = [row[:] for row in M]; m = len(A); d = K.one
    for j in range(m):
        p = next((i for i in range(j, m) if A[i][j] != 0), None)
        if p is None: return K.zero
        if p != j: A[j], A[p] = A[p], A[j]; d = -d
        d = d*A[j][j]; inv = 1/A[j][j]
        for i in range(j+1, m):
            if A[i][j] != 0:
                f = A[i][j]*inv
                for k in range(j, m): A[i][k] = A[i][k] - f*A[j][k]
    return d
BLOCKS = [{0},{1},{2},{3},{4},{5,9,10},{6},{7,8}]
def bl_ok(B, C):
    return all(len(set(B)&b) == len(set(C)&b) for b in BLOCKS) and all((i in C) for i in B if any(i in b and len(b)==1 for b in BLOCKS))
def raise_form(F, gi, p, K):
    out = {}
    for B in itertools.combinations(range(n), p):
        s = K.zero
        for C, val in F.items():
            if not bl_ok(B, C): continue
            dm = sdet_f([[gi[b][c] for c in C] for b in B], K)
            if dm != 0: s = s + dm*val
        if s != 0: out[B] = s
    return out
def compute_E(K, conv, ptsub, fp, lam, kap):
    """conv: sympy expr -> K element. ptsub: dict for coordinate substitution (r,v[,s_a,s_b])."""
    sub = cand_subs(fp, lam, kap)
    Gs = GH.subs(sub); Ds = DEL.subs(sub)
    # transform to (s_a,s_b) coordinates: components with alpha/beta legs pick up Jacobians
    gS = sp.zeros(11)
    for i in range(n):
        for j in range(n):
            if Gs[i,j] != 0: gS[i,j] = to_s(Gs[i,j], (i, j))
    DS = to_s(Ds)
    cs = {4: r, 6: v, 7: sa, 8: sb}
    def ev(e): return conv(e.subs(ptsub))
    g = [[ev(gS[i,j]) if gS[i,j] != 0 else K.zero for j in range(n)] for i in range(n)]
    dg = {}; ddg = {}
    for i in range(n):
        for j in range(i, n):
            if gS[i,j] == 0: continue
            for a in DEP:
                d1 = sp.diff(gS[i,j], cs[a])
                if d1 != 0:
                    dg[(i,j,a)] = dg[(j,i,a)] = ev(d1)
                    for b in DEP:
                        if b < a: continue
                        d2 = sp.diff(d1, cs[b])
                        if d2 != 0:
                            x = ev(d2)
                            for (I,Jj) in [(i,j),(j,i)]:
                                ddg[(I,Jj,a,b)] = x; ddg[(I,Jj,b,a)] = x
    Dv = ev(DS); dD = {a: ev(sp.diff(DS, cs[a])) for a in DEP}; ddD = {(a,b): ev(sp.diff(DS, cs[a], cs[b])) for a in DEP for b in DEP}
    # inverse (block structure)
    gi = [[K.zero]*n for _ in range(n)]
    for bl in BLOCKS:
        idx = sorted(bl); m = len(idx)
        M = [[g[i][j] for j in idx] for i in idx]
        # Gauss-Jordan
        A = [M[i][:] + [K.one if k == i else K.zero for k in range(m)] for i in range(m)]
        for j in range(m):
            p = next(i for i in range(j, m) if A[i][j] != 0); A[j], A[p] = A[p], A[j]
            inv = 1/A[j][j]; A[j] = [x*inv for x in A[j]]
            for i in range(m):
                if i != j and A[i][j] != 0:
                    f = A[i][j]; A[i] = [A[i][k]-f*A[j][k] for k in range(2*m)]
        for a_, i in enumerate(idx):
            for b_, j in enumerate(idx): gi[i][j] = A[a_][m+b_]
    Dg = lambda i,j,a: dg.get((i,j,a), K.zero)
    DDg = lambda i,j,a,b: ddg.get((i,j,a,b), K.zero)
    nz_gi = {a: [d for d in range(n) if gi[a][d] != 0] for a in range(n)}
    # S_dbc, Gamma
    Gam = {}; dGam = {}
    for a in range(n):
        for b in range(n):
            for c in range(b, n):
                s = K.zero
                for d in nz_gi[a]:
                    S = (Dg(d,c,b) + Dg(d,b,c) - Dg(b,c,d))
                    if S != 0: s = s + gi[a][d]*S
                if s != 0: Gam[(a,b,c)] = Gam[(a,c,b)] = s/2
    # d_e gi = - gi (d_e g) gi
    dgi = {}
    for e in DEP:
        T = [[K.zero]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                s = K.zero
                for k in nz_gi[i]:
                    for l in range(n):
                        x = Dg(k,l,e)
                        if x != 0 and gi[l][j] != 0: s = s + gi[i][k]*x*gi[l][j]
                T[i][j] = -s
        dgi[e] = T
    for a in range(n):
        for b in range(n):
            for c in range(b, n):
                for e in DEP:
                    s = K.zero
                    for d in range(n):
                        S = (Dg(d,c,b) + Dg(d,b,c) - Dg(b,c,d))
                        if S != 0 and dgi[e][a][d] != 0: s = s + dgi[e][a][d]*S
                        if gi[a][d] != 0:
                            S2 = DDg(d,c,b,e) + DDg(d,b,c,e) - DDg(b,c,d,e)
                            if S2 != 0: s = s + gi[a][d]*S2
                    if s != 0: dGam[(a,b,c,e)] = dGam[(a,c,b,e)] = s/2
    G = lambda a,b,c: Gam.get((a,b,c), K.zero)
    dG = lambda a,b,c,e: dGam.get((a,b,c,e), K.zero)
    Ric = [[K.zero]*n for _ in range(n)]
    for b in range(n):
        for d in range(b, n):
            s = K.zero
            for a in range(n):
                if a in DEP: s = s + dG(a,b,d,a)
                if d in DEP: s = s - dG(a,a,b,d)
                for e in range(n):
                    x = G(a,a,e)
                    if x != 0: s = s + x*G(e,b,d)
                    y = G(a,d,e)
                    if y != 0: s = s - y*G(e,a,b)
            Ric[b][d] = Ric[d][b] = s
    # conformal: g = e^{2w} ghat, w = -(1/3) ln Delta
    dw = {a: (dD[a]/Dv)*sp.Rational(-1,3) for a in DEP}
    ddw = {(a,b): (ddD[(a,b)]/Dv - dD[a]*dD[b]/Dv**2)*sp.Rational(-1,3) for a in DEP for b in DEP}
    W = lambda a: dw.get(a, K.zero)
    H = [[K.zero]*n for _ in range(n)]
    for M_ in range(n):
        for N_ in range(M_, n):
            s = ddw.get((M_,N_), K.zero)
            for p_ in DEP:
                x = G(p_,M_,N_)
                if x != 0: s = s - x*W(p_)
            H[M_][N_] = H[N_][M_] = s
    lapw = K.zero; dw2 = K.zero
    for M_ in range(n):
        for N_ in nz_gi[M_]:
            lapw = lapw + gi[M_][N_]*H[M_][N_]
            dw2 = dw2 + gi[M_][N_]*W(M_)*W(N_)
    RicF = [[Ric[M_][N_] - 9*(H[M_][N_] - W(M_)*W(N_)) - (lapw + 9*dw2)*g[M_][N_] for N_ in range(n)] for M_ in range(n)]
    # flux
    Om = {}
    for k, val in Om_s.items():
        e = to_s(val.subs(sub), k)
        x = ev(e)
        if x != 0: Om[k] = x
    up7 = raise_form(Om, gi, 7, K)
    Gp = {}
    for B, val in up7.items():
        A = tuple(x for x in range(n) if x not in B)
        Gp[A] = Gp.get(A, K.zero) + perm_sign(B+A)*val
    Gpu = raise_form(Gp, gi, 4, K)
    Y = 24*sum((Gp[A]*Gpu.get(A, K.zero) for A in Gp), K.zero)
    def comp(F, M_, T):
        if M_ in T: return K.zero
        key = tuple(sorted((M_,)+T)); val = F.get(key)
        return perm_sign((M_,)+T)*val if val is not None else K.zero
    triples = list(itertools.combinations(range(n), 3))
    lowM = [[comp(Gp, M_, T) for T in triples] for M_ in range(n)]
    upS = [[comp(Gpu, S, T) for T in triples] for S in range(n)]
    detg = sdet_f(g, K); absdet = -detg
    E = {}
    for M_ in range(n):
        for N_ in range(M_, n):
            s = K.zero
            for ti in range(len(triples)):
                x = lowM[M_][ti]
                if x == 0: continue
                yv = K.zero
                for S in nz_gi[N_]:
                    pass
                # G'_N^{T} = ghat_{NS} G'^{S T}
                yv = sum((g[N_][S]*upS[S][ti] for S in range(n) if g[N_][S] != 0 and upS[S][ti] != 0), K.zero)
                s = s + x*yv
            X = 6*s
            e = RicF[M_][N_] - Dv**4*absdet*(X - g[M_][N_]*Y/12)/12
            if e != 0: E[(M_,N_)] = e
    # Ricci scalar of the full metric (for the cross-check vs V2 numerics): R = e^{-2w} ghat^{MN} R_MN = Delta^{2/3} * Rhat_conf
    Rc = sum((gi[M_][N_]*RicF[M_][N_] for M_ in range(n) for N_ in nz_gi[M_]), K.zero)
    return E, Rc, Dv
# ======================= DRIVER =======================
T0 = time.time()
mp.mp.dps = 60
def fp_num(fp):
    return {X1s: mp.mpf(sp.N(fp['X1'], 80)), X2s: mp.mpf(sp.N(fp['X2'], 80))}
def nz_at_fp(fe, fp, extra):
    # numeric value of a polynomial/expr at the true fixed point (60 digits)
    e = fe.as_expr().subs(extra) if extra else fe.as_expr()
    return mp.mpf(sp.N(e.subs({X1s: sp.N(fp['X1'], 80), X2s: sp.N(fp['X2'], 80)}), 60))
if MODE == 'points':
    K = field([X1s, X2s], QQ)[0]; conv = K.from_expr
    random.seed(20261109)
    NPTS = int(sys.argv[3]) if len(sys.argv) > 3 else 6
    for k in WHICH:
        fp = FP[k]; mpoly, x2map = minpoly_data(fp)
        P(f"\n## {k}: minimal polynomial of X1 over Q: {mpoly}  (deg {sp.degree(mpoly, X1s)}); X2 -> {x2map}")
        tally = [0, 0, 0]
        for ip in range(NPTS):
            q = lambda: sp.Rational(random.randint(1, 97), random.randint(1, 97))
            ptsub = {r: q(), v: q(), sa: q(), sb: q()}
            t1 = time.time()
            E, Rc, Dv = compute_E(K, conv, ptsub, fp, sp.Rational(1,16), 1)
            nzero = 0; bad = []
            for key, e in E.items():
                ok, rem = exact_zero_test(e.numer.as_expr(), fp, mpoly, x2map)
                dnum = nz_at_fp(e.denom, fp, None)
                if ok and dnum != 0: nzero += 1
                else: bad.append((key, ok, mp.nstr(dnum, 5)))
            tally[0] += len(E); tally[1] += nzero
            P(f"  pt {ip}: (r,v,s_a,s_b)=({ptsub[r]},{ptsub[v]},{ptsub[sa]},{ptsub[sb]}): {66} comps; {66-len(E)} identically 0 in Q(X1,X2); "
              f"{nzero}/{len(E)} remaining reduce EXACTLY to 0 mod minpoly; failures {bad[:4]}  [{time.time()-t1:.0f}s]")
        P(f"  {k} SUMMARY: {NPTS} random rational points x 66 components: all exact zero = {tally[0]==tally[1]}")
    if 'CONTROLS' in sys.argv:
        # controls (z=2 point 0): wrong LAMBDA and wrong X1 (exact rational parameters off the fixed point)
        fp = FP["BBBW(z=2)"]; mpoly, x2map = minpoly_data(fp)
        ptsub = {r: sp.Rational(3,7), v: sp.Rational(5,11), sa: sp.Rational(2,9), sb: sp.Rational(7,5)}
        for lam in [sp.Rational(1,8), sp.Rational(0)]:
            E, Rc, Dv = compute_E(K, conv, ptsub, fp, lam, 1)
            nonz = sum(1 for key, e in E.items() if not exact_zero_test(e.numer.as_expr(), fp, mpoly, x2map)[0])
            P(f"CONTROL z=2 LAMBDA={lam}: components NOT zero at the exact fixed point = {nonz} (must be > 0)")
        E, Rc, Dv = compute_E(K, conv, ptsub, fp, sp.Rational(1,16), sp.Rational(11,10))
        nonz = sum(1 for key, e in E.items() if not exact_zero_test(e.numer.as_expr(), fp, mpoly, x2map)[0])
        P(f"CONTROL z=2 flux x 11/10: components NOT zero = {nonz} (must be > 0)")
        # wrong X1: evaluate at X1 -> (11/10) X1* numerically (60 digits), X2 unchanged
        E, Rc, Dv = compute_E(K, conv, ptsub, fp, sp.Rational(1,16), 1)
        x1w = sp.N(fp['X1'], 80)*sp.Rational(11,10); x2v = sp.N(fp['X2'], 80)
        mx = max(abs(sp.N(e.as_expr().subs({X1s: x1w, X2s: x2v}), 30)) for e in E.values())
        P(f"CONTROL z=2 X1 x 1.1 (X2 fixed): max |E_MN| (lower, s-coords) = {sp.N(mx, 5)} (must be >> 0)")
        # cross-check Ricci scalar vs V2 numerics: R(full g) = Delta^{2/3} * Rc ; on-shell R = G^2/144 ; compare to V2 NumGeom at same point
        P(f"cross-check data: z=2 at the control point, R(full)*Delta^(-2/3) = Rc = {sp.N(Rc.as_expr().subs({X1s: sp.N(fp['X1'],80), X2s: sp.N(fp['X2'],80)}), 30)}, Delta = {sp.N(Dv.as_expr().subs({X1s: sp.N(fp['X1'],80), X2s: sp.N(fp['X2'],80)}), 30)}")

elif MODE == 'symbolic':
    K = field([X1s, X2s, sa, sb], QQ)[0]; conv = K.from_expr
    for k in WHICH:
        fp = FP[k]; mpoly, x2map = minpoly_data(fp)
        t1 = time.time()
        E, Rc, Dv = compute_E(K, conv, {r: 1, v: 1}, fp, sp.Rational(1,16), 1)
        P(f"## {k}: symbolic E_MN built in Q(X1,X2,s_a,s_b) at r=v=1: {66-len(E)} comps identically 0, {len(E)} to reduce [{time.time()-t1:.0f}s]")
        allok = True
        for key, e in E.items():
            ok, rem = exact_zero_test(e.numer.as_expr(), fp, mpoly, x2map)
            # denominator: nonzero polynomial at the fixed point for generic (s_a, s_b)
            dok = not exact_zero_test(e.denom.as_expr(), fp, mpoly, x2map)[0]
            allok &= (ok and dok)
            P(f"   E{key}: numerator == 0 mod minpoly(X1) identically in (s_a,s_b): {ok}; denominator not identically 0: {dok}")
        P(f"## {k}: FULL SYMBOLIC ZERO = {allok}  [{time.time()-t1:.0f}s]")
P(f"DONE {time.time()-T0:.0f}s")
