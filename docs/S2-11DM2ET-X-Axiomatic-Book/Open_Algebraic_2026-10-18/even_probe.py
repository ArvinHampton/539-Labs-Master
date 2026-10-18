# Item 2 probe: CRT split of labels into odd and 2-parts; Schmidt rank of S and T across (odd | 2-adic).
import sys, math, numpy as np
from family_s import Family
def odd2(D):
    m=D
    while m%2==0: m//=2
    return m, D//m
for s in [int(z) for z in sys.argv[1].split(',')]:
    F=Family(s); D=F.D; mo,m2=odd2(D)
    eo=pow(m2,-1,mo)*m2 % D   # idempotent: ≡1 mod mo, ≡0 mod m2
    e2=(1-eo)%D
    S=F.Smatrix(); T=F.Tmatrix()
    # split each label (al,be) into odd part of al, and (2-part of al, 2-part of be); be odd part must be in L' (phase)
    keys=[]
    for al,be in F.LABELS:
        al=np.array(al); be=np.array(be)
        keys.append((tuple((eo*al)%D),(tuple((e2*al)%D),tuple((e2*be)%D)),tuple((eo*be)%D)))
    O=sorted({k[0] for k in keys}); Tw=sorted({k[1] for k in keys}); ob={k[2] for k in keys}
    ok=len(O)*len(Tw)==F.N and len({(k[0],k[1]) for k in keys})==F.N
    print(f"s={s}: N={F.N}, |odd labels|={len(O)}, |2-adic labels|={len(Tw)}, product bijective: {ok}, odd parts of beta: {len(ob)}",flush=True)
    if not ok: continue
    oi={o:i for i,o in enumerate(O)}; ti={t:i for i,t in enumerate(Tw)}
    perm=[oi[k[0]]*len(Tw)+ti[k[1]] for k in keys]
    P=np.zeros((F.N,F.N)); P[perm,range(F.N)]=1
    for nm,M in (("S",S),("T",T)):
        Mp=P@M@P.T
        R=Mp.reshape(len(O),len(Tw),len(O),len(Tw)).transpose(0,2,1,3).reshape(len(O)**2,len(Tw)**2)
        sv=np.linalg.svd(R,compute_uv=False)
        print(f"   {nm}: operator-Schmidt values (top 4) {np.round(sv[:4]/sv[0],6)}",flush=True)
