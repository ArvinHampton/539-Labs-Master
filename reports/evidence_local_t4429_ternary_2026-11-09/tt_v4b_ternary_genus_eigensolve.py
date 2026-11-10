# Local-derived. v4b (NI=N//9 artefact fix). t4429 fallback (i) step 3: ternary theta series of ALL positive ternary forms of discriminant d
# (Gross / Pacetti-Tornaria style: theta series of the classes of ternary lattices; differences across classes give weight-3/2 cusp forms).
# Q = a x^2 + b y^2 + c z^2 + r yz + s xz + t xy, Gram G = [[2a,t,s],[t,2b,r],[s,r,2c]], d := det(G)/2.
# Enumerate Minkowski-type reduced (a<=b<=c, |t|,|s|<=a, |r|<=b, abc<=d/2), dedupe by theta series (span is all that matters).
# Then: formal T(p^2) eigen-solve (Shimura, PARI convention c(p^2n)+kron(D,p)kron(-n,p)c(n)+p c(n/p^2)) for targets f=49a1 (sanity) and g=49a1(x)chi_-4 / Xi,
# for D in DLIST, mod prime PM via python-flint; nullity at NN and at NN2=0.6*NN (a genuine kernel is stable; spurious ones shrink with NN).
# A nonzero stable kernel is a CANDIDATE only (formal, truncated, mod PM); exact recheck is a separate later step.
import sys, time, numpy as np, flint, cypari2
pari=cypari2.Pari(); pari.allocatemem(6*10**8)
ds=[int(x) for x in sys.argv[1].split(',')]; NN=int(sys.argv[2]); TARGETS=sys.argv[3].split(',')
DLIST=[1,-1,2,-2,5,-5,7,-7,10,-10,14,-14,35,-35,70,-70]
PM=2**31-1; t0=time.time()
EC={'f':'ellinit([1,-1,0,-2,-1])','g':'elltwist(ellinit([1,-1,0,-2,-1]),-4)','Xi':'elltwist(ellinit([1,-1,0,-2,-1]),140)'}
PR0=[3,5,11,13,17,19,23,29,31,37,41,43]
LAM={}
for T in TARGETS:
    pari(f"E_={EC[T]}"); LAM[T]={p:int(pari(f"ellap(E_,{p})")) for p in PR0}
def kron(a,n): return int(pari.kronecker(a,n))
def forms(d):
    out=[]; a=1
    while a**3<=d/2:
        b=a
        while a*b*b<=d/2:
            for t in range(-a,a+1):
                den=4*a*b-t*t
                for s in range(-a,a+1):
                    for r in range(-b,b+1):
                        num=d+a*r*r+b*s*s-r*s*t
                        if num%den==0:
                            c=num//den
                            if c>=b: out.append((a,b,c,r,s,t))
            b+=1
        a+=1
    return out
for d in ds:
    F=forms(d)
    TH={}
    for (a,b,c,r,s,t) in F:
        G=pari.matrix(3,3,[2*a,t,s,t,2*b,r,s,r,2*c])
        v=np.array([1]+[2*int(x) for x in pari.qfrep(G,NN,1)],dtype=np.int64)
        key=hash(v[:400].tobytes())
        if key in TH and np.array_equal(TH[key][0],v): continue
        TH.setdefault(key,(v,(a,b,c,r,s,t)))
    TV=[x[0] for x in TH.values()]; TL=[x[1] for x in TH.values()]
    Gm=np.array(TV)
    print(f"d={d}: reduced forms {len(F)}, distinct theta {len(TV)} [{time.time()-t0:.0f}s]",flush=True)
    # independent subset
    NI=NN//9  # v4b: independence measured on n<=N/9 so every kept combination is visible to the c(n) terms of the equations (removes the "invisible" artefacts of v4 run2/run3)
    A=flint.nmod_mat([[int(x)%PM for x in Gm[:,n]] for n in range(NI+1)],PM)
    R,rk=A.rref(); piv=[]
    for i in range(rk): piv.append(next(j for j in range(A.ncols()) if int(R[i,j])!=0))
    Gm=Gm[piv]; TL=[TL[j] for j in piv]
    print(f"  rank of theta span (n<={NI}) = {rk}",flush=True)
    for T in TARGETS:
        lam=LAM[T]; PR=[p for p in PR0 if d%p!=0 and not (T=='Xi' and p==5)]
        out=[]
        for D in DLIST:
            nuls=[]
            for N_ in (int(0.6*NN),NN):
                rows=[]
                for p in PR:
                    cD=kron(D,p)
                    for n in range(1,N_//(p*p)+1):
                        vec=Gm[:,p*p*n]+(cD*kron(-n,p)-lam[p])*Gm[:,n]
                        if n%(p*p)==0: vec=vec+p*Gm[:,n//(p*p)]
                        rows.append([int(x)%PM for x in vec])
                X,nul=flint.nmod_mat(rows,PM).nullspace(); nuls.append(nul)
            out.append((D,nuls))
            if nuls[1]>0:
                kv=[int(X[i,0]) for i in range(len(piv))]; kv=[x if x<PM//2 else x-PM for x in kv]
                h=[sum(kv[i]*int(Gm[i,n]) for i in range(len(piv)))%PM for n in range(80)]
                h=[x if x<PM//2 else x-PM for x in h]
                print(f"  [{T}] D={D}: nullity(N={int(0.6*NN)})={nuls[0]} nullity(N={NN})={nuls[1]}; first kernel vector h (n<80 nonzero):",{n:h[n] for n in range(80) if h[n]},flush=True)
                print("     support:",[(TL[i],kv[i]) for i in range(len(piv)) if kv[i]][:30],flush=True)
        print(f"  [{T}] d={d} nullities (N={int(0.6*NN)},N={NN}) by D:",out,f"[{time.time()-t0:.0f}s]",flush=True)
print("DONE",f"[{time.time()-t0:.0f}s]")
