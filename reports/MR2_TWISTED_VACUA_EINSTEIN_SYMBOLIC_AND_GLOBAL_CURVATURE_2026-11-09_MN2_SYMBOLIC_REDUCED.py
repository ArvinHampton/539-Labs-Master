#!/usr/bin/env python3
# MR2 2026-11-09: MN N=2 (z=1) FULL SYMBOLIC Einstein check, reduced variant. Execs the frozen item-A script
# MR2_TWISTED_VACUA_EINSTEIN_SYMBOLIC_AND_GLOBAL_CURVATURE_2026-11-09.py (sha d0191f02...) with MODE='none' (definitions only), then
# runs compute_E over the exact field Q(X1, s_a, s_b) with X2 = 2 X1 substituted (MN2 fixed-point relation X2/X1 = 2 is exact:
# X1 = 2^(-3/5), X2 = 2^(2/5)); r = v = 1 (homogeneity argument stated in the item-A header). Then every numerator is reduced modulo
# the minimal polynomial 8 X1^5 - 1 with (s_a, s_b) kept symbolic. Zero remainder for all 66 components = full symbolic zero.
import sys, time
sys.argv = ['x', 'none']
A = '/workspace/quantum-comp/reports/MR2_TWISTED_VACUA_EINSTEIN_SYMBOLIC_AND_GLOBAL_CURVATURE_2026-11-09.py'
exec(open(A).read())
T1 = time.time()
fp = FP["MN2(z=1)"]; mpoly, x2map = minpoly_data(fp)
K = field([X1s, sa, sb], QQ)[0]
conv = lambda e: K.from_expr(sp.sympify(e).subs(X2s, 2*X1s))
P(f"MN2 symbolic (reduced): field {K}; minpoly {mpoly}")
E, Rc, Dv = compute_E(K, conv, {r: 1, v: 1}, fp, sp.Rational(1,16), 1)
P(f"E_MN built: {66-len(E)} components identically 0 in Q(X1,s_a,s_b); {len(E)} to reduce [{time.time()-T1:.0f}s]")
allok = True
for key, e in E.items():
    num = sp.Poly(e.numer.as_expr(), X1s); rem = sp.rem(num, sp.Poly(mpoly, X1s))
    den = sp.Poly(e.denom.as_expr(), X1s); rden = sp.rem(den, sp.Poly(mpoly, X1s))
    ok = rem.is_zero; dok = not rden.is_zero
    allok &= ok and dok
    P(f"   E{key}: numerator (deg_X1 {num.degree()}, {len(num.terms())} X1-terms) == 0 mod (8X1^5-1) identically in (s_a,s_b): {ok}; denominator nonzero: {dok}")
P(f"MN2 FULL SYMBOLIC ZERO (all 66 components, all s_a, s_b; r=v=1 + homogeneity): {allok}  [{time.time()-T1:.0f}s]")
# control: same pipeline at LAMBDA = 1/8 must NOT reduce to zero
E2, _, _ = compute_E(K, conv, {r: 1, v: 1}, fp, sp.Rational(1,8), 1)
nz = sum(1 for e in E2.values() if not sp.rem(sp.Poly(e.numer.as_expr(), X1s), sp.Poly(mpoly, X1s)).is_zero)
P(f"CONTROL LAMBDA=1/8 symbolic: components not reducing to 0 = {nz} (must be > 0)  [{time.time()-T1:.0f}s]")
