import gzip, numpy as np
from ladder import run
g = {}
for line in gzip.open('../../data/exact_1000000.txt.gz','rt'):
    d, v = line.split(); g[int(d)] = int(v)
ds = [d for d in list(range(999900, 1000001)) + list(range(99900, 100001)) if d % 7 in (0,1,2,4)]
E, O, terms, _ = run(ds, 1000000//7+2)
worst = 0
for d in ds:
    ex = (-1)**d * g[d]; ap = E[d]-O[d]
    rel = abs(float((ap - ex)/ex)); worst = max(worst, rel)
print('validated', len(ds), 'd values; max rel error of E-O vs exact g7:', worst)
for d in ds[-4:]: print(d, 'E/O =', float(E[d]/O[d]))
for d in (99995, 999999, 1000000):
    print(d, str(g[d])[:20], len(str(g[d])), repr(E[d]-O[d]), repr(E[d]), repr(O[d]))
