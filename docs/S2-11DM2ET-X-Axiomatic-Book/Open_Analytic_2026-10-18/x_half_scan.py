# Engine-only scan at x = 1/2: test the even-s closed forms and the odd-s vanishing at more s (K = 7 gives t^{7/2} too).
import mpmath as mp, json, sys
from asym_engine import expansion
out = []
for s in [int(z) for z in sys.argv[1].split(',')]:
    c = expansion(s, 1, 2, 7); r = mp.sqrt(2*mp.pi*s)
    norm = {e: c[e]/r for e in c}
    pred = {1: -mp.mpf(1)/8, 3: mp.mpf(s-4)/64, 5: -mp.mpf(31*s*s - 168*s + 192)/3072} if s % 2 == 0 else {e: 0 for e in (1, 3, 5)}
    row = dict(s=s, normalized={str(e): [float(norm[e].real), float(norm[e].imag)] for e in norm},
               max_dev_pred=float(max(abs(norm[e] - pred[e]) for e in pred)), max_int_order=float(max(abs(c[e]) for e in c if e % 2 == 0)),
               t_m1half=float(abs(c[-1])))
    out.append(row); print(json.dumps(row), flush=True)
json.dump(out, open('x_half_scan_' + sys.argv[1].replace(',', '_') + '.json', 'w'), indent=1)
