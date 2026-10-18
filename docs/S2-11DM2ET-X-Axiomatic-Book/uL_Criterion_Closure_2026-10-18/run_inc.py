# Incremental version: analyse coprime data once, then each c-part, appending one JSON line per part (partials survive interruption).
import sys, json, numpy as np
from coset import *
s = int(sys.argv[1]); expos = [tuple(e) for e in json.loads(sys.argv[2])]; tag = sys.argv[3]
E = setup(s); cycv = np.array(E['cyc'])
T0 = T_c(E, {}); cr, S0, SJ = crit(E, T0)
Wl = W_local(E); psiW = closure([psi(E, u) for p in Wl for u in Wl[p]], cycv)
H = closure(Hgens(E), cycv)
head = dict(s=s, cyc=E['cyc'], crit=cr, psiW=len(psiW), S0=len(S0), S0_eq_psiW=(S0 == psiW),
            H_in_S0_plus_j=H <= SJ, primes=[list(map(str, E['key'](P))) for P in E['Ps']])
f = open(f'inc_s{s}_{tag}.jsonl', 'a'); f.write(json.dumps(head) + '\n'); f.flush()
for ex in expos:
    expo = {E['key'](P): e for P, e in zip(E['Ps'], ex)}
    T, cnt, tot = T_c_fast(E, expo, True)
    if not T: rec = dict(e=ex, empty=True, residues_total=tot)
    else:
        inv = all(tuple(((np.array(t) + np.array(g)) % cycv).tolist()) in T for t in T for g in S0)
        rec = dict(e=ex, n=len(T), residues=cnt, residues_total=tot, S0_union_cosets=inv, n_cosets=len(T)//len(S0), pure=genus_pure(E, T))
    f.write(json.dumps(rec) + '\n'); f.flush()
