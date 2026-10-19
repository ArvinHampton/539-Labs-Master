# Checkpointed t^{17/2} run: reuses the exact e <= 15 entries of sym_universal_P1_K15.pkl (identical code path) and computes
# only e = 17 with the functions of sym_engine_K15.py; each (i, r) edge term is checkpointed to e17_ckpt.pkl.
import pickle, os, sympy as sp
import sym_engine_K15 as E
s, g, lam, m = E.s, E.g, E.lam, E.m
P, e = 1, 17
ck = pickle.load(open('e17_ckpt.pkl', 'rb')) if os.path.exists('e17_ckpt.pkl') else {}
def save(): pickle.dump(ck, open('e17_ckpt.pkl.tmp', 'wb')); os.replace('e17_ckpt.pkl.tmp', 'e17_ckpt.pkl')
i = e + 2
if 'A' not in ck:
    ck['A'] = E.sp_simplify(-2*lam**i/sp.factorial(i)*E.J(i)) if i % 2 == 1 else 0; save(); print('A done', flush=True)
for i in range(0, e + 2):
    r = e + 1 - i
    if r < 0 or (i + r) % 2 or ('edge', i) in ck: continue
    IY, IX = E.edge_integrals(i, r, P)
    f = -2*(-lam)**i/(sp.factorial(i)*sp.factorial(r + 1))
    ck[('edge', i)] = (r + 1, f*IY*m**(-r), f*IX*m**(-r)); save(); print('edge i=%d done' % i, flush=True)
U = pickle.load(open('sym_universal_P1_K15.pkl', 'rb'))
Yc, Xc = {}, {}
for k, v in ck.items():
    if k == 'A': continue
    rr, y, x = v; Yc[rr] = Yc.get(rr, 0) + y; Xc[rr] = Xc.get(rr, 0) + x
U[17] = (ck['A'], Yc, Xc)
pickle.dump(U, open('sym_universal_P1_K17.pkl', 'wb')); print('wrote sym_universal_P1_K17.pkl', flush=True)
