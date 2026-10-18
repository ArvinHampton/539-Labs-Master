# Validate the bound-free T_c against every previously enumerated (complete) part.
import json, glob, os, sys
from alg_T import *
OLD = '../2026-10-18-Cusp-Onset-Closure/'
res = {}
def load_uL(s):
    for f in [OLD+f'big/uL_rayclass_{s}_M1.json', OLD+f'uL_rayclass_{s}_M1.json']:
        if os.path.exists(f):
            d = json.load(open(f)); return d[0] if isinstance(d, list) else d
out = []
for s in range(5, 45):
    r = load_uL(s)
    if r is None: continue
    E = setup(s)
    assert E['cyc'] == r['cyc'], (s, E['cyc'], r['cyc'])
    T = T_c(E, {}); cr, S, SJ = crit(E, T)
    c0 = [o for o in r['cparts'] if o['c'] == []]
    old = r['crit']
    rec = dict(s=s, alg=cr, alg_pure=genus_pure(E, T), old_complete=(c0[0]['complete'] if c0 else None),
               old_T=old.get('T_size'), old_S_equal=(set(map(tuple, old.get('S_elems', []))) == S),
               old_Gbar=old.get('Gbar'), old_Hbar=old.get('Hbar'), old_pure=(c0[0].get('genus_pure') if c0 else None))
    rec['agree'] = (rec['old_T'] == cr['T'] and rec['old_S_equal'])
    print(json.dumps(rec), flush=True); out.append(rec)
# deep parts with stored T sets
for f in sorted(glob.glob(OLD+'deepB/deep_cparts_s*_p*.json')):
    d = json.load(open(f)); s = d['summary']['s']; E = setup(s)
    keymap = {f'{E["key"](P)[0]}:{E["key"](P)[1]}': E['key'](P) for P in E['Ps']}
    for cp in d['cparts']:
        expo = {keymap[k]: v for k, v in cp['expo'].items()}
        T = T_c(E, expo); Told = set(map(tuple, cp['T']))
        rec = dict(file=os.path.basename(f), s=s, expo=cp['expo'], old_complete=cp['complete'], equal=(T == Told), alg_n=len(T), old_n=len(Told),
                   alg_pure=genus_pure(E, T), old_pure=cp['genus_pure'])
        print(json.dumps(rec), flush=True); out.append(rec)
json.dump(out, open('validate.json', 'w'), indent=1)
