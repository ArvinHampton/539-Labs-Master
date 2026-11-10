# Local-derived. t4407 O-b B5 completion: level 6272 = 2^7*49, the two characters D=28, D=56 left unfinished by ob_v2 (ob_v2.log kept as is).
# Same test as ob_v1/ob_v2: joint kernel of T(p^2) - chi_-4(p) a_p(f), p = 3,5,11, in S_{3/2}(Gamma0(6272), chi_D). Larger PARI stack.
import cypari2, time; pari=cypari2.Pari(); pari.allocatemem(6*10**9); P=pari
t0=time.time()
P("E=ellinit([1,-1,0,-2,-1]); af=ellan(E,500); ag=vector(500,n,kronecker(-4,n)*af[n])")
N=6272
for D in [28,56]:
    t1=time.time()
    try:
        P(f"m=mfinit([{N},3/2,{D}],1); d=mfdim(m); K=matid(d)")
        print(f" N={N} D={D}: mfinit done, dim {P('d')} [{time.time()-t1:.0f}s]",flush=True)
        for p in [3,5,11]:
            P(f"Mh=mfheckemat(m,{p}^2); K=K*matker((Mh-ag[{p}]*matid(d))*K)")
            print(f"   after p={p}: joint kernel dim {P('#K')} [{time.time()-t1:.0f}s]",flush=True)
            if int(P("#K"))==0: break
        print(f" N={N} D={D}: dim {P('d')}, joint kernel (T(p^2)=chi_-4(p)a_p(f), p=3,5,11) dim = {P('#K')}  [{time.time()-t1:.0f}s]",flush=True)
        P("m=0; Mh=0; K=0; gettime()")
    except cypari2.PariError as e:
        print(f" N={N} D={D}: PARI error {e}",flush=True)
print("elapsed %.0fs"%(time.time()-t0))
