# Exact tensor factorisation for odd s: basis u'_{x,eps,delta} = u_{x g + eps a2, -delta a2},
# g = A^{-1} e2 (generator of L'/Z^2 = Z/n, n = s(s-2)), a2 = (1/2,0).  All arithmetic in Fractions.
import sys, json, math, numpy as np
from fractions import Fraction as F
from family_s import Family
def factorize(s):
    Fm=Family(s); D=Fm.D; n=s*(s-2); A=Fm.A
    def red(al,be):
        al=np.array(al); be=np.array(be)
        for b0 in Fm.BES:
            mu=be-np.array(b0)
            if Fm.inLp(mu): return Fm.IDX[(tuple(al%D),b0)], Fm.B(al,mu)%1
        raise ValueError
    g=Fm.AINV@np.array([0,1]); a2=np.array([D//2,0])
    assert len({tuple((x*g)%D) for x in range(n)})==n, "L'/Z^2 not cyclic via g"
    lab=[(x,e,d) for x in range(n) for e in (0,1) for d in (0,1)]; idx={l:k for k,l in enumerate(lab)}
    J={k:red((x*g+e*a2)%D,-d*a2) for k,(x,e,d) in enumerate(lab)}
    assert len({j for j,_ in J.values()})==Fm.N==4*n
    inv={j:(k,ph) for k,(j,ph) in J.items()}
    # exact S,T on labels
    Sx={}
    for i,(al,be) in enumerate(Fm.LABELS):
        al=np.array(al); be=np.array(be); pre=Fm.B(al,be)
        for p in Fm.LP:
            j,ph=red(p-be,al); Sx.setdefault(i,[]).append((j,(pre+ph)%1))
    Tx={}
    for i,(al,be) in enumerate(Fm.LABELS):
        al=np.array(al); be=np.array(be); j,ph=red(al,al+be+Fm.WC); Tx[i]=(j,(-Fm.Q(al)-Fm.B(al,Fm.WC)+ph)%1)
    Sp={}
    for k,(jk,phk) in J.items():
        for j,r in Sx[jk]:
            l,phl=inv[j]; Sp[(k,l)]=(phk+r-phl)%1
    Tp={}
    for k,(jk,phk) in J.items():
        j,r=Tx[jk]; l,phl=inv[j]; Tp[k]=(l,(phk+r-phl)%1)
    res={"s":s,"n":n,"N":4*n}
    # T: perm only on 2-adic, exponent = x^2 * kT / n + t2 ?
    res["T_perm_2adic_only"]=all(lab[l][0]==lab[k][0] for k,(l,_) in Tp.items())
    T2={str(lab[k][1:]):[str(lab[Tp[k][0]][1:]),str(Tp[k][1])] for k in range(4)}
    t2={lab[k][1:]:Tp[k][1] for k in range(4)}
    kT=[c for c in [n-1] if all((Tp[idx[(x,e,d)]][1]-t2[(e,d)]-F(c*x*x,n))%1==0 for (x,e,d) in lab)]
    res["T_exponent_kT_over_n"]=kT; res["T2"]=T2
    # S: support pattern and exponent = cS*x*y/n + s2
    pat={}
    for (k,l) in Sp:
        if lab[k][0]==0: pat.setdefault(lab[k][1:],set()).add(lab[l][1:])
    res["S_2adic_support"]={str(k):sorted(map(str,v)) for k,v in pat.items()}
    s2={}; ok=True
    for (e,d),tg in pat.items():
        (e2,d2),=tg; s2[((e,d),(e2,d2))]=Sp[(idx[(0,e,d)],idx[(0,e2,d2)])]
    c=(n-2)%n; cS=[c]
    tgt=lambda e,d: next(iter(pat[(e,d)]))
    ok=all((Sp[(idx[(x,e,d)],idx[(y,)+tgt(e,d)])]-s2[((e,d),tgt(e,d))]-F(c*x*y,n))%1==0 for x in range(n) for (e,d) in pat for y in range(n))
    ok=ok and len(Sp)==4*n*n
    res["S_exponent_cS_over_n"]=cS[:1]; res["S_full_check"]=ok
    res["S2"]={str(k):str(v) for k,v in s2.items()}
    # negation and gamma actions
    def act(fa):
        out={}
        for k,(x,e,d) in enumerate(lab):
            al=(x*g+e*a2)%D; be=-d*a2; j2,ph2=red(fa(al)%D,fa(be)); k2,phk2=inv[j2]; out[k]=(k2,(ph2-phk2)%1)
        return out
    G=Fm.G
    for nm,fa in (("neg",lambda v:-v),("gamma",lambda v:G@v)):
        Aa=act(fa)
        mults={(lab[Aa[idx[(x,e,d)]][0]][0]*pow(x,-1,n))%n for (x,e,d) in lab if math.gcd(x,n)==1}
        two={str(lab[k][1:]):[str(lab[Aa[k][0]][1:]),str(Aa[k][1])] for k in range(4)}
        unif=len(mults)==1
        if unif:
            m=mults.pop()
            okm=all(lab[Aa[idx[(x,e,d)]][0]]==((m*x)%n,e,d) for (x,e,d) in lab)
            phx=all(Aa[idx[(x,e,d)]][1]==Aa[idx[(0,e,d)]][1] for (x,e,d) in lab)
        else: m=None; okm=False; phx=False
        res[nm]={"x_multiplier_mod_n":m,"exact":okm,"phase_x_independent":phx,"2adic":two,
                 "local_signs":{f"{p}^{e}": (m%(p**e) if m is not None else None) for p,e in sympy_factor(n)}}
    res["c_local"]={f"{p}^{e}":{"kT":kT[0]%(p**e) if kT else None,"cS":cS[0]%(p**e) if cS else None} for p,e in sympy_factor(n)}
    res["matches_symbolic"]=bool(res["T_perm_2adic_only"] and kT==[n-1] and ok
        and T2=={"(0, 0)":["(0, 1)","0"],"(0, 1)":["(0, 0)","0"],"(1, 0)":["(1, 0)","1/4"],"(1, 1)":["(1, 1)","1/4"]}
        and res["S2"]=={"((0, 0), (0, 0))":"0","((0, 1), (1, 0))":"0","((1, 0), (0, 1))":"0","((1, 1), (1, 1))":"1/2"}
        and res["neg"]["x_multiplier_mod_n"]==n-1 and res["neg"]["exact"] and res["neg"]["phase_x_independent"]
        and all(v[1]=="0" for v in res["neg"]["2adic"].values())
        and res["gamma"]["x_multiplier_mod_n"]==(s-1)%n and res["gamma"]["exact"] and res["gamma"]["phase_x_independent"]
        and [v[1] for v in res["gamma"]["2adic"].values()]==["0","0","0","1/2"])
    return res
def sympy_factor(n):
    out=[]; p=2
    while p*p<=n:
        if n%p==0:
            e=0
            while n%p==0: n//=p; e+=1
            out.append((p,e))
        p+=1
    if n>1: out.append((n,1))
    return out
if __name__=="__main__":
    allr=[]
    for s in [int(z) for z in sys.argv[1].split(',')]:
        r=factorize(s); allr.append(r); print(json.dumps(r),flush=True)
        json.dump(allr,open(f"gen_factor_{sys.argv[1].replace(',','_')}.json","w"),indent=1)
