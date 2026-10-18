# Part (2b): PARI-free recheck of the cusp-row identities  Phi_c(x) = kappa_c(-1/x) - |x| sum_{c' cusp} S[c,c'] kappa_c'(x)
# at the 7 test rationals.  kappa_c(h/k) = sum_{a coprime to 70} F_c(cl a) e(h N(a)/(140 k)) N(a)^-s |_{s=0}, F_c = PARI-free class
# function of Part 1 (positive-norm part, content g = 140), evaluated by Shintani cone sums with period lattice 140k (Part 2 engine).
# For k = 1 additionally through the 96 exact L(0, chi) mod p2^3 p5 p7 oo1 oo2 (Part 2).
import numpy as np, math, pickle, sys, cmath, re
from fractions import Fraction as Fr
from collections import defaultdict
sys.dont_write_bytecode = True
import rc, part2, comp, cyc24 as Z
sys.path.insert(0, '/workspace/quantum-comp/reports/heavy-daily/2026-10-17-psi-conditions')
import kappa_all                       # PARI-free exact-Bernoulli lattice evaluation used by the original rows (for comparison only)
from family import LABELS as LAB2
lines = []; P = lambda s: (print(s, flush=True), lines.append(s))
p1 = pickle.load(open('part1.pkl', 'rb')); p2 = pickle.load(open('part2.pkl', 'rb')); cm = pickle.load(open('char_match.pkl', 'rb'))
C = cm['C']; R = rc.Ray(3); E = R.elems
assert [tuple(map(tuple, l)) for l in comp.labels()] == [tuple(map(tuple, l)) for l in LAB2]
F = np.array([p1['F'][(i, 1)] for i in C])            # (24, 96)
assert all(p1['res'][i][1]['g'] == 140 for i in C)
# (0) no coefficients of the cusp components at Q = n/140 with gcd(n,70) > 1 (so the ideal sum over a coprime to 70 is the full series)
worst = 0
for i in C:
    n1, n2, q, ph = comp.points(*comp.labels()[i], 400)
    d = defaultdict(complex)
    for x, v in zip(q.tolist(), ph.tolist()):
        if x > 0: d[x] += v
    worst = max([worst] + [abs(v) for x, v in d.items() if (x % 140) or math.gcd(x//140, 70) != 1])
P(f"cusp components, Q <= 400: max |coefficient| at frequencies 19600Q not of the form 140 n, gcd(n,70)=1: {worst:.1e}")
cache = {}
def kappa(x):
    x = Fr(x); h, k = x.numerator, x.denominator
    if k not in cache: cache[k] = part2.bins(R, 140*k, 140*k, exact=True)
    zb, npts = cache[k]; K = 140*k
    out = np.zeros(len(C), complex)
    for (ci, n), z in zb.items(): out += F[:, ci]*float(z)*cmath.exp(2j*math.pi*((h*n) % K)/K)
    return out, npts
# k = 1 through exact L-values
L3 = p2[3]['L']; CH = R.characters(); NC = len(E)
X = np.array([[cmath.exp(2j*math.pi*float(R.chival(c, x))) for x in E] for c in CH])
Nres = {}
for (ci, n) in p2[3]['zb']: Nres[ci] = n
def kappa_L(h):
    G = F*np.array([cmath.exp(2j*math.pi*h*Nres[ci]/140) for ci in range(NC)])[None, :]
    Gh = G @ X.conj().T / NC                      # (24, 96) Fourier coefficients
    Lc = np.array([Z.to_complex(v) for v in L3])
    used = sorted({j for j in range(NC) if np.abs(Gh[:, j]).max() > 1e-12 and abs(Lc[j]) > 0})
    return Gh @ Lc, used
S = np.load('/workspace/quantum-comp/reports/heavy-daily/2026-10-17-psi-conditions/S_matrix.npy')
ph = np.load('/workspace/quantum-comp/reports/heavy-daily/2026-10-17-psi-conditions/phi_rows.npy'); Sc = S[np.ix_(C, C)]
xs = [Fr(1), Fr(1, 3), Fr(2), Fr(3, 5), Fr(7, 4), Fr(-1), Fr(-2, 3)]
info3 = p2[3]['info']
for h in (1, -1):
    a, _ = kappa(h); b, used = kappa_L(h)
    P(f"kappa_c({h:+d}): Shintani (exact rationals) vs sum_chi Ghat(chi) L(0,chi) with the exact PARI-free L-values: {np.abs(a-b).max():.1e}; characters with nonzero contribution: {len(used)}, all totally odd non-sigma-invariant of conductor p2^2 p5 p7: {all(info3[j]['type']==(1,1) and not info3[j]['inv'] and info3[j]['cond']==(2,1,1) for j in used)}")
allok = []
for idx, x in enumerate(xs):
    xa = -1/x
    ka, na = kappa(xa); kb, nb = kappa(x)
    ea = np.array([kappa_all.fcoef(LAB2[i], xa)[2] for i in C]); eb = np.array([kappa_all.fcoef(LAB2[i], x)[2] for i in C])
    Phi = ka - abs(float(x))*Sc@kb
    d = np.abs(Phi - ph[idx, C]).max(); allok.append(d)
    P(f"x={str(x):>5}: kappa({xa}) [{na} cone pts] vs exact-Bernoulli lattice kappa {np.abs(ka-ea).max():.1e}; kappa({x}) [{nb} pts] {np.abs(kb-eb).max():.1e}; Phi_c(x) vs phi_rows (24 cusp rows) max dev {d:.1e}; Phi_73 = {Phi[C.index(73)]:.12f}")
P(f"max deviation over the 7 x 24 cusp-row identities: {max(allok):.1e}")
# per-PARI-label L(0) comparison (via the Part-1 sigma-orbit matching) with the PARI lfun values in lvalues.txt
txt = open('/workspace/quantum-comp/reports/heavy-daily/2026-10-17-psiEis-Lvalues/lvalues.txt').read()
dev = 0; n = 0
for m in re.finditer(r"chi\((\d+), (\d), (\d)\).*?L\(0\)=([-+]?[0-9.]+e[-+][0-9]+)([-+][0-9.]+e[-+][0-9]+)j", txt):
    chi = tuple(int(t) for t in m.group(1, 2, 3)); v = complex(float(m.group(4)), float(m.group(5)))
    if chi not in cm['match']: continue
    for j in cm['match'][chi]:
        dev = max(dev, abs(Z.to_complex(L3[j]) - v)); n += 1
P(f"PARI lfun L(0) (lvalues.txt, printed to 4 digits) for the 24 PARI-labelled cusp characters vs PARI-free exact L(0) of the matched sigma-orbit: max dev {dev:.1e} over {n} comparisons")
open('part3.txt', 'w').write("\n".join(lines)+"\n")
