# Compare the PARI-free Part-1 results with the PARI-based fit (fitF.pkl / component_split.json, read-only), and recheck
# the 116/24 split, the 60+12 dimensions and the S-equivariance with the PARI-free cusp set.
import pickle, json, numpy as np, math, itertools, sys
from collections import defaultdict
sys.dont_write_bytecode = True
import comp
CP = '/workspace/quantum-comp/reports/heavy-daily/2026-10-17-cusp-part/'
me = pickle.load(open('part1.pkl', 'rb')); res = me['res']; info = me['info']; CH = me['chars']
old = pickle.load(open(CP+'fitF.pkl', 'rb')); opc = old['per_comp']
CS = json.load(open(CP+'component_split.json'))
out = []
# (a) empty pattern, content g, theta residual, class-function spread
empt_me = {(i, s) for i in res for s in (1, -1) if res[i][s] is None}
empt_old = {(i, s) for i in opc for s in (1, -1) if opc[i][s] is None}
out.append(f"(label,sign) pairs with no coefficients: PARI-free {len(empt_me)}, PARI fit {len(empt_old)}, identical sets: {empt_me == empt_old}")
gdiff = [(i, s) for i in res for s in (1, -1) if res[i][s] and res[i][s]['g'] != opc[i][s]['g']]
out.append(f"content g differs on {len(gdiff)} (label,sign) pairs")
out.append(f"max class-function spread (lattice weight per ideal not constant on a class): {max(r['spread'] for i in res for r in res[i].values() if r):.1e}")
out.append(f"max theta residual |c(g n) - sum_cl F(cl) I(cl,n)| over all n <= 19600*400*0.98/g coprime to 70, all 258 (label,sign): {max(r['resid'] for i in res for r in res[i].values() if r):.1e}  (PARI least-squares fit residual: {max(r['resid'] for i in opc for r in opc[i].values() if r):.1e})")
# (b) Eis / cusp / mixed norms
dE = max(abs(res[i][s]['eis']-opc[i][s]['eis']) for i in res for s in (1, -1) if res[i][s])
dC = max(abs(res[i][s]['cusp']-opc[i][s]['cusp']) for i in res for s in (1, -1) if res[i][s])
mx = max(res[i][s]['mixed'] for i in res for s in (1, -1) if res[i][s])
out.append(f"|Eis|^2 per (label,sign): max |PARI-free - PARI| = {dE:.1e};  |cusp|^2: {dC:.1e};  max mixed content (PARI-free) = {mx:.1e}")
C_me = sorted({i for i in res for r in res[i].values() if r and r['cusp'] > 1e-12})
C_old = sorted({i for i, rec in opc.items() for s, r in rec.items() if r and r['cusp'] > 1e-12})
E_me = [i for i in range(140) if i not in C_me]
out.append(f"cusp components: PARI-free {len(C_me)}, PARI {len(C_old)}, identical: {C_me == C_old};  max |Eis|^2 inside cusp comps = {max(res[i][s]['eis'] for i in C_me for s in (1,-1) if res[i][s]):.1e}; max |cusp|^2 inside Eis comps = {max(res[i][s]['cusp'] for i in E_me for s in (1,-1) if res[i][s]):.1e}")
# (c) character types in the PARI-free group
from collections import Counter
cnt = Counter((d['inv'], 'pure' if d['type'][0] == d['type'][1] else 'mixed', d['type'], d['cond']) for d in info)
cuspchars = [k for k, d in enumerate(info) if not d['inv'] and d['type'][0] == d['type'][1]]
out.append(f"Cl^+ mod p2^3 p5 p7 oo1 oo2: 96 characters; non-sigma-invariant pure-type: {len(cuspchars)}; their (finite conductor exponents at p2,p5,p7): {sorted(Counter(info[k]['cond'] for k in cuspchars).items())}; types: {sorted(Counter(info[k]['type'] for k in cuspchars).items())}")
# (d) match PARI-labelled characters to PARI-free characters through the cusp coefficient vectors Fhat_{c,s}(chi)
E = me['elems']; NC = len(E)
X = np.array([[np.exp(2j*np.pi*float((sum(p*g for p, g in zip(c[0], x[0])) + x[1]*c[1]) % 1)) for x in E] for c in CH])
keys = [(i, s) for i in C_me for s in (1, -1)]
Vme = {k: np.array([(X[k].conj() @ me['Fs'][key])/NC for key in keys]) for k in cuspchars}
Vold = defaultdict(lambda: np.zeros(len(keys), complex))
for j, key in enumerate(keys):
    for chi, v in opc[key[0]][key[1]]['cusp_chars']: Vold[tuple(chi)][j] = v
sigk = {}
for k in cuspchars:   # chi o sigma inside the PARI-free list
    vals = [float(((sum(p*g for p, g in zip(CH[k][0], x[0])) + x[1]*CH[k][1])) % 1) for x in E]
    from rc import Ray
    RR = Ray(3)
    sv = [float(((sum(p*g for p, g in zip(CH[k][0], RR.sigma(x)[0])) + RR.sigma(x)[1]*CH[k][1])) % 1) for x in E]
    sigk[k] = next(j for j in cuspchars if all(abs(((float((sum(p*g for p, g in zip(CH[j][0], x[0])) + x[1]*CH[j][1]) % 1) - w + 0.5) % 1) - 0.5) < 1e-12 for x, w in zip(E, sv)))
match = {}; worst = 0; ok = True
for chi, v in Vold.items():
    cand = frozenset(k for k in cuspchars if np.abs(Vme[k]-v).max() < 1e-6)
    worst = max(worst, min(np.abs(Vme[k]-v).max() for k in cand))
    ok &= (len(cand) == 2 and all(sigk[k] in cand and sigk[k] != k for k in cand))
    match[chi] = cand
pari_orbit_ok = all(match[chi] == match[((13*chi[0]) % 24, chi[1], chi[2])] for chi in match)
out.append(f"PARI cusp characters vs PARI-free ones via Fhat vectors (24 comps x 2 signs): every PARI character matches exactly one PARI-free sigma-orbit {{chi, chi o sigma}}: {ok}; PARI sigma-partners (j -> 13j) map to the same orbit: {pari_orbit_ok}; 12 orbits <-> 12 orbits: {len(set(match.values())) == 12}; max |Fhat_PARI - Fhat_PARIfree| = {worst:.1e}.  (Theta data only see Fs = sigma-symmetrised F, so characters are determined up to chi <-> chi o sigma, as in the PARI fit.)")
# exact form (1/48) e(k/60) and the json phases
dev = 0; phases = set()
for k in cuspchars:
    for v in Vme[k]:
        if abs(v) < 1e-12: continue
        dev = max(dev, abs(abs(v)-1/48)); t = (np.angle(v)/(2*np.pi)) % 1; phases.add(round(t*60, 6) % 60)
out.append(f"PARI-free cusp coefficients: max ||Fhat| - 1/48| = {dev:.1e}; phases*60 all integers: {all(abs(p-round(p)) < 1e-6 for p in phases)}")
jdev = 0
for i in C_me:
    for e in CS[str(i)]['data']['1']['cusp_coeffs']:
        from fractions import Fraction as Fr
        v = float(Fr(e['abs']))*np.exp(2j*np.pi*float(Fr(e['phase_turns'])))
        jdev = max(jdev, abs(v - Vme[min(match[tuple(e['chi'])])][keys.index((i, 1))]))
out.append(f"component_split.json exact cusp coefficients (1/48)e(k/60) vs PARI-free values: max dev {jdev:.1e}")
pickle.dump(dict(match=match, C=C_me), open('char_match.pkl', 'wb'))
# (e) 60+12 and equivariance with the PARI-free cusp set (S, T from the Poisson-summation family, PARI-free)
S = np.load('/workspace/quantum-comp/reports/heavy-daily/2026-10-17-psi-conditions/S_matrix.npy')
T = np.load('/workspace/quantum-comp/reports/heavy-daily/2026-10-17-psi-conditions/T_matrix.npy')
P = S@S; Pi = (np.eye(140)+P)/2
out.append(f"dim (P-invariant): cusp rows {np.linalg.matrix_rank(Pi[C_me], 1e-9)}, Eis rows {np.linalg.matrix_rank(Pi[E_me], 1e-9)}, total {np.linalg.matrix_rank(Pi, 1e-9)}")
out.append(f"T block-diagonal: max|T[cusp,Eis]| = {np.abs(T[np.ix_(C_me, E_me)]).max():.1e}, max|T[Eis,cusp]| = {np.abs(T[np.ix_(E_me, C_me)]).max():.1e}")
L = comp.labels(); QM = 40; rows = []; kk = {}
for i, (al, be) in enumerate(L):
    n1, n2, q, ph = comp.points(al, be, QM); dd = defaultdict(complex)
    for x, v in zip(q.tolist(), ph.tolist()): dd[x] += v
    if all(al[t] % 70 == 0 for t in (0, 1)): dd[0] += math.log(6+math.sqrt(35))
    rows.append(dd); [kk.setdefault(x, len(kk)) for x in dd]
Cf = np.zeros((140, len(kk)), complex)
for i, dd in enumerate(rows):
    for x, v in dd.items(): Cf[i, kk[x]] = v
a = np.abs(S[np.ix_(C_me, E_me)]@Cf[E_me]).max(); b = np.abs(S[np.ix_(E_me, C_me)]@Cf[C_me]).max()
out.append(f"S-equivariance (coefficientwise, {len(kk)} frequencies |Q|<=40, PARI-free lattice data): |sum_(c' Eis) S[c,c'] u_c'| (c cusp) = {a:.1e}; |sum_(c' cusp) S[c,c'] u_c'| (c Eis) = {b:.1e}")
print("\n".join(out)); open('part1.txt', 'w').write("\n".join(out)+"\n")
