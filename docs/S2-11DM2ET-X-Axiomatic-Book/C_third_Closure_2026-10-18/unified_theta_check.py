# Path C closure: one theta kernel, two segment integrals.
#   Xi_0(tau;t) = sqrt(y) sum_n q^{Q(n)} exp(-pi y B(n,c(t))^2)                      (Siegel theta, weight 0)
#   Xi_1(tau;t) = sqrt(y) sum_n 2 B(n,c_perp(t)) q^{Q(n)} exp(-pi y B(n,c(t))^2)      (Kudla-Millson-type insertion, weight 1)
#   int_{t1}^{t2} Xi_0 dt = Zwegers' completed mock Maass theta  Theta^_mu      (formula as restated in BCN arXiv:2409.17818, Sec. 2.2)
#   int_{t1}^{t2} Xi_1 dt = sum_n [E(B(n,c2) sqrt y) - E(B(n,c1) sqrt y)] q^{Q(n)}  (Zwegers 2002 completion; fundamental theorem of calculus)
# Lattice Z^2, A = [[2,s],[s,s]], mu = a = (s/(2(s-2)), -1/(s-2)); c1 _|_ e1 (so the c1-line boundary of the sign region is the e1-ray),
# c(t) = cosh(t) c1 + sinh(t) e1, c2 = gamma c1 = c(t2).  Checks: (A) Theta^_a == Theta_a (K_0 sign series), i.e. shadow cancels (Lemma 2.4 / gamma);
# (B) the two integrals numerically, and (C) Theta_a's Q>0 sign series equals 2*E_L as q-series weights (Lemma R).
import numpy as np, math, mpmath as mp, sys
from scipy.special import k0, erf
from scipy.integrate import quad
s = int(sys.argv[1]) if len(sys.argv) > 1 else 7
A = np.array([[2, s], [s, s]], float); B = lambda x, y: x @ A @ y; Qf = lambda x: 0.5*B(x, x)
G = np.array([[-1, -s], [2, 2*s-1]], float)
a = np.array([s/(2*(s-2)), -1/(s-2)])
c1 = np.array([s, -2.0])/math.sqrt(s*s - 2*s); e1 = np.array([1.0, 0.0])
assert abs(Qf(c1) + 1) < 1e-12 and abs(B(c1, e1)) < 1e-12 and abs(Qf(e1) - 1) < 1e-12
ct = lambda t: math.cosh(t)*c1 + math.sinh(t)*e1; cp = lambda t: math.sinh(t)*c1 + math.cosh(t)*e1
c2 = G @ c1
# solve c(t2) = c2
t2 = math.asinh(B(c2, e1)/B(e1, e1)*1.0) if False else None
# c2 = cosh t c1 + sinh t e1  => sinh t = B(c2,e1)/B(e1,e1)  (B(e1,e1)=2, B(c1,e1)=0)
t2 = math.asinh(B(c2, e1)/2.0); assert np.allclose(ct(t2), c2), (ct(t2), c2)
t1 = 0.0
E = lambda z: erf(math.sqrt(math.pi)*z)        # Zwegers' E(z) = 2 int_0^z e^{-pi u^2} du = erf(sqrt(pi) z)
tau = complex(0.137, 0.61); x, y = tau.real, tau.imag
R = 30
pts = [a + np.array([i, j]) for i in range(-R, R+1) for j in range(-R, R+1)]
pts = [n for n in pts if abs(Qf(n)) > 1e-12]
def theta_hat0():
    tot = 0j
    for n in pts:
        I, _ = quad(lambda t: math.exp(-math.pi*y*(2*Qf(n) + B(n, ct(t))**2)), t1, t2, limit=200)
        tot += math.sqrt(y)*I*np.exp(2j*math.pi*Qf(n)*x)
    return tot
def theta_sign():
    tot = 0j; c1p, c2p = cp(t1), cp(t2)
    for n in pts:
        q = Qf(n)
        if q > 0: w = 0.5*(1 - np.sign(B(n, c1))*np.sign(B(n, c2)))
        else: w = 0.5*(1 - np.sign(B(n, c1p))*np.sign(B(n, c2p)))
        if w: tot += math.sqrt(y)*w*k0(2*math.pi*abs(q)*y)*np.exp(2j*math.pi*q*x)
    return tot
def xi1_int():
    tot = 0j
    for n in pts:
        I, _ = quad(lambda t: 2*math.sqrt(y)*B(n, cp(t))*math.exp(-math.pi*y*(2*Qf(n) + B(n, ct(t))**2)), t1, t2, limit=200)
        tot += I*np.exp(2j*math.pi*x*Qf(n))
    return tot
def zw2002():
    mp.mp.dps = 50; tot = mp.mpc(0)
    for n in pts:
        z1 = mp.mpf(B(n, c1))*mp.sqrt(y); z2_ = mp.mpf(B(n, c2))*mp.sqrt(y)
        d = mp.erf(mp.sqrt(mp.pi)*z2_) - mp.erf(mp.sqrt(mp.pi)*z1)
        tot += d*mp.exp(-2*mp.pi*y*Qf(n))*mp.expjpi(2*x*Qf(n))
    return complex(tot)
th0 = theta_hat0(); ths = math.copysign(1, t2 - t1)*theta_sign(); x1 = xi1_int(); z2 = zw2002()
# non-gamma-related pair (c1, c(t2/3)): the weight-1 part is then non-trivial and the weight-0 shadow does not cancel
t2_save, c2_save = t2, c2
t2 = t2_save/3; c2 = ct(t2)
th0b = theta_hat0(); thsb = math.copysign(1, t2 - t1)*theta_sign(); x1b = xi1_int(); z2b = zw2002()
t2, c2 = t2_save, c2_save
out = [f"s={s}: t2 - t1 = {t2:.12f}, log(eps) = {math.log(s-1+math.sqrt(s*s-2*s)):.12f}",
       f"(A) Theta^_a (segment integral of Xi_0) = {th0:.12f}",
       f"    sgn(t2-t1) * Zwegers K_0 sign series = {ths:.12f}   |diff| = {abs(th0-ths):.2e}",
       f"(B) int Xi_1 dt = {x1:.12f}",
       f"    Zwegers-2002 completion sum        = {z2:.12f}   |diff| = {abs(x1-z2):.2e}   (vanishes: c2 = gamma c1 and gamma a = a mod Z^2)",
       f"non-gamma pair (c1, c(t2/3)):  int Xi_1 = {x1b:.12f}; Zwegers-2002 sum = {z2b:.12f}; |diff| = {abs(x1b-z2b):.2e}",
       f"                               Theta^ = {th0b:.12f}; sign series Theta = {thsb:.12f}; |Theta^ - Theta| = {abs(th0b-thsb):.2e} (nonzero shadow expected)"]
# (C): sign weights on Q>0 vs 2 * 1_F via gamma-orbit sums of exponents (compare multisets up to Q<=Qc)
from collections import Counter
Qc = 30; w1 = Counter(); w2 = Counter()
F = lambda n: (B(n, c1) > 0 >= B(n, c2)) or (B(n, c1) == 0 and B(n, c2) < 0)
for n in pts:
    q = Qf(n)
    if 0 < q <= Qc:
        wt = 0.5*(1 - np.sign(B(n, c1))*np.sign(B(n, c2)))
        if wt: w1[round(q, 9)] += wt
gr = (-1, 2)
for n in pts:   # E_L cone F=[e1, gamma e1) cap (a+Z^2) as in uL_rayclass_exact.py: X2 >= 0 and 2X1 + X2 > 0  (nu coordinates)
    q = Qf(n)
    if 0 < q <= Qc and n[1] >= -1e-12 and (2*n[0] + n[1]) > 1e-12: w2[round(q, 9)] += 1
diffC = max(abs(w1[k] - 2*w2[k]) for k in set(w1) | set(w2))
out.append(f"(C) max_q |sign-weight count - 2 * #F-cone points| over Q <= {Qc}: {diffC}")
print("\n".join(out)); open(f'unified_theta_check_s{s}.txt', 'w').write("\n".join(out) + "\n")
