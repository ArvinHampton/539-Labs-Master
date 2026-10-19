# Held-out direct check (Cat B, numerics): (H^axes(e^{-t}) - sum_{e<=9} c_e eps^e)/eps^11 -> c_11 as t->0.
import pickle, mpmath as mp, sympy as sp, json
from verify import Hdirect
mp.mp.dps=40
d=pickle.load(open('axes_closed_K13.pkl','rb')); c=d['c']; w=sp.symbols('w',positive=True)
out={}
for s in (20,):
    cv={e:mp.mpf(sp.N(c[e].subs(w,sp.sqrt(sp.Rational(s,2))),45)) for e in range(-2,14)}
    rows=[]
    for t in ('0.004','0.002','0.001'):
        t=mp.mpf(t); e_=mp.sqrt(t)
        r=(Hdirect(s,t)-sum(cv[e]*e_**e for e in range(-2,10)))/e_**11
        rows.append((mp.nstr(t,3),mp.nstr(r,10),mp.nstr(cv[11]+cv[13]*t,10)))
        print(s,rows[-1],flush=True)
    out[s]=rows
json.dump(out,open('verify_direct.json','w'),indent=1,default=str)
