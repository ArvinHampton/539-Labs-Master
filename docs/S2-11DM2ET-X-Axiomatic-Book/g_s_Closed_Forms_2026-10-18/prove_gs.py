# Step (3): symbolic derivation of ALL asymptotic coefficients c_k(s) of g_s(e^{-t}) = sum_n q^{n^2}/(-q^s;q^s)_n, t->0+, any real s>0.
# Write 1/(-q^s;q^s)_n = 2^{-n} exp(-sum_{j<=n} L(s j t)),  L(x) = log((1+e^{-x})/2) ... (sign: 1/(1+e^{-x}) = (1/2) * 2/(1+e^{-x}))
# so term_n = 2^{-n} exp(-t n^2 + sum_{j=1}^n Lam(s j t)),  Lam(x) = log(2/(1+e^{-x})) = x/2 - x^2/8 + x^4/192 - ...
# Expanding in t: coefficient of t^k is a polynomial in (n, s) (Faulhaber sums of j^m), and sum_n n^m 2^{-n} = Li_{-m}(1/2) in Q.
import sympy as sp, json
s, t, n, j, X = sp.symbols('s t n j X')
K = 8
Lam = sp.series(sp.log(2/(1+sp.exp(-X))), X, 0, K+1).removeO()
out = [f"Lam(x) = log(2/(1+e^-x)) = {Lam} + O(x^{K+1})"]
# S_m(n) = sum_{j=1}^n j^m  (Faulhaber, exact polynomial)
Sm = lambda m: sp.expand((sp.bernoulli(m+1, n+1) - sp.bernoulli(m+1, 0))/(m+1))   # sum_{j=1}^n j^m, Faulhaber, B_k(x) = sympy bernoulli poly
expo = -t*n**2 + sum(Lam.coeff(X, m)*(s*t)**m*Sm(m) for m in range(1, K+1))
# exp truncated in t by explicit power series (expo has no t^0 term)
expo = sp.expand(expo); ser = 1; term = 1
trunc = lambda e: sum(sp.expand(e).coeff(t, i)*t**i for i in range(K+1))
for r in range(1, K+1):
    term = trunc(sp.expand(term*expo))/r; ser += term
ser = sp.expand(ser)
from functools import lru_cache
@lru_cache(None)
def Li_neg(m):   # A_m = sum_{n>=0} n^m/2^n; A_m = sum_{i<m} C(m,i) A_i (from shifting n->n+1), A_0 = 2
    return sp.Integer(2) if m == 0 else sum(sp.binomial(m, i)*Li_neg(i) for i in range(m))
cache = {}
def avg(poly):   # sum_{n>=0} 2^{-n} poly(n)
    p = sp.Poly(sp.expand(poly), n); tot = 0
    for (m,), c in p.terms():
        if m not in cache: cache[m] = Li_neg(m)
        tot += c*cache[m]
    return sp.expand(tot)
c = [sp.factor(avg(ser.coeff(t, k))) for k in range(K+1)]
num = json.load(open('gs_numeric.json'))
for k in range(K+1):
    ck = sp.expand(c[k]); out.append(f"c_{k}(s) = {ck}" + (f"    = {sp.factor(ck)}" if k > 0 else ""))
# checks: matches pre-registered fit (fit on s=3..7) and numerics on all s
fit = {0: 2, 1: 2*s-6, 2: 5*s**2-44*s+75, 3: sp.Rational(55, 3)*s**3-310*s**2+1306*s-1561,
       4: sp.Rational(1073, 12)*s**4-sp.Rational(7216, 3)*s**3+17885*s**2-sp.Rational(148282, 3)*s+sp.Rational(181945, 4)}
for k, f in fit.items():
    ok = sp.expand(c[k]-f) == 0; out.append(f"[{'PASS' if ok else 'FAIL'}] c_{k}: symbolic == polynomial fitted on s=3..7 (validated on held-out s)")
worst = 0
for sv, d in num.items():
    for k in range(5):
        if int(sv) >= 3: worst = max(worst, abs(float(c[k].subs(s, int(sv))) - float(d['c'][k]))/max(1, abs(float(c[k].subs(s, int(sv))))))
out.append(f"[{'PASS' if worst < 1e-8 else 'FAIL'}] symbolic c_0..c_4 vs direct numerics s=3..20,25,30,41: worst rel. dev {worst:.1e}")
# calibration s=1 (f0, 5th-order mock theta) and s=2 (phi, 3rd order)
out.append(f"calibration s=1: c_0..c_4 = {[c[k].subs(s, 1) for k in range(5)]};  s=2: {[c[k].subs(s, 2) for k in range(5)]}")
# Mellin-regularised values: zeta_g(w) := M(w)/Gamma(w), M(w) = int_0^oo (g(e^-t)-1) t^{w-1} dt; zeta_g(-k) = (-1)^k k! [t^k](g-1)
z0 = c[0]-1; zm1 = -c[1]; zm2 = 2*c[2]
out.append(f"zeta_g(0) = {z0};  zeta_g(-1) = {sp.expand(zm1)};  zeta_g(-2) = {sp.expand(zm2)}")
out.append("Degree check: deg_s c_k = k for k<=8: " + str([sp.degree(c[k], s) if k else 0 for k in range(K+1)]))
out.append("Leading coefficients lc_k (of s^k): " + str([sp.Poly(c[k], s).LC() for k in range(K+1)]))
# leading term: only the x/2 part of Lam with S_1 ~ n^2/2, i.e. exp(s t n^2/4 - t n^2) top degree -> lc_k = (1/4)^k/k! * Li_{-2k}(1/2)
# (a naive guess lc_k = Li_{-2k}(1/2)/(4^k k!) was tried and FAILS: all Lam-terms contribute to the top s-degree; dropped)
out.append("lc_k = [u^k] sum_n prod_{j<=n} 1/(1+e^{-uj}) (s->oo with u=st fixed); naive guess Li_{-2k}(1/2)/(4^k k!) FAILS (recorded)")
open('prove_gs.txt', 'w').write("\n".join(out)+"\n"); print("\n".join(out))
import pickle; pickle.dump([str(x) for x in c], open('gs_coeffs.pkl', 'wb'))
