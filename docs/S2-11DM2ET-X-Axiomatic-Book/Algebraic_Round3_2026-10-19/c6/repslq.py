import json, glob, mpmath as mp
mp.mp.dps=70
res={}
for f in sorted(glob.glob('run6_s*_b*.json')):
    d=json.load(open(f)); s=d['s']; core=int(d['sqf'])
    errs=[abs(mp.mpf(d['coeffs'][str(e)]['val'])) for e in (0,2,4,6,8)]
    row={'err_even_max':mp.nstr(max(errs),3)}
    for e in ('-1','1','3','5','7','9'):
        r=mp.mpf(d['coeffs'][e]['val'])/mp.sqrt(2*mp.pi*s)
        basis=[r,1]+([mp.sqrt(core)] if core!=1 else [])
        rel=None
        for tol in (25,22,18):
            rel=mp.pslq(basis,tol=mp.mpf(10)**-tol,maxcoeff=10**12,maxsteps=10**6)
            if rel: break
        if rel:
            rel=[int(x) for x in rel]; den=rel[0]
            row[e]=dict(rat=f"{-rel[1]}/{den}",irr=(f"{-rel[2]}/{den}*sqrt({core})" if len(rel)>2 else None),height=max(abs(x) for x in rel),tol=tol)
        else: row[e]=None
    res[f"s{s}_a{d['a']}_b{d['b']} Delta={d['Delta']}"]=row
    print(f, json.dumps(row))
json.dump(res,open('repslq.json','w'),indent=1)
