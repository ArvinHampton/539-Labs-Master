# Same exact orbit bound, adding the improper automorph R_s=[[1,s],[0,-1]] (Lemma R / V42 R) as a third generator.
# Purpose: does R_s explain the two even-s exceptions (s=8,18) where the <gamma,-1> bound exceeds the SVD rank?
import sys, json
import numpy as np
from fractions import Fraction as Fr
from family_s import Family
from cr2_orbit_bound import reduce_exact
def bound(s, gens_names):
    F = Family(s)
    R = np.array([[1, s], [0, -1]])
    assert np.all(R.T @ F.A @ R == F.A)
    allg = {'gamma': F.G, 'neg': -np.eye(2, dtype=int), 'R': R}
    adj = {i: [] for i in range(F.N)}
    for nm in gens_names:
        g = allg[nm]
        for i, (al, be) in enumerate(F.LABELS):
            j, ph = reduce_exact(F, g @ np.array(al), g @ np.array(be))
            adj[i].append((j, ph)); adj[j].append((i, (-ph) % 1))
    seen = {}; cons = 0
    for r in range(F.N):
        if r in seen: continue
        seen[r] = Fr(0); st = [r]; ok = True
        while st:
            i = st.pop()
            for j, ph in adj[i]:
                v = (seen[i] - ph) % 1
                if j in seen:
                    if seen[j] != v: ok = False
                else: seen[j] = v; st.append(j)
        cons += ok
    return cons
tab = {5:20,6:12,7:42,8:18,9:72,10:30,11:110,12:42,13:156,14:56,15:210,16:72,17:272,18:84,19:342,20:110,21:420,22:132,23:506,24:156,25:600}
res = []
for s in sorted(tab):
    b2 = bound(s, ['gamma', 'neg']); b3 = bound(s, ['gamma', 'neg', 'R'])
    r = dict(s=s, svd=tab[s], gamma_neg=b2, gamma_neg_R=b3)
    print(r, flush=True); res.append(r)
json.dump(res, open('cr2b_with_R.json', 'w'), indent=1)
