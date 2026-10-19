# Universal-piece identity check: frozen x=0 rational part R_e (this folder; closed_P1_*) vs the axes S^ax_e of
# ../2026-10-18-Algebraic-Round3/c7/axes_RS_forms.json, e = 7, 9, 11, 13 (t^{7/2}..t^{13/2}); exact rational-function comparison.
import json, pickle, sympy as sp
from sym_engine import s
ax = json.load(open('../2026-10-18-Algebraic-Round3/c7/axes_RS_forms.json'))
S_ = sp.Symbol('s', positive=True)
src = {7: 'closed_P1_e7_lowK13.pkl', 9: 'closed_P1_e9_lowK13.pkl', 11: 'closed_P1_e11.pkl', 13: 'closed_P1_e13.pkl'}
out = {}
for e, f in src.items():
    R = pickle.load(open(f, 'rb'))['R']
    Sax = sp.sympify(ax[str(e)]['S'], locals={'s': s})
    Rax = sp.sympify(ax[str(e)]['R'], locals={'s': s})
    out[e] = dict(R_frozen_minus_Sax=str(sp.simplify(R - Sax)), R_frozen_minus_Rax_is_zero=bool(sp.simplify(R - Rax) == 0))
    print(e, out[e], flush=True)
json.dump(out, open('compare_axes.json', 'w'), indent=1)
