# A(2): Burnside count of orbits of G = <gamma, R_s, -1> (elementary abelian of order 8 on Delta) ; fixed-point counts per element.
import numpy as np, sys, json
from family_s import Family
def data(s):
    F = Family(s); D = F.D
    G = np.array([[-1, -s], [2, 2*s-1]]); R = np.array([[1, s], [0, -1]]); I = np.eye(2, dtype=int)
    if s % 2: els = sorted({(al[0] % D, (al[1] + eps*D) % (2*D)) for al in F.ALS for eps in (0, 1)}); mod = (D, 2*D)
    else: els = sorted({(al[0] % D, al[1] % D) for al in F.ALS}); mod = (D, D)
    act = lambda g, x: (int((g@np.array(x))[0] % mod[0]), int((g@np.array(x))[1] % mod[1]))
    elts = {'1': I, '-1': -I, 'g': G, '-g': -G, 'R': R, '-R': -R, 'gR': G@R, '-gR': -G@R}
    # check G abelian of exponent 2 on Delta
    for a in elts.values():
        assert all(act(a@a, x) == x for x in els)
        for b in elts.values(): assert all(act(a@b, x) == act(b@a, x) for x in els)
    fix = {k: sum(act(g, x) == x for x in els) for k, g in elts.items()}
    return dict(s=s, fix=fix, orbits=sum(fix.values())//8, total=sum(fix.values()))
if __name__ == "__main__":
    out = [data(int(z)) for z in sys.argv[1].split(',')]
    for o in out: print(json.dumps(o))
    json.dump(out, open('burnside_V.json', 'w'), indent=1)
