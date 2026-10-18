"""Rigorous block verification over the base-u window [UA,UB] for all n >= N1.
Precomputes per u-cell (width 0.01): S_lo (sigma^2/n^3 lower bound) and delta (local CLT error), both for n >= N1-7.
Then checks every block pattern on u-boxes of width H; reports max E/O block ratio (must be <= 1-eta_b)."""
import sys, json, math
from mpmath import iv
from clt import constants, delta_bound
from blocks import block_ratio
I = iv.mpf
N1 = int(sys.argv[1]); UA = float(sys.argv[2]); UB = float(sys.argv[3]); H = float(sys.argv[4]) if len(sys.argv) > 4 else 0.0025
CW = 0.01
lo_cell = math.floor(UA*(1-7/N1)/CW)*CW - CW; hi_cell = math.ceil(UB*(1+13/N1)/CW)*CW + CW
cells = []
x = lo_cell
while x < hi_cell - 1e-12:
    a, b = round(x, 6), round(x+CW, 6)
    S = constants(a, b, N1-7, 0.5)['S_lo']
    D = delta_bound(a, b, N1-7)
    assert D['mono_ok']
    cells.append((a, b, float(S), D['delta']))
    x += CW
def cover(lo, hi):
    return [c for c in cells if c[1] > lo and c[0] < hi]
def S_lo_fn(u):
    cs = cover(float(u.a), float(u.b)); assert cs and cs[0][0] <= float(u.a) and cs[-1][1] >= float(u.b)
    return I(min(c[2] for c in cs))
res = {}
s1 = 1.0/(N1-7)
for cls in (0, 1, 2, 4):
    worst = 0; wu = None; dmax = 0
    u = UA
    while u < UB - 1e-12:
        ub = min(u+H, UB)
        cs = cover(u*(1-7*s1), ub*(1+12*s1)); assert cs[0][0] <= u*(1-7*s1) and cs[-1][1] >= ub*(1+12*s1)
        delta = max(c[3] for c in cs); dmax = max(dmax, delta)
        R = block_ratio(cls, I([u, ub]), N1, S_lo_fn, I(delta))
        if R > worst: worst, wu = R, u
        u = ub
    res[cls] = dict(max_ratio=float(worst), at_u=wu, max_delta=dmax)
    print('class', cls, res[cls], flush=True)
json.dump(dict(N1=N1, UA=UA, UB=UB, H=H, cells=cells, result=res), open(f'blocks_N{N1}_{UA}_{UB}.json', 'w'), indent=1)
