import json
from alg_T import *
out = {}
for s in (32, 34, 36, 40):
    E = setup(s); T = T_c(E, {}); d = json.load(open(f'enum/deep_cparts_s{s}_coprime_B200000.json'))
    Te = set(map(tuple, d['cparts'][0]['T'])); out[s] = dict(equal=(T == Te), n=len(T), complete=d['cparts'][0]['complete'], pure_enum=d['cparts'][0]['genus_pure'], pure_alg=genus_pure(E, T))
    print(s, out[s], flush=True)
json.dump(out, open('cmp_enum_32_40.json', 'w'), indent=1)
