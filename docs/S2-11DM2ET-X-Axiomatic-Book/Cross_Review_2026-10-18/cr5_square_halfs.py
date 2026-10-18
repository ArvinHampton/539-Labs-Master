# Cross-review check 5 (prediction test, Cat B): at even s with s/2 = m^2 (s=8,18) the SVD rank of the lift span is below the exact
# <gamma,-1> orbit bound (s/2)(s/2+1) by 2 and 6.  Conjectured gap m(m-1) => predict s=32: 272-12=260, s=50: 650-20=630.
# Controls (s/2 not a square): s=26, 28 should show no gap.  Uses Cusp-Onset funcspan.run unchanged (read-only import).
import sys, json
sys.path.insert(0, '../2026-10-18-Cusp-Onset')
from funcspan import run
from cr2_orbit_bound import bound
out = []
for s in [int(x) for x in sys.argv[1].split(',')]:
    b = bound(s)['dimV_upper']
    r1 = run(s, 25, verbose=False); r2 = run(s, 40, verbose=False)
    r = dict(s=s, exact_upper=b, svd_dimV_Q25=r1['dimV'], svd_dimV_Q40=r2['dimV'], dimW_Q25=r1['dimW'], dimW_Q40=r2['dimW'], gap=b - r2['dimV'])
    print(json.dumps(r), flush=True); out.append(r)
json.dump(out, open(f"cr5_square_halfs_{sys.argv[1].replace(',', '_')}.json", 'w'), indent=1)
