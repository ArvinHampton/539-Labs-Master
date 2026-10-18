import json, time
from alg_T import *
ok = True
for s, exps in [(9, [(0,0,0,0),(0,1,1,0),(0,1,2,0),(0,2,2,0)]), (16, [(0,0),(1,0),(2,0),(0,1)]), (24, [(0,0,0),(1,2,0),(3,1,0),(0,0,1),(1,1,1)]), (18, [(0,0,0),(0,1,0),(0,2,0)]), (32, [(0,0,0),(2,0,0),(3,0,0)])]:
    E = setup(s)
    for ex in exps:
        expo = {E['key'](P): e for P, e in zip(E['Ps'], ex)}
        t = time.time(); A = T_c(E, expo); t1 = time.time() - t
        t = time.time(); B, cnt, tot = T_c_fast(E, expo, True); t2 = time.time() - t
        print(s, ex, len(A), len(B), A == B, tot, round(t1, 2), round(t2, 2), flush=True); ok &= (A == B)
print('ALL_EQUAL', ok)
