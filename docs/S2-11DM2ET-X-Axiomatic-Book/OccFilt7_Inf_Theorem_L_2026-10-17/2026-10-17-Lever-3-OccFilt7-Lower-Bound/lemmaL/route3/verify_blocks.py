"""Rigorous block verification over the base-u window [UA,UB] for all n >= N1.
Precomputes per u-cell (width 0.01): S_lo (sigma^2/n^3 lower bound) and delta (local CLT error), both for n >= N1-7.
Then checks every block pattern on u-boxes of width H; reports max E/O block ratio (must be <= 1-eta_b)."""
import sys, json, math
from mpmath import iv
from clt import constants, delta_bound
from blocks import block_ratio, MIN_ODD_FACTOR
from mpmath import mp
def down(x): return math.nextafter(float(x), -math.inf) if float(x) > x else float(x)   # outward (for JSON only)
def up(x): return math.nextafter(float(x), math.inf) if float(x) < x else float(x)
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
    cells.append((a, b, S, D['delta'], D['D2'], D['D3']))   # rev2: mpf endpoints kept (S lower end, delta upper end)
    x += CW
def cover(lo, hi):
    return [c for c in cells if c[1] > lo and c[0] < hi]
def S_lo_fn(u):
    cs = cover(u.a, u.b); assert cs and cs[0][0] <= u.a and cs[-1][1] >= u.b   # rev2: mpf endpoints
    return I(min(c[2] for c in cs))
res = {}
s1 = (I(1)/I(N1-7)).b   # rev2: upper end of s
for cls in (0, 1, 2, 4):
    worst = 0; wu = None; dmax = 0
    u = UA
    while u < UB - 1e-12:
        ub = min(u+H, UB)
        mlo = (I(u)*(1-7*I(s1))).a; mhi = (I(ub)*(1+12*I(s1))).b   # rev2: outward member-tilt range
        cs = cover(mlo, mhi); assert cs[0][0] <= mlo and cs[-1][1] >= mhi
        delta = max(c[3] for c in cs); dmax = max(dmax, delta)
        R = block_ratio(cls, I([u, ub]), N1, S_lo_fn, I(delta))
        if R > worst: worst, wu = R, u
        u = ub
    res[cls] = dict(max_ratio=up(worst), at_u=wu, max_delta=up(dmax))
    print('class', cls, res[cls], flush=True)
res['min_odd_factor'] = down(MIN_ODD_FACTOR[0]); res['max_D2'] = up(max(c[4] for c in cells)); res['max_D3'] = up(max(c[5] for c in cells))
print('min odd-side factor', res['min_odd_factor'], 'max D2', res['max_D2'], 'max D3', res['max_D3'])
cells = [(a, b, down(S), up(dl), up(d2), up(d3)) for (a, b, S, dl, d2, d3) in cells]   # outward-rounded copies for the JSON record
json.dump(dict(N1=N1, UA=UA, UB=UB, H=H, cells=cells, result=res), open(f'blocks_N{N1}_{UA}_{UB}.json', 'w'), indent=1)
