# Exact integer q-series (numpy int64 bincounts) to q^N for C_third, q^8 f_{2,7,7}(-q^10,-q^14,q), theta_3, Theta_hol, P_s
# and THREE independent constructions of E:
#   E1 := R + C_third + sum_{n>=1} q^{n^2}                       (P_s report definition)
#   E2 := sum over the unit-group fundamental cone F = [e1, gamma e1) in nu = v + a coordinates, a = (7/10,-1/5)
#   E3 := sum_{a in K} q^{(Na+7)/20}, enumerated on the IDEAL side: a = (mu) p7^{-1} with mu in p7, mu = 7 mod p2p5,
#         sgn mu = (-,+), mu in the fundamental domain 1 <= |mu1|/mu2 < eps^2 of eps^Z (eps = 6+sqrt35).
import numpy as np, math, sys, json
N = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
B = int(4*math.isqrt(N) + 60)
def ser(e, w=None):
    e = np.asarray(e).ravel(); w = np.ones_like(e) if w is None else np.asarray(w).ravel()
    m = (e >= 0) & (e <= N)
    return np.bincount(e[m], weights=w[m], minlength=N+1).astype(np.int64)
n, k = np.meshgrid(np.arange(-B, B+1), np.arange(-B, B+1), indexing='ij')
Qs2 = 2*n*n + 14*n*k + 7*k*(k+1)          # 2 Q_s
Qm2 = 2*n*n + 14*n*k + 7*k*(k-1)          # 2 Q_-
assert (Qs2 % 2 == 0).all() and (Qm2 % 2 == 0).all()
Qs, Qm = Qs2//2, Qm2//2
P = ser(Qs[(n >= 0) & (k >= 0)])
Ct = ser(Qm[(n >= 1) & (k >= 1)])
R = ser(Qs[(n >= 0) & (k >= 1)])
r = np.arange(-B, B+1)
th3 = ser(r*r); sq1 = ser(r[r >= 1]**2)
one = np.zeros(N+1, np.int64); one[0] = 1
TH = ser(Qm[(n >= 1) & (k >= 0)]) - ser(Qm[(n <= 0) & (k <= -1)])
# HM Def 0.2: f_{a,b,c}(x,y,q) = sum_{sg r = sg s} sg(r) (-1)^{r+s} x^r y^s q^{a r(r-1)/2 + b r s + c s(s-1)/2}; x=-q^10, y=-q^14
sgr = np.where(n >= 0, 1, -1); sgs = np.where(k >= 0, 1, -1)
ef2 = 2*8 + 2*n*(n-1) + 14*n*k + 7*k*(k-1) + 20*n + 28*k
assert (ef2 % 2 == 0).all()
same = sgr == sgs
q8f = ser((ef2//2)[same], sgr[same])
E1 = R + Ct + sq1
# E2: nu = (n + 7/10, k - 1/5); cone F: nu2 >= 0 and 2 nu1 + nu2 > 0  (10nu = (10n+7, 10k-2))
X, Y = 10*n + 7, 10*k - 2
E2 = ser(Qs[(Y >= 0) & (2*X + Y > 0)])
# E3: ideal side
Mmax = 7*(20*N - 7)
Bb = int(math.ceil((math.sqrt(Mmax)*(6+math.sqrt(35)) + math.sqrt(Mmax))/(2*math.sqrt(35)))) + 5
Aa = int(math.ceil(math.sqrt(Mmax)*(6+math.sqrt(35))/2)) + 5
A, Bm = np.meshgrid(np.arange(-Aa, 1), np.arange(-Bb, 1), indexing='ij')
NN = 35*Bm*Bm - A*A                                        # |N mu| (N mu < 0 for signs (-,+))
ok = (A % 7 == 0) & ((A - 5*Bm) % 10 == 7) & (NN > 0) & (6*A - 35*Bm > 0) & (A <= 0)
# signs: mu1 = A + Bm sqrt35 < 0 and mu2 = A - Bm sqrt35 > 0 <=> NN > 0 and Bm < 0 (given A <= 0)
ok &= (Bm < 0)
assert (NN[ok] % 7 == 0).all()
Na = NN[ok]//7
assert ((Na + 7) % 20 == 0).all()
E3 = ser((Na + 7)//20)
# edge safety for E3: largest point of the domain must exceed the box needs
res = {}
res['E1 == E2 (P_s-report definition = unit-fundamental-cone sum)'] = bool((E1 == E2).all())
res['E2 == E3 (lattice cone = ideal-side ray-class enumeration, norms (Na+7)/20)'] = bool((E2 == E3).all())
res['I2  C_third = q^8 f + P_s'] = bool((Ct == q8f + P).all())
res['I3  Theta_hol = q^8 f + theta_3'] = bool((TH == q8f + th3).all())
res['P_s report: 2 P_s = E + 1 + theta_3 - Theta_hol'] = bool((2*P == E1 + one + th3 - TH).all())
res['(1) 2 C_third = q^8 f + 1 + E'] = bool((2*Ct == q8f + one + E1).all())
res['(1) 2 C_third = (Theta_hol - theta_3) + (1 + E)'] = bool((2*Ct == TH - th3 + one + E1).all())
res['E has nonnegative integer coefficients, E(0) = 0'] = bool((E1 >= 0).all() and E1[0] == 0)
res['C_third coefficients nonnegative integers'] = bool((Ct >= 0).all())
first = {nm: [int(i) for i in np.nonzero(s)[0][:12]] for nm, s in (('E', E1), ('q8f', q8f), ('C_third', Ct))}
coef = {nm: [int(s[i]) for i in np.nonzero(s)[0][:12]] for nm, s in (('E', E1), ('q8f', q8f), ('C_third', Ct))}
lines = [f"N = {N}, box B = {B}"] + [f"{k}: {'PASS' if v else 'FAIL'}" for k, v in res.items()]
lines += [f"first exponents {nm}: {first[nm]}  coefficients {coef[nm]}" for nm in first]
# the alternative normalisation that would hold if a constant/sign differed
lines.append(f"sanity: 2C_third - q^8f - E has only the constant term: {sorted({int(i) for i in np.nonzero(2*Ct - q8f - E1)[0]})}, value {int((2*Ct-q8f-E1)[0])}")
print("\n".join(lines)); open('series.txt', 'w').write("\n".join(lines)+"\n")
np.savez('series.npz', Ct=Ct, q8f=q8f, E=E1, th3=th3, TH=TH, P=P)
