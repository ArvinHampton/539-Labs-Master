# Exact label actions of the unit gamma=G and of negation, in local coordinates (x mod 35 -> (x5,x7), eps, delta).
import sys; sys.path.insert(0,'.')
import numpy as np
from fractions import Fraction as F
from exact import red, D
from family import G, LABELS, B70
g=np.array([14,6]); a2=np.array([35,0])
lab=[(x,e,d) for x in range(35) for e in (0,1) for d in (0,1)]; idx={l:k for k,l in enumerate(lab)}
J={k:red((x*g+e*a2)%D,-d*a2) for k,(x,e,d) in enumerate(lab)}; inv={j:(k,ph) for k,(j,ph) in J.items()}
def act(fa,fb):
    """u'_k (label k) equals e(phase) u'_{k'} under the identity u_{f(al),f(be)} = u_{al,be}. Return dict k->(k',phase)."""
    res={}
    for k,(x,e,d) in enumerate(lab):
        al=(x*g+e*a2)%D; be=-d*a2
        # u'_k = e(ph_k) u_{j_k};  u_{al,be} = u_{f al, f be} = e(ph2) u_{j2}
        j2,ph2=red(fa(al)%D, fb(be))
        k2,ph_k2=inv[j2]       # u'_{k2} = e(ph_k2) u_{j2}
        # u'_k = u_{al,be} * 1 (since red(al,be) gives J[k]) ; careful: u_{al,be} = e(J[k].ph) u_{J[k].j} = u'_k
        res[k]=(k2,(ph2-ph_k2)%1)   # u'_k = e(ph2-ph_k2) u'_{k2}
    return res
out=[]
for nm,fa in (("gamma G",lambda v:G@v),("negation",lambda v:-v),("gamma*neg",lambda v:-(G@v))):
    A=act(fa,fa)
    xs=[(lab[k][0],lab[k2][0]) for k,(k2,_) in A.items()]
    s5={x%5 and (y%5)*pow(x%5,-1,5)%5 for x,y in xs if x%5}; s7={(y%7)*pow(x%7,-1,7)%7 for x,y in xs if x%7}
    two={lab[k][1:]:lab[k2][1:] for k,(k2,_) in A.items() if lab[k][0]==0}
    # phase structure: phase = f5(x5)+f7(x7)+f2(2adic)?
    ph=lambda x,e,d: A[idx[(x,e,d)]][1]
    def xo(a,b): return [x for x in range(35) if x%5==a and x%7==b][0]
    ok=all((ph(x,e,d)-ph(xo(x%5,0),e,d)-ph(xo(0,x%7),e,d)+ph(0,e,d))%1==0 for (x,e,d) in lab)
    p2={lab[k][1:]:str(A[k][1]) for k in A if lab[k][0]==0}
    pxv=sorted({str(ph(x,0,0)) for x in range(35)})
    out.append(f"{nm}: x5 -> {s5}·x5, x7 -> {s7}·x7; 2-adic map {two}; phases separable: {ok}; 2-adic phases at x=0: {p2}; x-phases (eps=delta=0): {pxv}")
print("\n".join(out)); open("gaction.txt","w").write("\n".join(out)+"\n")
