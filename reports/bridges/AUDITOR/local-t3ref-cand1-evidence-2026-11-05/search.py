#!/usr/bin/env python3
"""Finite exact-integer exploration; not a proof for all positive integers."""
import json, hashlib
from array import array
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
N = 10_000_000
STEP_CAP = 100_000
TIP = Path('/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md')
EXPECTED = '7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91'
def sha(): return hashlib.sha256(TIP.read_bytes()).hexdigest()
def T(n):
    r = n % 3
    if r == 0: return n // 3
    if r == 1: return (4*n+2) // 3
    return (2*n+1) // 3
assert sha() == EXPECTED
h = array('I', [0]) * (N+1)
max_h = (0, 1)
max_stop = (0, 1)
max_peak = (2, 2)
result = {'N':N, 'step_cap':STEP_CAP, 'arithmetic':'Python arbitrary-precision integers',
          'start_time_chicago':datetime.now(ZoneInfo('America/Chicago')).isoformat()}
for n in range(3, N+1):
    x=n; seen=set(); steps=0
    # All positive starts below n are already known to reach {1,2}.
    while x >= n:
        if x in seen:
            result.update(status='COUNTEREXAMPLE_CYCLE', start=n, repeated=x)
            break
        if steps == STEP_CAP:
            result.update(status='UNRESOLVED_CAP', start=n, current=x)
            break
        seen.add(x)
        x=T(x); steps+=1
        if x > max_peak[0]: max_peak=(x,n)
    else:
        assert 1 <= x < n
        h[n]=steps+h[x]
        if h[n] > max_h[0]: max_h=(h[n],n)
        if steps > max_stop[0]: max_stop=(steps,n)
        continue
    break
else:
    result.update(status='ALL_REACH_1_2', checked_positive_starts=N)
result.update(max_first_entry_steps_and_first_start=max_h,
              max_first_descent_steps_and_first_start=max_stop,
              max_observed_value_and_start_segment=max_peak)
x=4880; orbit=[x]
while x not in (1,2): x=T(x); orbit.append(x)
y=4880
for _ in range(539): y=T(y)
result.update(sample_4880_to_first_entry=orbit, sample_entry_steps=len(orbit)-1,
              sample_iterate_539=y, tip_sha256_before=EXPECTED, tip_sha256_after=sha(),
              end_time_chicago=datetime.now(ZoneInfo('America/Chicago')).isoformat())
assert result['tip_sha256_after'] == EXPECTED
out=Path(__file__).with_name('search-result.json')
out.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
