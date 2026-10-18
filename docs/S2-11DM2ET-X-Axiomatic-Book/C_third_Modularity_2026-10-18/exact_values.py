# Exact renormalised radial values of C_third at rationals x = h/m:
#   c_C(x) = alpha(x) + beta(x) * I,  I = log(eps)/(2 sqrt35),  alpha, beta in Q(zeta_m):
#   alpha(x) = 1/2 + (1/2) e(7x/20) Z_x(0),  Z_x(0) = sum_{a in K} e(x Na/20) Na^{-s} |_{s=0}   (genus/Hurwitz formula, exact rationals)
#   beta(x)  = -(7/20) G(x),  G = Gauss mean of Q_s.
# (Uses c_C = (1 + c_E)/2, i.e. the parity lemma kappa_{q^8 f} = 0, and c_E = e(7x/20) Z_x(0) - (7/10) I G(x).)
import numpy as np, math, cmath, pickle, sys
from fractions import Fraction as Fr
import sympy as sp
sys.dont_write_bytecode = True
from radial import kron140, Cthird_exp, I
hh = pickle.load(open('genus_h_280.pkl', 'rb')); Sres = sorted(k for k, v in hh.items() if v)
Sm = np.zeros(280, bool); Sm[Sres] = True
def alpha_beta(h, m):
    L = 280*20*m//math.gcd(280, 20*m)
    e0 = np.arange(1, L+1, dtype=np.int64); acc = np.zeros(m, dtype=object)
    for d0 in range(1, L+1):
        c = kron140(d0 % 140) if d0 % 140 else 0
        if not c: continue
        N = (d0*e0) % L; ok = Sm[N % 280]
        j = (((N[ok] % (20*m)) + 7)//20) % m
        w = c*(L - 2*d0)*(L - 2*e0[ok])
        for jj in range(m):
            sel = j == jj
            if sel.any(): acc[jj] += int(w[sel].sum())
    wj = [Fr(int(a), 16*L*L) for a in acc]         # (1/2) [from c_C = (1+c_E)/2] * (1/2) [h = 1/2] * 1/(4L^2)
    n, k = np.meshgrid(np.arange(2*m), np.arange(2*m), indexing='ij')
    Q = (n*n + 7*n*k + (7*k*(k+1))//2) % m
    gj = [Fr(int((Q == jj).sum()), 4*m*m) for jj in range(m)]
    return wj, gj
def to_sym(coeffs, h, m):
    z = sp.exp(2*sp.pi*sp.I*h/m)
    return sp.nsimplify(sp.simplify(sum(sp.Rational(c.numerator, c.denominator)*z**j for j, c in enumerate(coeffs))))
out = []
for (h, m) in [(0, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 5), (1, 6), (1, 7), (3, 7), (1, 10), (3, 10)]:
    wj, gj = alpha_beta(h, m)
    zm = cmath.exp(2j*math.pi*h/m)
    a = 0.5 + sum(float(w)*zm**j for j, w in enumerate(wj)); b = -0.35*sum(float(g)*zm**j for j, g in enumerate(gj))
    cnum = Cthird_exp(Fr(h, m))[2]
    try:
        asym = sp.simplify(sp.Rational(1, 2) + to_sym(wj, h, m)); bsym = sp.simplify(-sp.Rational(7, 20)*to_sym(gj, h, m))
        asym_s = str(sp.radsimp(sp.expand_complex(asym))); bsym_s = str(sp.radsimp(sp.expand_complex(bsym)))
    except Exception as ex:
        asym_s = bsym_s = f"(sympy failed: {ex})"
    out.append(f"x={h}/{m}: c_C = alpha + beta*Ireg with alpha = {asym_s.replace('I','i')}, beta = {bsym_s.replace('I','i')};  numeric alpha+beta*I = {a+b*I:.12f}, independent EM value {cnum:.12f}, |diff| = {abs(a+b*I-cnum):.1e}")
    print(out[-1], flush=True)
open('exact_values.txt', 'w').write("# i = sqrt(-1) inside alpha, beta; Ireg = log(6+sqrt35)/(2 sqrt35)\n" + "\n".join(out)+"\n")
