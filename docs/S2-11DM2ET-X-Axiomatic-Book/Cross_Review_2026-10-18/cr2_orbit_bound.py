# Cross-review check: exact upper bound for dim V (lift function span) from the two exact
# function identities u_{g al, g be} = u_{al,be} for g = gamma (unit) and g = -I (negation),
# for every s in the Cusp-Onset table.  Monomial relations -> orbits with a phase cocycle;
# an orbit contributes 1 dimension iff its cocycle is consistent (else all its labels vanish).
# Exact arithmetic (Fractions mod 1).  Compared with the floating SVD dim V of Cusp-Onset.
import sys, json, math
import numpy as np
from fractions import Fraction as Fr
from family_s import Family

def reduce_exact(F, al, be):
    al = np.array(al); be = np.array(be)
    for b0 in F.BES:
        mu = be - np.array(b0)
        if F.inLp(mu):
            return F.IDX[(tuple(al % F.D), b0)], F.B(al, mu) % 1
    raise ValueError

def bound(s):
    F = Family(s)
    gens = [F.G, -np.eye(2, dtype=int)]
    # edges: u_i = e(ph) u_j
    adj = {i: [] for i in range(F.N)}
    for g in gens:
        for i, (al, be) in enumerate(F.LABELS):
            j, ph = reduce_exact(F, g @ np.array(al), g @ np.array(be))
            adj[i].append((j, ph))           # u_i = e(ph) u_j
            adj[j].append((i, (-ph) % 1))    # u_j = e(-ph) u_i
    seen = {}; consistent = 0; zero_labels = 0; sizes = []
    for r in range(F.N):
        if r in seen: continue
        seen[r] = Fr(0); stack = [r]; orbit = [r]; ok = True
        while stack:
            i = stack.pop()
            for j, ph in adj[i]:
                # u_i = e(ph) u_j and u_i = e(seen[i]) u_r  => u_j = e(seen[i]-ph) u_r
                v = (seen[i] - ph) % 1
                if j in seen:
                    if seen[j] != v: ok = False
                else:
                    seen[j] = v; stack.append(j); orbit.append(j)
        if ok: consistent += 1; sizes.append(len(orbit))
        else: zero_labels += len(orbit)
    return dict(s=s, labels=F.N, dimV_upper=consistent, zero_labels=zero_labels)

if __name__ == "__main__":
    tab = {5:20,6:12,7:42,8:18,9:72,10:30,11:110,12:42,13:156,14:56,15:210,16:72,17:272,18:84,
           19:342,20:110,21:420,22:132,23:506,24:156,25:600,41:1640}
    ss = [int(x) for x in sys.argv[1].split(',')] if len(sys.argv) > 1 else sorted(tab)
    out = []
    for s in ss:
        r = bound(s); r['dimV_cusp_onset_svd'] = tab.get(s)
        r['match'] = (r['dimV_upper'] == tab.get(s))
        if s % 2: r['s(s-1)'] = s*(s-1)
        print(r, flush=True); out.append(r)
    json.dump(out, open('cr2_orbit_bound.json', 'w'), indent=1)
