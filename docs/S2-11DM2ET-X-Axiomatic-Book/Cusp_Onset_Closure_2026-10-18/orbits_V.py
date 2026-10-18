# A(2): upper bound for dim V: V lies in the fixed space of the automorphs gamma, R_s, -1 of the lattice acting on the
#   discriminant module (odd s: Delta = L0'/L0, L0 = {n2 even}; even s: Delta = L'/Z^2).  dim Fix = #orbits.
import numpy as np, sys, json, math
from family_s import Family
def orbits(s):
    F = Family(s); D = F.D
    G = np.array([[-1, -s], [2, 2*s-1]]); R = np.array([[1, s], [0, -1]]); Mi = -np.eye(2, dtype=int)
    if s % 2:
        els = sorted({(al[0] % D, (al[1] + eps*D) % (2*D)) for al in F.ALS for eps in (0, 1)}); mod = (D, 2*D)
    else:
        els = sorted({(al[0] % D, al[1] % D) for al in F.ALS}); mod = (D, D)
    S = set(els); seen = set(); orbs = 0; sizes = []
    gens = {'gamma': G, 'R': R, '-1': Mi}
    def act(g, x): y = g @ np.array(x); return (int(y[0] % mod[0]), int(y[1] % mod[1]))
    for x in els:
        if x in seen: continue
        orbs += 1; st = [x]; comp = {x}
        while st:
            z = st.pop()
            for g in gens.values():
                w = act(g, z); assert w in S
                if w not in comp: comp.add(w); st.append(w)
        seen |= comp; sizes.append(len(comp))
    return dict(s=s, order=len(els), orbits=orbits_count if False else orbs)
if __name__ == "__main__":
    for s in [int(z) for z in sys.argv[1].split(',')]:
        r = orbits(s); r['s(s-1)'] = s*(s-1); r['(s/2)(s/2+1)'] = (s//2)*(s//2+1); print(json.dumps(r), flush=True)
