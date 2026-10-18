# A(3): are all c-part class sets T_c translates of T_0 (or of sigma(T_0)) in G = Cl^+_M?  If so, genus-purity (H-invariance,
# H = (1-sigma)G) of every c-part follows from that of the coprime part, since translation commutes with H-invariance.
import json, sys, numpy as np, glob
out = {}
for f in sorted(glob.glob('deepB/deep_cparts_s*_p*.json')):
    d = json.load(open(f)); cps = d['cparts']; s = d['summary']['s']
    # cyc not stored: infer modulus per coordinate as max+1 is unsafe -> recompute from uL json
    r = json.load(open(f'uL_rayclass_{s}_M1.json')); r = r[0] if isinstance(r, list) else r
    cyc = np.array(r['cyc'])
    T0 = {tuple(t) for t in cps[0]['T']} if cps[0]['expo'] == {} else None
    if T0 is None: continue
    T0a = np.array(sorted(T0))
    res = []
    for cp in cps:
        T = {tuple(t) for t in cp['T']}
        if not T: continue
        t0 = np.array(next(iter(T)))
        ok = any({tuple(((x + (t0 - g)) % cyc).tolist()) for x in T0a} == T for g in T0a)
        res.append((cp['expo'], len(T), ok))
    out[f] = dict(s=s, n=len(res), all_translates=all(x[2] for x in res), sizes=sorted({x[1] for x in res}))
    print(f, out[f])
json.dump(out, open('deep_translate.json', 'w'), indent=1)
# second test: every T_c is a union of cosets of S0 = Stab(T_0)  (=> union of translates of T_0, T_0 being one S0-coset)
print('--- S0-coset unions ---')
out2 = {}
for f in sorted(glob.glob('deepB/deep_cparts_s*_p*.json')):
    d = json.load(open(f)); cps = d['cparts']; s = d['summary']['s']
    r = json.load(open(f'uL_rayclass_{s}_M1.json')); r = r[0] if isinstance(r, list) else r
    cyc = np.array(r['cyc']); T0 = {tuple(t) for t in cps[0]['T']}
    t0 = np.array(next(iter(T0)))
    S0 = [np.array(x) - t0 for x in T0]
    S0 = [g % cyc for g in S0 if {tuple(((np.array(x) + g) % cyc).tolist()) for x in T0} == T0]
    oks = []
    for cp in cps:
        T = {tuple(t) for t in cp['T']}
        oks.append(all({tuple(((np.array(x) + g) % cyc).tolist()) for x in T} == T for g in S0))
    out2[f] = dict(s=s, S0=len(S0), T0=len(T0), T0_is_S0_coset=len(S0) == len(T0), all_Tc_S0_invariant=all(oks), n=len(oks))
    print(f, out2[f])
json.dump(dict(translates=out, s0_unions=out2), open('deep_translate.json', 'w'), indent=1)
