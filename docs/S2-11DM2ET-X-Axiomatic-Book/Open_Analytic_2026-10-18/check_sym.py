# compare symbolic universal form + Gauss data against the exact-term engine (asym_engine.py) and the exact atomic sums
import pickle, sys, json, sympy as sp, mpmath as mp
from sym_engine import s as S, g as Gs
from gauss_data import data
from asym_engine import expansion
P = int(sys.argv[1]); K = int(sys.argv[2]); a, N = (int(z) for z in sys.argv[3].split('/')); ss = [int(z) for z in sys.argv[4:]]
U = pickle.load(open('sym_universal_P%d_K%d.pkl' % (P, K), 'rb'))
out = []
for s in ss:
    d = data(s, a, N, R=K + 3)
    eng = expansion(s, a, N, K)
    row = dict(s=s, g=d['g'])
    for e, (A, Yc, Xc) in U.items():
        val = d['gamma0']*A + sum(d['eb'][k]*Yc[k] for k in Yc) + sum(d['ea'][k]*Xc[k] for k in Xc)
        v = complex(sp.N(val.subs({S: s, Gs: d['g']}), 30))
        row['e%d' % e] = [v.real, v.imag, float(eng[e].real), float(eng[e].imag), abs(v - complex(eng[e]))]
    out.append(row); print(json.dumps(row), flush=True)
json.dump(out, open('check_sym_%d-%d_K%d.json' % (a, N, K), 'w'), indent=0)
