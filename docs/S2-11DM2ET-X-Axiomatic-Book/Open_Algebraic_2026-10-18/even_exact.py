# Item 2: exact (Fractions) tensor factorisation for even s: labels = (odd part of alpha) x (2-parts of alpha, beta).
# Checks exactly: supp(S) = supp_odd x supp_2 and exponent r = f(x,y) + h(A,B) mod 1; T monomial with perm/phase splitting.
# Then: odd factor = Weil rep of (L'_odd, -Q) ; 2-adic factor dims; negation and gamma split; U = Fix(N)∩Fix(gamma) per sector.
import sys, json, math, itertools, numpy as np
from fractions import Fraction as Fr
from family_s import Family
def red(F,al,be):
    al=np.array(al); be=np.array(be)
    for b0 in F.BES:
        mu=be-np.array(b0)
        if F.inLp(mu): return F.IDX[(tuple(al%F.D),b0)], F.B(al,mu)%1
    raise ValueError
def run(s):
    F=Family(s); D=F.D; N=F.N
    mo=D
    while mo%2==0: mo//=2
    m2=D//mo; eo=(pow(m2,-1,mo)*m2)%D; e2=(1-eo)%D
    key=[]
    for al,be in F.LABELS:
        al=np.array(al); be=np.array(be); key.append((tuple((eo*al)%D),(tuple((e2*al)%D),tuple((e2*be)%D))))
    O=sorted({k[0] for k in key}); Tw=sorted({k[1] for k in key})
    assert len(O)*len(Tw)==N and len(set(key))==N
    kidx={k:i for i,k in enumerate(key)}
    # exact S rows
    Sx={}
    for i,(al,be) in enumerate(F.LABELS):
        al=np.array(al); be=np.array(be); pre=F.B(al,be)
        for p in F.LP:
            j,ph=red(F,p-be,al); Sx[(i,j)]=(pre+ph)%1
    Tx={}
    for i,(al,be) in enumerate(F.LABELS):
        al=np.array(al); be=np.array(be); j,ph=red(F,al,al+be+F.WC); Tx[i]=(j,(-F.Q(al)-F.B(al,F.WC)+ph)%1)
    # support factorisation
    supO={}; sup2={}
    for (i,j) in Sx:
        supO.setdefault(key[i][0],set()).add(key[j][0]); sup2.setdefault(key[i][1],set()).add(key[j][1])
    pairsO={(key[i][0],key[j][0]) for (i,j) in Sx}; pairs2={(key[i][1],key[j][1]) for (i,j) in Sx}
    okSupp=len(Sx)==len(pairsO)*len(pairs2)
    x0=O[0]; A0,B0=next(iter(sorted(pairs2)))
    okExp=okSupp and all((r-Sx[(kidx[(key[i][0],A0)],kidx[(key[j][0],B0)])]-Sx[(kidx[(x0,key[i][1])],kidx[(x0,key[j][1])])]
                 +Sx[(kidx[(x0,A0)],kidx[(x0,B0)])])%1==0 for (i,j),r in Sx.items())
    oddS={(x,y):Sx[(kidx[(x,A0)],kidx[(y,B0)])]-Sx[(kidx[(x0,A0)],kidx[(x0,B0)])] for (x,y) in pairsO}
    sB=all((oddS[(x,y)]+F.B(np.array(x),np.array(y)))%1==0 for (x,y) in pairsO)
    sBp=all((oddS[(x,y)]-F.B(np.array(x),np.array(y)))%1==0 for (x,y) in pairsO)
    okT=all(key[j][0]==key[i][0] for i,(j,_) in Tx.items())
    okTexp=all((Tx[kidx[(x,A)]][1]-Tx[kidx[(x,Tw[0])]][1]-Tx[kidx[(O[0],A)]][1]+Tx[kidx[(O[0],Tw[0])]][1])%1==0 for x in O for A in Tw)
    # odd factor: T exponent t(x) vs -Q(x) ; S kernel vs -B(x,y)
    tO={x:(Tx[kidx[(x,Tw[0])]][1]-Tx[kidx[(O[0],Tw[0])]][1])%1 for x in O}
    qmatch=all((tO[x]-(-F.Q(np.array(x))+F.Q(np.array(O[0]))))%1==0 for x in O)
    qplus=all((tO[x]-(F.Q(np.array(x))-F.Q(np.array(O[0]))))%1==0 for x in O)
    # gamma and negation splitting
    def act(f):
        out={}
        for i,(al,be) in enumerate(F.LABELS):
            j,ph=red(F,f(np.array(al))%D,f(np.array(be))); out[i]=(j,ph)
        return out
    G=F.G
    acts={}
    for nm,f in (("neg",lambda v:-v),("gamma",lambda v:G@v)):
        Aa=act(f)
        oddmap={key[i][0]:key[j][0] for i,(j,_) in Aa.items()}
        cons=all(oddmap[key[i][0]]==key[j][0] for i,(j,_) in Aa.items())
        twomap={}; cons2=True
        for i,(j,ph) in Aa.items():
            k=key[i][1]
            if k in twomap and twomap[k][0]!=key[j][1]: cons2=False
            twomap.setdefault(k,(key[j][1],ph))
        # phase independent of odd coordinate?
        phx=all(ph==Aa[kidx[(O[0],key[i][1])]][1] for i,(j,ph) in Aa.items())
        # odd map is multiplication by scalar?
        mult=None
        acts[nm]={"odd_map_consistent":cons,"two_map_consistent":cons2,"phase_independent_of_odd":phx}
    res={"s":s,"N":N,"|odd|":len(O),"|2adic|":len(Tw),"S_support_product":okSupp,"S_exponent_split":okExp,
         "T_perm_2adic_only":okT,"T_exponent_split":okTexp,"odd_T_is_e(-Q)":qmatch,"odd_T_is_e(+Q)":qplus,"odd_S_kernel_e(-B)":sB,"odd_S_kernel_e(+B)":sBp,"|supp_odd|":len(pairsO),"|supp_2|":len(pairs2),"actions":acts}
    return res,F,O,Tw,key,Sx,Tx
if __name__=="__main__":
    out=[]
    for s in [int(z) for z in sys.argv[1].split(',')]:
        r=run(s)[0]; out.append(r); print(json.dumps(r),flush=True)
    json.dump(out,open(f"even_exact_{sys.argv[1].replace(',','_')}.json","w"),indent=1)
