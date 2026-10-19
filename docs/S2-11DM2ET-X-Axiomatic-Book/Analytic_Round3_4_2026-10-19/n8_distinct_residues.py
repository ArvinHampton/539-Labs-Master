# Task 2 (Round 3): residue-level (all s at once, NOT a scan over s) check of the invariants that separate the six N = 8 classes.
# H(c) = sum_{y mod 16} e(Q+(c w + y u)/8) depends only on (s mod 16, u mod 16, w mod 16) [Q+ mod 8 depends on s mod 16 and
# (n,k) mod 16].  We enumerate ALL residue tuples (s16, m, b, nw, kw) mod 16 with k_w m - b n_w = 1 mod 16 that satisfy the
# residue constraints of each class (derived in the report from v2 bookkeeping), and record the invariants
#   I1 = max|H|, I2 = support pattern, I3 = H(0)/|H(0)| (a=1), I4 = H(1)/H(0) (a=1).
import cmath, itertools, json
def Qp(s, n, k): return n*n + s*n*k + s*k*(k+1)//2
def H(s, m, b, nw, kw, c, a=1):
    return sum(cmath.exp(2j*cmath.pi*a*Qp(s, c*nw + y*m, c*kw + y*b)/8) for y in range(16))
def r(z): return complex(round(z.real, 6), round(z.imag, 6))
classes = {
 # s mod 16, constraint on (m, b) mod 16 (from m = 3s/g, b = (s-8)/g; see report)
 'A: s=0 mod 32  (s16=0, v2(m)>=2, b odd)': (lambda s, m, b: s == 0 and m % 4 == 0 and b % 2 == 1),
 'B: s=16 mod 32 (s16=0, v2(m)=1, b odd)':  (lambda s, m, b: s == 0 and m % 4 == 2 and b % 2 == 1),
 'C: s=8 mod 16  (s16=8, m odd, b even)':   (lambda s, m, b: s == 8 and m % 2 == 1 and b % 2 == 0),
 'D: s=4 mod 8, b=3 mod 4':                 (lambda s, m, b: s in (4, 12) and m % 2 == 1 and b % 4 == 3),
 'E: s=4 mod 8, b=1 mod 4':                 (lambda s, m, b: s in (4, 12) and m % 2 == 1 and b % 4 == 1),
}
out = {}
for name, cond in classes.items():
    inv = set()
    for s, m, b in itertools.product(range(16), repeat=3):
        if not cond(s, m, b): continue
        for nw, kw in itertools.product(range(16), repeat=2):
            if (kw*m - b*nw) % 16 != 1: continue
            Hs = [H(s, m, b, nw, kw, c) for c in range(16)]
            I1 = round(max(abs(z) for z in Hs), 6)
            I2 = tuple(int(abs(z) > 1e-9) for z in Hs)
            I3 = r(Hs[0]/abs(Hs[0])) if abs(Hs[0]) > 1e-9 else 0
            I4 = r(Hs[1]/Hs[0]) if abs(Hs[0]) > 1e-9 else None
            inv.add((I1, I2 == tuple([1]*16), I2 == tuple([0, 1]*8), str(I3), str(I4)))
    out[name] = sorted(map(str, inv)); print(name, out[name], flush=True)
json.dump(out, open('n8_distinct_residues.json', 'w'), indent=1)
