# Item (d): s = 64 (k = 6): negation on the 2-adic factor (labels with zero odd part) and on the odd factor; dim W exactly.
import sys, json, cmath, math, numpy as np
from fractions import Fraction as Fr
from family_s import Family
from even_exact import red
out=[]
for s in map(int,sys.argv[1].split(',')):
    F=Family(s); D=F.D; mo=D
    while mo%2==0: mo//=2
    m2=D//mo; eo=(pow(m2,-1,mo)*m2)%D
    two=[i for i,(al,be) in enumerate(F.LABELS) if all((eo*np.array(al))%D==0)]
    odd=[i for i,(al,be) in enumerate(F.LABELS) if all(((1-eo)*np.array(al))%D==0) and all(((1-eo)*np.array(be))%D==0)]
    def trneg(L):
        tr=0; Ls=set(L)
        for i in L:
            al,be=F.LABELS[i]; j,ph=red(F,(-np.array(al))%D,-np.array(be)); assert j in Ls
            if j==i: tr+=cmath.exp(2j*math.pi*float(ph))
        return tr
    t2=trneg(two); to=trneg(odd)
    n2,no=len(two),len(odd)
    W2p=(n2+t2.real)/2; W2m=(n2-t2.real)/2; Wop=(no+to.real)/2; Wom=(no-to.real)/2
    # direct full count
    tfull=trneg(range(F.N))
    k=0; t=s//2; v=2*t*(t-1)
    while v%2==0: v//=2; k+=1
    r=dict(s=s,k=k,u_mod8=v%8,N=F.N,n2=n2,n_odd=no,W2_plus=round(W2p,6),W2_minus=round(W2m,6),Wodd_plus=round(Wop,6),Wodd_minus=round(Wom,6),
           dimW_from_factors=round(W2p*Wop+W2m*Wom,6),dimW_direct=round((F.N+tfull.real)/2,6),imag_check=abs(t2.imag)+abs(to.imag))
    print(json.dumps(r),flush=True); out.append(r)
json.dump(out,open("s64_W.json","w"),indent=1)
