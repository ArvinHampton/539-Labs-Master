import sys, json
from coset import *
s = int(sys.argv[1]); expos = [tuple(e) for e in json.loads(sys.argv[2])]; tag = sys.argv[3]
r = analyse(s, expos); print(json.dumps(r), flush=True)
json.dump(r, open(f'coset_s{s}_{tag}.json', 'w'), indent=1)
