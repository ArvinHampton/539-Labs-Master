import json, sys
from funcspan import run
res = []
for s in [int(x) for x in sys.argv[1].split(',')]:
    Q = float(sys.argv[2]) if len(sys.argv) > 2 else 25
    r1 = run(s, Q, verbose=False); r2 = run(s, 1.6*Q, verbose=False)
    r1['stable_under_Qmax_x1.6'] = all(r1[k] == r2[k] for k in ('dimV', 'dimW', 'cusp_lo'))
    print(json.dumps(r1), flush=True); res.append(r1)
json.dump(res, open(f"funcspan_{sys.argv[1].replace(',', '_')}.json", 'w'), indent=1)
