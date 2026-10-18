# Exact tables: every component c, sign s, character chi of Cl_m^+ (m = p2^3 p5 p7 oo oo, cyc [24,2,2]) with Fhat_{c,s}(chi) != 0,
# written as r * e(k/K) with r rational, k/K rational (recognised from floats; recognition residual reported).
import pickle, numpy as np, json, cmath, math
from fractions import Fraction as Fr
from family import LABELS
d=pickle.load(open("fitF.pkl","rb")); pc=d['per_comp']; info=d['info']
import itertools
chars=list(itertools.product(*[range(c) for c in d['cyc']]))
def rec(v):
    r=abs(v); th=(cmath.phase(v)/(2*math.pi))%1
    R=Fr(r).limit_denominator(2000); T=Fr(th).limit_denominator(840)
    err=abs(float(R)*cmath.exp(2j*math.pi*float(T))-v)
    return str(R),str(T),err
# Recompute full Fhat (not only cusp) from saved fits is not stored; cusp_chars stores non-invariant ones.  Re-derive all from fitF? store cusp only + Eis norms.
tab={}; maxerr=0
for i,r in pc.items():
    e={}
    for s,rr in r.items():
        if rr is None: e[str(s)]=None; continue
        lst=[]
        for chi,v in rr['cusp_chars']:
            R,T,err=rec(complex(v)); maxerr=max(maxerr,err); lst.append(dict(chi=list(chi),abs=R,phase_turns=T))
        e[str(s)]=dict(g=rr['g'],eis_norm2=rr['eis'],cusp_norm2=rr['cusp'],mixed_norm2=rr['mixed'],fit_resid=rr['resid'],cusp_coeffs=lst)
    tab[i]=dict(alpha70=[int(t) for t in LABELS[i][0]],beta70=[int(t) for t in LABELS[i][1]],data=e)
json.dump(tab,open("component_split.json","w"),indent=1)
print("rational recognition max error",maxerr)
c=73; print(c, tab[c]['alpha70'], tab[c]['beta70'], [(x['chi'],x['abs'],x['phase_turns']) for x in tab[c]['data']['1']['cusp_coeffs']])
