"""AUDIT: blocks.block_ratio has no assertion that the odd-side lower bound (1 - gfac - delta) is positive.
Recompute min over u-boxes (width 0.05, all n>=900) of each odd member's lower factor with delta=0.1518, using
the same formulas (imported), S_lo from clt.constants on a cell hull."""
import sys; sys.path.insert(0, 'rerun')
from mpmath import iv
from blocks import PATTERNS, member_data
from clt import constants
I = iv.mpf; ONE = I(1); n1 = 900; s = I([0, (ONE/I(n1-7)).b]); delta = I(0.1518)
worst = {}
u = 0.30
while u < 1.6 - 1e-12:
    U = I([u, u+0.05])
    for cls, pat in PATTERNS.items():
        for off, w, typ in pat['mem']:
            if typ != 'O': continue
            lr, dmu, dvar = member_data(off, pat['base_par'], U, s)
            X = -(2*off + off*off*s)/7 - dmu; X2 = I(max(abs(X.a), abs(X.b)))**2
            ui = U*(ONE + off*s); Si = I(constants(ui.a, ui.b, n1-7, 0.5)['S_lo'])
            gfac = X2*s.b*(ONE+7*s.b)**3/(2*Si); lo = (ONE - gfac - delta).a
            key = (cls, off); worst[key] = min(worst.get(key, 9), float(lo))
    u = round(u+0.05, 10)
for k, v in sorted(worst.items()): print('class', k[0], 'odd offset', k[1], 'min lower factor 1-gfac-delta =', v)
