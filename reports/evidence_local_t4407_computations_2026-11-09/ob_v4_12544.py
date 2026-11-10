# Local-derived. t4429 fallback (ii): level 12544 = 2^8*49 search for a weight-3/2 preimage of g = 49a1 (x) chi_-4 (conductor 784).
# Same joint-kernel test as ob_v1/ob_v2/ob_v3: K = joint kernel of T(p^2) - chi_-4(p) a_p(49a1), p = 3, 5, 11, in S_{3/2}(Gamma0(12544), chi_D),
# D in [1, 8, 28, 56] (the characters used at 1568/3136/6272). Started only after ob_v3 and the t4436 s2e job closed (memory). Timeout ~1 day (set by launcher).
import cypari2, time; pari=cypari2.Pari(); pari.allocatemem(8*10**9); P=pari
t0=time.time()
P("E=ellinit([1,-1,0,-2,-1]); af=ellan(E,500); ag=vector(500,n,kronecker(-4,n)*af[n])")
N=12544
for D in [1,8,28,56]:
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
