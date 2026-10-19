# Item 2 (22:07 continuation): exact check of the conceptual 2-adic theorems
#  N=2: H_{1/2}(c) = 4(-1)^c [16|s]                       (Open-Analytic 1.6)
#  N=4: H_{a/4}(c) = 0 (4 !| s);  4(1+i^a) (s = 4 mod 8 or 8 mod 16);  8 e(a c^2/4) (16 | s)
#  N=8: shape table by s mod 96 (printed / json), plus the invariant analysis
import json, math
from gauss_local import H_brute, Cyc
def el(d, L): return d
C8 = Cyc(8); bad = 0; tests = 0
for s in range(5, 2000):
    for a in (1, 3):
        for c in range(8):
            if s % 4: pred = {}
            elif s % 16: pred = {0: 4, (2*a) % 8: 4}
            else: pred = {(2*a*c*c) % 8: 8}
            tests += 1
            if C8.red(pred) != C8.red(H_brute(s, a, 4, c, 8)): bad += 1
print('N=4 theorem: tests', tests, 'mismatches', bad)
C16 = Cyc(16); shapes = {}; table = {}
for s in range(5, 5 + 96):
    for a in (1, 3, 5, 7):
        key = tuple(C16.red(H_brute(s, a, 8, c, 16)) for c in range(16))
        shapes.setdefault(key, len(shapes)); table.setdefault(s % 96, {})[a] = shapes[key]
print('N=8: number of distinct H-vectors over s mod 96, a in {1,3,5,7}:', len(shapes))
cls = {}
for r in sorted(table): cls.setdefault(tuple(table[r][a] for a in (1, 3, 5, 7)), []).append(r)
for k, v in cls.items(): print('shape ids (a=1,3,5,7)', k, ': s mod 96 in', v)
json.dump(dict(N4=dict(tests=tests, mismatches=bad), N8_classes={str(k): v for k, v in cls.items()}), open('even_N_theorem.json', 'w'), indent=1)
