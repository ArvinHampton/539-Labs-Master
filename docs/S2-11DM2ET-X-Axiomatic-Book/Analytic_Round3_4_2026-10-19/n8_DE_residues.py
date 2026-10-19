# Task 2, D vs E: for s = 4 mod 8, g = 4 g3 (g3 in {1,3}), the lattice data are coupled exactly:
#   b g3 = s/4 - 2,  m g3 = 3 s/4  =>  m = 3b + 6 g3^{-1} (mod 16),  s = 4(b g3 + 2) (mod 16 needs s/4 mod 4 only).
# Enumerate all residues (g3, b mod 16 odd, w mod 16) and record I4 = H(1)/H(0) (a = 1,3,5,7).
import cmath, itertools, json
def Qp(s, n, k): return n*n + s*n*k + s*k*(k+1)//2
def H(s, m, b, nw, kw, c, a):
    return sum(cmath.exp(2j*cmath.pi*a*Qp(s, c*nw + y*m, c*kw + y*b)/8) for y in range(16))
res = {}
for g3 in (1, 3):
    gi = pow(g3, -1, 16)
    for b in range(1, 16, 2):
        m = (3*b + 6*gi) % 16; s16 = (4*(b*g3 + 2)) % 16
        for nw, kw in itertools.product(range(16), repeat=2):
            if (kw*m - b*nw) % 16 != 1: continue
            for a in (1, 3, 5, 7):
                h0, h1 = H(s16, m, b, nw, kw, 0, a), H(s16, m, b, nw, kw, 1, a)
                key = 'b=%d mod 4' % (b % 4)
                res.setdefault(key, set()).add(round((h1/h0).real, 6))
print({k: sorted(v) for k, v in res.items()})
json.dump({k: sorted(v) for k, v in res.items()}, open('n8_DE_residues.json', 'w'))
