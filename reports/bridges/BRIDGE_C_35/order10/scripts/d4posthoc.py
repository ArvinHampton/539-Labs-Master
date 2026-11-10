# POST-HOC (descriptive): D4 with endpoint sums over the full Q-shell (box |n|,|k|<=200, |Q|<=8), not the 29x29 box
import sys,json; sys.dont_write_bytecode=True
exec(open('d.py').read().split("inv=[0")[0])
inv=[0,12,18,23,29,35,47,53,58,64,70,82,88,93,99]; res=[]
for j in inv:
    al,be=pairs[j]; b0={}; b1={}
    for n in range(-200,201):
        for k in range(-200,201):
            nu=(al[0]+n,al[1]+k); Q=Fr(Bf(nu,nu),2)
            if abs(Q)>8: continue
            nm=tuple(mp.mpf(c.numerator)/c.denominator for c in nu); p=ph(nu,be)
            for y in (mp.mpf(1)/2,1,2):
                key=(Q,y); b0[key]=b0.get(key,0)+p*bnd(nm,y,0); b1[key]=b1.get(key,0)+p*bnd(nm,y,L2)
    d=max(abs(b1[k]-b0[k]) for k in b0); res.append([j,mp.nstr(d,4)]); print(j,mp.nstr(d,4),flush=True)
json.dump(res,open('../data/d4posthoc.json','w'))
